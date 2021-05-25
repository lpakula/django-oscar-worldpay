from django.conf.urls import url, re_path
from django.views.decorators.csrf import csrf_exempt

from worldpay import views


urlpatterns = [
    re_path(r'preview/$', views.PaymentDetailsView.as_view(preview=True), name='worldpay-preview'),
    re_path(r'callback$', csrf_exempt(views.CallbackResponseView.as_view()), name='worldpay-callback'),
    re_path(r'success$', views.SuccessView.as_view(), name='worldpay-success'),
    re_path(r'fail$', views.FailView.as_view(), name='worldpay-fail'),
]
