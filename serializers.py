from rest_framework import serializers
from  main.models import Burger
class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = ('id', 'title', 'description', 'date', 'image')
