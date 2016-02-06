from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from page.models import Page


class HomePageView(TemplateView):
    pass


class PageView(TemplateView):
    def get_context_data(self,**kwargs):
        import pdb;pdb.set_trace()
        title = self.kwargs.get("title")
        language_code = settings.LANGUAGE_CODE
        page = self.kwargs.get("page")
        return ""

class FAQPageView(TemplateView):
    pass


class ContactPageView(TemplateView):
    pass
