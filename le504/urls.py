from django.urls import path
from . import views
urlpatterns = [
    # ina too leitneraction hastand
    path("userlevels/", views.LevellistByUser.as_view(), name="levels"),
   
# ina nistand
    # path("", views.getlevels, name="levels"),
    # path("levellist/", views.levellist.as_view(), name="levels"),
    # path("level/<int:id>/", views.level.as_view(), name="levels"),
    path("wordlist/", views.Wordlist.as_view(), name="words"),
    path("word/<int:id>/", views.Worddetail.as_view(), name="words"),
    path("createWordarray/", views.createWordarray.as_view(), name="words"),
    # path("deletewords/<int:id>/", views.deleteword, name="words"), 
]


 