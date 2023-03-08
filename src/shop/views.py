from django.views import generic

from .models import Category


class ProductListView(generic.ListView):
    template_name = 'shop/products/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 8

    def get_queryset(self):
        return Category.objects.get(slug=self.kwargs['category_slug']).products.all()


class ProductDetailView(generic.DetailView):
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return Category.objects.get(
            slug=self.kwargs['category_slug']).products.get(
            slug=self.kwargs['product_slug']
        )

    def get_template_names(self):
        return f'shop/products/{type(self.object).__name__.lower()}_detail.html'


class ProductSpecificationView(ProductDetailView):
    def get_template_names(self):
        return f'shop/products/{type(self.object).__name__.lower()}_specification.html'
