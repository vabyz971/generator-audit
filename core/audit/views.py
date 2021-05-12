
from django.forms.models import modelformset_factory
from django.views.generic import TemplateView,ListView, DetailView, CreateView
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


from .forms import AddNewUserForm, AuditForm, ExploitForm
from .models import Audit, Exploit


class HomeView(TemplateView):

    template_name = "audit/dashboard.html"
    title = 'Générateur D\'audit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
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
    template_name = 'audit/addAudit.html'
    success_url = '/add-audit/'
    form_class = AuditForm

    ExploitFormSet = modelformset_factory(Exploit, form=ExploitForm, extra=3)
    exploit_form_set_class = ExploitFormSet()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def post(self,request):
        if self.form_valid:
            exploits = self.ExploitFormSet(request.POST)
            for exploit in exploits:
                exploit.instance.audit = self.model
                if exploit.is_valid():
                    exploit.save()



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exploit_form_set'] = self.exploit_form_set_class
        return context

class AuditListView(ListView):
    model = Audit
    template_name = 'audit/audit_list.html'
    context_object_name = 'audits'

class AuditDetailView(DetailView):

    model = Audit
    template_name = 'audit/audit_detail.html'
    context_object_name = 'audit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exploits = Exploit.objects.filter(audit=self.kwargs.get('pk'))
        context['exploits'] = exploits
        return context

