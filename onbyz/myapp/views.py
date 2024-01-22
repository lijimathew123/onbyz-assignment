from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import Student
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import Student
from .forms import FilterForm  # Create a form for filtering

def index(request):
    students = Student.objects.all()

    # Handling the form submission
    if request.method == 'GET':
        form = FilterForm(request.GET)
        if form.is_valid():
            year = form.cleaned_data.get('year')
            month = form.cleaned_data.get('month')

            if year:
                students = students.filter(passing_out_date__year=year)

            if month:
                students = students.filter(passing_out_date__month=month)

    else:
        form = FilterForm()

    return render(request, 'index.html', {'students': students, 'form': form})


# def index(request):
#     # Get query parameters for filtering
#     students = Student.objects.all()
#     return render(request, 'index.html', {'students': students})
