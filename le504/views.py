from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import *
from .models import *
from users.models import *
from rest_framework.views import APIView
from rest_framework import status

class LevellistByUser(APIView): 
    
    def get(self,request):
        global wordarray,words,levelobject
        user = request.user
        words=Word.objects.all()
        wordarray=list(words.values())
    
        levels = Levelstring.objects.filter(user=user)
        yechi=list(levels.values())[0]     
        levelobject = json.loads(yechi['level'])  
        for i in wordarray:    
            if str(i['id']) in levelobject:             
                i['level']=levelobject[str(i['id'])]
        return Response(wordarray)
    permission_classes = (IsAuthenticated,)

    def put(self,request):
        changes = request.data

        levels = Levelstring.objects.get(user=request.user)
  
        for itemchange in changes:
            for worditem in wordarray:
                if itemchange['id']==worditem['id']:
                    levelobject[str(worditem['id'])]=itemchange['level']
  
        levels.level = json.dumps(levelobject)
        levels.save()
        return Response('levels updated')
    permission_classes = (IsAuthenticated,)



# @permission_classes([IsAdminUser])
# def getlevels(request):
#     levels = Level.objects.all()
#     serializer = Levelserializer(levels, many=True)
#     return Response(serializer.data)


# class levellist(APIView):
 
#     def post(request):
#         userr = User.objects.get(id=request.data.get('user'))
#         wordr = Word.objects.get(id=request.data.get('word'))
#         levelr = request.data.get('level')
#         level = Level.objects.create(word=wordr, user=userr, level=levelr)
#         serializer = Levelserializer(level, many=False)
#         return Response(serializer.data)
#     permission_classes = (IsAdminUser,)

# class level(APIView):        
#     def put(request, id):
#         level = Level.objects.get(id=id)
#         level.level = request.data.get('level')
#         level.save()
#         serializer = Levelserializer(level, many=False)
#         return Response(serializer.data)
#     permission_classes = (IsAdminUser,)



class Wordlist(APIView):
    def get(self,request):
        word = Word.objects.all()
        serializer = wordsserializer(word, many=True)
        return Response(serializer.data)
    def post(self,request):
        kalamee = request.data['kalame']
        maanie = request.data['maani']
        descriptione = request.data['description']
        audiofilee = request.data['audiofile']

        word = Word.objects.create(kalame=kalamee,
                                maani=maanie,
                                description=descriptione,
                                audiofile=audiofilee)
        serializer = wordsserializer(word, many=False)
        return Response(serializer.data)
    permission_classes = (IsAdminUser,)

class Worddetail(APIView): 
    def delete(self,request,id):
        word=Word.objects.get(id=id)
        word.delete()
        return Response('word deleted')
    permission_classes = (IsAdminUser,)



class createWordarray(APIView):
    def post(self,request):
        wordarray = request.data    
        for i in wordarray:
            kalamee = i['kalame']
            maanie = i['maani']
            descriptione = i['description']
            audiofilee = i['audiofile']
            word = Word.objects.create(kalame=kalamee,
                                maani=maanie,
                                description=descriptione,
                                audiofile=audiofilee)
        return Response('words created')
    permission_classes = (IsAdminUser,)