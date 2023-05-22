from django.contrib import admin
from .models import Review, ReplyReview


# Register your models here.

@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ['id', 'ware', 'rating', 'body', 'author', 'date_created', ]
    search_fields = ['author', 'ware', 'rating', ]

    class Meta:
        verbose_name_plural = 'Review'


@admin.register(ReplyReview)
class ReplyReview(admin.ModelAdmin):
    list_display = ['reply_review', 'reply_content', 'replier_author',
                    'replied_date', ]
    search_fields = ['reply_review', ]

    class Meta:
        verbose_name_plural = 'Replies'
