from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from playslot.models import Bookings,Turf
from playslot.serializers import BookingSerializer
# Create your views here.
class BookingsListCreateView(APIView):

    def get(self,request):

        qs = Bookings.objects.all()

        serializer_instance = BookingSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self, request):

            form_data = request.data

            serializer_instance = BookingSerializer(data=form_data)

            if serializer_instance.is_valid():

                cleaned_data = serializer_instance.validated_data

                Bookings.objects.create(**cleaned_data)

                response_data = {
                    "status": "booked"
                }

                return Response(data=response_data)

            else:

                return Response(data=serializer_instance.errors)

            

class BookingsRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk):

        qs = Bookings.objects.get(id=pk)

        serializer_instance = BookingSerializer(qs)

        return Response(serializer_instance.data)
    

    def put(self,request,pk):

         form_data = request.data

         serializer_instance = BookingSerializer(data=form_data)

         if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Bookings.objects.filter(id=pk).update(**cleaned_data)

            response_data = {
                "status": "updated"
            }

            return Response(data=response_data)

         else:

            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):

        Bookings.objects.get(id=pk).delete()

        response_data = {
            "status": "deleted"
        }

        return Response(data=response_data)