# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Animal(models.Model):
    id = models.SmallAutoField(primary_key=True)
    espece = models.CharField(max_length=40)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    date_naissance = models.DateTimeField()
    nom = models.CharField(max_length=30, blank=True, null=True)
    commentaires = models.TextField(blank=True, null=True)
    espece_0 = models.ForeignKey('Espece', models.DO_NOTHING, db_column='espece_id')  # Field renamed because of name conflict.
    race = models.ForeignKey('Race', models.DO_NOTHING, blank=True, null=True)
    mere = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    pere = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Animal'
        unique_together = (('nom', 'espece_0'),)


class Espece(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nom_courant = models.CharField(max_length=40)
    nom_latin = models.CharField(unique=True, max_length=40)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Espece'


class Livre(models.Model):
    auteur = models.CharField(max_length=50, blank=True, null=True)
    titre = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Livre'


class Race(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=40)
    espece = models.ForeignKey(Espece, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Race'


class Livre(models.Model):
    auteur = models.CharField(max_length=50, blank=True, null=True)
    titre = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livre'
