from django.urls import path
from .views import PostView, CommentView, UpvoteAddView

app_name = "blog"

post_create = PostView.as_view({"post": "create"})
posts_list = PostView.as_view({"get": "list"})
post_detail = PostView.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)

comments = CommentView.as_view({"get": "list", "post": "create"})
comment_detail = CommentView.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)

urlpatterns = [
    path("post/create/", post_create),
    path("posts/", posts_list),
    path("post/<int:pk>/", post_detail),
    path("post/<int:pk>/upvote/", UpvoteAddView.as_view()),
    path("comments/", comments),
    path("comment/<int:pk>/", comment_detail),
]
