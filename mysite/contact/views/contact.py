from django.views.generic.base import TemplateView


class ContactView(TemplateView):
    template_name = 'contact/contact.tpl.html'
