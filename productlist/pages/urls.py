
from django.urls import include, path
from . import views
from .views import ProductViewSet, ProductDelete, MarkProduct, ProductAdd

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)

app_name = 'pages'

urlpatterns = ([
	# main view
	path('', views.index, name='home'),
	path('api/all_products', ProductViewSet.as_view({'get': 'list'}), name="all_products"),
	path('api/add_product', ProductAdd.as_view(), name="add_product"),
	path('api/delete_product/<int:pk>', ProductDelete.as_view(), name="add_product"),
	path('api/mark_product/<int:pk>', MarkProduct.as_view(), name="mark_product")
]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + router.urls)