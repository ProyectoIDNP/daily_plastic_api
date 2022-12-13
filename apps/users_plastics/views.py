from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from ..users_plastics.models import User_Plastic
from ..plastics.models import Category, Presentation

class ReportCategoryUnit(APIView):
  permission_classes = [permissions.AllowAny]

  def get(self, request):
    try: 
      user = request.query_params.get('user')
      consumptions = User_Plastic.objects.all()
      categories = Category.objects.all()
      if user is not None:
        consumptions = consumptions.filter(user=user)
      reportUnits = {}
      for category in categories:
        reportUnits[category.name] = 0
        for consumption in consumptions.filter(plastic__category=category.id):
          reportUnits[category.name] = reportUnits[category.name] + consumption.units
      return Response(reportUnits, status = status.HTTP_200_OK)
    except:
      return Response({'error': 'Error de formato'}, status = status.HTTP_400_BAD_REQUEST)  


class ReportCategoryWeight(APIView):
  permission_classes = [permissions.AllowAny]

  def get(self, request):
    try: 
      user = request.query_params.get('user')
      consumptions = User_Plastic.objects.all()
      categories = Category.objects.all()
      if user is not None:
        consumptions = consumptions.filter(user=user)
      reportWeight = {}
      for category in categories:
        reportWeight[category.name] = 0
        for consumption in consumptions.filter(plastic__category=category.id):
          reportWeight[category.name] = reportWeight[category.name] + consumption.units * consumption.plastic.unit_weight
      return Response(reportWeight, status = status.HTTP_200_OK)
    except:
      return Response({'error': 'Error de formato'}, status = status.HTTP_400_BAD_REQUEST)


class ReportPresentationUnit(APIView):
  permission_classes = [permissions.AllowAny]

  def get(self, request):
    try: 
      user = request.query_params.get('user')
      consumptions = User_Plastic.objects.all()
      presentations = Presentation.objects.all()
      if user is not None:
        consumptions = consumptions.filter(user=user)
      reportUnits = {}
      for presentation in presentations:
        reportUnits[presentation.name] = 0
        for consumption in consumptions.filter(plastic__presentation=presentation.id):
          reportUnits[presentation.name] = reportUnits[presentation.name] + consumption.units
      return Response(reportUnits, status = status.HTTP_200_OK)
    except:
      return Response({'error': 'Error de formato'}, status = status.HTTP_400_BAD_REQUEST)  


class ReportPresentationWeight(APIView):
  permission_classes = [permissions.AllowAny]

  def get(self, request):
    try: 
      user = request.query_params.get('user')
      consumptions = User_Plastic.objects.all()
      presentations = Presentation.objects.all()
      if user is not None:
        consumptions = consumptions.filter(user=user)
      reportWeight = {}
      for presentation in presentations:
        reportWeight[presentation.name] = 0
        for consumption in consumptions.filter(plastic__presentation=presentation.id):
          reportWeight[presentation.name] = reportWeight[presentation.name] + consumption.units * consumption.plastic.unit_weight
      return Response(reportWeight, status = status.HTTP_200_OK)
    except:
      return Response({'error': 'Error de formato'}, status = status.HTTP_400_BAD_REQUEST)