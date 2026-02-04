"""
URL configuration for kids_project project.
API + раздача React-фронта с одного домена.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.http import FileResponse

from rest_framework.routers import DefaultRouter
from children.views import ChildViewSet, client_list

router = DefaultRouter()
router.register(r'children', ChildViewSet)


def serve_react(request):
    """Отдаёт index.html для всех не-API путей (SPA)."""
    index = settings.REACT_BUILD_DIR / 'index.html'
    if index.exists():
        return FileResponse(index.open('rb'), content_type='text/html')
    return FileResponse(
        b'<h1>Frontend not built</h1><p>Run: cd pr && npm run build</p>',
        content_type='text/html',
        status=404,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/clients/', client_list, name='api-clients'),
    path('api-auth/', include('rest_framework.urls')),
    # Статика React (JS/CSS из pr/build/static)
    path(
        'static/<path:path>',
        serve,
        {'document_root': str(settings.REACT_BUILD_DIR / 'static')},
    ),
    # SPA: все остальные пути → index.html
    re_path(r'^.*$', serve_react),
]