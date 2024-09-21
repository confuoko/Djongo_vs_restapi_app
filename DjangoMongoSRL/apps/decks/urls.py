from django.urls import include, path

from rest_framework_nested import routers as r2
from rest_framework import routers
from .views import DecksViewSet
from .views import DeckCardsViewSet


router = routers.SimpleRouter()
router.register('', DecksViewSet)

#register /decks/:id/cards url
cards_router = r2.NestedSimpleRouter(router, '', lookup='decks')
cards_router.register('cards', DeckCardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls)),
    ]
