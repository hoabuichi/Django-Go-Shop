from django.views.generic.base import TemplateView
from django.http import JsonResponse


class DashBoardView(TemplateView):
    template_name = 'dashboard/dashboard.tpl.html'

    def post(self, request, *args, **kwargs):
        campaign_name = 1
        return JsonResponse({"status": 2, "msg": 'ok'})
