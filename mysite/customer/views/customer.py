from django.views.generic.base import TemplateView
from customer.models import Customer


class CustomerListView(TemplateView):
    template_name = 'customer/customer.tpl.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        customer_list = Customer.objects.all()
        context.update({
            "customer_list": customer_list
        })
        return context
