from django.db import models

class Film(models.Model):
    """Describes a film or a tv-show."""
    title = models.CharField(max_length=300)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='films', null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        "Return a string representation of the model."
        return self.title


class Entry(models.Model):
    """Describes an entry to a certain Film/show."""
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        if len(self.text)>50:
            return self.text[:50] + '...'
        else:
            return self.text

class Message(models.Model):
    """A message by anonymous users"""
    sender = models.CharField(max_length=30)
    message = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return "message from " + self.sender

