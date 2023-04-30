# render : html 페이지 랜더링
# get_object_or_404 : 글이 있으면보여주고, 해당번호의 글이 없으면 404 페이지
# redirect : 글쓰기시 글을 DB에 넣었으면 다시 글내용보기 화면으로 이동
# 메시지 알람을 띄운다.
from django.contrib import messages
# 게시글이 많을때 페이지처리하기
# 로그인필요한 함수를 실행안되고 로그인으로 넘어가도록 함
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
# timezone : 글수정시 수정일을 넣고싶을때 현재 시간을 가져옴. 사용안할때는 그냥 주석처리함.
from django.utils import timezone

# 폼 콘트롤을 위한 게시판 폼 로드
from ..forms import CommentForm
# 내가 만든 Board 앱
from ..models import Board, Comment


@login_required(login_url='common:login')
def comment_write(request, board_id):
    # bullets 댓글 등록하기
    board = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.board = board
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('bullets:detail', board_id=board_id), comment.id))
    else:
        form = CommentForm()
    context = {'board': board, 'form': form}
    return render(request, 'bullets/board_detail.html', context)
@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('bullets:detail', board_id=comment.board.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.date_modified = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('bullets:detail', board_id=comment.board.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form':form}
    return render(request, 'bullets/comment_modify.html', context)
@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다.')
    else:
        comment.delete()
    return redirect('bullets:detail', board_id=comment.board.id)
@login_required(login_url='common:login')
def comment_vote(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        messages.error(request, '본인댓글은 추천을 할 수 업습니다.')
    else:
        comment.voter.add(request.user)
    return redirect('{}#comment_{}'.format(resolve_url('bullets:detail', board_id=comment.board.id), comment.id))