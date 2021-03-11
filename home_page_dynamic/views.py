from django.shortcuts import render
from .models import Instructors

# Create your views here.

def home(request):
    ins_details = Instructors()
    ins_details.name = 'Charan Teja Pobbathi'
    ins_details.subject = 'devops'
    return render(request,"index.html", {"ins" : ins_details}) 


from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
  
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint.")  
    p.showPage()  
    p.save()  
    return response  