from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove/', views.DeletePostView.as_view(), name='delete_post'),
    # path('article/<int:pk>/toggle_status', views.TogglePostStatusView.as_view(), name='hide_post'),
    path('article/<int:pk>/toggle_status', views.hide_post, name="hide_post"),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', views.CategoryListView, name='category-list'),
    path('article/<int:pk>/add_comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('article/<int:pk>/remove_comment/', views.hide_comment, name='delete_comment'),
    
    # path('all_authors', views.AllAuthorsView.as_view(), name='all_authors'),
    path('all_authors', views.allauthors, name='all_authors'),
    
]