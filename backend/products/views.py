from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class  = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def perform_create(self, serializer):
		print("Product has been Validated and created")
		serializer.save()

class ProductUpdateAPIView(generics.UpdateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def perform_update(self, serializer):
		print("Product has been Validated and created")
		serializer.save()

class ProductMixinView(mixins.ListModelMixin, generics.GenericAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)