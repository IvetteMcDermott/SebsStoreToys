from django.shortcuts import render, get_object_or_404

from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView
from .models import Ware, WareImage, Category, Subcategory


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

    def get(self, request, id, *args, **kwargs):
        model = Ware
        queryset = model.objects.all()
        ware = get_object_or_404(queryset, id=id)

        return render(
            request,
            "ware_detail.html",
            {
               "ware": ware,
            },
        )
