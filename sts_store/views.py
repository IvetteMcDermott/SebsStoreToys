from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404

from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView
from .models import Ware, WareImage, Category, Subcategory
from checkout.models import Order, OrderLineItem

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
        print(search)
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
    template_name = 'admin/add_ware.html'
    model = Ware
    form_class = WareForm

    def get_success_url(self):
        return self.request.path


@method_decorator(staff_member_required, name='dispatch')
class AddImageForm(SuccessMessageMixin, CreateView):
    """ VIEW FOR ADD A NEW WARE """
    template_name = 'admin/add_image_form.html'
    model = WareImage()
    form_class = ImageForm

    def get_success_url(self):
        return self.request.path


@staff_member_required
def image_delete(request, image_id):
    """ VIEW FOR ADD A NEW WARE """
    if request.method == 'GET':
        image = WareImage.objects.get(image_id=pk)
        image.delete()

    return render(request, 'admin/store_panel.html')


@staff_member_required
def WareEdit(request, ware_id):
    """ VIEW FOR ADD A NEW WARE """
    form = WareForm()
    ware = Ware.objects.get(id=ware_id)
    if request.method == 'POST':
        form = WareForm(request.POST, instance=ware)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return render(request, 'admin/store_panel.html')
    else:
        form = WareForm(instance=ware)

    return render(request, 'admin/ware_edit.html', {'form': form})


@staff_member_required
def WareDelete(request, ware_id):
    """ VIEW FOR ADD A NEW WARE """
    if request.method == 'GET':
        ware = Ware.objects.get(id=ware_id)
        ware.delete()

    return render(request, 'admin/store_panel.html')


@staff_member_required
def orders_list(request, *args, **kwargs):
    """ TO SEARCH ORDERS BY DATE - ADMIN FEATURE """
    """ TO SEARCH ORDERS BY USER - ADMIN FEATURE """
    model = Order
    orders = model.objects.all().order_by('-date')

    return render(
            request,
            "admin/orders_list.html",
            {
               "orders": orders,
            },
        )
