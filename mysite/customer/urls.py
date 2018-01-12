from django.conf.urls import url
from .views.customer import CustomerListView
from .views.add_customer import AddCustomer
from .views.update_customer import UpdateCustomer
from .views.delete_customer import DeleteCustomer
from .views.upload_profile import UploadCustomerProfile

app_name = 'customer'

urlpatterns = [
    url(r'^$', CustomerListView.as_view(), name='customer'),
    url(r'^add$', AddCustomer.as_view(), name='add_customer'),
    url(r'^update/(?P<customer_id>[0-9]+)$', UpdateCustomer.as_view(), name='update_customer'),
    url(r'^delete/(?P<customer_id>[0-9]+)$', DeleteCustomer.as_view(), name="delete_customer"),
    url(r'^upload_profile/(?P<customer_id>[0-9]+)$', UploadCustomerProfile.as_view(), name="upload_profile_customer"),
]