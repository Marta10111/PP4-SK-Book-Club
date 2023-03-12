from django.shortcuts import render, get_object_or_404, reverse
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm


def index(request):
    """ Returns index.html """
    return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'post_list.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

 
def post(self, request, slug, *args, **kwargs):
    queryset = Post.objects
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.order_by("created_on")
    liked = False
    if post.likes.filter(id=self.request.user.id).exists():
        liked = True

    comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request, 'Thanks for Your comment!')
    else:
        comment_form = CommentForm()

    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "comments": comments,
            "liked": liked,
            "comment_form": CommentForm()
         },
    )
            

class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'featured_image']
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'You created a new Book Review')
        return super(PostCreate, self).form_valid(form)


class PostEdit(UpdateView):
    model = Post()
    fields = ['title', 'content', 'featured_image']
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'You edited Your Book Review')
        return super(PostEdit, self).form_valid(form)


class PostDelete(DeleteView):
    model = Post()
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list') 
    success_message = "You have successfully deleted the post"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)