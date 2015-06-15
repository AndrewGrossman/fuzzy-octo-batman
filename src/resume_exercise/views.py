from django.views import generic
from django.shortcuts import redirect

class HomePage(generic.TemplateView):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_anonymous():
            return redirect('resume:main')  #FIXME: This should be a reverse or resolve
        else:
            return super(HomePage, self).get(request, *args, **kwargs)


class AboutPage(generic.TemplateView):
    template_name = "about.html"
