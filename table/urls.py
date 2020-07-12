from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include

from app import settings
from .views import table_view_new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table_new/', table_view_new),
    path('', lambda x: HttpResponseRedirect('/table_new/')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
