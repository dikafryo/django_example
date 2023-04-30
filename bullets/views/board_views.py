# render : html 페이지 랜더링
# get_object_or_404 : 글이 있으면보여주고, 해당번호의 글이 없으면 404 페이지
# redirect : 글쓰기시 글을 DB에 넣었으면 다시 글내용보기 화면으로 이동
# 메시지 알람을 띄운다.
from django.contrib import messages
# 게시글이 많을때 페이지처리하기
# 로그인필요한 함수를 실행안되고 로그인으로 넘어가도록 함
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# timezone : 글수정시 수정일을 넣고싶을때 현재 시간을 가져옴. 사용안할때는 그냥 주석처리함.
from django.utils import timezone

# 폼 콘트롤을 위한 게시판 폼 로드
from ..forms import BoardForm
# 내가 만든 Board 앱
from ..models import Board


@login_required(login_url='common:login')
def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user # 현재 로그인 사용자 정보
            board.date_modified = timezone.now()
            board.save()
            return redirect('bullets:index')
    else:
        form = BoardForm()
    data = {'form': form}
    return render(request, 'bullets/board_write.html', data)
@login_required(login_url='common:login')
def board_modify(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('bullets:detail', board_id=board_id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.date_modified = timezone.now()
            board.save()
            return redirect('bullets:detail', board_id=board_id)
    else:
        form = BoardForm(instance=board)
    context = {'form': form}
    return render(request, 'bullets/board_write.html', context)
@login_required(login_url='common:login')
def board_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('bullets:detail', board_id=board_id)
    board.delete()
    return redirect('bullets:index')
@login_required(login_url='common:login')
def board_vote(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.user == board.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        board.voter.add(request.user)
    return redirect('bullets:detail', board_id=board_id)
