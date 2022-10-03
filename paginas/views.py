from django.views.generic import TemplateView

#create a template views
class IndexView(TemplateView):
    template_name = 'index.html'