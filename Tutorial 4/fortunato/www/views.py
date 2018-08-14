from .person import Person

from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def __init__(self, *args, person=None, **kwargs):
        if person is None:
            person = Person(None, None)
        self.person = person
        super().__init__(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['fortune'] = self.person.get_fortune()
        return context_data
