
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
    """ Page Add audit """
    model = Audit
    template_name = 'audit/addAudit.html'
    success_url = '/add-audit/'
    form_class = AuditForm

    # ExploitFormSet = modelformset_factory(Exploit, form=ExploitForm, extra=5)
    # exploit_form_set_class = ExploitFormSet()


    def post(self, request):
        if request.method == 'POST':
            audit = AuditForm(request.POST)
            print(audit.data)
            if audit.is_valid():
                audit.save()
                reverse_lazy('add-audit')
                
                # audit.save(commit=False)
                # exploits = self.ExploitFormSet(request.POST, initial={'audit': self.audit})
                # for exploit in exploits:
                #     if exploit.is_valid():
                #         exploit.save





    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['exploit_form_set'] = self.exploit_form_set_class
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

