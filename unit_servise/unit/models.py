from django.db import models
from django.contrib.postgres.fields import ArrayField


class UnitTypes(models.TextChoices):
    Event = 'EVENT',
    Task = 'TASK'


class Status(models.TextChoices):
    New = "NEW"
    OnModeration = "ON_MODERATION"
    Open = "OPEN"
    Closed = "CLOSED"


class ResponseStatus(models.TextChoices):
    New = "NEW"
    Accepted = "ACCEPTED"
    Rejected = "REJECTED"


class UnitModel(models.Model):
    unit_id = models.BigAutoField(primary_key=True)
    reporter_id = models.BigIntegerField() 
    unit_type = models.CharField(max_length=5, choices=UnitTypes.choices)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.New)
    tags = ArrayField(models.CharField(max_length=50, blank=True))
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    duedate = models.DateTimeField() 
    # я хз что тут надо вписать
    _file = models.FileField(upload_to ='uploads/') 
    assignee =  models.BigIntegerField() 
    # и тут тоже
    solution_file = models.FileField(upload_to ='uploads/')


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    _file = models.FileField(upload_to ='uploads/') 
    date =  models.DateTimeField() 
    author_id = models.BigIntegerField()
    unit_id = models.ForeignKey(UnitModel)


class Responses(models.Model):
    application_id = models.BigAutoField(primary_key=True)
    message = models.CharField(max_length=500)
    status = models.CharField(max_length=12, choices=ResponseStatus.choices, default=ResponseStatus.New)
    date = models.DateTimeField() 
    unit_id = models.ForeignKey(UnitModel)
