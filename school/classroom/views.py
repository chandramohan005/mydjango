from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from .forms import ContactForm
from .models import Teacher
# Create your views here.


class HomeView(TemplateView):
     template_name = 'classroom/home.html'


class ThankyouView(TemplateView):
     template_name = 'classroom/thankyou.html'


class TeacherCreateView(CreateView):
     model = Teacher
     fields = "__all__"
     success_url = reverse_lazy('classroom:thankyou')

class TeacherListView(ListView):
     model = Teacher
     queryset = Teacher.objects.order_by('first_name')
     context_object_name = 'teacher_list'

class TeacherDetailView(DetailView):
       model = Teacher

class TeacherUpdateView(UpdateView):
     model = Teacher
     fields = '__all__'
     success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
     model = Teacher
     success_url = reverse_lazy('classroom:list_teacher')

class ContactFormView(FormView):
     form_class = ContactForm
     template_name = 'classroom/contact.html'
     success_url = reverse_lazy("classroom:thankyou")

     def form_valid(self, form):
          print(form.cleaned_data)
          return super().form_valid(form)
