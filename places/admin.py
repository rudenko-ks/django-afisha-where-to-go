from django.contrib import admin
from django.utils.html import format_html
from places.models import Image, Place
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):

    model = Image
    extra = 0
    readonly_fields = ('image_preview',)
    fields = (
        'place',
        'image',
        'image_preview',
        'number',
    )

    def image_preview(self, img):
        return format_html(
            '<img src="{url}" height={height} />',
            url=img.image.url,
            height=200,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
