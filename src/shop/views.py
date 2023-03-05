from django.views import generic

from .models import Category


class ProductListView(generic.ListView):
    template_name = 'shop/product/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 8

    def get_queryset(self):
        return Category.objects.get(slug=self.kwargs['category_slug']).products.all()


class ProductDetailView(generic.DetailView):
    template_name = 'shop/product/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return Category.objects.get(
            slug=self.kwargs['category_slug']).products.get(
            slug=self.kwargs['product_slug']
        )
