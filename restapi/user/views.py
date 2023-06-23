from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer

from django.contrib.sites.shortcuts import get_current_site  

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.core.mail import EmailMessage 

from .models import User
# Create your views here.


class HomePage(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'msg': f"Authenticatied user {request.user}"}

        return Response(content)



class Register(APIView):

    def post(self, request):
        password = request.data.get('password', None)
        confirm_password = request.data.get('confirm_password', None)
        if not password == confirm_password:
            return Response({'password_mismatch': 'Password fields did not match'}, status.HTTP_400_BAD_REQUEST)

        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data

        current_site = get_current_site(request)  
        mail_subject = 'ECHO account activation'  
        message = render_to_string('acc_active_email.html', {  
            'user': user,  
            'domain': current_site.domain,  
            'uid':urlsafe_base64_encode(bytes(str(user.pk),'utf-8')),  
            'token':account_activation_token.make_token(user),  
        })  
        to_email = [user.email]
        email = EmailMessage(mail_subject, message, to=to_email)
        email.send()
        
        
        return Response(data, status=status.HTTP_201_CREATED)



class Logout(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


class activate(APIView):

    def get(self, request, uidb64, token):
        id = urlsafe_base64_decode(uidb64)
        id = id.decode('utf-8')
        try:
            user = User.objects.get(pk=id)
            if account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return Response({"msg": "Account Activated"}, status.HTTP_200_OK)

            
            return Response({"msg": "Account is already Activated"}, status.HTTP_200_OK)
            
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"msg": "Activation link is invalid"}, status.HTTP_400_BAD_REQUEST)
