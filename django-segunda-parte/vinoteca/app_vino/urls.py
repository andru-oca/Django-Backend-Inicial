from django.urls import path 
from .router import router 

from .views import      VinosListView   \
                    ,   VinosDetailView \
                    ,   VinosCreateView \
                    ,   VinosUpdateView \
                    ,   VinosDeleteView

app_name = "vinos"

urlpatterns = [
    path("", VinosListView.as_view(), name="all"),
    path("create/", VinosCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", VinosDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", VinosUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", VinosDeleteView.as_view(), name="delete")
    
]

urlpatterns += router.urls