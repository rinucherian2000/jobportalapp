from rest_framework.serializers import ModelSerializer
from employer.models import CompanyProfile,Jobs
from users.models import User
from django.contrib.auth.models import User


class EmployerSerializer(ModelSerializer):
    class Meta:
        model=CompanyProfile
        fields=['id','company_name','services','address']
        read_only_fileds=['id']

# class UserCreationSerializer(ModelSerializer):
#     class Meta():
#         model=User
#         fields=["username","password","email"]
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)



#
class JobSerializer(ModelSerializer):
    class Meta:
        model=Jobs
        fields="__all__"
