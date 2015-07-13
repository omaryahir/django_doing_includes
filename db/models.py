from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(verbose_name=u'Nombre', max_length=50)
    last_name = models.CharField(verbose_name=u'Apellido', max_length=50)
    initials = models.CharField(verbose_name=u'Iniciales', max_length=10)

    def save(self, *args, **kwargs):
        prueba_py = open('db/prueba.py','r')
        super(Person, self).save(*args, **kwargs)
        exec(prueba_py)
        print self.initials

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Otro(models.Model):
    otrocampo = models.CharField("otro campo", max_length=50)
    person = models.ForeignKey(Person)

    class Meta:
        verbose_name = "Otro"
        verbose_name_plural = "Otros"

    