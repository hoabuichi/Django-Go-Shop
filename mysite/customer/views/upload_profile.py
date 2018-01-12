from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic.base import TemplateView


class UploadCustomerProfile(TemplateView):
    template_name = 'customer/upload_profile.tpl.html'

    def post(self, request, *args, **kwargs):
        if request.FILES['myfile']:
            my_file = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(my_file.name, my_file)
            uploaded_file_url = fs.url(filename)
            return render(request, 'customer/upload_profile.tpl.html', {
                'uploaded_file_url': uploaded_file_url
            })
