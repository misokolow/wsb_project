from django.urls import path

from .views import mobility, lte_list, mobility_all
from .views import start
from .views import doc
urlpatterns = [

    path('', start, name='start'),
    path('doc/', doc, name='doc'),
    path('mobility/<lte_layer>/', mobility, name='mobility'),
    path('layer/', lte_list, name='lte_list'),
    path('mobility_all/', mobility_all, name='mobility_all'),
]