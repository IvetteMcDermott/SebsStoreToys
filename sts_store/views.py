from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404

from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView
from .models import Ware, WareImage, Category, Subcategory

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .forms import WareForm, ImageForm

# Create your views here.


class Store(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: COAST """
    model = Ware
    queryset = Ware.objects.all()
    # paginate_by = 4
    template_name = "store_list.html"


class WareDetail(CreateView):
    """
    RENDER THE DETAILS PAGE OF THE SELECTED WARE
    """
    model = Ware

    def get(self, request, ware_id, *args, **kwargs):
        model = Ware
        queryset = model.objects.all()
        ware = get_object_or_404(queryset, pk=ware_id)

        return render(
            request,
            "ware_detail.html",
            {
               "ware": ware,
            },
        )


def search(request):
    """ VIEW FOR SEARCH A PLACE POST """
    if request.method == 'POST':
        search = request.POST.get('q')
        query = Ware.objects.all().filter(Q(name__icontains=search) | Q(description__icontains=search))
        template = 'store_list.html'
        context = {
            'result': query,
        }
        return render(request, template, context)


@staff_member_required
def StorePanel(request):
    """ VIEW FOR ADD A NEW WARE """
    return render(request, 'admin/store_panel.html')


@method_decorator(staff_member_required, name='dispatch')
class WareEntry(SuccessMessageMixin, CreateView):
    """ VIEW FOR ADD A NEW WARE """
    template_name = 'admin/admin_page.html'
    model = Ware
    form_class = WareForm
    success_url = '/'


@method_decorator(staff_member_required, name='dispatch')
class ImageForm(SuccessMessageMixin, CreateView):
    """ VIEW FOR ADD A NEW WARE """
    template_name = 'admin/image_form.html'
    model = WareImage()
    form_class = ImageForm
    success_url = '/'


@staff_member_required
def WareEdit(request, ware_id):
    """ VIEW FOR ADD A NEW WARE """
    form = WareForm()
    ware = Ware.objects.get(id=ware_id)
    print(ware)
    if request.method == 'POST':
        form = WareForm(request.POST, instance=ware)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return render(request, 'admin/success.html')
    else:
        form = WareForm(instance=ware)

    return render(request, 'admin/ware_edit.html', {'form': form})


@staff_member_required
def WareDelete(request, ware_id):
    """ VIEW FOR ADD A NEW WARE """
    if request.method == 'GET':
        ware = Ware.objects.get(id=ware_id)
        print(ware)
        ware.delete()

    return render(request, 'admin/success.html')
