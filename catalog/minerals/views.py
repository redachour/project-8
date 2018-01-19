from django.shortcuts import render
from django.db.models import Q

from .models import Mineral

categories = ['Silicate', 'Oxide', 'Sulfate', 'Sulfide', 'Carbonate', 'Halide',
              'Sulfosalt', 'Phosphate', 'Borate', 'Organic', 'Arsenate',
              'Native']


def index(request, letter='A', category=None, color=None):
    """Sorted queryset of minerals by letter, category or color"""
    if category:
        if category == 'Other':
            minerals = Mineral.objects.all()
            for category in categories:
                minerals = minerals.exclude(category__icontains=category)
            chosen = category
        else:
            minerals = Mineral.objects.filter(category__icontains=category)
            chosen = category
    elif color:
        minerals = Mineral.objects.filter(color__icontains=color)
        chosen = color
    else:
        minerals = Mineral.objects.filter(name__startswith=letter)
        chosen = letter
    return render(request, 'minerals/index.html', {'minerals': minerals,
                                                   'chosen': chosen})


def detail(request, pk):
    '''Details view of each mineral'''
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})


def mineral_search(request):
    """Lets search by parameters using html form"""
    term = request.GET.get('term')
    minerals = Mineral.objects.filter(
            Q(name__icontains=term) |
            Q(category__icontains=term) |
            Q(formula__icontains=term) |
            Q(strunz_classification__icontains=term) |
            Q(crystal_system__icontains=term) |
            Q(unit_cell__icontains=term) |
            Q(color__icontains=term) |
            Q(crystal_symmetry__icontains=term) |
            Q(cleavage__icontains=term) |
            Q(mohs_scale_hardness__icontains=term) |
            Q(luster__icontains=term) |
            Q(streak__icontains=term) |
            Q(diaphaneity__icontains=term) |
            Q(optical_properties__icontains=term) |
            Q(refractive_index__icontains=term) |
            Q(crystal_habit__icontains=term) |
            Q(specific_gravity__icontains=term)
    )
    return render(request, 'minerals/index.html', {'minerals': minerals})
