from django.shortcuts import render



def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)
# Create your views here.
def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')