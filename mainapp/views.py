import json
from datetime import datetime

from django.http import HttpResponse
from django.views.generic import TemplateView

from config.settings import BASE_DIR, STATICFILES_DIRS


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["range"] = range(5)
        context["card_title"] = "Awesome card title"
        context["card_date_time"] = datetime.now()
        context["card_short_text"] = "Short description title or now short..."
        with open("static/json/data.json", encoding="utf-8") as json_file:
            posts = json.load(json_file)
        context["posts"] = posts
        return context

    template_name = "mainapp/news.html"


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
