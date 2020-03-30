from django.urls import path
from .views import (IndexView,
                    PostDetail,
                    CharacterView,
                    DreamHeroView,
                    StoryDetailView,
                    DeleteCharacterView,
                    UpdateCharacterView,
                    ShopView,
                    ItemDetailView,
                    add_to_cart,
                    remove_from_cart,
                    like_post,
                    like_post_blog,
                    OrderSummaryView,
                    AuthorProfileView,
                    ProfileView,
                    )
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('single-post/<slug>', PostDetail.as_view(), name='single-post'),
    path('character-post/', CharacterView.as_view(), name='character-post'),
    path('story-post/<slug>', StoryDetailView.as_view(), name='story-post'),
    path('update-post/<slug>', UpdateCharacterView.as_view(), name='update-post'),
    path('delete-post/<slug>', DeleteCharacterView.as_view(), name='delete-post'),
    path('create-hero/', DreamHeroView.as_view(), name='create-hero'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('like-posts/<slug>', like_post, name='like-posts'),
    path('like-posts-blog/<slug>', like_post_blog, name='like-posts-blog'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('author/', AuthorProfileView.as_view(), name='author'),
    path('profile/<user>', ProfileView.as_view(), name='profile')
]
