from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import Burger
from main.serializers import BurgerSerializer

class BurgerViewSet(ModelViewSet):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer
