
from django.views.generic import TemplateView, DetailView, DeleteView
from django.views.generic.base import RedirectView
from .forms import AddNewUserForm
# Create your views here.



class HomeView(TemplateView):
    """ Page Home """

    template_name = "audit/dashboard.html"
    title = 'Générateur D\'audit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class LoginUserView(TemplateView):
    """ Page Connexion User """

    template_name = "audit/login.html"

class RegisterUserView(TemplateView):
    """ Page Add new user """

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

class AddAuditView(TemplateView):
    """ Page Add audit """
    pass

class DetailAuditView(DetailView):
    """ Page Detail audit """
    pass

class DeteleAuditView(DeleteView):
    """ Page Remove audit """
    pass
