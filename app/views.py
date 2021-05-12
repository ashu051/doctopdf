from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from django.views.decorators.csrf import csrf_protect
from .models import Document
import mimetypes
from django.conf import settings

from django.http import FileResponse, response
from djangoconvertvdoctopdf.convertor import ConvertFileModelField
from djangoconvertvdoctopdf.convertor import StreamingConvertedPdf
from django.core.files import File
import sys
import os
from docx2pdf import convert
import os
import string
from subprocess import  Popen
LIBRE_OFFICE = "../lib/libreoffice/program/soffice"

def convert_to_pdf(input_docx, out_folder):
    p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir',
               out_folder, input_docx])
    print([LIBRE_OFFICE, '--convert-to', 'pdf', input_docx])
    p.communicate()


@csrf_protect
def index(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        r_file = request.FILES['document']
        form.save()

        return redirect('/')
    else:
        form = DocumentForm()
        # mystring = settings.MEDIA_ROOT
        # string= mystring+'\documents'
        # s = string+"\"+r_file
        file = Document.objects.all()
        # fr =[]
        # for f in file:
        #     fr.append(f.document)
    print('_____________________________________________________________________________________________________')
    print(settings.MEDIA_ROOT)
    return render(request, 'app/index.html', {
        'form': form,
         'file': file
    })
    
def convertpdf(request,id):
    if id is not None:
        pdf = Document.objects.get(id=id)
        r_file = str(pdf.document)
        
        print(r_file)
        p ="AD__SHIV_NARESH__VIMUKTI__SAKIL__KATORA_4tl02tB.docx"
        q="AD__SHIV_NARESH__VIMUKTI__SAKIL__KATORA_4tl02tB.docx"
        if p==q:
            print("**************")
        r_file.replace(" ","_")
        print(r_file[:-5])
        print(r_file[:9])
        print(r_file)
        a,b=r_file.split('/')
        print(a+" "+b)
        finalstring = settings.MEDIA_ROOT+'\\'+a+'\\'+b
        finalstring2 = settings.MEDIA_ROOT+'\\'+a+'\\'+b[:-5]
        final = settings.MEDIA_ROOT+'\\'+a
        convert_to_pdf(finalstring,final)        
        # print(finalstring2)
        # convert(finalstring, 
        # finalstring2+".pdf")
        return render(request,'app/pdf.html',
            {
                'all':pdf
            }
        )
    else:
        all= Document.objects.all()
        return render(request,'app/pdf.html',
            {
                'all':all
            }
        )
def showpdf(request):
    all= Document.objects.all()
    return render(request,'app/all.html',
            {
                'all':all
            }
    )

def downloadfile(request,id):
        pdf = Document.objects.get(id=id)
        r_file = str(pdf.document)
        # print(r_file)
        shuru = r_file[:-5]
        l=len(shuru)
        # print(shuru[0])
        # last=shuru[:9]
        # print(last)
        s=""
        for i in range(0,l):
            if i>9:
                s+=shuru[i]
                
        print(s)
        gg =r_file[:-5]
        print(r_file[:9])
        print(r_file)
        for i in gg:
            if i == '/':
                i='\\'
        print(gg)
        a,b=r_file.split('/')
        print(a+" "+b)
        finalstring = settings.MEDIA_ROOT+'\\'+a+'\\'+b
        finalstring2 = settings.MEDIA_ROOT+'\\'+a+'\\'+b[:-5]
        if r_file != '':
            
        # Define Django project base directory
            # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # Define the full file path
           
            filepath = finalstring2+".pdf"
            print('-------------------------------------------------------------------------------------------------------')
            print(filepath)
            # Open the file for reading content
            path = open(filepath, 'rb')
            print(path)
            # Set the mime type
            mime_type, _ = mimetypes.guess_type(filepath)
            print(mime_type)
            # Set the return value of the HttpResponse
            response = HttpResponse(path, content_type=mime_type)
            print(response)
            # Set the HTTP header for sending to browser
            response['Content-Disposition'] = "attachment; filename=%s.pdf" % s
            # Return the response value
            return response
        else:
            return redirect('/')
# def download_pdf_file(request, filename=''):
#     if filename != '':
#         # Define Django project base directory
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         # Define the full file path
#         filepath = f"C:\\Users\\ashub\\OneDrive\\Desktop\\doctopdf\\doctopdf\\media\\{filename}"
#         # Open the file for reading content
#         path = open(filepath, 'rb')
#         # Set the mime type
#         mime_type, _ = mimetypes.guess_type(filepath)
#         # Set the return value of the HttpResponse
#         response = HttpResponse(path, content_type=mime_type)
#         # Set the HTTP header for sending to browser
#         response['Content-Disposition'] = "attachment; filename=%s" % filename
#         # Return the response value
#         return response
#     else:
#         # Load the template
#         return render(request, 'file.html')
# import comtypes.client
# def index(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()    
#             r_file = request.FILES['document']
#             inst = ConvertFileModelField(r_file)
#             print('******************************************************************')
#             print(inst)
#             r_file = inst.get_content()
#             print("upar")
#             print(r_file)
#             doc_obj = Document()
#             doc_obj.pdf_doc = File(open(r_file.get('path'), 'rb'))
#             doc_obj.pdf_doc.name = r_file.get('name')
#             doc_obj.save()
#             form.save()    
#         return redirect('/')
#     else:
#         form = DocumentForm()
#         file = Document.objects.all()
#         # fr =[]
#         # for f in file:
#         #     fr.append(f.document)
#     return render(request, 'app/index.html', {
#         'form': form,
#          'file': file
#     })
# import docx
# import pypandoc
# # from pypandoc.pandoc_download import download_pandoc

        



# def making_a_doc_function(request):
#     doc = docx.Document()
#     doc.add_heading("MY DOCUMENT")
#     doc.save('thisisdoc.docx')
#     pypandoc.convert_file('thisisdoc.docx', 'pdf', outputfile="thisisdoc.pdf")     
#     pdf = open('thisisdoc.pdf', 'rb')
#     response = FileResponse(pdf) 
# return response





# import sys
# import os
# import comtypes.client
# import argparse

# def wordToPdf(self,file1):
#     wdFormatPDF = 17
#     input_file = os.path.abspath(file1)
#     output_file = os.path.splitext(input_file)[0]+".pdf"
#     output_file = os.path.abspath(output_file)
#         # create COM object
#     word = comtypes.client.CreateObject('Word.Application')
#         # key point 1: make word visible before open a new document
#     word.Visible = True
#         # key point 2: wait for the COM Server to prepare well.
#     time.sleep(3)

#         # convert docx file 1 to pdf file 1
#     doc = word.Documents.Open(input_file)
#     doc.SaveAs(output_file, FileFormat=wdFormatPDF)
#     doc.Close()
#     word.Quit()

#     return output_file
   
