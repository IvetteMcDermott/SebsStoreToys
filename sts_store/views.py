from django.db.models import Q
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404

from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Ware, WareImage, Category, Subcategory
from checkout.models import Order, OrderLineItem

from profiles.models import UserProfile
from bookmarks.models import Bookmarks
from reviews.models import Review, ReplyReview
from contact_us.models import ContactUs

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .forms import WareForm, ImageForm
from reviews.forms import ReviewForm

# Create your views here.


class Store(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: COAST """
    model = Ware
    queryset = Ware.objects.all().order_by('description')
    queryset_count = queryset.count()
    paginate_by = 4
    template_name = "store_list.html"

    def get_bookmarks(request):
        user = request.user
        model = Bookmarks
        bookmark = Bookmarks.objects.filter(user=user)

        context = {
            'bookmarks': bookmark,
        }
        return context


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
        reviews = ware.reviews.all().order_by('-date_created')[:5]
        review_form = ReviewForm()
        if request.user.is_authenticated:
            if not request.user.is_staff:
                user = UserProfile.objects.get(user=request.user)
                bookmarke = Bookmarks.objects.filter(
                    user=user, ware=ware).exists()

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


# Took from https://stackoverflow.com/questions/71396075/i-want-to-make-reply-to-comments-feature-in-django
def reply_review(request, review_id):
    reviews = Review.objects.get(id=review_id)

    if request.method == 'POST':
        replier_author = request.user
        reply_content = request.POST.get('reply_content')

        newReply = ReplyReview(
            replier_author=replier_author, reply_content=reply_content)
        newReply.reply_review = reviews
        newReply.save()
        messages.success(request, 'Review replied!')

    return redirect(request.META.get('HTTP_REFERER'))


def search(request):
    """ VIEW FOR SEARCH A PLACE POST """
    if request.method == 'POST':
        search = request.POST.get('q')
        print(search)
        query = Ware.objects.all().filter(Q(name__icontains=search)
                                          | Q(description__icontains=search))
        template = 'store_list.html'

        context = {
            'object_list': query,
            'search': search,
        }

        return render(request, template, context)


def search_category(request):
    model = Ware
    if request.method == 'POST':
        search = request.POST.get('q')
        queryset = Ware.objects.all()
        query = queryset.filter(subcategory__name__icontains=search)
        template = 'store_list.html'
        context = {
            'object_list': query,
        }
        return render(request, template, context)


@staff_member_required
def StaffPanel(request):
    """ VIEW FOR ADD A NEW WARE """
    return render(request, 'admin/staff_panel.html')


@method_decorator(staff_member_required, name='dispatch')
class WareEntry(SuccessMessageMixin, CreateView):
    """ VIEW FOR ADD A NEW WARE """
    template_name = 'admin/add_ware.html'
    model = Ware
    form_class = WareForm
    success_message = 'The ware had been save successfully!'

    def get_success_url(self):
        return self.request.path


@method_decorator(staff_member_required, name='dispatch')
class AddImageForm(SuccessMessageMixin, CreateView):
    """ VIEW FOR ADD A NEW WARE """
    template_name = 'admin/add_image_form.html'
    model = WareImage()
    form_class = ImageForm
    success_message = 'The image had been ADD successfully!'

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
        messages.success(request, 'The image had been DELETE successfully!')

    return redirect(request.META.get('HTTP_REFERER'))


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
            messages.success(request, 'The ware had been EDIT successfully!')
            return render(request, 'admin/staff_panel.html')
    else:
        form = WareForm(instance=ware)

    return render(request, 'admin/ware_edit.html', {'form': form})


@staff_member_required
def WareDelete(request, ware_id):
    """ VIEW FOR ADD A NEW WARE """
    if request.method == 'GET':
        ware = Ware.objects.get(id=ware_id)
        ware.delete()
        messages.success(request, 'The ware had been DELETE successfully!')

    return render(request, 'admin/staff_panel.html')


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


@staff_member_required
def contacted_us_list(request, *args, **kwargs):
    """ TO SEARCH ORDERS BY DATE - ADMIN FEATURE """
    """ TO SEARCH ORDERS BY USER - ADMIN FEATURE """
    model = ContactUs
    contacts = model.objects.all().order_by('-id')

    return render(
        request,
        "admin/contact_us_list.html",
        {
            "contacts": contacts,
        },
    )
