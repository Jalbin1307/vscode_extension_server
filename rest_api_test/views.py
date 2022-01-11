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


    @csrf_exempt
    def post(self, request):
        if os.path.exists('./out'):
            shutil.rmtree('./out')
        
        if os.path.exists('./uploads'):
            shutil.rmtree('./uploads')

        os.mkdir('./uploads')
        os.mkdir('./out')
        
        files = request.FILES['file']
        path = default_storage.save('./uploads/test.onnx', ContentFile(files.read()))
         
        cmd = "python -m onnx_connx "+ "uploads/test.onnx"
        out = subprocess.run(cmd, shell=True, check= True,capture_output=True,text=True)

        z = shutil.make_archive("connx","zip","out")

        # path = "out/model.connx"
        path = "connx.zip"
        name = "connx.zip"

    
        File_exists = os.path.exists(path)
        if File_exists == True:
            # file = open(path, 'rb')
            response = HttpResponse(open(path,'rb'), content_type='application/zip')
            response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(name)

            return response

    def put(self, request):
        return HttpResponse("Put 요청을 잘받았다")

    def delete(self, request):
        return HttpResponse("Delete 요청을 잘받았다")

        
