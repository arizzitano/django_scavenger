from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from main_app.models import Clue
from simplescavenger import settings

def index(request):
	return render_to_response('index.html', {}, context_instance=RequestContext(request))

def view_clue(request, clue_slug):
	c = get_object_or_404(Clue, url_slug=clue_slug)
	if request.method == 'POST':
		if request.POST['keyword']:
			if request.POST['keyword'].lower() == c.prev_clue.keyword.lower():
# 				send_mail('%s Unlocked Clue #%i!' % (c.number, request.POST['name']),
# 				render_to_string('checkin_email.html', {'clue': c, 'hunter': request.POST['name'], 'remaining': (settings.NUM_CLUES - c.number)}),
# 				'tomscavengerhunt@gmail.com',
# 				settings.EMAIL_LIST,
# 				fail_silently=False)
# 				
				return render_to_response('clue_user.html', {'clue': c}, context_instance=RequestContext(request))

		return render_to_response('clue_form.html', {'message': 'Incorrect keyword!', 'clue':c, 'request':request}, context_instance=RequestContext(request))
	else:
		return render_to_response('clue_form.html', {'request': request, 'clue':c}, context_instance=RequestContext(request))
		
@login_required
def admin_view_clue(request, clue_number):
	c = get_object_or_404(Clue, number=clue_number)
	return render_to_response('clue_admin.html', {'clue': c}, context_instance=RequestContext(request))