#### Setting up URLs ####


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseIncomeViewSet, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


router = DefaultRouter()
router.register('expenses', ExpenseIncomeViewSet, basename='expenses')

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls))
]