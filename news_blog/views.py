from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.views import generic, View
from django.views.generic import ListView, CreateView
from .models import NewsBlog
from .forms import NewsForm


# Create your views here.


class NewsList(ListView):
    """ VIEW FOR LIST OF NEWS """
    model = NewsBlog
    queryset = model.objects.all()
    # paginate_by = 4
    template_name = "news_blog/news_list.html"


class NewsDetails(CreateView):
    """
    RENDER THE DETAILS OF NEWS
    """
    model = NewsBlog

    def get(self, request, title_id, *args, **kwargs):
        model = NewsBlog
        queryset = model.objects.all()
        new = get_object_or_404(queryset, pk=title_id)

        return render(
            request,
            "news_blog/new_details.html",
            {
               "new": new,
            },
        )


@method_decorator(staff_member_required, name='dispatch')
class NewsEntry(SuccessMessageMixin, CreateView):
    """ VIEW FOR ADD A NEWs """
    template_name = 'admin/add_news.html'
    model = NewsBlog
    form_class = NewsForm

    def get_success_url(self):
        return self.request.path
