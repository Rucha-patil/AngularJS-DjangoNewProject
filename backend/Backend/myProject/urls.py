from rest_framework import routers
from myProject.views import EmployeeViewSet

router = routers.SimpleRouter()
router.register(r'Employee', EmployeeViewSet)
urlpatterns = router.urls