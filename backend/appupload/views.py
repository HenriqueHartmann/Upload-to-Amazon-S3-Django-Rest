from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from datetime import datetime
from boto3.session import Session
import os
import environ

from .serializers import FileSerializer

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


class FileUploadView(generics.GenericAPIView):

    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.FILES)
        serializer.is_valid(raise_exception=True)

        file_extension = os.path.splitext(str(request.FILES['file']))[1]
        filename = datetime.now().strftime("%d-%m-%YT%H:%M:%S") + file_extension
        session = Session(region_name=env('REGION_NAME'),
                          aws_access_key_id=env('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=env('AWS_SECRET_ACCESS_KEY'))
        s3 = session.resource('s3')
        s3.Bucket(env('BUCKET')).put_object(Key=filename, Body=request.FILES['file'])

        return Response({"message": "Upload Successful"}, status=status.HTTP_200_OK)
