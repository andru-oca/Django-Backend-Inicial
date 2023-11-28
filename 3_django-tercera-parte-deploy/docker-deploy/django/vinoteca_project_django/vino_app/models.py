from django.db import models

# Create your models here.

class Vino(models.Model):
    nombre      =   models.CharField(max_length=100)
    valor       =   models.DecimalField(max_digits=12 , decimal_places=2, default = 1000.99)
    abv         =   models.FloatField(blank=False, null=False)
    locacion    =   models.CharField(max_length=100)
    
    
    class Meta:
        db_table = "table_vino_app"
        
    def __str__(self):
        return f"{self.nombre} - Locacion{self.locacion}"
    
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]