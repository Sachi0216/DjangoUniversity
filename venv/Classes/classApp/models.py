from django.db import models

title_choices = {
    ('Math','Math'),
    ('English','English'),
    ('Science','Science'),
    ('History','History')
}

class djangoClasses(models.Model):
    title = models.CharField(max_length=30, choices=title_choices)
    InstructorName = models.CharField(max_length=30, default="", blank=True, null=False)
    courseNumber = models.IntegerField()
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title
