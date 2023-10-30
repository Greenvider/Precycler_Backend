from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Member, Stores, Inquiry
from .serializers import MemberSerializer, StoreSerializer, InquirySerializer
from .qrcheck import qrck
from haversine import haversine
from geopy.geocoders import Nominatim

@csrf_exempt
@api_view(['POST'])
def register(request): #가입 api
    req = request.data
    serializer = MemberSerializer(data=req)
    search_mid = req['mid']
    passw = req['password']
    if (not any(char.isalpha() for char in passw)) or (not any(char.isdigit() for char in passw)) or (len(passw) < 8) or (len(passw) > 15): #비밀번호 양식 확인
        return Response('rpas') #양식 불일치시 응답
    for pname in Member.objects.values('mid'): #아이디 중복 확인
        if "{'mid': '%s'}"%search_mid in "%s"%pname:
            return Response('alr') #아이디 중복 시 응답
    if serializer.is_valid():
        serializer.save()
        return Response('ok') #가입완료시 응답
    return Response('error') #양식이 올바르지 않을때 응답

@csrf_exempt
@api_view(['POST'])
def inquiry(request): #문의 api
    req = request.data
    serializer = InquirySerializer(data=req)
    if serializer.is_valid():
        serializer.save()
        return Response('ok') #문의완료시 응답
    return Response('error') #양식이 올바르지 않을때 응답
    
@csrf_exempt
@api_view(['GET'])
def Store(request): #가게 목록 api (정렬X)
    snippets = Stores.objects.all()
    serializer = StoreSerializer(snippets, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST']) #가게 정렬 목록 api
def map(request):
    data = request.data
    ulat = data['lat']
    ulog = data['log']
    a = [0] * len(Stores.objects.values('name','latitude','longitude','location'))
    c = 0
    for pname in Stores.objects.values('name','latitude','longitude','location'):
        print(pname)
        m = (round(float(ulat),7),round(float(ulog),7))
        n = (round(pname['latitude'],7),round(pname['longitude'],7))
        dis = haversine(m,n,unit='m')
        b = {}
        b['nl'] = pname['name']+"|"+pname['location']
        b['dis'] = dis
        a[c] = b
        c = c+1
    d = sorted(a, key=lambda x: x["dis"])
    return Response(d, content_type=u"application/json; charset=utf-8") #리스트 반환

@csrf_exempt
@api_view(['POST']) #가게 정렬 목록 api
def addr(request):
    data = request.data
    ulat = data['lat']
    ulog = data['log']
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = str(geolocoder.reverse(str(ulat)+", "+str(ulog)))
    a = address.split(', ')
    return Response(a[5] + "시 " + a[4] + " " + a[3], content_type=u"application/json; charset=utf-8") #리스트 반환

@csrf_exempt
@api_view(['POST']) #로그인 api
def login(request):
    data = request.data
    search_mid = data['mid']
    b = {}
    for pname in Member.objects.values('mid','name'):
        print(pname)
        b[pname['mid']] = pname['name']
    print(b)
    for pname in Member.objects.values('mid'): #아이디가 올바른지 확인
        if "%s"%pname in "{'mid': '%s'}"%search_mid:
            obj = Member.objects.get(mid=search_mid)
            if data['password'] == obj.password:
                return Response('match') #로그인 성공시 응답
            else:
                return Response('mismatch') #비밀번호가 올바르지 않을때 응답
    return Response('misid') #아이디가 올바르지 않을때 응답

@csrf_exempt
@api_view(['POST']) #이름,포인트 확인 api
def point(request):
    data = request.data
    search_mid = data['mid']
    obj = Member.objects.get(mid=search_mid)
    return Response(obj.name+"|"+str(obj.point), content_type=u"application/json; charset=utf-8") #이름, 포인트 문자열로 반환


@api_view(['POST'])
@csrf_exempt
def qr(request): #qr처리 api
    data = request.data
    search_mid = data['mid']
    qrcode = data['image']
    obj = Member.objects.get(mid=search_mid)
    a = qrck(qrcode) #qr코드 처리
    if a == "error":
        return Response('error1') #qr인식 실패시 응답
    elif a == "precycler_bus":
        obj.point = obj.point + 10 #포인트 추가
        obj.save()
        return Response('bus') #bus탑승 시 응답
    elif a == "precycler_ecoact":
        obj.point = obj.point + 20 #포인트 추가
        obj.save()
        return Response('ecoact') #환경활동 시 응답
    elif "precycler_use" in a:
        b = a[14:]
        if obj.point >= int(b):
            obj.point = obj.point - 10   #int(b) #포인트 차감
            obj.save()
            return Response("use_"+ "10") #  b) #포인트 사용시 응답
        return Response('nom') #포인트 사용 시도, 포인트 부족 시 응답
    else:
        return Response('error2') #다른 qr인식 시 응답
