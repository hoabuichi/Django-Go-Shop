from django.views.generic.base import TemplateView


class DashBoardView(TemplateView):
    template_name = 'dashboard/dashboard.tpl.html'
