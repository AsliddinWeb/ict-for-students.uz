from django.contrib import admin
from django.urls import path, include

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# Views
from main_app.views import home_page
from contact_app.views import contact_page, me_page

urlpatterns = [
    path('admin/', admin.site.urls),

    # Views
    path('', home_page, name='home_page'),

    path('courses/', include('course_app.urls')),

    path('contact/', contact_page, name='contact_page'),
    path('me/', me_page, name='me_page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)