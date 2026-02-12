from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BirinchiListCreateAPiView,IkkinchiListCreateAPiView,UchinchiViewSet,TortinchiViewSet

router = DefaultRouter()
router.register("salom3", UchinchiViewSet)
router.register("salom4", TortinchiViewSet)

urlpatterns = [
    path('birinchi/', BirinchiListCreateAPiView.as_view(), name='birinchi-list-create'),
    path('ikkinchi/',IkkinchiListCreateAPiView.as_view(), name = 'ikkinchi-list-create'),
    path('uchinchi/', include(router.urls)),
    path('tortinchi/',include(router.urls))
]
