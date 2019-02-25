# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	#return HttpResponse('HELLO')
	return render(request, 'sites/index.html', {
		'title': 'Help grow the web with referrals!!'
		})
