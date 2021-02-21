from django.db import models
from django.contrib.auth.models import User


class player(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    current_level = models.IntegerField(default=1)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    profile_url = models.URLField(default="")

    def __str__(self):
        return self.name


class level(models.Model):
    l_number = models.IntegerField()
    display_image = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', default='')
    display_audio = models.BooleanField(default=False)
    audio = models.FileField(upload_to='audio', blank=True, default='')
    display_video = models.BooleanField(default=False)
    video = models.FileField(upload_to='video', blank=True, default='')
    text = models.TextField()
    hint = models.TextField(default="na")
    answer = models.CharField(max_length=200)
    numuser = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0)
    wrong = models.IntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.l_number, self.text)


class config(models.Model):
    totallevel = models.IntegerField(default=30)
    numlevel = models.IntegerField(default=30)
    countdown = models.BooleanField(default=False)
    time = models.CharField(max_length=40, default=1)

    def __str__(self):
        return "App Level Configuration"
