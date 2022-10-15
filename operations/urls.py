from django.urls import path

from .views import upload, OperationView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("operations/", upload, name="operation"),
    path("operations/<int:store_id>/", OperationView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("doc/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
