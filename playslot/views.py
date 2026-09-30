from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from playslot.models import Bookings
from playslot.serializers import BookingSerializer
# Create your views here.
class BookingsListCreateView(APIView):

    def get(self,request):

        qs = Bookings.objects.all()

        serializer_instance = BookingSerializer(qs,many=True)

        return Response(data=serializer_instance.data)