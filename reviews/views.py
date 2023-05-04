from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from products.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def create_review(request, product_pk):
    product = Product.objects.get(pk = product_pk)
    form = ReviewForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('products:product_detail', product_pk=product_pk)
    context = {
        'product':product,
        'form':form,
    }
    return render(request, 'reviews/create_review.html', context)



def rate_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    rating = int(request.POST.get('rating'))
    if rating in range(1, 6):
        review.rating = rating
        review.save()
    return redirect('review_detail', review_id)


def delete_review(request, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk, product__pk=product_pk)
    if request.user == review.user:
        review.delete()
        return redirect('products:product_detail', product_pk=product_pk)
    

def update_review(request, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk, product__pk=product_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=request.review)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', product_pk=product_pk, review_pk=review.pk)
            

def comment_create(request, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('products:product_detail', product_pk=product_pk)
    context = {
        'review':review,
        'comment_form':comment_form,
    }
    return render(request, 'products/product_detail.html', context)


def comment_delete(request, product_pk, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('products:detail', product_pk=product_pk, review_pk=review_pk)


def like_review(request, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('products:prodcut_detail', product_pk=product_pk)


def like_comment(request, product_pk, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('products:prodcut_detail', product_pk=product_pk)