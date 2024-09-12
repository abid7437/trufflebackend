from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import generics, status,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer,LoginSerializer
from django.conf import settings
import jwt

def aboutUs(request):
    return HttpResponse("Welcome to New django website aboutus")

def login(request):
    data={
        'title':'Login Page',
        'LoopData':['one','two','three']
    }
    return render(request,"login.html",data)

def changepassword(request):
    return HttpResponse("Welcome to New django website aboutus")

def dashboard(request):
    return render(request,"dashboard.html")

def users(request):
      users = User.objects.all()  # Query all users from the existing table
      print(users)
      return render(request, 'users.html', {'users': users})
      print(users)

def profile(request):
    return HttpResponse("profile")

def userDetail(request,userid):
    return HttpResponse(userid)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(RegisterSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email,password=password)
                if user is not None and isinstance(user, User):
                       refresh = RefreshToken.for_user(user)
                       return Response({'access': str(refresh.access_token),'refresh': str(refresh)}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)