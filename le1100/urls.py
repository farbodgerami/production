from django.urls import path
from . import views
urlpatterns = [
    # ina too leitneraction hastand
    path("userlevels/", views.LevellistByUser.as_view(), name="levels"),
   
# ina nistand
 
    path("wordlist/", views.Wordlist.as_view(), name="words"),
    path("Worddetail/<int:id>/", views.Worddetail.as_view(), name="words"),
    path("createWordarray/", views.createWordarray.as_view(), name="words"),
]


 