"""
    Created by: Bhavya Agrawal
"""


# Django
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
#Local Django
from .models import Team, Match, Player
from .forms import MatchForm

######################Team Views #######################################
class TeamListView(ListView):

    """Summary

    Attributes:
        queryset (TYPE): Description
        template_name (str): Description
    """

    queryset = Team.objects.all()
    template_name = 'cricket/team_list.html'

###################### Player Views #######################################

class PlayersListView(ListView):

    """Summary

    Attributes:
        queryset (TYPE): Description
        template_name (str): Description
    """

    template_name = 'cricket/player_list.html'
    queryset = Player.objects.all()

    def get_queryset(self):
        """Summary

        Returns:
            TYPE: Description
        """
        return Player.objects.filter(team__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        """Summary

        Args:
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        context = super().get_context_data(**kwargs)
        team_name = Team.objects.get(slug=self.kwargs['slug'])
        context['slug'] = team_name
        return context



###################### Match Views #######################################


class MatchFixtureView(ListView):

    """Summary
    
    Attributes:
        queryset (TYPE): Description
    """
    
    queryset = Match.objects.all()



class MatchCreateView(CreateView):

    """Summary

    Attributes:
        form_class (TYPE): Description
        model (TYPE): Description
    """

    model = Match
    form_class = MatchForm

    def get_success_url(self):
        """Summary

        Returns:
            TYPE: Success url
        """
        return reverse('matches-list')



class MatchUpdateView(UpdateView):

    """Summary

    Attributes:
        form_class (TYPE): Form Class
        model (TYPE): Model class
    """

    model = Match
    form_class = MatchForm

    def get_success_url(self):
        """Summary

        Returns:
            TYPE: Success url
        """

        return reverse('matches-list')



class PointTableView(ListView):

    """Summary

    Attributes:
        queryset (TYPE): Description
        template_name (str): Description
    """

    template_name = 'cricket/point_table.html'

    def get_queryset(self):
        """Summary

        Returns:
            TYPE: object of Team class
        """
        return Team.objects.all()