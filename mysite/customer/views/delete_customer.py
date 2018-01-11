from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from customer.models import Customer


class DeleteCustomer(TemplateView):

    def get(self, request, *args, **kwargs):
        context = super(DeleteCustomer, self).get_context_data(**kwargs)
        customer_id = context['customer_id']
        customer = Customer.objects.filter(id=customer_id)
        customer.delete()
        return redirect('customer:customer')