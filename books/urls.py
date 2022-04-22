from django.urls import path, include
from rest_framework import routers
from books import views


router = routers.DefaultRouter()
router.register('book', views.BookViewSet, basename='viewaddbook')
router.register('best-book', views.BestBookViewSet, basename='bestbook')
router.register('order', views.OrderViewSet, basename='viewaddorder')

urlpatterns = [
    path('', include(router.urls)),
]
