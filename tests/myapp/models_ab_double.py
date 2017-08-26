# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AbTestTable(models.Model):
    my_col1 = models.IntegerField(primary_key=True)
    my_col2 = models.CharField(blank=True, null=True)
    m3 = models.NullBooleanField()
    m4 = models.VarField(blank=True, null=True)  # This field type is a guess.
    m5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    m6 = models.DoubleField(blank=True, null=True)  # This field type is a guess.
    m7 = models.FloatField(blank=True, null=True)  # This field type is a guess.
    m8 = models.TextField(blank=True, null=True)
    m9 = models.DateTimeField(blank=True, null=True)
    m10 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_test_table'
