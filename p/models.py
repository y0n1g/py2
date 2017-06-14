from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(unique=True, max_length=200)
    parent_team = models.ForeignKey(
        'self',
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="sub_teams",
        related_query_name="sub_team",
     )

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Player(models.Model):
    last_update = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    special_time = models.DateTimeField(blank=True, null=True)
    special_int = models.PositiveIntegerField(default=0)
    special_bool = models.BooleanField(default=True)
    s_char = models.CharField(blank=True, null=True,  max_length=3)
    name = models.CharField(unique=True, max_length=200)
    email = models.EmailField(blank=True,)
    team = models.ManyToManyField(
        Team,
        default=None,
        blank=True,
        #null=True,
        #on_delete=models.CASCADE,
     )

    #def __str__(self):              # __unicode__ on Python 2
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

