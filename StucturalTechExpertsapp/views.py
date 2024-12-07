from urllib import request

from django.shortcuts import render, redirect

from StucturalTechExpertsapp.forms import QuoteForm, ContactForm
from StucturalTechExpertsapp.models import Contact, Quote, Comment, Member


# Create your views here.
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def blog_details(request):
    if request.method == 'POST':
        comment = Comment(
            name=request.POST['name'],
            email=request.POST['email'],
            website=request.POST['website'],
            comment = request.POST['comment']
        )

        comment.save()
        return redirect('/comment')
    else:
        return render(request, 'blog-details.html')

def comment(request):
    Comments = Comment.objects.all()
    return render(request, 'comment.html', {'comments': Comments})

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('/comment')

def contact(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message = request.POST['message']
        )

        contact.save()
        return redirect('/show/contact/')
    else:
        return render(request, 'contact.html')

def show_contact(request):
    Contacts = Contact.objects.all()
    return render(request, 'show-contact.html', {'contacts': Contacts})

def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/show/contact/')



def index(request):
    if request.method == 'POST':
        quote = Quote(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message = request.POST['message']
        )

        quote.save()
        return redirect('quote')
    else:
        return render(request, 'index.html')

def quote(request):
    Quotes = Quote.objects.all()
    return render(request, 'quote.html', {'quotes': Quotes})

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
            username = request.POST['username'],
            password = request.POST['password']
        ).exists():
            return render(request,'index.html')
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

def delete_quote(request, id):
    quote = Quote.objects.get(id=id)
    quote.delete()
    return redirect('/quote')

def edit_quote(request, id):
   editquote = Quote.objects.get(id=id)
   return render(request, 'edit.html', {'quote':editquote})

def update_quote(request, id):
    updateinfo = Quote.objects.get(id=id)
    form = QuoteForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/quote')
    else:
        return render(request, 'edit.html')

def edit(request, id):
   editcontact = Contact.objects.get(id=id)
   return render(request, 'edit-contact.html', {'contact':editcontact})

def update(request, id):
    updatecontact = Contact.objects.get(id=id)
    form = ContactForm(request.POST, instance=updatecontact)
    if form.is_valid():
        form.save()
        return redirect('/show/contact')
    else:
        return render(request, 'edit-contact.html')



def project_details(request):
    return render(request,'project-details.html')

def project(request):
    return render(request,'projects.html')

def service_details(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request,'services.html')

def register(request):
    if request.method == 'POST':
        members = Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')

def login(request):
    return render(request,'login.html')
def portfolio(request):
    return render(request,'portfolio.html')
def starter_page(request):
    return render(request,'starter-page.html')




