from .models import Category
from userAuths.models import CustomUser

def default(request):
    categories = Category.objects.all()
    p = CustomUser.objects.get(username=request.user.username)

    return {
        'categories': categories,
        'p': p
    }