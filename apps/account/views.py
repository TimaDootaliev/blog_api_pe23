from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserRegistrationSerializer


User = get_user_model()


class RegistrationView(APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request: Request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Thanks for registration! Activate your account via link in your mail',
                status=status.HTTP_201_CREATED
            )

# TODO: Активация, смена пароля, удаление аккаунта, восстановления пароля
# TODO: подключить celery, redis
# TODO: исправить HTML