from .views import index, UserViewSet, Login, Logout, token
from django.urls import path
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path('index/', index, name='index'),
    path('token/', token, name='token'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout')
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns.extend(router.urls)
