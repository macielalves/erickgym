from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from erickgym.serializers import CommomUserSerializer
from erickgym.permissions import AllowPOST
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CommomUserSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


@api_view(["POST"])
@permission_classes([AllowPOST])
def singin(request):
    try:
        user = User.objects.get(username=request.data.get("username"))
    # user = get_object_or_404(User, username=request.data.get("username"))
    except User.DoesNotExist:
        return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(request.data.get("password")):
        return Response({"details": "Not Found."}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = CommomUserSerializer(user)
    return Response(
        {"token": {"key": token.key, "created": created}, "user": serializer.data}
    )


@api_view(["POST"])
@permission_classes([AllowPOST])
def singup(request):
    serializer = CommomUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        user = User.objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([])
@authentication_classes([])
def test_token(request):
    return Response({f"authenticated to {request.user.username}"})
