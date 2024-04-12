from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.appartments.views import EstablishmentModelViewSet

# from api.v1.accounts.views import (
#     RegularUserUpdateView, 
#     PartnerUpdateView, 
#     ChatMessageCreateAPIView,
#     PasswordResetRequestView
#     )


router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [   
        # Establishment
        path("apartments/", EstablishmentModelViewSet.as_view({"get": "list"}), name="apartments-list"),
        path("apartments/create/", EstablishmentModelViewSet.as_view({"post": "create"}), name="apartments-create"),
        path("apartments/update/<int:pk>/", EstablishmentModelViewSet.as_view({"put": "update"}), name="apartments-update"),
        path("apartments/delete/<int:pk>/",EstablishmentModelViewSet.as_view({"delete": "delete"}), name="apartments-delete"),
    ]
)