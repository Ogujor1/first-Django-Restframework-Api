from .models import Product
from rest_framework import permissions, authentication
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView,DestroyAPIView, ListAPIView
from .serializer import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.permissions import IsStaffEditPermission
from api.authentication import TokenAuthentication
# Create your views here.

class ProductListCreate(ListCreateAPIView,):
  """GET & POST VIEW""" 
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.IsAdminUser, IsStaffEditPermission]
  authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]



class ProductListApp(ListAPIView):
  """POST VIEW""" 
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  


class ProductCreateApp(CreateAPIView):
  """POST VIEW""" 
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  

  def perform_create(self, serializer):
    #serializer.save(user=self.request.user)
    # email = serializer.validated_data.pop('email')
    # print(email)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = title
    serializer.save(content=content)

    


class ProductRetrieveApp(RetrieveAPIView):
  """POST VIEW""" 
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ProductUpdateApp(UpdateAPIView):
  """UPDATE VIEW""" 
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'  

def perfomr_update(self, serializer):
  instance = serializer.save()
  if not instance.content:
    instance.content = instance.title
    instance.save(instance.content)


class ProductDeleteApp(DestroyAPIView):
  """DELETE VIEW""" 
  queryset = Product.objects.all()
  serializer_class = ProductSerializer   
  lookup_field = 'pk'   

  def perform_destroy(self, instance):
    super().perform_destroy(instance)




@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
  """DETAIL VIEW"""
  if request.method == "GET":
    if pk != None:
      data = get_object_or_404(Product, pk=pk)
      instance = ProductSerializer(data, many=False).data
      return Response(instance)
     
    else:
      """GET VIEW""" 
      data = Product.objects.all()
      instance = ProductSerializer(data, many=True).data
      return Response(instance)
    
  elif  request.method == "POST":
    """POST VIEW""" 
    instance = ProductSerializer(data=request.data)
    if instance.is_valid(raise_exception=True):
      title = instance.validated_data.get('title')
      content = instance.validated_data.get('content')
      if content is None:
        content = title
      instance.save(content=content)  
      return Response(instance.data)
  return Response({"invalide":"Bad Response"}, status=404)

  

