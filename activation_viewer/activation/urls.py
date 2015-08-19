from django.conf.urls import patterns, url

from django.views.generic import TemplateView


urlpatterns = patterns('activation_viewer.activation.views',
    url(r'^$', TemplateView.as_view(template_name='activation_list.html'), name='activation_browse'),
    url(r'^(?P<activation_id>[^/]*)$', 'activation_detail', name="activation_detail"),
)