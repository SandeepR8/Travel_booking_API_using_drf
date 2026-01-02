from django.contrib.auth import authenticate,login
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from .serializers import SeatSerializer,BusSerializer,SignUpSerializers,BookingSerializers,LoginSerializer
from rest_framework import status,generics,viewsets
from rest_framework.views import APIView
from .models import Bus,Seat,Booking
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view,extend_schema
from rest_framework.generics import GenericAPIView

@extend_schema_view(
    post=extend_schema(
    request=SignUpSerializers,
    responses={201:SignUpSerializers},
    description='User register using Username and password (token-authentication)'
),
)
class RegisterView(APIView):
    def post(self,request):
        serializers = SignUpSerializers(data = request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        token, created = Token.objects.get_or_create(user = user)
        return Response({'token':token.key},status=status.HTTP_201_CREATED)
    

@extend_schema(
    request=LoginSerializer,
    responses={200: LoginSerializer},
    description='User login using username and password (token-authentication)'
)
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)
        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.id
            },
            status=status.HTTP_200_OK
        )


@extend_schema_view(
    get=extend_schema(
        responses={200: BusSerializer(many=True)},
        description="List all buses"
    ),
    post=extend_schema(
        request=BusSerializer,
        responses={201: BusSerializer},
        description="Create a new bus"
    )
)  
class BusListCreateView(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    


@extend_schema_view(
    list=extend_schema(
        responses={200: BusSerializer(many=True)},
        description="List all buses"
    ),
    retrieve=extend_schema(
        responses={200: BusSerializer},
        description="Retrieve details of a specific bus"
    ),
    create=extend_schema(
        request=BusSerializer,
        responses={201: BusSerializer},
        description="Create a new bus (admin only)"
    ),
    update=extend_schema(
        request=BusSerializer,
        responses={200: BusSerializer},
        description="Update bus details (admin only)"
    ),
    partial_update=extend_schema(
        request=BusSerializer,
        responses={200: BusSerializer},
        description="Partially update bus details (admin only)"
    ),
    destroy=extend_schema(
        responses={204: None},
        description="Delete a bus (admin only)"
    ),
)
class BusDetailView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Bus.objects.all()
    serializer_class = BusSerializer



class BookingView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        request=BookingSerializers,
        responses={201: BookingSerializers}
    )

    def post(self,request):
        seat_id = request.data.get('seat')
        try:
            seat = Seat.objects.get(id = seat_id)
            if seat.is_booked:
                return Response({
                    'Oops':'Seat already booked'
                },status=status.HTTP_400_BAD_REQUEST
                )
            seat.is_booked = True
            seat.save()

            bookings = Booking.objects.create(
                user = request.user,
                bus = seat.bus,
                seat = seat
            )
            serializers = BookingSerializers(bookings)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        except Seat.DoesNotExist:
            return Response({'error':'Invalid seat id'},status=status.HTTP_400_BAD_REQUEST)
        
class UserBookingView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
            responses={200:BookingSerializers(many=True)}
    )

    def get(self,request,user_id):
        if request.user.id != user_id:
            return Response({'error':'Unauthorised'},status=status.HTTP_403_FORBIDDEN)
        bookings = Booking.objects.filter(user_id = user_id)
        serializers = BookingSerializers(bookings, many = True)

        return Response(serializers.data)
    