from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
  metrics = [
      {"value": "120+", "label": "Sistemas mapeados"},
      {"value": "800+", "label": "Corpos celestes"},
      {"value": "24h", "label": "Atualizações contínuas"},
      {"value": "99.9%", "label": "Disponibilidade"},
  ]
  return render(request, "home.html", {"metrics": metrics})

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')