from django.urls import path
from myapp.views import index, index_items

app_name ="myapp"

urlpatterns = [
    path('', index),
    path('<int:my_id>/', index_items, name="detail")
]
