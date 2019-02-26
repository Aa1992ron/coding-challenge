# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Sites
from django.shortcuts import redirect, reverse

# Create your views here.
def index(request):
	#return HttpResponse('HELLO')
	if request.method == 'POST':
		form_name = request.POST.get('new_site_name')
		print(form_name)
		site = Sites()
		site.website_title = form_name
		site.hits = 0
		site.save()
	
	sites = Sites.objects.all()[:15]

	context = {
		'title': 'Help grow the web with referrals!!',
		'sites': sites,
	}

	return render(request, 'sites/index.html', context)

def delete_site(request, site_id=None):

	site = Sites.objects.get(id=site_id)
	site.delete()

	sites = Sites.objects.all()[:15]

	context = {
		'title': 'Help grow the web with referrals!!',
		'sites': sites,
	}

	return redirect('/')