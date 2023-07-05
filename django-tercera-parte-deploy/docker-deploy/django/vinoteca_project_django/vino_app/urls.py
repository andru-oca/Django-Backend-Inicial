
from django.urls import path 

from .views import VinoListView ,\
                        VinoDetailView ,\
                            VinoCreateView ,\
                                VinoUpdateView,\
                                    VinoDeleteView 
                
from .router import router 

app_name = "vinos"

urlpatterns = [
    path("",VinoListView.as_view(),name="all"),
    path("create/",VinoCreateView.as_view(),name="create"),
    path("<int:pk>/detail/",VinoDetailView.as_view(),name="detail"),
    path("<int:pk>/update/",VinoUpdateView.as_view(),name="update"),
    path("<int:pk>/delete/",VinoDeleteView.as_view(),name="delete"),
]

urlpatterns += router.urls