from django.views import View
from django.http import HttpResponse, JsonResponse
from django.http.response import FileResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils.http import urlquote
from django.core.files.storage import FileSystemStorage
import json
import os, shutil
import os
import subprocess



class IndexView(View):

    def get(self, request):
        dummy_data = {
            'name': 'jinwoo',
            'type': 'person',
            'job': 'students',
            'age': 25
        }
        return JsonResponse(dummy_data)


    def post(self, request):
        # print(request.headers)
        # print(request.body)
        # print(request.FILES)
        
        files = request.FILES['file']
        path = default_storage.save('./uploads/test.onnx', ContentFile(files.read()))

        cmd = "python -m onnx_connx "+ "uploads/test.onnx"

        # file_name = files[0].name
        # print(file_name)
        # destination = open(os.path.join("./upload", file_name), 'wb+')
        # path = "python -m onnx_connx "+ "upload/"+file_name
        out = subprocess.run(cmd, shell=True, check= True,capture_output=True,text=True)

        shutil.make_archive("connx","zip","out")

        name = "model.connx"

        # path = "out/model.connx"
        path = "out.zip"

        File_exists = os.path.exists(path)
        if File_exists == True:
            file = open(path, 'rb')
            response = FileResponse(file)

            response[
                'Content-Disposition'] = 'attachment;filename="%s"' % urlquote(
                    name)

            return response

    def put(self, request):
        return HttpResponse("Put 요청을 잘받았다")

    def delete(self, request):
        return HttpResponse("Delete 요청을 잘받았다")

        