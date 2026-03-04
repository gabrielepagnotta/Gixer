from django.db import models


class OreInserite(models.Model):
    ore_straordinario = models.IntegerField(blank=True, null=True)
    ore_permesso = models.IntegerField(blank=True, null=True)
    ore_ferie = models.IntegerField(db_column='Ore_ferie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ore_inserite'