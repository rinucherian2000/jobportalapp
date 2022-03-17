from candidate.models import Candidate
from candidate.serializer import CandidateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from employer.serializer import JobSerializer
from employer.models import Jobs


# Create your views here.




class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class =CandidateSerializer
    model=Candidate

    def list(self, request, *args, **kwargs):
        candidate= Candidate.objects.all()
        serializer = CandidateSerializer(candidate, many=True)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        serializer=CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #     api/v1/portal/candidate/matching_jobs
    @action(methods=["GET"], detail=False)
    def matching_jobs(self, request, *args, **kwargs):
        jobs = Jobs.objects.filter(skills__contains=Candidate.skills)
        serializer =JobSerializer(jobs, many=True)
        return Response(serializer.data)
