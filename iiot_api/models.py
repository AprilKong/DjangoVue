from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name

# Create your models here.
class Device(models.Model):
    # identifier for records
    device_id = models.IntegerField()
    steam_pool_id = models.IntegerField()
    #status registers
    auto_run = models.BooleanField()
    temp_hold = models.BooleanField()
    valve_mannal = models.BooleanField()
    sensor_alarm = models.BooleanField()
    valve_auto = models.BooleanField()
    running_light = models.BooleanField()
    # status registers  --- for power off only
    enable_schedule = models.BooleanField()
    # word registers
    temp = models.IntegerField()
    temp_time_count = models.IntegerField()
    current_step = models.IntegerField()
    target_temp = models.IntegerField()
    target_rate = models.IntegerField()
    target_time = models.IntegerField()
    estimated_temp = models.IntegerField()
    pid_output = models.IntegerField()
    heating_count = models.IntegerField()
    ad_temp = models.IntegerField()
    # word registers  --- for power off only
    valve_count = models.IntegerField()
    craft_selection = models.IntegerField()

    # metadata for records
    add_time = models.DateTimeField(auto_now_add=True)
    upload_time = models.DateTimeField()


