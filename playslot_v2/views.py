from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from playslot_v2.serializers import SignUpSerializer,BookingSerializer

from playslot_v2.models import Bookings_v2

# Create your views here.
class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = SignUpSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            user_object = User.objects.create_user(**cleaned_data)

            serializer_inst = SignUpSerializer(user_object)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_instance.errors)
            

class BookingListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = Bookings_v2.objects.all()

        serializer_instance = BookingSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = BookingSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            start_time = cleaned_data.get("time")

            duration = cleaned_data.get("duration")

            end_time = (datetime.combine(datetime.today(), start_time)+ timedelta(hours=duration)).time()

            qs = Bookings_v2.objects.create(**cleaned_data,end_time=end_time)

            serializer_instance = BookingSerializer(qs)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

class BookingRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

        authentication_classes = [authentication.BasicAuthentication]

        permission_classes = [permissions.IsAuthenticated]

        serializer_class = BookingSerializer

        queryset = Bookings_v2.objects.all()




         


