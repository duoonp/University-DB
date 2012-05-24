#from django.views.generic.simple import direct_to_template
import os
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.defaults import *
from students.views import *

site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',
# Browsing
    (r'^$', main_page),
    (r'^students/$', students_list),
    (r'^groups/$', groups_list),
    (r'^group/([^\s]+)/$', students_list),
# Managing
    (r'^students/add/$', student_add),
    (r'^students/add/([^\s]+)/$', student_add),
    (r'^groups/add/$', group_add),
    (r'^edit/([^\s]+)/([^\s]+)/$', edit_data),
    (r'^delete/([^\s]+)/([^\s]+)/$', delete_data),
    
    
    (r'^editview/$', DataUpdate.as_view()),
  #  (r'^about/', AboutView.as_view()),
    
    
# Session managment
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
# Adminpage
    (r'^admin/', include(admin.site.urls)),
)
