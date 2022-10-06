from django.urls import path
from barang_wishlist.views import add_wishlist_item, get_wishlist_json, wishlist
from example_app.views import index

urlpatterns = [
    path('', wishlist, name='index'),
    path('/get_data', get_wishlist_json, name='get_wishlist_json'),
    path('/create_data', add_wishlist_item, name='add_wishlist_item')
]
