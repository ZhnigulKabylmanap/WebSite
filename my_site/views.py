from django.shortcuts import render
from.forms import TouristForm
from.models import Art
from.models import Lab4
from.models import Sport

def home(reguest):
   form=TouristForm()
   if reguest.method=='POST':
       print(reguest.POST)
       form=TouristForm(reguest.POST)
       if form. is_valid():
           form.save()
   context = {'form': form}

   return render(reguest,'my_site/p1.html',context)


def about(reguest):
    sport=Sport.objects.order_by('-id')
    return render(reguest, 'my_site/p2.html',{'sport':sport})

def hi(reguest):
  return render(reguest, 'my_site/p3.html')


def art(reguest):
    art = Art.objects.order_by('-id')
    return render(reguest, 'my_site/p4.html',{'art':art})

def intro(reguest):
    return render(reguest, 'my_site/p5.html')

def movie(reguest):
    return render(reguest, 'my_site/p6.html')

def test(reguest):
    return render(reguest, 'my_site/p7.html')


from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

def index(request):
    shelf = Lab4.objects.all()
    return render(request, 'my_site/p8.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'my_site/p9.html', {'upload_form':upload})
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'my_site/p9.html', {'upload_form':book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')





from .forms import AddPostForm
from my_site import models


def addpage(request):

    if request.method == "GET":
        form = AddPostForm()
        return render(request, "my_site/addpage.html", {"form":form})
    else:
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop("Password")
            models.Lab4.objects.create(**data)
            return redirect("/index")
        else:
            clear_errors = form.errors.get("__all__")

        context={"form": form}
        return render(request, "my_site/addpage.html", context)

'''
from django.core.mail import send_mail
def send_message(request):
    send_mail("Web programming: back end","My account","200103272@stu.sdu.edu.kz",['200103272@stu.sdu.edu.kz'],
              fail_silently=False,html_message="<b> Bold text </b> <i> Italic text </i> <p>hello</p>")
    return render(request,'my_site/mail.html')'''



from django.core.mail import EmailMessage
def send_message(request):
    email=EmailMessage("Zhainigul","Here is a picture for you","200103272@stu.sdu.edu.kz",['200103272@stu.sdu.edu.kz'],headers={'Message-ID':'foo'})
    email.attach_file('C:/WebFinal/picture.jpg')
    email.send(fail_silently=False) 
    return render(request,'my_site/mail.html')


