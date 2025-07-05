
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from tracker.serializers.tracker_serializers import ExpenseIncomeSerializer

from .models import ExpenseIncome
from rest_framework import viewsets


# Create your views here.



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)

        try:
            validate_password(password)
        except ValidationError as e:
            return Response({'error': e.messages}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User registered successfully'}, status=201)
    

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseIncome.objects.all()
    serializer_class = ExpenseIncomeSerializer