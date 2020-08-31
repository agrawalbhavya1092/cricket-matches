"""Summary
"""
from django.db import models


class Team(models.Model):

    """Summary
    
    Attributes:
        club_state (TYPE): Description
        logo_uri (TYPE): Description
        name (TYPE): Description
        slug (TYPE): Description
    """
    
    slug = models.SlugField(max_length=255, unique=True, db_column='cr_team_slug', null=True)
    name = models.CharField(max_length=255, db_column='cr_team_name', unique=True)
    logo_uri = models.CharField(null=True, db_column='cr_team_logo_uri', max_length=255)
    club_state = models.CharField(null=True, db_column='cr_team_club_state', max_length=255)


    def __str__(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        return self.name

    class Meta:

        """Summary

        Attributes:
            db_table (str): Description
        """

        db_table = 'cr_team_tbl'



class PlayerHistory(models.Model):

    """Summary
    
    Attributes:
        fifties (TYPE): Description
        highest_scores (TYPE): Description
        hundreds (TYPE): Description
        matches (TYPE): Description
        run (TYPE): Description
    """
    
    matches = models.CharField(max_length=255, db_column='cr_player_matches')
    run = models.CharField(max_length=255, db_column='cr_player_run')
    highest_scores = models.CharField(max_length=255, db_column='cr_player_highest_scores')
    fifties = models.CharField(max_length=255, db_column='cr_player_fifties')
    hundreds = models.CharField(max_length=255, db_column='cr_player_hundreds')


    class Meta:

        """Summary
        
        Attributes:
            db_table (str): Description
        """
        
        db_table = 'cr_player_history_tbl'

class Player(models.Model):

    """Summary
    
    Attributes:
        country (TYPE): Description
        firstname (TYPE): Description
        image_uri (TYPE): Description
        jersey_number (TYPE): Description
        lastname (TYPE): Description
        player_history (TYPE): Description
        slug (TYPE): Description
        team (TYPE): Description
    """
    
    slug = models.SlugField(max_length=255, unique=True, db_column='cr_player_slug', null=True)
    firstname = models.CharField(max_length=255, db_column='cr_player_firstname')
    lastname = models.CharField(max_length=255, db_column='cr_player_lastname')
    image_uri = models.CharField(null=True, db_column='cr_player_image_uri', max_length=255)
    jersey_number = models.CharField(db_column='cr_player_jersey_number', max_length=255)
    country = models.CharField(db_column='cr_team_club_state', max_length=255)
    player_history = models.OneToOneField(PlayerHistory, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='cr_player_team')



    def __str__(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        return self.firstname + ' ' + self.lastname

    class Meta:

        """Summary
        
        Attributes:
            db_table (str): Description
        """
        
        db_table = 'cr_player_tbl'



class Match(models.Model):

    """Summary
    
    Attributes:
        CHOICES (tuple): Description
        schedule_date (TYPE): Description
        status (TYPE): Description
        team1 (TYPE): Description
        team2 (TYPE): Description
        winner_team (TYPE): Description
    """
    
    CHOICES = (('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Draw', 'Draw'), ('Cancelled', 'Cancelled'))
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='cr_match_team1', related_name='match_team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='cr_match_team2', related_name='match_team2')
    winner_team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='cr_match_winner', related_name='cr_match_winner', null=True, blank=True)
    schedule_date = models.DateField(db_column='CG_URM_MODIFICATION_DT', null=True)
    status = models.CharField(choices=CHOICES, db_column='cr_match_status', null=True, max_length=100, default=CHOICES[0][1])



    def __str__(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        return self.team1.name + ' VS ' + self.team2.name

    class Meta:

        """Summary

        Attributes:
            db_table (str): Description
        """

        db_table = 'cr_match_tbl'

