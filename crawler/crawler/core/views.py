# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.template  import RequestContext

def login(request):
   return render_to_response('login.html',
       context_instance=RequestContext(request)
   )
