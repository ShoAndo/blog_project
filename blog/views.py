from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Tweet

class TopView(TemplateView):
  template_name = 'index.html'

class HomeView(LoginRequiredMixin, TemplateView):
  template_name = 'home.html'

class SignUpView(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'

class TweetList(LoginRequiredMixin, ListView):
  model = Tweet
  template_name="blog/list.html"

  #object_listの表示順変更
  def get_queryset(self):
    return Tweet.objects.order_by('-created_at')

class TweetEdit(LoginRequiredMixin, UpdateView):
  model = Tweet
  fields = ('message',)
  success_url = reverse_lazy('list')

class NewTweet(LoginRequiredMixin, CreateView):
  model = Tweet
  fields = ('message',)
  success_url = reverse_lazy('list')
  
  #外部キーuser_idを保存
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(NewTweet, self).form_valid(form)

class DeleteTweet(LoginRequiredMixin, DeleteView):
  model = Tweet
  success_url = reverse_lazy('list')