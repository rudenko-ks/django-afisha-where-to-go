from django.contrib import admin
from django.utils.html import format_html
from places.models import Image, Place


class ImageInline(admin.TabularInline):

    model = Image
    readonly_fields = ['image_preview']
    fields = ('title', 'image', 'image_preview', 'number')

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
