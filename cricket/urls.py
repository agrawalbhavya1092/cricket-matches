from django.urls import path
from .views import TeamListView, PlayersListView, MatchFixtureView,\
    MatchCreateView, MatchUpdateView, PointTableView


urlpatterns = [
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('matches/', MatchFixtureView.as_view(), name='matches-list'),
    path('points/', PointTableView.as_view(), name='points-table'),
    path('schedulematch/', MatchCreateView.as_view(), name='schedule-match'),
    path('updatematch/<pk>', MatchUpdateView.as_view(), name='update-match'),
    path('teamplayers/<slug>', PlayersListView.as_view(), name='team-details'),
]