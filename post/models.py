from django.db import models
from common.models import User


class Comment(models.Model):
    content = models.TextField(max_length=2048)


PUBLIC = "public"
PRIVATE = "private"
ONLY_FRIENDS = "only_friends"

POST_TYPE_CHOICES = (
    (PUBLIC, "public"),
    (PRIVATE, "private"),
    (ONLY_FRIENDS, "only_friends")
)

class Post(models.Model):
    content = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to="post_image/", null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="post_author")
    post_type = models.CharField(max_length=16, choices=POST_TYPE_CHOICES)
    
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, related_name="post_commnet")

    likes_count = models.PositiveIntegerField(null=True, blank=True)
    comments_count = models.PositiveIntegerField(null=True, blank=True)
    shares_count = models.PositiveIntegerField(null=True, blank=True)
