from django.db import models


class Score(models.Model):
    good = models.IntegerField(default=0)
    bad = models.IntegerField(default=0)

    def __str__(self):
        return "{good: %s, bad: %s}"% (self.good, self.bad)


class Card(models.Model):
    source = models.CharField(max_length=200)
    tr = models.CharField("translation", max_length=200)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)

    def __str__(self):
        return "{id: %s, source: '%s', tr: '%s', score: %s}" % (self.id, self.source, self.tr, self.score)
