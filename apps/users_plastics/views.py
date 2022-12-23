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
      for index, category in enumerate(categories, start=1):
        key = "category_" + str(index)
        reportUnits[key] = {
          "value": 0,
          "label": category.name
        }
        for consumption in consumptions.filter(plastic__category=category.id):
          reportUnits[key]["value"] = reportUnits[key]["value"] + consumption.units
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

      for index, category in enumerate(categories, start=1):
        key = "category_" + str(index)
        reportWeight[key] = {
          "value": 0,
          "label": category.name
        }
        for consumption in consumptions.filter(plastic__category=category.id):
          reportWeight[key]["value"] = reportWeight[key]["value"] + consumption.units * consumption.plastic.unit_weight
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
      for index, presentation in enumerate(presentations, start=1):
        key = "presentation_" + str(index)
        reportUnits[key] = {
          "value": 0,
          "label": presentation.name
        }
        for consumption in consumptions.filter(plastic__presentation=presentation.id):
          reportUnits[key]["value"] = reportUnits[key]["value"] + consumption.units
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
      for index, presentation in enumerate(presentations, start=1):
        key = "presentation_" + str(index)
        reportWeight[key] = {
          "value": 0,
          "label": presentation.name
        }
        for consumption in consumptions.filter(plastic__presentation=presentation.id):
          reportWeight[key]["value"] = reportWeight[key]["value"] + consumption.units * consumption.plastic.unit_weight
      return Response(reportWeight, status = status.HTTP_200_OK)
    except:
      return Response({'error': 'Error de formato'}, status = status.HTTP_400_BAD_REQUEST)