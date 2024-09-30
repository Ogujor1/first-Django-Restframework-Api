from django.urls import path
from .views import ProductCreateApp, ProductRetrieveApp, ProductListCreate,product_alt_view, ProductUpdateApp, ProductDeleteApp, ProductListApp


urlpatterns = [
    path('create/', ProductCreateApp.as_view()),
    path('<int:pk>', ProductRetrieveApp.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateApp.as_view(), name='product-edit'),
    path('<int:pk>/delete/', ProductDeleteApp.as_view()),
    path('list-create/', ProductListCreate.as_view()),
    path('list/', ProductListApp.as_view()),
    
    # path('<int:pk>', product_alt_view),
    # path('create/', product_alt_view),

]    