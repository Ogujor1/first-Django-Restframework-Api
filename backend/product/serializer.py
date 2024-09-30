from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
  edit_url = serializers.SerializerMethodField(read_only=True)
  discount = serializers.SerializerMethodField(read_only=True)
  #email = serializers.EmailField(write_only=True)
  class Meta:
    model = Product
    fields = ['pk', 'url', 'edit_url','title', 'content', 'price', 'sale_price', 'discount']

  # def create(self, validated_data):
  #   #email = validated_data.pop('email')
  #   #return Product.objects.create(**validated_data)
  #   obj = super().create(validated_data)  
  #   #print(email, obj)
  #   return obj
  
  def update(self, validated_data, instance):
    instance.title = validated_data.get('title')
    return instance

  def get_edit_url(self, obj):
    request = self.context.get('request')  
    return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)
  
  def get_discount(self, obj):
    return obj.get_discount()