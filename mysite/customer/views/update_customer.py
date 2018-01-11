from customer.models import Customer
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect


class UpdateCustomer(TemplateView):
    template_name = 'customer/update_customer.tpl.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateCustomer, self).get_context_data(**kwargs)
        customer_id = context['customer_id']
        customer = Customer.objects.get(id = customer_id)
        context.update({
            'customer': customer
        })
        return context

    def post(self, request, *args, **kwargs):
         context = super(UpdateCustomer, self).get_context_data(**kwargs)
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         image_url = request.POST['image_url']
         age = request.POST['age']
         id = context['customer_id']
         customer = Customer(id = id, first_name = first_name, last_name = last_name, image_url = image_url, age = age)
         try:
            customer.save()
         except:
             customer_id = context['customer_id']
             customer = Customer.objects.filter(customer_id=customer_id)
             context.update({
                 'customer': customer
             })
             return render(request, self.template_name, context=context)
         else:
              return redirect('customer:customer')

