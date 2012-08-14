from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from main_app.models import Clue

def index(request):
	return render_to_response('index.html', {}, context_instance=RequestContext(request))
	
def view_clue(request, clue_slug):
	c = get_object_or_404(Clue, url_slug=clue_slug)
	if request.method == 'POST':
		if request.POST['keyword']:
			if request.POST['keyword'] == c.keyword:
				return render_to_response('clue_user.html', {'clue': c}, context_instance=RequestContext(request))
		return render_to_response('clue_form.html', {'message': 'Incorrect keyword!'}, context_instance=RequestContext(request))
	else:
		return render_to_response('clue_form.html', {'request': request}, context_instance=RequestContext(request))
		
@login_required
def admin_view_clue(request, clue_id):
	c = get_object_or_404(Clue, id=clue_id)
	nc = c.next_clue
	return render_to_response('clue_admin.html', {'clue': c, 'next_clue': nc}, context_instance=RequestContext(request))