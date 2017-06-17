from home.models import HomePage

def home(request):
    return {'home': HomePage.load()}