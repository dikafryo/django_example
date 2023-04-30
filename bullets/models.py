# DB사용
from django.db import models
# 회원DB
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_author')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    voter = models.ManyToManyField(User, related_name='board_voter')    # 추천인 추가

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    voter = models.ManyToManyField(User, related_name='comment_voter')    # 추천인 추가

    def __str__(self):
        return self.content