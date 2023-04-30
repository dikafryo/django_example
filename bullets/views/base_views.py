# 게시글이 많을때 페이지처리하기
# render : html 페이지 랜더링
# get_object_or_404 : 글이 있으면보여주고, 해당번호의 글이 없으면 404 페이지
# 내가 만든 Board 앱
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from ..models import Board


# 로그인필요한 함수를 실행안되고 로그인으로 넘어가도록 함
# 메시지 알람을 띄운다.

def index(request):
    page = request.GET.get('page', '1') # 페이지값을 가져오고 없을경우 기본값을 1로한다.
    kw = request.GET.get('kw', '')  # 검색어를 가져오고 없을경우 기본값을 ""로한다.
    board_list = Board.objects.order_by('-date_created')
    if kw:
        board_list = board_list.filter(
            Q(title__icontains=kw) |   # 글제목 검색
            Q(content__icontains=kw) |   # 글내용 검색
            Q(comment__content__icontains=kw) |   # 댓글 제목검색
            Q(author__username__icontains=kw) |   # 글쓴이 검색
            Q(comment__author__username__icontains=kw)   # 댓글쓴이 검색
        ).distinct()
    paginator = Paginator(board_list, 30)   # 페이지당 보여질 갯수 설정
    page_obj = paginator.get_page(page)
    context = {'board': page_obj, 'page': page, 'kw': kw}
    return render(request, 'bullets/board_list.html', context)
def detail(request, board_id):
    # data = Board.objects.get(id=board_id)
    board = get_object_or_404(Board, pk=board_id)
    context = {'board': board}
    return render(request, 'bullets/board_detail.html', context)