from .models import Post


def reset_post_upvotes():
    """Remove all votes via cronetab"""

    posts = Post.objects.all()
    for post in posts:
        post.votes.clear()
