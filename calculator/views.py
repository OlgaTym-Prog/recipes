from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_view(request, dish):
    recipe = DATA.get(dish)

    if not recipe:
        return HttpResponse(f'Неизвестный рецепт для {dish}', status=404)

    # Проверка и обработка количества порций
    try:
        servings = int(request.GET.get('servings', 4))
        if servings < 1:
            raise ValueError
    except ValueError:
        return HttpResponse('Количество порций должно быть положительным целым числом', status=400)

    # Вычисление порций
    updated_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': updated_recipe
    }

    return render(request, 'calculator/index.html', context)
