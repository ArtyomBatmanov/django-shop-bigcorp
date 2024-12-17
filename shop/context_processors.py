from .models import Category


def categories(request):
    categories = Category.objects.all(parent=None)
    return {"categories": categories}
