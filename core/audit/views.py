
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.db import transaction

from .forms import AddNewUserForm, AuditForm, ExploitFormSet
from .models import Audit, Exploit


class HomeView(TemplateView):

    template_name = "audit/dashboard.html"
    title = 'Dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        audit = Audit.objects.filter(author = self.request.user)
        context['title'] = self.title
        context['audits'] = audit
        return context


class LoginUserView(TemplateView):
    template_name = "audit/login.html"


class RegisterUserView(TemplateView):

    template_name = "audit/register.html"
    form = AddNewUserForm
    title = 'Inscription'

    def post(self, request):
        if request.method == 'POST':
            form = AddNewUserForm(request.POST)
            if form.is_valid():
                form.save()
                return RedirectView("audit:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['title'] = self.title
        return context


class AddAuditView(CreateView):
    model = Audit
    title = 'Ajout d\'un audit '
    template_name = 'audit/addAudit.html'
    form_class = AuditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        # Récuperation des donnés passer dans le post
        if self.request.POST:
            context['exploits'] = ExploitFormSet(self.request.POST)
        else:
            context['exploits'] = ExploitFormSet()

        context['title'] = self.title
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        exploits = context['exploits']
        with transaction.atomic(): 
            form.instance.author = self.request.user
            self.object = form.save()
            if exploits.is_valid():
                exploits.instance.audit = self.object
                exploits.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('audit:detail-audit', kwargs={'pk': self.object.pk})

class UpdateAuditView(UpdateView):
    
    model = Audit
    template_name = 'audit/updateAudit.html'
    form_class = AuditForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        # Récuperation des donnés passer dans le post
        if self.request.POST:
            context['exploits'] = ExploitFormSet(self.request.POST, instance=self.object)
        else:
            context['exploits'] = ExploitFormSet(instance=self.object)

        context['title'] = self.object.name
        return context

    
    def form_valid(self, form):
        context = self.get_context_data()
        exploits = context['exploits']
        with transaction.atomic(): 
            form.instance.author = self.request.user
            self.object = form.save()
            if exploits.is_valid():
                exploits.instance.audit = self.object
                exploits.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('audit:detail-audit', kwargs={'pk': self.object.pk})


class DetailAuditView(DetailView):

    model = Audit
    template_name = 'audit/detailAudit.html'
    context_object_name = 'audit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exploits'] = Exploit.objects.filter(audit=self.kwargs.get('pk'))
        context['title'] = self.object.name
        return context


class DeleteAuditView(DeleteView):

    model = Audit
    success_url = reverse_lazy('audit:home');
    template_name = 'audit/deleteAudit.html'