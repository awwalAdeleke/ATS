from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Post, Category, Comment, Profile, User
from .forms import PostForm, UpdatePostForm, CommentForm

# Create your views here.
# def home(request):
#     return render(request,'home.html', {})


class HomeView(generic.ListView):
    model = Post
    template_name = 'home.html'
    # cats = Category.objects.all()
    # deleted_posts = Post.deleted_posts.all()
    # active_posts = Post.active_posts.all()
    ordering = ['post_date']
    paginate_by = 5
    

    def get_queryset(self):
        return Post.active_posts.all()

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        # all_posts = Post.objects.all()
        deleted_posts = Post.deleted_posts.all()
        # active_posts = Post.active_posts.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        # context = {"cat_menu": cat_menu,"all_posts":all_posts ,"deleted_posts": deleted_posts, "active_posts": active_posts}
        context.update({"cat_menu": cat_menu, "deleted_posts": deleted_posts})
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})


class ArticleDetailView(generic.View):
    model = Post
    template_name = 'article_details.html'

    # def get_context_data(self, **kwargs):
    #     cat_menu = Category.objects.all()
    #     post = Post.objects.get(id=pk)
    #     comments = ''
    #     if self.request.user == post.author.id:
    #         comments = Comment.objects.filter(post=post)
    #     else:
    #         comments = Comment.active_comments.filter(post=post)
    #     # deleted_comments = Comment.deleted_comments.all()
    #     # active_comments = Comment.active_comments.all()
    #     context = super(ArticleDetailView, self).get_context_data(**kwargs)
    #     context["cat_menu"] = cat_menu
    #     context['comments'] = comments
    #     # context.update({"deleted_comments":deleted_comments, "active_comments":active_comments})
    #     return context

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        cat_menu = Category.objects.all()
        if request.user.id == post.author.id:
            comments = Comment.objects.filter(post=post)
        else:
            comments = Comment.active_comments.filter(post=post)
        # context = super().get_context_data()
        context = {
            'cat_menu': cat_menu,
            'post': post,
            'comments': comments
        }
        return render(
            request,
            'article_details.html',
            context=context
            )
    
    def post(self, request, pk):
        pass
    
    # def get_queryset(self):
    #     return super().get_queryset(), Comment.active_comments.all()


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class DeleteCommentView(generic.DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')

class AddCategoryView(generic.CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name= 'update_post.html'
    # fields = ['title','title_tag','body'] # No need for the author, it is unnecessary to change the author of a post.


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def hide_post(request, pk):
    post = Post.objects.get(id=pk)
    post.is_deleted = not post.is_deleted
    post.save()
    return redirect(reverse_lazy('show_profile_page', args=[post.author.id]))

def hide_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    post = Post.objects.get(comments=comment)
    comment.is_deleted = not comment.is_deleted
    comment.save()
    return redirect(reverse_lazy('article-detail', kwargs={'pk': post.id}))


# class TogglePostStatusView(generic.UpdateView):
#     model = Post
#     template_name= 'hide_post.html'
#     fields = ["is_deleted"]





# class AllAuthorsView(generic.ListView):
#     model = User
#     template_name = 'all_authors.html'
#     ordering = ['first_name']
    
#     def get_context_data(self, **kwargs):
#         posts = Post.objects.all()
        
#         all_authors = []

#         for post in posts:
#             if post.author not in all_authors:
#                 all_authors.append(post.author)
#         context = super(AllAuthorsView, self).get_context_data(**kwargs)
#         context["posts"] = posts
#         return context

def allauthors(request):
    posts = Post.objects.all()
    all_authors = []

    for post in posts:
        if post.author not in all_authors:
            all_authors.append(post.author)

    context = {"all_authors" : all_authors}
    return render(request, 'all_authors.html', context)
