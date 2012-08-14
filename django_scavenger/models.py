from django.db import models
from django.db.models.signals import post_save
from django.utils import simplejson
import os, string, random, urllib, urllib2
from simplescavenger import settings

class Clue(models.Model):
	text = models.TextField()
	code_url = models.URLField(null=True, blank=True)
	number = models.PositiveIntegerField(default=0)
	location = models.TextField(null=True, blank=True)
	hint = models.TextField(null=True, blank=True)
	keyword = models.CharField(max_length=32, null=True, blank=True)
	url_slug = models.CharField(max_length=32, null=True, blank=True, unique=True)
	short_url = models.URLField(max_length=32, null=True, blank=True)
	next_clue = models.OneToOneField('self', related_name='prev_clue', blank=True, null=True)
	
	def __unicode__(self):
		return 'Clue #%i: %s' % (self.number, self.location)

def finish_clue(sender, instance, created, **kwargs):
	if created:
		if not instance.url_slug:
			instance.url_slug = os.urandom(16).encode('hex')
		if not instance.keyword:
			instance.keyword = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(8))
		if not instance.short_url:
			long_url = urllib.quote_plus('http://%s/clue/%s' % (settings.DOMAIN, instance.url_slug))
			r = urllib2.Request('http://is.gd/create.php?format=simple&url=%s' % long_url,)
			opener = urllib2.build_opener()
			f = opener.open(r)
			instance.short_url = f.read()
		if not instance.code_url:
			instance.code_url = 'http://api.qrserver.com/v1/create-qr-code/?size=%s&data=%s' % (settings.QR_CODE_SIZE, instance.short_url)
		instance.save()

post_save.connect(finish_clue, sender=Clue)