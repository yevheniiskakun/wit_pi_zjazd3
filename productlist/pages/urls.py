
from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

app_name = 'pages'

urlpatterns = ([
	# main view
	path('', views.index, name='home'),
	path('delete_product/<int:id>', views.delete_product, name='delete_product'),
	path('mark_product/<int:id>', views.mark_product, name='mark_product'),
	path('add_product', views.add_product, name='add_product'),
]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + router.urls)