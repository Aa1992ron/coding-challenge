# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Sites
from django.shortcuts import redirect, reverse

# Create your views here.
def index(request):
	
	if request.method == 'POST':
		form_name = request.POST.get('new_site_name')
		if form_name != "":
			site = Sites()
			site.website_title = form_name
			site.hits = 0
			site.save()
	
	sites = Sites.objects.all()[:15]

	context = {
		'title': 'Help grow the web with referrals!!',
		'sites': sites,
		'link_text': '',
	}

	return render(request, 'sites/index.html', context)


def delete_site(request, site_id=None):

	if site_id != None:
		site = Sites.objects.get(id=site_id)
		site.delete()

	return redirect('/')

def rename_site(request, site_id=None):
	if request.method == 'POST':
		new_site_title = request.POST.get('site_title')
		if new_site_title != "":
			site = Sites.objects.get(id=site_id)
			site.website_title = new_site_title
			site.save()
	
	return redirect('/')


def landing(request, site_id=None, site_name=None):
	site = Sites.objects.get(id=site_id)
	site.hits += 1
	site.save()
	display_string = "Welcome to the site that says: "+site.website_title+"!"

	context = {
		'title': display_string,
		'link_text': 'Back to Homepage'
	}

	return render(request, 'sites/layout.html', context)

#simple method needed to make the back button work
def home(request):
	return redirect('/')