from customer.models import Customer
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect


class AddCustomer(TemplateView):
    template_name = 'customer/add_customer.tpl.html'

    def post(self, request, *args, **kwargs):
         context = super(AddCustomer, self).get_context_data(**kwargs)
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         image_url = request.POST['image_url']
         age = request.POST['age']
         customer = Customer.objects.create(first_name = first_name, last_name = last_name, image_url = image_url, age = age)
         try:
            customer.save()
         except:
              return render(request, self.template_name, context=context)
         else:
              return redirect('customer:customer')

