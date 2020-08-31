from django import forms
from django.utils.translation import gettext as _
from .models import Match


class MatchForm(forms.ModelForm):
    """Summary
    Last modified by: Bhavya Agrawal, Sprint 25, JIRA card: COM-994, Date: 21apr2020
    """
    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        self.fields['team1'].empty_label = None
        self.fields['team2'].empty_label = None
        self.fields['status'].empty_label = None
        self.fields['winner_team'].required = False


    class Meta:
        model = Match
        fields = ('team1', 'team2', 'schedule_date', 'status', 'winner_team')
        widgets = {
            'team1': forms.Select(attrs={'class': 'form-control', 'data-toggle': 'tooltip',
                                         'data-placement': 'right',}),
            'team2': forms.Select(attrs={'class': 'form-control', 'data-toggle': 'tooltip',
                                         'data-placement': 'right',
                                                }),
            'winner_team': forms.Select(attrs={'class': 'form-control', 'data-toggle': 'tooltip',
                                               'data-placement': 'right',
                                                }),
            'status': forms.Select(attrs={'class': 'form-control', 'data-toggle': 'tooltip',
                                          'data-placement': 'right',
                                                }),
            'schedule_date': forms.DateInput(attrs={'class': 'form-control',
                                                    'data-toggle': 'tooltip',
                                                    'data-placement': 'right',
                                                    'placeholder': 'YYYY-MM-DD'
            })

        }
