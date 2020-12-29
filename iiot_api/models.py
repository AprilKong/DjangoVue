from __future__ import unicode_literals
from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, null=True)
    information = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class Device(models.Model):
    # identifier for records
    STATUS = (
        ('A', 'Active'),
        ('O', 'Offline'),
    )
    company_id = models.ForeignKey(
        'Company', on_delete=models.SET_NULL, null=True, related_name='devices')
    mac_address = models.CharField(max_length=100, null=True)
    ip_address = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=1, choices=STATUS)
    register_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class SteamPool(models.Model):
    STATUS = (
        ('A', 'Active'),
        ('O', 'Offline'),
    )
    device_id = models.ForeignKey(
        'Device', on_delete=models.SET_NULL, null=True,related_name='steampools')
    status = models.CharField(max_length=1, choices=STATUS)
    create_time = models.DateTimeField(auto_now_add=True)


class PoolInfo(models.Model):
    steampool_id = models.ForeignKey(
        'SteamPool', on_delete=models.SET_NULL, null=True,related_name="pool_status")
    # status registers
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
    create_time = models.DateTimeField(auto_now_add=True)
    collect_time = models.DateTimeField()


class SystemInfo(models.Model):
    device_id = models.ForeignKey(
        'Device', on_delete=models.SET_NULL, null=True,related_name='system_status')
    steam_ad = models.IntegerField()
    steam_pressure = models.IntegerField()
    air_ad = models.IntegerField()
    air_pressure = models.IntegerField()
    temp_first_step_craft_1 = models.IntegerField(default=0)
    temp_rate_first_step_craft_1 = models.IntegerField(default=0)
    duration_first_step_craft_1 = models.IntegerField(default=0)
    temp_second_step_craft_1 = models.IntegerField(default=0)
    temp_rate_second_step_craft_1 = models.IntegerField(default=0)
    duration_second_step_craft_1 = models.IntegerField(default=0)
    temp_third_step_craft_1 = models.IntegerField(default=0)
    temp_rate_third_step_craft_1 = models.IntegerField(default=0)
    duration_third_step_craft_1 = models.IntegerField(default=0)

    temp_first_step_craft_2 = models.IntegerField(default=0)
    temp_rate_first_step_craft_2 = models.IntegerField(default=0)
    duration_first_step_craft_2 = models.IntegerField(default=0)
    temp_second_step_craft_2 = models.IntegerField(default=0)
    temp_rate_second_step_craft_2 = models.IntegerField(default=0)
    duration_second_step_craft_2 = models.IntegerField(default=0)
    temp_third_step_craft_2 = models.IntegerField(default=0)
    temp_rate_third_step_craft_2 = models.IntegerField(default=0)
    duration_third_step_craft_2 = models.IntegerField(default=0)

    temp_first_step_craft_3 = models.IntegerField(default=0)
    temp_rate_first_step_craft_3 = models.IntegerField(default=0)
    duration_first_step_craft_3 = models.IntegerField(default=0)
    temp_second_step_craft_3 = models.IntegerField(default=0)
    temp_rate_second_step_craft_3 = models.IntegerField(default=0)
    duration_second_step_craft_3 = models.IntegerField(default=0)
    temp_third_step_craft_3 = models.IntegerField(default=0)
    temp_rate_third_step_craft_3 = models.IntegerField(default=0)
    duration_third_step_craft_3 = models.IntegerField(default=0)

    temp_first_step_craft_4 = models.IntegerField(default=0)
    temp_rate_first_step_craft_4 = models.IntegerField(default=0)
    duration_first_step_craft_4 = models.IntegerField(default=0)
    temp_second_step_craft_4 = models.IntegerField(default=0)
    temp_rate_second_step_craft_4 = models.IntegerField(default=0)
    duration_second_step_craft_4 = models.IntegerField(default=0)
    temp_third_step_craft_4 = models.IntegerField(default=0)
    temp_rate_third_step_craft_4 = models.IntegerField(default=0)
    duration_third_step_craft_4 = models.IntegerField(default=0)
    temp_forth_step_craft_4 = models.IntegerField(default=0)
    temp_rate_forth_step_craft_4 = models.IntegerField(default=0)
    duration_forth_step_craft_4 = models.IntegerField(default=0)
    temp_fifth_step_craft_4 = models.IntegerField(default=0)
    temp_rate_fifth_step_craft_4 = models.IntegerField(default=0)
    duration_fifth_step_craft_4 = models.IntegerField(default=0)
    temp_sixth_step_craft_4 = models.IntegerField(default=0)
    temp_rate_sixth_step_craft_4 = models.IntegerField(default=0)
    duration_sixth_step_craft_4 = models.IntegerField(default=0)
    temp_seventh_step_craft_4 = models.IntegerField(default=0)
    temp_rate_seventh_step_craft_4 = models.IntegerField(default=0)
    duration_seventh_step_craft_4 = models.IntegerField(default=0)
    temp_eighth_step_craft_4 = models.IntegerField(default=0)
    temp_rate_eighth_step_craft_4 = models.IntegerField(default=0)
    duration_eighth_step_craft_4 = models.IntegerField(default=0)
    temp_ninth_step_craft_4 = models.IntegerField(default=0)
    temp_rate_ninth_step_craft_4 = models.IntegerField(default=0)
    duration_ninth_step_craft_4 = models.IntegerField(default=0)
    temp_tenth_step_craft_4 = models.IntegerField(default=0)
    temp_rate_tenth_step_craft_4 = models.IntegerField(default=0)
    duration_tenth_step_craft_4 = models.IntegerField(default=0)

    pid_sample_rate = models.IntegerField(null=True) #采样时间
    pid_proportional_gain = models.IntegerField(null=True) #比例增益
    pid_integral_gain = models.IntegerField(null=True) #积分增益
    pid_differential_gain = models.IntegerField(null=True) #微分增益
    pid_control_mode = models.IntegerField(null=True) #控制模式
    pid_no_action_range = models.IntegerField(null=True) #不动作范围
    pid_output_upper_limit = models.IntegerField(null=True) #输出上限
    pid_output_lower_limit = models.IntegerField(null=True) #输出下限
    pid_integral_upper_limit = models.IntegerField(null=True) #积分上限
    pid_integral_lower_limit = models.IntegerField(null=True) #积分下限

    create_time = models.DateTimeField(auto_now_add=True)
    collect_time = models.DateTimeField()


class AlarmHistory(models.Model):
    TYPES = (
        ('W', 'Warning'),
        ('E', 'Error')
    )
    STATES = (
        ('A','Active'),
        ('R','Resolved')
    )
    steampool_id = models.ForeignKey(
        'SteamPool', on_delete=models.SET_NULL, null=True,related_name='pool_alarms')
    alarm_type = models.CharField(max_length=1, choices=TYPES)
    sevirity = models.PositiveSmallIntegerField() # 1,2,3,4
    currnt_state = models.CharField(max_length=1, choices=STATES)
    alarm_title = models.CharField(max_length=200) # 報警内容
    create_time = models.DateTimeField(auto_now_add=True)
    resolved_time = models.DateTimeField()
