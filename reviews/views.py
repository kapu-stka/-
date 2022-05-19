from django.shortcuts import render
from reviews.forms import ReviewForm 
from django.shortcuts import redirect 

# Create your views here.
def reviews (request):
    
    if request.method=='GET':
        form=ReviewForm()
        return render(request,'reviews.html',{'form':form})
    elif request.method=='POST':

        form=ReviewForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            name=data.get('name')
            email=data.get('email')
            review=data.get('review')

            with open('data.csv', 'a') as file:
                file.write(f'{name}|{email}|{review}\n')
            return redirect('reviews')
    else:
        form=ReviewForm()
        return render (request, 'reviews.html',  { 'form':form})