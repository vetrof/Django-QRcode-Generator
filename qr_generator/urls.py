from django.urls import path

from qr_generator.views import generate_qr

# index/qr/...
urlpatterns = [
    path('<path:url>/', generate_qr, name='generate_qr'),
]