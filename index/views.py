from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.db.models.signals import pre_save
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin, ModelFormMixin
from .models import GameNews, Character, Comment, Shop, OrderItem, Order, CharacterComment, Slider, Social, Author, Friend, User
from .forms import DreamHeroForm, CommentForm, CharCommentForm, AuthorProfForm
from django.utils.text import slugify
from django.shortcuts import reverse
from django.urls import reverse_lazy


class IndexView(ListView):
    model = GameNews
    context_object_name = 'blog_post'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['list_post'] = Character.objects.all()[:5]
        context['slide'] = Slider.objects.all()
        context['social'] = Social.objects.all()
        context['friends_list'] = Author.objects.exclude(id=self.request.user.id)
        return context

class PostDetail(FormMixin, DetailView):
    model = GameNews
    template_name = 'single_post.html'
    context_object_name = 'comment_post'
    form_class = CommentForm


    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('single-post', kwargs={
            'slug': self.object.slug
    })

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.get_object()
        form.save()
        return super().form_valid(form)


def like_post_blog(request, slug):
    like = get_object_or_404(GameNews, slug=slug)
    if like.likes.filter(id=request.user.id).exists():
        like.likes.remove(request.user)
    else:
        like.likes.add(request.user)
    return redirect('single-post', slug=slug)





class CharacterView(ListView):
    model = Character
    template_name = 'character.html'


class StoryDetailView(FormMixin, DetailView):
    model = Character
    template_name = 'story.html'
    context_object_name = 'comment_set'
    form_class = CharCommentForm


    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        context['commenting'] = self.object.charactercomment_set.all()
        context['pro_pic'] = get_object_or_404(Author, user=self.request.user)
        context['charform'] = CharCommentForm()
        return context

    def get_success_url(self):
        return reverse('story-post', kwargs={
            'slug': self.object.slug
    })

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.get_object()
        form.save()
        return super().form_valid(form)



class DeleteCharacterView(DeleteView):
    model = Character
    success_url = reverse_lazy('character-post')





def like_post(request, slug):
    like = get_object_or_404(Character, slug=slug)
    if like.likes.filter(id=request.user.id).exists():
        like.likes.remove(request.user)
    else:
        like.likes.add(request.user)
    return redirect('story-post', slug=slug)


def post_like_post(request, slug):
    like = get_object_or_404(GameNews, slug=slug)
    if like.likes.filter(id=request.user.id).exists():
        like.likes.remove(request.user)
    else:
        like.likes.add(request.user)
    return redirect('single-post', slug=slug)


def my_post(request, slug):
    viewes = Character.objects.get(user=request.user, slug=slug)
    viewes.save()
    return redirect('story')



class DreamHeroView(CreateView):
    template_name = 'dream_hero.html'
    model = Character
    form_class = DreamHeroForm

    def get(self, *args, **kwargs):
        form = DreamHeroForm()
        return render(self.request, 'dream_hero.html', {'form': form})

    def post(self, *args, **kwargs):
        form = DreamHeroForm(self.request.POST, self.request.FILES or None)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            strenght = form.cleaned_data['strenght']
            power = form.cleaned_data['power']
            weapon = form.cleaned_data['weapon']
            hero_image = form.cleaned_data['hero_image']
            slug = form.cleaned_data['slug']
            post = Character(
                title=title,
                description=description,
                strenght=strenght,
                power=power,
                weapon=weapon,
                hero_image=hero_image,
                slug=slug,
                user=self.request.user,
            )
            post.save()
            return redirect('character-post')
        return render(self.request, 'dream_hero.html')





class UpdateCharacterView(UpdateView):
    model = Character
    form_class = DreamHeroForm
    template_name = "dream_hero.html"

    def get(self, *args, **kwargs):
        out = get_object_or_404(Character)
        form = DreamHeroForm(self.request.PATCH, self.request.FILES or None)
        return render(self.request, 'dream_hero.html', {'form': form})








class ShopView(ListView):
    model = Shop
    template_name = 'shop.html'


class ItemDetailView(DetailView):
    model = Shop
    template_name = 'product.html'


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            return redirect('/')


def add_to_cart(request, slug):
    item = get_object_or_404(Shop, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item is updated to cart")
        else:
            messages.info(request, "This item is added to cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect('product', slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Shop, slug=slug)
    order_qs = Order.objects.filter(user=request.user,
                                    ordered=False
                                    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                )[0]
            order.items.remove(order_item)
            messages.info(request, "This item is removed to cart")
    else:
        messages.info(request, "This item is added to cart")
        return redirect('product', slug=slug)
    return redirect('product', slug=slug)


class AuthorProfileView(View):
    def get(self, *args, **kwargs):
        form = AuthorProfForm()
        return render(self.request, 'author.html', {'form': form})

    def post(self, *args, **kwargs):
        form = AuthorProfForm(self.request.POST, self.request.FILES or None)
        if form.is_valid():
            image = form.cleaned_data['image']
            cover_image = form.cleaned_data['cover_image']
            bio = form.cleaned_data['bio']
            pro = Author(
                image=image,
                cover_image=cover_image,
                bio=bio,
                user=self.request.user,
            )
            pro.save()
            return redirect('/')
        return render(self.request, 'signin.html')


class ProfileView(LoginRequiredMixin, DetailView):
    model = Author

    def get(self, *args, **kwargs):
        try:
            prof = Author.objects.get(user=self.request.user)
            your_post = Character.objects.filter(user=self.request.user).order_by('-date')
            context = {
                'prof': prof,
                'your_post': your_post,
            }
            return render(self.request, 'profile.html', context)
        except ObjectDoesNotExist:
            return redirect('author')



