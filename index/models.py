from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Slider(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    paragraph = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class GameNews(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single-post', kwargs={
            'slug': self.slug
    })

    def get_post_like(self):
        return reverse('like-posts-blog', kwargs={
            'slug': self.slug
    })





class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    strenght = models.IntegerField()
    power = models.IntegerField()
    weapon = models.IntegerField()
    hero_image = models.ImageField(upload_to='media')
    slug = models.SlugField(unique=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    Views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


    def get_hero_story_url(self):
        return reverse('story-post', kwargs={
            'slug': self.slug
    })


    def get_absolute_url(self):
        return reverse('like-posts', kwargs={
            'slug': self.slug
    })



    def get_delete_url(self):
        return reverse('delete-post', kwargs={
            'slug': self.slug
    })


    def total_like(self):
        return self.likes.count()


    def get_num_post(self):
        return Character.objects.filter(user=self.user).count()



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=1500)
    post = models.ForeignKey(GameNews, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class CharacterComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=1500)
    post = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Shop(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_shop_url(self):
        return reverse('product', kwargs={
            'slug': self.slug
    })

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', kwargs={
            'slug': self.slug
    })

    def get_remove_from_cart_url(self):
        return reverse('remove-from-cart', kwargs={
            'slug': self.slug
    })



class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def total_price(self):
        return self.quantity * self.item.price



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Social(models.Model):
    image = models.ImageField()


class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=8, choices=GENDER, null=True, blank=True)
    bio = models.TextField()
    cover_image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.user.username

    def get_suggest_url(self):
        return reverse('suggest', kwargs={
            'pk': self.id
        })


class Friend(models.Model):
    users = models.ManyToManyField(Author)
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.current_user.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.current_user.remove(new_friend)
