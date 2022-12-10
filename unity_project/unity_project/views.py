from django.shortcuts import render

def render_home(request):
  context = { 'title': 'asdf'}
  return render(request, 'home.html', context)
