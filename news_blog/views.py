from django.db.models import Q
from django.contrib import messages

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
    queryset = model.objects.all().order_by('-id')
    paginate_by = 4
    template_name = "news_blog/news_list.html"


class NewsDetails(CreateView):
    """
    RENDER THE DETAILS OF NEWS
    """
    model = NewsBlog
    form = NewsForm()

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


@staff_member_required
def news_edit(request, title_id):
    """ VIEW FOR ADD A NEW WARE """
    form = NewsForm
    new = get_object_or_404(NewsBlog, id=title_id)
    template_name = 'admin/news_edit.html'

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=new)

        if form.is_valid():
            form.save(commit=False)
            form.save()
            messages.success(request, 'The new had been EDIT successfully!')
            return render(request, 'admin/staff_panel.html')
    else:
        form = NewsForm(instance=new)

    return render(request, template_name, {'form': form, 'new': new})


@staff_member_required
def news_delete(request, title_id):
    """ VIEW FOR ADD A NEW WARE """
    if request.method == 'GET':
        new = NewsBlog.objects.get(id=title_id)
        new.delete()
        messages.success(request, 'The new had been DELETE successfully!')

    return render(request, 'admin/staff_panel.html')
