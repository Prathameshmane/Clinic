from django.shortcuts import render
from .forms import AppointmentForm
from .models import Blog
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    blogs = Blog.objects.all()

    return render(request,'blog.html', {'blog': blog})

def team(request):
    return render(request,'team.html')

def contact(request):
    return render(request,'contact.html')

def clinics(request):

    return render(request,'clinics.html')

def appointment(request):
    form_class = AppointmentForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            m_number = request.POST.get('m_number')
            date = request.POST.get('date')
            time = request.POST.get('time')
            addr = request.POST.get('addr')
            template = get_template('appointment.txt')

            context = {
                'name' : name,
                'email' : email,
                'm_number' : m_number,
                'date' : date,
                'time' : time,
                'addr' : addr,
            }
            content = template.render(context)

            email = EmailMessage(
                "New Appointment Form Submission",
                content,
                "Your Website" + '',
                ['youremail@gmail.com'],
                headers = {'Reply-To' : contact_email}
            )
            email.send()
            return redirect('appointment_success')

    return render(request,'appointment.html')

def appointment_success(request):
    return render(request,'appointment_success.html')
