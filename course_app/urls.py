from django.urls import path

from .views import video_page, slayd_page, maruza_page, amaliy_page, test_page

urlpatterns = [
    path('video/', video_page, name='video_page'),
    path('slayd/', slayd_page, name='slayd_page'),
    path('maruza/', maruza_page, name='maruza_page'),
    path('amaliy/', amaliy_page, name='amaliy_page'),
    path('test/', test_page, name='test_page'),
]