from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user # 작성자 설정
        # form.instance.article = Article.objects.get(pk=self.request.POST.get('article_pk'))
        # 특정한 게시글을 우리가 작성할 게시글에 연결
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk' : self.object.article.pk})