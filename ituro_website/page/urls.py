from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from page.views import HomePageView, FAQPageView, ContactPageView, PageView


urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^(?P<page>[-_\w]+)/(?P<title>[-_\w]+)/$', PageView.as_view()),
    url(r'^faq/$', FAQPageView.as_view()),
    url(r'^contact/$', ContactPageView.as_view()),
]
