from employer import views
from django.urls import path
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('employer/register',views.EmployerView,basename="register"),
router.register('job/register',views.JobsView,basename="jobs"),


urlpatterns=[
                # path("account/signup", views.UserCreationView.as_view()),

            ]+router.urls