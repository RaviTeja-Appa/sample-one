# Assuming User model is in contrib.auth
from authentications.models import User
from django.db import models
from datetime import datetime  # Import the datetime module

from django.utils.timezone import now

# Create your models here.


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

    class Meta:
        # Order boards by creation date (latest first)
        ordering = ['-created_at']


class Image_Posting(models.Model):
    title = models.CharField(max_length=300)  # Title of the pin
    image_description = models.CharField(
        max_length=600)  # Description of the pin
    # User who created the pin
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Board the pin belongs to
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=None)
    # Comma-separated list of related topics
    image_tagged_topics = models.CharField(max_length=200)
    image_Post = models.ImageField(upload_to='posts/')  # Example upload path
    created_at = models.DateTimeField(auto_now_add=True)  # Creation date/time

    def __str__(self):
        return f"{self.user.username} - {self.title}"

    class Meta:
        # Order boards by creation date (latest first)
        ordering = ['-created_at']


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(
        User, related_name='liked_by', on_delete=models.CASCADE)
    image_post = models.ForeignKey(
        Image_Posting, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} likes {self.image_post.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(
        User, related_name='commented_by', on_delete=models.CASCADE)
    image_post = models.ForeignKey(
        Image_Posting, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.image_post.title}"


class Following(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following_user')
    followed_by = models.ForeignKey(
        User, related_name='followed_by', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.followed_by.username} follows {self.user.username}"

    @property
    def followers_count(self):
        return self.user.followers.count()

    @property
    def following_users(self):
        return Following.objects.filter(followed_by=self.user)


class Save_Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_saver')
    user2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_owner')
    image = models.ForeignKey(Image_Posting, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user2.username} saves {self.image.title}"
