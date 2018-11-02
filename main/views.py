from django.shortcuts import render

from .models import Branch, Locomotive, Run, Year


def main(request):
    context = dict()
    context['branches'] = Branch.objects.all()
    context['locomotives'] = Locomotive.objects.all()
    context['run'] = Run.objects.all()
    context['year'] = Year.objects.all()

    get = dict(request.GET)
    context['period'] = []
    context['gain'] = []
    context['selected_branches'] = []
    context['selected_loco'] = []

    if request.GET.get('branch', ''):   # Список выбранных филиалов
        context['selected_branches'] = get['branch']
        context['run'] = context['run'].filter(
            branch__name__in=context['selected_branches'])

    if request.GET.get('loco', ''):     # Список выбранных локомотивов
        context['selected_loco'] = get['loco']
        context['run'] = context['run'].filter(
            locomotive__series__in=context['selected_loco'])

    if request.GET.get('year', ''):     # Список выбранных лет
        selected_years = get['year']
        context['run'] = context['run'].filter(
            year__year__in=selected_years)

    for y in context['year']:   # Подсчитываем количество прибыли за период
        run = context['run'].filter(year=y)
        result = int()
        for r in run:
            result = result + (r.km * r.locomotive.rate)
            if r.year.year not in context['period']:
                context['period'].append(r.year.year)
        context['gain'].append(result)

    return render(request, "main.html", context)
