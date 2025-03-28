from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import Usuario

# Create your views here.

@api_view(['POST'])
def registrar(request):
    nome = request.data.get('username')
    senha = request.data.get('senha')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    cpf = request.data.get('cpf')
    email = request.data.get('email')

    if not nome or not senha or not cpf or not email:
        return Response({'Erro': 'Os campos nome, email e senha são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

    if Usuario.objects.filter(username=nome).exists():
        return Response({'Erro': 'Usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)

    usuario = Usuario.objects.create_user(
        username=nome,
        password=senha,
        telefone=telefone,
        email=email,
        cpf=cpf,
        endereco=endereco
    )
    
    return Response({'Mensagem': 'Usuário cadastrado com sucesso'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar(request):
    nome = request.data.get('username')
    senha = request.data.get('senha')

    if not nome or not senha:
        return Response({'Erro': 'Os campos nome e senha são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

    usuario = authenticate(username=nome, password=senha)

    if usuario is not None:
        # Gera o token
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegida(request):
    return Response({"Mensagem": "Olá 2DS-MB15!"}, status=status.HTTP_200_OK)