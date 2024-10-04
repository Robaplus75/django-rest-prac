from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request):
	data = {}
	serializer = ProductSerializer(data=request.data)

	if serializer.is_valid():
		print("VALID DATA")
		instance = serializer.save()
		print(instance)
		data = serializer.data
	else:
		Print("INVALID DATA")

	return Response(serializer.data)
