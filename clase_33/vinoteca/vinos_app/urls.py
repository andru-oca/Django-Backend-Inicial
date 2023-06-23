from django.urls import path , include
from .views import VinosListView, VinosCreateView , VinosDetailView ,VinosDeleteView ,VinosUpdateView

from .router import router

app_name = 'vinos'

urlpatterns = [

    path('', VinosListView.as_view(),name="all") ,
    path('<int:pk>/detail/', VinosDetailView.as_view(),name="vino_detail") ,
    path('<int:pk>/update/', VinosUpdateView.as_view(),name="vino_actualizar") ,
    path('<int:pk>/delete/', VinosDeleteView.as_view(),name="vino_borrado") ,
    path('crear/', VinosCreateView.as_view(),name="vino_crear") ,
    
] + router.urls