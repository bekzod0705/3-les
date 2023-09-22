from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .serializers import TeacherSerializer
from .models import TeacherModel
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminPermissionClass,StaffPermissionClass
# Create your views here.

# class Create(APIView):
#     def post(self,request):
#         if str(request.user)!='AnonymousUser':
#             if request.user.roles==2:
#                 serializer=TeacherSerializer(data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#         else:
#             return Response({'msg':'only for staff members'})
class Create(generics.CreateAPIView):
    queryset=TeacherModel.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=(IsAuthenticated,StaffPermissionClass)
        
# class List(APIView):
#     def get(self,request):
#         print(request.user)
#         if str(request.user)=='AnonymousUser':
#             return Response({'msg':'log in !!'})
#         all=TeacherModel.objects.filter(ismarried=True)
#         serializer=TeacherSerializer(all,many=True)
#         return Response(serializer.data)
class List(generics.ListAPIView):
    serializer_class=TeacherSerializer
    permission_classes=(IsAuthenticated,)
    def get_queryset(self):
        return TeacherModel.objects.filter(ismarried=True)

# class Update(APIView):
#     def patch(self,request,*args,**kwargs):
#         if str(request.user)!='AnonymousUser':
#             if request.user.roles==3:
#                 news=get_object_or_404(TeacherModel,id=kwargs['teacher_id'])
#                 serializer=TeacherSerializer(news,data=request.data,partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#         else:
#             return Response({'msg':'only admins can change !!'})
class Update(generics.RetrieveUpdateDestroyAPIView):
    queryset=TeacherModel.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=(IsAuthenticated,AdminPermissionClass)