from customer.models import Customer
from django.views.generic.base import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


class AddCustomer(TemplateView):
    template_name = 'customer/add_customer.tpl.html'

    def post(self, request, *args, **kwargs):
         context = super(AddCustomer, self).get_context_data(**kwargs)
         if request.FILES['customer_image']:
             customer_image = request.FILES['customer_image']
             fs = FileSystemStorage()
             filename = fs.save(customer_image.name, customer_image)
             uploaded_file_url = fs.url(filename)
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         image_url = uploaded_file_url
         age = request.POST['age']
         customer = Customer.objects.create(first_name = first_name, last_name = last_name, image_url = image_url, age = age)
         try:
            customer.save()
         except:
              return render(request, self.template_name, context=context)
         else:
              return redirect('customer:customer')

