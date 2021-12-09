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
        
        if os.path.exists('./out'):
            shutil.rmtree('./out')
        
        if os.path.exists('./uploads'):
            shutil.rmtree('./uploads')

        os.mkdir('./uploads')

        files = request.FILES['file']
        path = default_storage.save('./uploads/test.txt', ContentFile(files.read()))


        os.mkdir('./out')
        result_path = './out/TEST.txt'
        upper = ''
        with open(path, 'r',) as f:
            lines = f.readlines()
            for i, l in enumerate(lines):
                upper += l.upper()

        with open(result_path, 'w') as f:
            f.write(upper)
    
        File_exists = os.path.exists(result_path)
        if File_exists == True:
            # file = open(path, 'rb')
            response = HttpResponse(open(result_path,'rb'), content_type='text/plain')
            response['Content-Disposition'] = 'attachment;filename="TEST.txt"'

            return response

    def put(self, request):
        return HttpResponse("Put 요청을 잘받았다")

    def delete(self, request):
        return HttpResponse("Delete 요청을 잘받았다")

        