from .models import Post

def reset_post_upvotes():
    print("cron work")
    posts = Post.objects.all()
    for post in posts:
        post.votes.clear()
    print("success")
