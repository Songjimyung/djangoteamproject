from django.shortcuts import render, redirect
from django.views.generic import View
# from .forms import BookmarkForm
from .models import Bookmark
from django.contrib.auth.decorators import login_required
from boards.models import Board
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def add_bookmark(request, board_id):
    board = Board.objects.get(pk=board_id)
    user_bookmarks = Bookmark.objects.filter(user=request.user)
    if user_bookmarks.filter(boards=board).exists():
        # 북마크에 있는 게시글
        messages.warning(request, '이미 북마크에 추가된 게시글입니다.')
    else:
        # 북마크에 없는 게시글
        bookmark = Bookmark.objects.create(user=request.user)
        bookmark.boards.add(board)
        messages.success(request, '게시글이 북마크에 추가되었습니다.')

    return redirect('board_detail', board_id=board_id)


# @login_required는 해당 view함수가 실행되기 전에 인증 여부를 확인하므로,
# View 클래스를 상속한 클래스에서는 작동하지 않는다.
# LginRequiredMixin 클래스를 상속해야 클래스에 적용이 가능하다.
class BookmarkList(LoginRequiredMixin, View):
    def get(self, request):
        bookmarks = Bookmark.objects.filter(user=request.user)
        boards = [bookmark.boards.all()[0] for bookmark in bookmarks]
        context = {'boards': boards, 'username': request.user.username}
        return render(request, 'bookmark/bookmark_list.html', context)

# updated_at을 이용해서 최신 순으로 주르륵 떠야하고

# img가 있다면 img도 가져오고
# content와 updated_at도 가져오기
# if request.method == 'GET':
#             boards = Board.objects.all().order_by('-updated_at')

# def bookmark_list(request):

#     bookmarks = request.user.bookmark_set.all()
#     context = {'bookmarks': bookmarks}
#     return render(request, 'bookmark/bookmark_list.html', context)
