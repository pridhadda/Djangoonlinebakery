from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('product/',include("product.urls",namespace='product')),
    path('',include("product.urls",namespace='product')),
   # path('login/',auth_views.login,{'template_name': 'product/loginpg.html'},name='login'),
    path('logout/',auth_views.logout,name='logout'),
    path('login/', LoginView.as_view(template_name='product/loginpg.html'), name="login"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



