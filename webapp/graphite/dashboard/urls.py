from django.conf.urls import *

urlpatterns = patterns('graphite.dashboard.views',
  url('^save/(?P<name>[^/]+)', 'save', name="dashboard.save"),
  url('^load/(?P<name>[^/]+)', 'load', name="dashboard.load"),
  url('^delete/(?P<name>[^/]+)', 'delete', name="dashboard.delete"),
  url('^create-temporary/?', 'create_temporary', name="dashboard.create_temporary"),
  url('^email', 'email', name="dashboard.email"),
  url('^find/', 'find', name="dashboard.find"),
  url('^login/?', 'user_login', name="dashboard.login"),
  url('^logout/?', 'user_logout', name="dashboard.logout"),
  url('^help/', 'help', name="dashboard.help"),
  url('^(?P<name>[^/]+)', 'dashboard', name="dashboard"),
  url('', 'dashboard', name="dashboard"),
)
