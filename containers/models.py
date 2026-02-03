from django.db import models


class Container(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    volume = models.FloatField(help_text="Volume in liters", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Container"
        verbose_name_plural = "Containers"


class Box(Container):
    length = models.FloatField(help_text="Length in cm")
    width = models.FloatField(help_text="Width in cm")
    height = models.FloatField(help_text="Height in cm")

    def save(self, *args, **kwargs):
        self.volume = (
            self.length * self.width * self.height
        ) / 1000  # Convert to liters
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Box"
        verbose_name_plural = "Boxes"


class Cylinder(Container):
    radius = models.FloatField(help_text="Radius in cm")
    height = models.FloatField(help_text="Height in cm")

    def save(self, *args, **kwargs):
        import math

        self.volume = (
            math.pi * (self.radius**2) * self.height
        ) / 1000  # Convert to liters
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Cylinder"
        verbose_name_plural = "Cylinders"


class Sphere(Container):
    radius = models.FloatField(help_text="Radius in cm")

    def save(self, *args, **kwargs):
        import math

        self.volume = (4 / 3) * math.pi * (self.radius**3) / 1000  # Convert to liters
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Sphere"
        verbose_name_plural = "Spheres"


class Pyramid(Container):
    base_length = models.FloatField(help_text="Base length in cm")
    base_width = models.FloatField(help_text="Base width in cm")
    height = models.FloatField(help_text="Height in cm")

    def save(self, *args, **kwargs):
        self.volume = (
            (self.base_length * self.base_width * self.height) / 3
        ) / 1000  # Convert to liters
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Pyramid"
        verbose_name_plural = "Pyramids"


class Cone(Container):
    radius = models.FloatField(help_text="Radius in cm")
    height = models.FloatField(help_text="Height in cm")

    def save(self, *args, **kwargs):
        import math

        self.volume = (
            (1 / 3) * math.pi * (self.radius**2) * self.height
        ) / 1000  # Convert to liters
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Cone"
        verbose_name_plural = "Cones"


class Bottle(Container):
    radius = models.FloatField(help_text="Radius in cm")
    height = models.FloatField(help_text="Height in cm")
    neck_radius = models.FloatField(help_text="Neck radius in cm")
    neck_height = models.FloatField(help_text="Neck height in cm")

    def save(self, *args, **kwargs):
        import math

        body_volume = math.pi * (self.radius**2) * self.height
        neck_volume = math.pi * (self.neck_radius**2) * self.neck_height
        self.volume = (body_volume + neck_volume) / 1000  # Convert to liters
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Bottle"
        verbose_name_plural = "Bottles"
