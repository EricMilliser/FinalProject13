from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.





class Topping(models.Model):
    
    
    TYPE_CHOICES = (
        (1, 'Meats'),
        (2, 'Cheese'),
        (3, 'Vegetables'),
        (4, 'Specialty'),
    )
    
    type = models.IntegerField(choices = TYPE_CHOICES)
    name = models.CharField(max_length=100)
    isAvailable = models.BooleanField(default=True)
    
        
    def __str__(self):
        if(self.isAvailable == True):
            return f"{self.name}"
        else:
            return f"{self.name} - Unavailable"
        
    


class Pizza(models.Model):
    
    SIZE_CHOICES = (
        (1, 'Small'),
        (2, 'Medium'),
        (3, 'Large'),
    )
    PAN_CHOICES = (
        (1, 'Hand-Tossed'),
        (2, 'Deep Dish'),
        (3, 'Pan'),
    )
    SAUCE_CHOICES = (
        (1, 'Tomato'),
        (2, 'Barbeque'),
        (3, 'Alfredo'),
    )

    size = models.IntegerField(choices = SIZE_CHOICES)
    panType = models.IntegerField(choices = PAN_CHOICES)
    sauce = models.IntegerField(choices = SAUCE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    toppings = models.ManyToManyField(Topping, related_name='toppings')

    def calculate_price(self):
        base_prices = {1: 5.99, 2: 7.99, 3: 9.99}
        total_price = base_prices[self.size]

        toppings = self.toppings.all()
        countToppings = toppings.count()

        if countToppings > 3:
            total_price += sum(1.87 for topping in toppings[:3])


        self.price = total_price
        self.save()

    def calculate_extra(self):
        
        extra_price = 0

        toppings = self.toppings.all()
        countToppings = toppings.count()
        
        if countToppings > 3:
            extra_price += sum(1.87 for topping in toppings[:3])

    def __str__(self):
        size = dict(self.SIZE_CHOICES).get(self.size, 'Size')
        pan = dict(self.PAN_CHOICES).get(self.panType, 'Pan')
        sauce = dict(self.SAUCE_CHOICES).get(self.sauce, 'Sauce')
        return f"{size} {pan} Pizza with {sauce}"









class Order(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pizzas = models.ManyToManyField(Pizza, related_name='pizzas')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f"Order {self.id} - {self.name}: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def calculate_price(self):
        for pizza in self.pizzas:
            self.price += self.pizza.price
        self.save()
    

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
