from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CategoryViewSet, ProductModelViewSet, ProductDetailsViewSet, \
    OrderViewSet, HistoryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register('Category', CategoryViewSet, basename='category')
router.register('Product', ProductModelViewSet, basename='product')
router.register('History', HistoryViewSet, basename='history')

urlpatterns = ([
                   path('Product/<int:pk>/', ProductDetailsViewSet.as_view()),
                   path('order/', OrderViewSet.as_view())
               ] + router.urls)
