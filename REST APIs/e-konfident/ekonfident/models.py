from django.db import models

class Submission(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    who = models.CharField(max_length=200)
    what = models.CharField(max_length=2000)
    where = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.id) + " " + self.who + " " + self.what + " " + self.where