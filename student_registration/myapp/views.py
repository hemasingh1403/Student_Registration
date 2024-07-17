from django.shortcuts import render ,redirect
from .models import Student
import os
# Create your views here.

def student_view(request):
    if request.method=='POST':
        n=request.POST.get('name')
        c=request.POST.get('course')
        a=request.POST.get('age')
        g=request.POST.get('gender')
        q=request.POST.get('res')
        i=request.FILES.get('imgs')
        print(n,c,a)
        sv=Student(name=n,course=c,age=a,gender=g,qualification=q,img=i)
        sv.save()
    im=Student.objects.all()
    return render(request,'stu.html',{'im':im})
def edit_view(request,id):
    if request.method=='POST':
        m=Student.objects.get(id=id)
        img=m.img
        if 'imgs' in request.FILES:
            new_img = request.FILES['imgs']
            if m.img:
                print("22222222222222")
                if os.path.isfile(m.img.path):
                    os.remove(m.img.path)
            img=new_img

        n=request.POST.get('name')
        c=request.POST.get('course')
        a=request.POST.get('age')
        g=request.POST.get('gender')
        q=request.POST.get('qualification')        
        m.name=n
        m.course=c
        m.age=a
        m.gender=g
        m.qualification=q
        m.img=img
        m.save()
        return redirect('/')
    im=Student.objects.get(id=id)
    return render(request,'edit.html',{'im':im})
    

def delete_view(request,id):
    dd=Student.objects.get(id=id)
    dd.delete()
    os.remove(dd.img.path)
    return redirect('/')