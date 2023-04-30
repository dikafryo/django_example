from django.urls import path
from .views import base_views, board_views, comment_views
# url의 name 값이 다른 모듈과 겹치면 오류가 발생하기에 app_name 을 지정해서 bullets에서만 사용하도록 하자.
app_name = 'bullets'
urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:board_id>/', base_views.detail, name='detail'),
    path('board/write/', board_views.board_write, name='board_write'),
    path('board/modify/<int:board_id>/', board_views.board_modify, name='board_modify'),
    path('board/delete/<int:board_id>/', board_views.board_delete, name='board_delete'),
    path('board/vote/<int:board_id>/', board_views.board_vote, name='board_vote'),
    path('comment/write/<int:board_id>/', comment_views.comment_write, name='comment_write'),
    path('comment/modify/<int:comment_id>/', comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),
    path('comment/vote/<int:comment_id>/', comment_views.comment_vote, name='comment_vote'),
]