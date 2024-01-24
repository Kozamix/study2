from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import car_list, add_car, edit_car ,delete_car


urlpatterns = [
    path('', car_list, name='car_list'),
    path('add/', add_car, name='add_car'),
    path('edit/<int:car_id>/', edit_car, name='edit_car'),
    path('car_detail/<int:pk>/', edit_car, name='car_detail'),
    path('edit/<int:pk>/delete/', delete_car, name='delete_car'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
