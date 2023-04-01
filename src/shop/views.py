from django.db.models import Q, Min, Max
from django.views import generic

from cart.forms import CartAddProductForm
from .models import Product, Brand


class ProductListView(generic.ListView):
    template_name = 'shop/products/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 9

    def get_queryset(self):
        queryset = Product.objects.select_subclasses().filter(category__slug=self.kwargs['category_slug'])

        if min_price := self.request.GET.get('min-price'):
            queryset = queryset.filter(Q(price__gte=min_price) | Q(discount_price__gte=min_price))
        if max_price := self.request.GET.get('max-price'):
            queryset = queryset.filter(Q(price__lte=max_price) | Q(discount_price__lte=max_price))
        if brands := self.request.GET.getlist('brand'):
            queryset = queryset.filter(brand__slug__in=brands)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = self.get_queryset()

        if min_price := self.request.GET.get('min-price'):
            context['min_price'] = min_price
        else:
            context['min_price'] = int(min(
                queryset.aggregate(Min('price'))['price__min'],
                discount_price if (
                    discount_price := queryset.aggregate(Min('discount_price'))['discount_price__min']
                ) else 0
            ))

        if max_price := self.request.GET.get('max-price'):
            context['max_price'] = max_price
        else:
            context['max_price'] = int(max(
                queryset.aggregate(Max('price'))['price__max'],
                discount_price if (
                    discount_price := queryset.aggregate(Max('discount_price'))['discount_price__max']
                ) else 0
            ))

        context['brands'] = Brand.objects.all()
        context['checked_brands'] = self.request.GET.getlist('brand')
        context['cart_form'] = CartAddProductForm()
        return context


class ProductDetailView(generic.DetailView):
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return Product.objects.select_subclasses().get(slug=self.kwargs['product_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = CartAddProductForm()
        return context

    def get_template_names(self):
        return f'shop/products/{type(self.object).__name__.lower()}_detail.html'


class ProductSpecificationView(ProductDetailView):
    def get_template_names(self):
        return f'shop/products/{type(self.object).__name__.lower()}_specification.html'
