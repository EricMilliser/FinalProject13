from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from.models import Review, Pizza, Topping, Order
from .forms import OrderForm, ReviewForm, PizzaFormSet
from django.contrib.auth.decorators import login_required






# Create your views here.
def home(request):
    return render(request, 'pizzaSite/PizzaPalace.html')

def viewMenu(request):
    return render(request, 'pizzaSite/MenuItems.html')






def create_order(request):
    if request.method == 'POST':
            form = OrderForm(request.POST)
            formset = PizzaFormSet(request.POST)
            if form.is_valid() and formset.is_valid():
                order = form.save()
                formset.instance = order
                formset.save()
                return redirect('Cart', order_id=order.id)
    else:
        form = OrderForm()
        formset = PizzaFormSet()
    return render(request, 'pizzaSite/Orderpage.html', {'form': form, 'formset': formset})



#def create_order(request):
    #if request.method == 'POST':
        #form = OrderForm(request.POST)
        #formset = PizzaFormSet(request.POST)
        #if form.is_valid() and formset.is_valid():
            #order = form.save()
            #pizzas = formset.save(commit=False)
            #for pizza in pizzas:
                #pizza.order = order 
                #pizza.save()
            #return redirect('Cart')
   # else:
       # form = OrderForm()
        #formset = PizzaFormSet(queryset=Pizza.objects.none())

    #return render(request, 'pizzaSite/OrderPage.html', {'form': form, 'formset': formset})

def viewCart(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'pizzaSite/Cart.html', {'order': order, 'pizzas': pizzas})

def edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        formset = PizzaFormSet(request.POST, queryset=order.pizzas.all())
        if form.is_valid() and formset.is_valid():
            form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.order = order
                instance.save()
            for obj in formset.deleted_objects:
                obj.delete()
            return redirect('Cart')
    else:
        form = OrderForm(instance=order)
        formset = PizzaFormSet(queryset=order.pizzas.all())
    
    return render(request, 'pizzaSite/EditOrder.html', {'form': form, 'formset': formset, 'order': order})

def order_remove(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('home')

def cart(request):
    return render(request, 'pizzaSite/Cart.html')


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ReviewForm()
    return render(request, 'pizzaSite/ReviewPage.html')


def checkout(request):
    return render(request, 'pizzaSite/Checkout.html')



#def post_list(request):
    #posts = Review.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'pizzaSite/ReviewPage.html', {'reviews': reviews})

#@login_required
#def post_new(request):
    #if request.method == "POST":
        #form = ReviewForm(request.POST)
        #if form.is_valid():
            #post = form.save(commit=False)
            #post.author = request.user
            #post.save()
            #return redirect('post_detail', pk=post.pk)
    #else:
        #form = ReviewForm()
    #return render(request, 'blog/post_edit.html', {'form': form})


