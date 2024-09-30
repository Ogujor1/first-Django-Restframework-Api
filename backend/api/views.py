from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product
from product.serializer import ProductSerializer

# Create your views here.
@api_view(['GET'])
def home(request):
  data = Product.objects.all()
  instance = ProductSerializer(data, many=True).data
  return Response(instance)
  
@api_view(['POST']) 
def post(request):
  instance = ProductSerializer(data=request.data)
  if instance.is_valid():
    instance.save()
  return Response(instance.data)  

    
      
