from django.contrib import admin
from .models import Slider, GameNews, Character, Comment, CharacterComment, Shop, OrderItem, Order, Social, Author

admin.site.register(Slider)

class GameNewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'slug']
admin.site.register(GameNews, GameNewsAdmin)

class CharacterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'title', 'power', 'weapon', 'strenght']
admin.site.register(Character, CharacterAdmin)

admin.site.register(Comment)

admin.site.register(CharacterComment)

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
admin.site.register(Shop, ShopAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'quantity', 'item']
admin.site.register(OrderItem, OrderItemAdmin)

admin.site.register(Order)
admin.site.register(Social)
admin.site.register(Author)

