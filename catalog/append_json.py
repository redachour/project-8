import json
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalog.settings")
get_wsgi_application()

from minerals.models import Mineral

directory = os.path.dirname(os.path.abspath(__file__))
json_file = os.path.join(directory, 'assets/minerals.json')


def checker(item, name):
    '''return contents if exists otherwise return an empty string'''
    try:
        contents = item[name]
    except KeyError:
        return ''
    else:
        return contents


def run():
    '''This append json file to our SQLite database'''
    with open(json_file, encoding="utf-8") as jsonfile:
        minerals = json.load(jsonfile)

    for mineral in minerals:
        obj = Mineral()
        obj.name = checker(mineral, 'name')
        obj.image_filename = checker(mineral, 'image filename')
        obj.image_caption = checker(mineral, 'image caption')
        obj.category = checker(mineral, 'category')
        obj.formula = checker(mineral, 'formula')
        obj.strunz_classification = checker(mineral, 'strunz classification')
        obj.color = checker(mineral, 'color')
        obj.crystal_system = checker(mineral, 'crystal system')
        obj.unit_cell = checker(mineral, 'unit cell')
        obj.crystal_symmetry = checker(mineral, 'crystal symmetry')
        obj.cleavage = checker(mineral, 'cleavage')
        obj.mohs_scale_hardness = checker(mineral, 'mohs scale hardness')
        obj.luster = checker(mineral, 'luster')
        obj.streak = checker(mineral, 'streak')
        obj.diaphaneity = checker(mineral, 'diaphaneity')
        obj.optical_properties = checker(mineral, 'optical properties')
        obj.refractive_index = checker(mineral, 'refractive index')
        obj.crystal_habit = checker(mineral, 'crystal habit')
        obj.specific_gravity = checker(mineral, 'specific gravity')
        obj.save()


if __name__ == '__main__':
    run()
