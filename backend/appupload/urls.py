from django.urls import path

from .views import FileUploadView

urlpatterns = [
    path('file-s3/', FileUploadView.as_view(), name='upload-to-s3'),
]
