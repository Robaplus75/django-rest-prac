from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
	discount = serializers.SerializerMethodField()

	class Meta():
		model = Product
		fields = ['id', 'title', 'content', 'price', 'sale_price', 'discount']

	def get_discount(self, obj):
		try:
			return int(float(obj.price) * 0.1)
		except:
			return None