# -*-coding: utf-8-*-
from django.db import connection
from django.template import Template, Context

class QuerStatistic (object):
    
    def process_response(self, request):
        if request.META['CONTENT_TYPE'] != 'text/html':
            return response
        
        
        
        