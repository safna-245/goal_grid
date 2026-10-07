from django.urls import path

from playslot_v2.views import SignUpView

from playslot_v2.views import BookingListCreateView,BookingRetrieveUpdateDeleteView

urlpatterns=[
    path("signup/",SignUpView.as_view()),
    path("booking/",BookingListCreateView.as_view()),
    path("booking/<int:pk>/",BookingRetrieveUpdateDeleteView.as_view())
]