# from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login as djlogin, get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError;
from django.db import IntegrityError


class RecipeViewSet(viewsets.ModelViewSet): 
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    @action(detail=True, methods=['get'])
    def retrieve_by_id(self, request, pk=None):
        recipe = self.get_object()
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)

@api_view(['POST'])
def login(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'message': 'Špatné přihlašovací údaje'}) 

@api_view(['POST'])
def register(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    password2 = request.data.get('password2')

    User = get_user_model()

    if User.objects.filter(username=username).exists():
        return Response({'message': 'Toto jméno je již zabrané'}, status=status.HTTP_400_BAD_REQUEST)
    
    if password != password2:
        return Response({'message': 'Hesla se neshodují'}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(password) < 5:
        return Response({'message': 'Heslo musí obsahovat alespoň 5 znaků'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({'message': 'Registrace proběhla úspěšně'})
    except IntegrityError:
        return Response({'message': 'objevil se Error při vytváření účtu'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ValidationError as e:
        return Response({'message': e.messages}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])  # Only authenticated users can toggle favorites
def toggle_favorite(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response({'message': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if request.method == 'POST':
        if user not in recipe.favorited_by.all():
            recipe.favorited_by.add(user)
            recipe.save()
            return Response({'message': 'Recipe added to favorites'})
        else:
            return Response({'message': 'Recipe already favorited'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if user in recipe.favorited_by.all():
            recipe.favorited_by.remove(user)
            recipe.save()
            return Response({'message': 'Recipe removed from favorites'})
        else:
            return Response({'message': 'Recipe not favorited by user'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)