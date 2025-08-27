from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Usuario
from .serializers import UsuarioSerialiazer
from django.http import HttpResponse


class UsuarioPagination(PageNumberPagination):
    page_size = 5  # cantidad máxima de registros por página
    page_size_query_param = 'page_size'  # permite cambiarlo con ?page_size=10
    max_page_size = 100  # límite máximo permitido


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerialiazer
    pagination_class = UsuarioPagination

    """
    MÉTODO POST
    {
        name,
        username,
        password,
        rol
    }
    """

    # * list: maneja el método GET
    def list(self, request, *args, **kwargs):
        usuarios = self.get_queryset()
        page = self.paginate_queryset(usuarios)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                "success": True,
                "mensaje": "Usuarios obtenidos correctamente" if usuarios else "No hay usuarios registrados",
                "errores": [],
                "data": serializer.data
            })

        # Si no hay paginación, devolver todo (caso raro si desactivas pagination_class)
        serializer = self.get_serializer(usuarios, many=True)
        return Response({
            "success": True,
            "mensaje": "Usuarios obtenidos correctamente" if usuarios else "No hay usuarios registrados",
            "errores": [],
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # * create: maneja el método POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "success": True,
                "mensaje": "Usuario creado correctamente",
                "errores": [],
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "mensaje": "Error al crear usuario",
            "errores": serializer.errors,
            "data": {}
        }, status=status.HTTP_400_BAD_REQUEST)

