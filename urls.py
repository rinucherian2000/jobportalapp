from candidate import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('candidate/register',views.CandidateViewSet,basename="candidate"),


urlpatterns=[

]+router.urls