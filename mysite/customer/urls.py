from django.conf.urls import url
from .views.customer import CustomerListView

app_name = 'customer'

urlpatterns = [
    url(r'^$', CustomerListView.as_view(), name='customer'),
]