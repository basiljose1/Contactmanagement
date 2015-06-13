from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .forms import ContactForm, EmailForm
from .models import Name
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.files import File
from django.template import RequestContext, Context
from django.core.urlresolvers import reverse
from django.contrib import messages


from django.core.mail import send_mail, BadHeaderError

import xlrd  
from contacts.models import Document,Group
from contacts.forms import DocumentForm

def index(request):
    return render(request, 'contacts/index.html')



#def register(request):
  #  return HttpResponse("Hello world")

def register(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ffirst_name = form.cleaned_data['first_name']
            flast_name = form.cleaned_data['last_name']
            femail = form.cleaned_data['email']
            fdob = form.cleaned_data['dob']
            fgender = form.cleaned_data['gender']
            forganization = form.cleaned_data['organization']
            p = Name(first_name=ffirst_name, last_name=flast_name, email=femail, dob=fdob, gender=fgender, organization=forganization )
            p.save()
            messages.success(request, 'Profile details updated.')
            form = ContactForm()
            return render(request, 'contacts/contact_form.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

test ='c'

def list(request):    
   if request.method == 'POST':
      form = DocumentForm(request.POST, request.FILES)
      if form.is_valid():
         newdoc = Document(docfile = request.FILES['docfile'])
         newdoc.save()
         newdoc = newdoc.docfile.name
         newdoc = str(newdoc)
         wb = xlrd.open_workbook(newdoc)
         sh = wb.sheet_by_index(0)
         c = 1
         while c < len(sh.col(0)):
            ffirst_name = sh.col_values(0)[c]
            flast_name = sh.col_values(1)[c]
            femail = sh.col_values(2)[c]
            fdob = str(sh.col_values(3)[c])
            fgender = sh.col_values(4)[c]
            forganization = sh.col_values(5)[c]
            p = Name(first_name=ffirst_name, last_name=flast_name, email=femail, dob='1984-10-26', gender=fgender, organization=forganization )
            p.save()
            c=c+1
         # Redirect to the document list after POST
      return HttpResponseRedirect(reverse('contacts.views.list'))
   else:
      form = DocumentForm() # A empty, unbound form

   # Load documents for the list page
   documents = Document.objects.all()
   # Render list page with the documents and the form
   return render_to_response(
       'contacts/list.html',
       {'documents': documents, 'form': form, 'test': test,},
       context_instance=RequestContext(request)
   )



def contactview(request):
            print ("called")
            if request.method == 'POST':
                form = EmailForm(request.POST)
                if form.is_valid():
                    cd = form.cleaned_data
                    name = form.cleaned_data['name']
                    email = form.cleaned_data['email']
                    pass_word = form.cleaned_data['pass_word']
                    subject = form.cleaned_data['topic']
                    fgroup_name = form.cleaned_data['group_name']
                    message = form.cleaned_data['message']
                    to=[]
                    g=Group.objects.get(group_name=fgroup_name)
                    c=0
                    while (c<g.people.count()):
                        to=[g.people.all()[c]]
                        c=c+1
                        print(to)
                        if subject and message and email:
                            try:
                                send_mail(subject, message, email, to, auth_user=email, auth_password=pass_word)
                            except BadHeaderError:
                                return HttpResponse('Invalid header found.')
                    return HttpResponseRedirect('')
                else:
                    return render(request, 'contacts/contacts.html', {'form': form})
                return render(request, 'contacts/contacts.html', {'form': form})
            else:
                form = EmailForm()
                return render(request, 'contacts/contacts.html', {'form': form})
