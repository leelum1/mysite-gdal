from django.contrib.gis import admin
from .models import Hike, HikeImage

class HikeAdmin(admin.OSMGeoAdmin):
    default_lat = 1166581
    default_lon = -6823992
    default_zoom = 10
    max_extent = '-6706814, 1099880, -6926341, 1301673'
    map_width = 1000
    map_height = 500
    units = 'm'

    list_display = ['name', 'type', 'difficulty', 'region',]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Hike, HikeAdmin)
admin.site.register(HikeImage)
