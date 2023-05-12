from django.db.models import Q
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404

from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView

from .models import Ware, WareImage, Category, Subcategory
from checkout.models import Order, OrderLineItem
from reviews.models import Review

from profiles.models import UserProfile
from bookmarks.models import Bookmarks

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .forms import WareForm, ImageForm
from reviews.forms import ReviewForm

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
    review_form = ReviewForm()
    bookmarked = False

    def get(self, request, ware_id, *args, **kwargs):
        model = Ware
        bookmarked = False

        queryset = model.objects.all()
        ware = get_object_or_404(queryset, pk=ware_id)
        reviews = ware.reviews.all().order_by('-date_created')
        review_form = ReviewForm()

        if request.user.is_authenticated:
            user = UserProfile.objects.get(user=request.user)
            bookmarke = Bookmarks.objects.filter(user=user, ware=ware).exists()

            if bookmarke:
                bookmarked = True
            else:
                bookmarked = False

        return render(
            request,
            'ware_detail.html',
            {
               'ware': ware,
               'reviews': reviews,
               'form': review_form,
               'bookmarked': bookmarked,
            },
        )

    def post(self, request, ware_id, *args, **kwargs):
        user = get_object_or_404(UserProfile, user=request.user)
        ware = get_object_or_404(Ware, id=ware_id)
        reviews = ware.reviews.all().order_by('-date_created')
        review_form = ReviewForm(data=request.POST)

        template = 'ware_detail.html'

        if review_form.is_valid():
            review_form.instance.author = request.user
            review = review_form.save(commit=False)
            review.ware = ware
            review.save()
            ReviewForm()
            messages.success(request, 'Your review was posted successfully!')
        else:
            review_form = ReviewForm()
        
        return redirect(request.META.get('HTTP_REFERER'))

        # context = {
        #             'form': ReviewForm(),
        #             'user': user,
        #             'ware': ware,
        #             'reviews': reviews,
        #             }

        # return render(request, template, context)


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
def open_image(request, image_id):
    """ VIEW FOR ADD A NEW WARE """
    if request.method == 'GET':
        image = get_object_or_404(WareImage, pk=image_id)

    return render(request, 'admin/ware_image.html', {'image': image})


@staff_member_required
def image_delete(request, id):
    """ VIEW FOR ADD A NEW WARE """
    if request.method == 'GET':
        image = WareImage.objects.get(pk=id)
        image.delete()

    return render(request, 'admin/store_panel.html')


@staff_member_required
def WareEdit(request, ware_id):
    """ VIEW FOR ADD A NEW WARE """
    form = WareForm()
    ware = get_object_or_404(Ware, id=ware_id)

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
