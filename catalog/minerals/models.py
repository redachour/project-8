from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=250)
    image_filename = models.CharField(max_length=250)
    image_caption = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    formula = models.CharField(max_length=250)
    strunz_classification = models.CharField(max_length=250)
    crystal_system = models.CharField(max_length=250)
    unit_cell = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    crystal_symmetry = models.CharField(max_length=250)
    cleavage = models.CharField(max_length=250)
    mohs_scale_hardness = models.CharField(max_length=250)
    luster = models.CharField(max_length=250)
    streak = models.CharField(max_length=250)
    diaphaneity = models.CharField(max_length=250)
    optical_properties = models.CharField(max_length=250)
    refractive_index = models.CharField(max_length=250)
    crystal_habit = models.CharField(max_length=250)
    specific_gravity = models.CharField(max_length=250)
