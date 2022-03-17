from employer.models import CompanyProfile, Jobs
from employer.serializer import EmployerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from employer.serializer import JobSerializer
from users.models import User
from rest_framework import generics, mixins


# Create your views here.

class EmployerView(viewsets.ModelViewSet):
    model = CompanyProfile
    serializer_class = EmployerSerializer
    queryset = CompanyProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        employer = CompanyProfile.objects.all()
        serializer = EmployerSerializer(employer, many=True)
        return Response(serializer.data)


# class UserCreationView(generics.GenericAPIView,
#                        mixins.CreateModelMixin):
#     serializer_class = EmployerSerializer
#     queryset = User.objects.all()
#     model = User
#
#     def get(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class JobsView(viewsets.ModelViewSet):
    model = Jobs
    serializers = JobSerializer
    queryset = Jobs.objects.all()

    def list(self, request, *args, **kwargs):
        job = Jobs.objects.all()
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
