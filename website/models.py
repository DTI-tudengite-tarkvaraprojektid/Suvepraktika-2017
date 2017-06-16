from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone
from django.core.validators import MinValueValidator

MY_CHOICES = (('Ilukirjandus', 'Ilukirjandus'),
              ('Esseistika', 'Esseistika'),
              ('Epistolaarne kirjandus', 'Epistolaarne kirjandus'),
              ('Memuaristika', 'Memuaristika'),
              ('Kroonikakirjandus', 'Kroonikakirjandus'),
              ('Teaduskirjandus', 'Teaduskirjandus'),
              ('Populaarteaduslik', 'Populaarteaduslik'),
              ('Faktikirjandus', 'Faktikirjandus'),
              ('Teabekirjandus', 'Teabekirjandus'),
              ('Õppekirjandus', 'Õppekirjandus'),
              ('Teatmekirjandus', 'Teatmekirjandus'),
              ('Tarbekirjandus', 'Tarbekirjandus'),
              ('Kommertsteksti', 'Kommertsteksti'),
              ('Poliitiline kirjandus', 'Poliitiline kirjandus'),
              ('Vaimulik kirjandus', 'Vaimulik kirjandus'),
              ('Epitaafid', 'Epitaafid'),
              ('Muusika literatuur', 'Muusika literatuur'))

MY_CHOICES2 = (('Ilukirjandus', 'Ilukirjandus'),
               ('Esseistika', 'Esseistika'),
               ('Epistolaarne kirjandus', 'Epistolaarne kirjandus'),
               ('Memuaristika', 'Memuaristika'),
               ('Kroonikakirjandus', 'Kroonikakirjandus'),
               ('Teaduskirjandus', 'Teaduskirjandus'),
               ('Populaarteaduslik', 'Populaarteaduslik'),
               ('Faktikirjandus', 'Faktikirjandus'),
               ('Teabekirjandus', 'Teabekirjandus'),
               ('Õppekirjandus', 'Õppekirjandus'),
               ('Teatmekirjandus', 'Teatmekirjandus'),
               ('Tarbekirjandus', 'Tarbekirjandus'),
               ('Kommertsteksti', 'Kommertsteksti'),
               ('Poliitiline kirjandus', 'Poliitiline kirjandus'),
               ('Vaimulik kirjandus', 'Vaimulik kirjandus'),
               ('Epitaafid', 'Epitaafid'),
               ('Muusika literatuur', 'Muusika literatuur'))


class Content(models.Model):
	user = models.ForeignKey("auth.User")
	text = models.TextField(default="")
	n_gram = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
	title = models.CharField(max_length=50, default="")
	types = models.CharField(max_length=100, choices=MY_CHOICES, default='Ilukirjandus')
	
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user + "_" + self.created


	# Ilukirjandus, Esseistika, Epistolaarne kirjandus, Memuaristika, Kroonikakirjandus, Teaduskirjandus, Populaarteaduslik, Faktikirjandus
	# Teabekirjandus, Õppekirjandus, Teatmekirjandus, Tarbekirjandus, Kommertsteksti, Poliitiline kirjandus, Vaimulik kirjandus, Epitaafid, Muusika literatuur

