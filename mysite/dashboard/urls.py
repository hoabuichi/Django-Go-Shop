from django.conf.urls import url
from .views.dashboard import DashBoardView

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', DashBoardView.as_view(), name='dashboard'),
]
