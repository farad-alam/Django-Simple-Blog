from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path("",views.home, name="home"),
    path('<slug:slug>/', views.singlePost, name='singlePost'),
    path('category/<slug:slug>/', views.categories, name='categories')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
