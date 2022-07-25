from ast import Not
from copy import Error
from logging import exception
 
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes  
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

 
from .serializers import *
# from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

# authentication_classes=[TokenAuthentication]
class UserlistByAdmin(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = Userserializer(users, many=True)
        return Response(serializer.data)
    permission_classes = (IsAdminUser,)

class UserdetailByadmin(APIView):
    def get(self,request, id):
        try:
            users = User.objects.get(id=id)
            serializer = Userserializer(users, many=False)
            return Response(serializer.data)
        except:
            message = {'detail': 'peyda nashod...'}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
    permission_classes = (IsAdminUser,)
    
    def put(self,request, id):
        try:
            user = User.objects.get(id=id)
            data = request.data
            user.username = data['username']
            user.email = data['email']
            user.is_admin = data['isadmin']
            user.save()
            serializer = Userserializer(user, many=False)
            return Response(serializer.data)

        except:
            message = {'detail': 'ایمیل یا نام کاربری تکراری هستند'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
            
    permission_classes = (IsAdminUser,)
    
    def delete(self,request, id):
        userfordeletation = User.objects.get(id=id)
        userfordeletation.delete()
        return Response('user deleted')
    permission_classes = (IsAdminUser,)
 

class UserregisterByuser(APIView):
    def post(self,request):
        data = request.data
        try:
            user = User.objects.create(username=data['username'],
                                            email=data['email'],
                                            password=make_password(data['password']))
            userprofile=Userprofile.objects.get(user_id=user.id)
            serializer = Userprofileserializerwithtoken(userprofile, many=False)
            login(request,user)  
            return Response(serializer.data)
        except:
            message = {'detail': 'user with this detail already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
            
class UserdetailByuser(APIView):
    def get(self,request):
        user = request.user
        serializer = Userserializer(user, many=False)
        return Response(serializer.data)   
    permission_classes = (IsAuthenticated,)
    def put(self,request):
        user = request.user
        # chon mikhaim ke tokene jadid ro ham besaze darim:
        userprofile=Userprofile.objects.get(user_id=user.id)
        serializer = Userprofileserializerwithtoken(userprofile, many=False)
        data = request.data
     
        user.username = data['username']
        user.email = data['email']
        if data['password'] != '':
            user.password = make_password(data['password'])
        user.save()
        return Response(serializer.data)
    permission_classes = (IsAuthenticated,)


 

@api_view(['POST'])
def loginman(request):
     
    from django.contrib.auth import authenticate   
    data = request.data
 
    try:
        username=User.objects.filter(
                email=data["username"]).values()[0]['username']
    except:
        username=data["username"]
    try:
        user = authenticate(
                request,
                username=username,
                password=data["password"])
        userprofile=Userprofile.objects.get(user_id=user.id)
        serializer = Userprofileserializerwithtoken(userprofile, many=False)
        if user is None:
                raise Exception()
        login(request,user)
        
       
        return Response(serializer.data)
    except:
        message = {'detail': 'username or password is wrong'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)



# @permission_classes([IsAuthenticated])
# @api_view(['POST'])
def logoutview(request):
 
    logout(request)
   
    return HttpResponse('loggedout')
         
        
from django.http import HttpResponse
from django.shortcuts import redirect
# import requests
import pip._vendor.requests 
import json
from datetime import date,timedelta
from django.utils import timezone

MERCHANT = '0f4fe3ec-6ea9-4d2e-b69d-7020bee2d130'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"

 
CallbackURL = 'https://fbgerami.ir/api/users/verify/'

def send_request(request,sendedplan,price):
    print(request.user.id)
    # return HttpResponse(uservaset.username )
    global pricevaset
    pricevaset=price

    if request.user.id is None:
      return HttpResponse("اول باید ثبت نام کنید و سپس وارد شوید")
    sendedplanarray=sendedplan.split(',')
    acceptedplans=['lebarrens','lecollins','le504','le800','le3500','le1100']
    for i in sendedplanarray:
      if i not in acceptedplans:
        return HttpResponse("not in accepted plans")
    userprofile=Userprofile.objects.get(user_id=request.user.id)
    userprofile.userplanindu=sendedplan
    userprofile.save()

 
 
    req_data = {
        "merchant_id": MERCHANT,
        "amount": price,
        "callback_url": CallbackURL,
        "description": 'خرید پلن ها',
       "metadata": {"mobile":str(userprofile.phonenumber), "email": userprofile.user.email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = pip._vendor.requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
 
    authority = req.json()['data']['authority']
   
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
     
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
   
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": pricevaset,
            "authority": t_authority
        }
        req = pip._vendor.requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
         
            t_status = req.json()['data']['code']
            if t_status == 100:
                # modiriate planha:
                userprofile=Userprofile.objects.get(user_id=request.user.id)
                userplanindui=userprofile.userplanindu
                userplandinduarray=userplanindui.split(',')
                userplanarray=userprofile.userplan.split(' ')
                for i in userplandinduarray:
                    if i not in userplanarray:
                        userplanarray.append(i)
                listToStr = ' '.join([str(elem) for elem in userplanarray])
                userprofile.userplan=listToStr
                # ezafe kardane etebar:
                currentdate=datetime.date.today()         
                _30days=timedelta(days=30)
                paiduntil=currentdate +_30days
                 
                userprofile.setpaiduntil(paiduntil)
                 
                userprofile.save()
                return HttpResponse('Transaction success.\nRefID: ' + str(
                    req.json()['data']['ref_id']
                ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')
