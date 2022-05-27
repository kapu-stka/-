from django.shortcuts import render
from reviews.forms import ReviewForm 
from django.shortcuts import redirect 
from reviews.models import Review

# Create your views here.
def reviews (request):
   
    if request.method=='POST':

        form=ReviewForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            name=data.get('name')
            email=data.get('email')
            review=data.get('review')
            rating=data.get('rating')
            Review.objects.create(name=name, email=email,review=review, rating=rating)
            return redirect('reviews')
        form=ReviewForm()
        review1=Review.objects.get(id=1)
        print(review1.name)
        return render (request, 'reviews.html',  { 'form':form})
