from django.contrib import admin


from .models import Container, Box, Cylinder, Sphere, Pyramid, Cone, Bottle


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ("name", "volume")
    search_fields = ("name",)


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ("name", "length", "width", "height", "volume")
    search_fields = ("name",)


@admin.register(Cylinder)
class CylinderAdmin(admin.ModelAdmin):
    list_display = ("name", "radius", "height", "volume")
    search_fields = ("name",)


@admin.register(Sphere)
class SphereAdmin(admin.ModelAdmin):
    list_display = ("name", "radius", "volume")
    search_fields = ("name",)


@admin.register(Pyramid)
class PyramidAdmin(admin.ModelAdmin):
    list_display = ("name", "base_length", "base_width", "height", "volume")
    search_fields = ("name",)


@admin.register(Cone)
class ConeAdmin(admin.ModelAdmin):
    list_display = ("name", "radius", "height", "volume")
    search_fields = ("name",)


@admin.register(Bottle)
class BottleAdmin(admin.ModelAdmin):
    list_display = ("name", "radius", "height", "neck_radius", "neck_height", "volume")
    search_fields = ("name",)
