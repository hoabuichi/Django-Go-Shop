from django.views.generic.base import TemplateView


class CustomerListView(TemplateView):
    template_name = 'customer/customer.tpl.html'
