from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from backend.models import Evenement
from backend.serializers import   EventSerializer 
from backend.models import PointInteret
from backend.serializers import  PISerializer 
from backend.models import Commentaire
from backend.serializers import  CommentaireSerializer
from backend.models import MoyenTransport
from backend.serializers import  MTSerializer
from backend.models import Region
from backend.serializers import  RegionSerializer
from backend.models import Visiteur
from backend.serializers import  VisiteurSerializer
from django.contrib.auth.hashers import make_password,check_password
import json
# Create your views here.
@csrf_exempt
def EventAPI(request ,pk=0):
 if request.method=='GET':
      if pk==0:
       events = Evenement.objects.all()
       events_serializer = EventSerializer(events, many=True)
       return JsonResponse(events_serializer.data, safe=False)
      elif pk!=0:
          events = Evenement.objects.filter(PiId=pk) 
          events_serializer = EventSerializer(events, many=True)
          return JsonResponse(events_serializer.data, safe=False)
 elif request.method == 'POST':
       event_data = JSONParser().parse(request)
       event_serializer = EventSerializer(data=event_data)
       if event_serializer.is_valid():
        event_serializer.save()
        return JsonResponse("creating event Successfully", safe=False)
       return JsonResponse("error ,make sure you have supply all the required fields ", safe=False)
 elif request.method == 'PUT':
       event_data = JSONParser().parse(request)
       event = Evenement.objects.get(idEvenemnt=event_data['idEvenement'])
       event_serializer = EventSerializer(event, data=event_data )
       if event_serializer.is_valid():
         event_serializer.save()
         return JsonResponse("Updated Successfully", safe=False)
       return JsonResponse("Failed To Update")	
 elif request.method == 'DELETE':
		 event = Evenement.objects.get(idEvenement=pk)
		 event.delete()
		 return JsonResponse("event has been Deleted Successfully", safe=False)				


@csrf_exempt
def PIAPI(request ,pk=0):
 if request.method=='GET':
      if(pk==0):
        pi = PointInteret.objects.all()
        pi_serializer = PISerializer(pi, many=True)
        return JsonResponse(pi_serializer.data, safe=False)
      elif(pk!=0):
        pi= PointInteret.objects.get(idPoint=pk)
        pi_serializer=PISerializer(pi)
        return JsonResponse(pi_serializer.data, safe=False)
 elif request.method == 'POST':
       pi_data = JSONParser().parse(request)
       pi_serializer = PISerializer(data=pi_data)
       if pi_serializer.is_valid():
         pi_serializer.save()
         return JsonResponse("creating PI Successfully", safe=False)
       return JsonResponse("error ,make sure you have supply all the required fields ", safe=False)
 elif request.method == 'PUT':
       pi_data = JSONParser().parse(request)
       pi= PointInteret.objects.get(idPoint=pi_data['idPoint'])
       pi_serializer = PISerializer(pi, data=pi_data )
       if pi_serializer.is_valid():
         pi_serializer.save()
         return JsonResponse("Updated Successfully", safe=False)
       return JsonResponse("Failed To Update")	
 elif request.method == 'DELETE':
		 pi= PointInteret.objects.get(idPoint=pk)
		 pi.delete()
		 return JsonResponse("PI has been Deleted Successfully", safe=False)				

@csrf_exempt
def CommentaireAPI(request ,pk=0):
 if request.method=='GET':
      if (pk!=0):
       commentaires= Commentaire.objects.filter(PiId=pk)
       commentaires_serializer = CommentaireSerializer(commentaires, many=True)
       return JsonResponse(commentaires_serializer.data, safe=False)
      elif (pk==0):
        return JsonResponse("specify the pi id",safe=False)    
 elif request.method == 'POST':
       commentaire_data = JSONParser().parse(request)
       commentaire_serializer = CommentaireSerializer(data=commentaire_data)
       if commentaire_serializer.is_valid():
         commentaire_serializer.save()
         return JsonResponse("creating commentaire Successfully", safe=False)
       return JsonResponse("error ,make sure you have supply all the required fields ", safe=False)
 elif request.method == 'PUT':
       commentaire_data = JSONParser().parse(request)
       commentaire= Commentaire.objects.get(idCommentaire=commentaire_data['idCommentaire'])
       commentaire_serializer = CommentaireSerializer(commentaire, data=commentaire_data )
       if commentaire_serializer.is_valid():
         commentaire_serializer.save()
         return JsonResponse("Updated Successfully", safe=False)
       return JsonResponse("Failed To Update")	
 elif request.method == 'DELETE':
		 commentaire = Commentaire.objects.get(idCommentaire=pk)
		 commentaire.delete()
		 return JsonResponse("Commentaire has been Deleted Successfully", safe=False)				

@csrf_exempt
def MTAPI(request ,pk=0):
 if request.method=='GET':
      if(pk!=0):
        mts = MoyenTransport.objects.filter(PiId=pk)
        mts_serializer =MTSerializer(mts, many=True)
        return JsonResponse(mts_serializer.data, safe=False)
      elif pk==0:
        return JsonResponse("specify the pi id",safe=False)       
 elif request.method == 'POST':
       mt_data = JSONParser().parse(request)
       mt_serializer = MTSerializer(data=mt_data)
       if mt_serializer.is_valid():
          mt_serializer.save()
          return JsonResponse("creating moyen transport Successfully", safe=False)
       return JsonResponse("error ,make sure you have supply all the required fields ", safe=False)
 elif request.method == 'PUT':
       mt_data = JSONParser().parse(request)
       mt = MoyenTransport.objects.get(idMoyenTrasport=event_data['idMoyenTransport'])
       mt_serializer = MTSerializer(MT, data=mt_data )
       if mt_serializer.is_valid():
         mt_serializer.save()
         return JsonResponse("Updated Successfully", safe=False)
       return JsonResponse("Failed To Update")	
 elif request.method == 'DELETE':
		 mt = MoyenTransport.objects.get(idMoyenTransport=pk)
		 mt.delete()
		 return JsonResponse("moyen transport has been Deleted Successfully", safe=False)				

@csrf_exempt
def RegionAPI(request ,pk=0):
 if request.method=='GET':
       regions = Region.objects.all()
       regions_serializer = RegionSerializer(regions, many=True)
       return JsonResponse(regions_serializer.data, safe=False)
 elif request.method == 'POST':
       region_data = JSONParser().parse(request)
       region_serializer = RegionSerializer(data=region_data)
       region_serializer.save()
       return JsonResponse("creating region Successfully", safe=False)
 elif request.method == 'PUT':
       event_data = JSONParser().parse(request)
       region = Evenement.objects.get(idRegion= region_data['idRegion'])
       region_serializer =  RegionSerializer( region, data= region_data )
       if  region_serializer.is_valid():
          region_serializer.save()
          return JsonResponse("Updated Successfully", safe=False)
       return JsonResponse("Failed To Update")	
 elif request.method == 'DELETE':
		  region = Region.objects.get(idEvenement=pk)
		  region.delete()
		  return JsonResponse(" region has been Deleted Successfully", safe=False)				

@csrf_exempt
def VisiteurAPI(request ):

 if request.method == 'POST':
       visiteur_data = JSONParser().parse(request)
       mdp=visiteur_data["motDePasse"]
       visiteur_data["motDePasse"]=make_password(mdp,hasher='bcrypt')
       visiteur_serializer = VisiteurSerializer(data=visiteur_data)
       visiteur=Visiteur.objects.filter(email=visiteur_data["email"])
       vis_ser= VisiteurSerializer(visiteur,many=True)
       if  visiteur_serializer.is_valid():
            if vis_ser.data==[]:  
             visiteur_serializer.save()
             return JsonResponse("creating visiteur Successfully", safe=False)
            return JsonResponse("user with the same email already exists", safe=False)
       return JsonResponse("error",safe=False)
 elif request.method == 'GET':
    email = request.GET.get("email")
    motDePasse = request.GET.get("motDePasse")
    hashed_password = make_password(motDePasse, hasher='bcrypt')
    visiteur = Visiteur.objects.filter(email=email)
    if visiteur.exists():
        if check_password(motDePasse, visiteur[0].motDePasse):
            return JsonResponse("Login successful", safe=False)
        else:
            return JsonResponse("Wrong password", safe=False)
    else:
        return JsonResponse("Unknown user", safe=False)
    
    
    
 elif request.method == 'PUT':
       visiteur_data = JSONParser().parse(request)
       visiteur =Visiteur.objects.get(email=visiteur_data['email'])
       visiteur_serializer = VisiteurSerializer(visiteur, data=visiteur_data )
       if  visiteur_serializer.is_valid():
         if check_password( visiteur_data["motDePasse"],visiteur.motDePasse):
           visiteur_serializer.save()
           return JsonResponse("Updated Successfully", safe=False)
       return JsonResponse("Failed To Update", safe=False)
       
 elif request.method == 'DELETE':
          visiteur_data = JSONParser().parse(request)
          visiteur = Visiteur.objects.get(email=visiteur_data['email'])
          if check_password( visiteur_data["motDePasse"],visiteur.motDePasse):
           visiteur.delete()
           return JsonResponse("visiteur has been deleted Successfully", safe=False)
          return JsonResponse("visiteur has not been Deleted Successfully", safe=False)				
            
