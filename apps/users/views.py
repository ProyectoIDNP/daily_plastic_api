from django.utils import timezone
from django.contrib.sessions.models import Session
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import UserTokenSerialzier

class Login(ObtainAuthToken):

  def post(self, request):
    login_serializer = self.serializer_class(data = request.data, context = { 'request': request })
    if login_serializer.is_valid():
      user = login_serializer.validated_data['user']
      if user.is_active: 
        token, created = Token.objects.get_or_create(user = user)
        user_serializer = UserTokenSerialzier(user)
        if created: 
          return Response({ 'token': token.key, 'user': user_serializer.data }, status = status.HTTP_200_OK)
        else:
          # Logout Sessions
          all_sessions = Session.objects.filter(expire_date__gte = timezone.now())
          if all_sessions.exists():
            for session in all_sessions:
              session_data = session.get_decoded()
              if user.id == int(session_data.get('_auth_user_id')):
                session.delete()
          # Logout Sessions
          token.delete()
          token = Token.objects.create(user = user)
          return Response({ 'token': token.key, 'user': user_serializer.data }, status = status.HTTP_200_OK)
      else:
        return Response({'error': 'El usuario no puede iniciar sesión'}, status = status.HTTP_403_FORBIDDEN)
    else:
      return Response({'error': 'Formato inválido'}, status = status.HTTP_400_BAD_REQUEST)

class Logout(APIView):

  def get(self, request):
    try: 
      token = request.GET.get('token')
      token = Token.objects.filter(key = token).first()
      if token: 
        user = token.user
        all_sessions = Session.objects.filter(expire_date__gte = timezone.now())
        if all_sessions.exists():
          for session in all_sessions:
            session_data = session.get_decoded()
            if user.id == int(session_data.get('_auth_user_id')):
              session.delete()
        token.delete()
        return Response({'message': 'Sesiones cerradas exitosamente'}, status = status.HTTP_200_OK)
      else: 
        return Response({'error': 'Token no corresponde a un usuario'}, status = status.HTTP_400_BAD_REQUEST)
    except:
      return Response({'error': 'No se ha encontrado el token'}, status = status.HTTP_400_BAD_REQUEST)