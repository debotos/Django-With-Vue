from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/article/', include('article.api.urls')),
    path('article/', TemplateView.as_view(template_name='article/index.html')),
    path('', TemplateView.as_view(template_name='article/index.html'))
]
