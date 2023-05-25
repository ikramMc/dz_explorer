from backend.models import PointInteret 
from backend.models import  Evenement
from backend.models import Commentaire
from backend.models import MoyenTransport
from backend.models import Region
from backend.models import Visiteur
from rest_framework import fields,serializers

class PISerializer (serializers.ModelSerializer):
 class Meta:
  model=PointInteret
  fields='__all__'
class EventSerializer (serializers.ModelSerializer):
 class Meta:
  model=Evenement
  fields='__all__'
class CommentaireSerializer (serializers.ModelSerializer):
 class Meta:
  model=Commentaire
  fields='__all__'
class MTSerializer (serializers.ModelSerializer):
 class Meta:
  model=MoyenTransport
  fields='__all__'
class RegionSerializer (serializers.ModelSerializer):
 class Meta:
  model=Region
  fields='__all__'
class VisiteurSerializer (serializers.ModelSerializer):
 class Meta:
  model=Visiteur
  fields='__all__'