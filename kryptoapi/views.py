from django.shortcuts import render,redirect
from rest_framework import generics,permissions
from .models import *
from .serializers import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class CreatedAlerts(generics.ListAPIView):
    model = alert
    serializer_class = ALertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return alert.objects.filter(author=self.request.user,status='created')

class TriggeredAlerts(generics.ListAPIView):
    model = alert
    serializer_class = ALertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return alert.objects.filter(author=self.request.user,status='triggered')

class DeletedAlerts(generics.ListAPIView):
    model = alert
    serializer_class = ALertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return alert.objects.filter(author=self.request.user,status='deleted')


class ListAllAlerts(generics.ListAPIView):
    model = alert
    serializer_class = ALertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return alert.objects.filter(author=self.request.user)

class CreateAlerts(generics.CreateAPIView):
    model = alert
    serializer_class = CreateALertSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self,alert):
        alert.save(author=self.request.user,status = 'created')

    def get_queryset(self):
        return alert.objects.filter(author=self.request.user)

class RetrieveAlert(generics.RetrieveAPIView):
    
    model = alert
    serializer_class = ALertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return alert.objects.filter(author=self.request.user)

class UpdateAlert(generics.UpdateAPIView):
    
    model = alert
    serializer_class = ALertUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self,alert):
        alert.save(status = 'deleted')

    def get_queryset(self):
        return alert.objects.filter(author=self.request.user)





def apply_alert_view(request):
    data = alert.objects.filter(status='created')
    for item in data:
        item.apply_alerts()
        item.save()
        if item.status == 'triggered':
            subject = 'Alert'
            message = f'Hi {item.author.username}, The Price of {item.name} is reached to the target price of {item.threshold}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [item.author.email]
            print(item.author.email)
            send_mail( subject, message, email_from, recipient_list )
    return redirect('listallalerts')

   



# class DeleteAlert(generics.DestroyAPIView):
#     model = alert
#     permissions_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return alert.objects.filter(id=self.kwargs['pk'])



        

def logout(request):
    auth.logout(request)
    return redirect('login')
    
def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = auth.authenticate(username=u,password=p)

        if user is not None:
            auth.login(request, user)
            return redirect('listallalerts')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'kryptoapi/login.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'email is already taken by others')
                return redirect('register')
            elif User.objects.filter(username = uname):
                messages.warning(request, 'Username is taken by others')
                return redirect('register')
            else:
                user = User.objects.create_user(username = uname, email = email, password=password1)
                return redirect('login')
        else:
            messages.warning(request, 'passwords not matching')
            return redirect('register')
        
    else:
        return render(request, 'kryptoapi/register.html')

