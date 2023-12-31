from .models import Category
from userAuths.models import CustomUser

def default(request):
    p  = None
    
    try:
        categories = Category.objects.all()
        p = CustomUser.objects.get(username=request.user.username)
    except:
        None

    return {
        'categories': categories,
        'p': p
    }