from django.urls import path
from .views import *

urlpatterns = [
    path('', PostIndex.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category'),
    path('tag/<slug:slug>/', TagDetails.as_view(), name='tag_detail'),

]
