from django.shortcuts import render, redirect
from .models import Review
from .forms import ReivewForm
# from products.models import Product


# Create your views here.
def create_review(request, category_pk, product_pk):
    prodcut = Product.objects.get(pk = product_pk)
    form = ReivewForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('products:product_detail',category_pk=category_pk, product_pk=product_pk)
    context = {
        'product':product,
        'form':form,
    }
    return render(request, 'reviews/create_review.html', context)


def review_detail(request, category_pk, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk, product__pk=product_pk, product__category__pk=category_pk)
    context = {
        'review':review,
    }
    return render(request, 'reviews/review_detail.html', context)


def delete_review(request, category_pk, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk, product__pk=product_pk, product__category__pk=category_pk)
    if request.user == review.user:
        review.delete()
        return redirect('products:prodcut_detail',category_pk=category_pk, product_pk=product_pk)
    

def update_review(request, category_pk, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk, product__pk=product_pk, product__category__pk=category_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReivewForm(request.POST, instance=request.review)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', category_pk=category_pk, product_pk=product_pk, review_pk=review.pk)