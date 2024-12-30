"""horilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, re_path

import notifications.urls

from . import settings


def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)


urlpatterns = [
    path(f"{settings.URL_PREFIX}admin/", admin.site.urls),
    path(f"{settings.URL_PREFIX}accounts/", include("django.contrib.auth.urls")),
    path(f"{settings.URL_PREFIX}i18n/", include("django.conf.urls.i18n")),
    path(f"{settings.URL_PREFIX}", include("base.urls")),
    path(f"{settings.URL_PREFIX}", include("horilla_automations.urls")),
    path(f"{settings.URL_PREFIX}", include("horilla_views.urls")),
    path(f"{settings.URL_PREFIX}api/", include("horilla_api.urls")),
    path(f"{settings.URL_PREFIX}horilla-widget/", include("horilla_widgets.urls")),
    path(f"{settings.URL_PREFIX}recruitment/", include("recruitment.urls")),
    path(f"{settings.URL_PREFIX}onboarding/", include("onboarding.urls")),
    path(f"{settings.URL_PREFIX}employee/", include("employee.urls")),
    path(f"{settings.URL_PREFIX}attendance/", include("attendance.urls")),
    path(f"{settings.URL_PREFIX}leave/", include("leave.urls")),
    path(f"{settings.URL_PREFIX}payroll/", include("payroll.urls.urls")),
    path(f"{settings.URL_PREFIX}pms/", include("pms.urls")),
    path(f"{settings.URL_PREFIX}offboarding/", include("offboarding.urls")),
    path(f"{settings.URL_PREFIX}asset/", include("asset.urls")),
    path(f"{settings.URL_PREFIX}helpdesk/", include("helpdesk.urls")),
    re_path(
        f"{settings.URL_PREFIX}inbox/notifications/", include(notifications.urls, namespace="notifications")
    ),
    path(f"{settings.URL_PREFIX}health/", health_check),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
