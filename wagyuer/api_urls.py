from rest_framework.routers import DefaultRouter

from . import api_views

package_router = DefaultRouter()
package_router.register(r"", api_views.PackageViewSet)
