from django.db import models

# Create your models here.

class Vino(models.Model):
    
    nombre  = models.CharField(max_length=200)
    rating  = models.PositiveSmallIntegerField(blank=False,null=False)
    abv     = models.FloatField(blank=True, null=True)
    zona    = models.CharField(max_length=200)
    
    class Meta:
        db_table = "vino_tabla_django"

    def __str__(self):
        return f"El vino: {self.nombre} con rating {self.abv}"
    
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
        
        