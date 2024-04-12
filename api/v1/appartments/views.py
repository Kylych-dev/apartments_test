from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# from api.utils.permissions import IsPartnerOrReadOnly
from apps.appartments.models import Apartment
from .serializers import EstablishmentSerializer



class EstablishmentModelViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = EstablishmentSerializer
    # permission_classes = [permissions.IsAuthenticated, IsPartnerOrReadOnly]

    @swagger_auto_schema(
        method="get",
        operation_description="Получить список квартир",
        operation_summary="Получение списка квартир",
        operation_id="list_apartment",
        tags=["Apartment"],
        responses={
            200: openapi.Response(description="OK - Список успешно получен"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=False, method=["get"])
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        method="put",
        operation_description="Обновление данных квартир",
        operation_summary="Обновление данных квартир",
        operation_id="update_apartment",
        tags=["Apartment"],
        responses={
            200: openapi.Response(description="OK - Квартира успешно обновлен"),
            400: openapi.Response(description="Bad Request - Неверный запрос или некорректные данные"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["put"])
    def update(self, request, *args, **kwargs):
        try:
            establishment = self.get_object()
            serializer = EstablishmentSerializer(establishment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, 
                    status=status.HTTP_200_OK
                    )
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as ex:
            return Response(
                {"Сообщение": str(ex)}, 
                status=status.HTTP_404_NOT_FOUND
                )

    @swagger_auto_schema(
        method="post",
        operation_description="Создание квартир",
        operation_summary="Создание квартир",
        operation_id="create_apartment",
        tags=["Apartment"],
        responses={
            201: openapi.Response(description="Created - Новая квартира успешно созданo"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["post"])
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(
                {"Сообщение": str(ex)}, 
                status=status.HTTP_400_BAD_REQUEST
                )


    @swagger_auto_schema(
        method="delete",
        operation_description="Удаление квартиры",
        operation_summary="Удаление квартиры",
        operation_id="delete_apartment",
        tags=["Apartment"],
        responses={
            204: openapi.Response(description="No Content - Квартира успешно удалена"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Квартира не найдена"),
        },
    )
    @action(detail=True, methods=["delete"])
    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Apartment.DoesNotExist:
            return Response(
                {"Сообщение": "Квартира не найдена"}, 
                status=status.HTTP_404_NOT_FOUND
                )
