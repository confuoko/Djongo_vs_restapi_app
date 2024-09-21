from django.shortcuts import render
from rest_framework import serializers, viewsets
from django_filters import rest_framework as filters_1
from .models import Card
from rest_framework.filters import SearchFilter, OrderingFilter

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card 
        fields = '__all__'
    


class CardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    filter_backends = (filters_1.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('question_type',)
    search_fields = ('question',)
    ordering = ('question_type',)


