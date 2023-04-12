<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardForm
from .models import Board
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user  # 로그인한 사용자를 작성자로 저장
            board.save()
            return redirect('board_list')
    else:
        form = BoardForm()
    return render(request, 'board/create_board.html', {'form': form})


def board_list(request):
    boards = Board.objects.all()
    return render(request, 'board/board_list.html', {'boards': boards})


# try except 구문을 이용한 상세보기
# def board_detail(request, board_id):
#     try:
#         board = Board.objects.get(pk=board_id)
#     except Board.DoesNotExist:
#         messages.error(request, '삭제된 글입니다')
#         return redirect('board.html')
#     return render(request, 'board/board_detail.html', {'board': board})


# django에서 제공하는 detailview를 활용함
class BoardDetail(DetailView):
    model = Board
    template_name = 'board/board_detail.html'


@login_required()
def board_edit(request, pk):
    board = Board.objects.get(pk=pk)

    if board.author != request.user:
        messages.error(request, '작성자만 수정이 가능합니다')
        return redirect('board_detail', pk=pk)

    else:

        if request.method == "POST":
            board.title = request.POST['title']
            board.content = request.POST['content']
            # board.id = request.POST['id']

            board.save()
            return redirect('board_detail', pk=board.pk)

        else:
            boardform = BoardForm(instance=board)
            return render(request, 'board/board_edit.html', {'boardform': boardform})

# django 내장 함수 UpdateView를 활용한 코드
# @login_required()
# class BoardUpdateView(UpdateView):
#     model = Board
#     form_class = BoardForm
#     template_name = 'board_edit.html'
#
#     def form_vaild(self, form):
#         board = form.save(commit=False)
#         board.id = self.request.user
#         board.(save)
#         return redirect('/board/{}/'.format(board.pk))

# django 내장 함수 FormView를 활용한 코드
# @login_required()
# class BoardEdit(FormView):
#     form_class = BoardForm
#     template_name = 'board_edit.html'
#
#     def get(self, request, pk):
#         board = get_object_or_404(Board, pk=pk)
#         form = self.form_clas(instance=board)
#         context = {'form': form, 'board': board}
#         return render(request, self.template_name, context)
#
#     def board(self, request, pk):
#         board = get_object_or_404(Board, pk=pk)
#         form = self.form_class(request.POST, instance=board)
#         if form.is_vaild():
#             form.save()
#             return redirect('board_detail', pk=board.pk)
#         context = {'form': form, 'board': board}
#         return render(request, self.template_name, context)
=======
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, DeleteView
from .models import Board
from django.urls import reverse_lazy, reverse
from .forms import BoardForm
from django.http import HttpResponse

# Create your views here.
# 추후 로그인 리콰이어

# APIView는 RESTful API를 만들기 위해 Djnago에서 제공하는 클래스 기반 뷰 중 하나
# RESTful API를 작성하는 데 필요한 다양한 기능을 제공한다.
# 요청과 응답을 직렬화하는 Serializer, 이증과 권한을 다루는 Permission 및 Authentication 클래스 등을 제공
# 각 HTTP 메서드(get,post,put,delete 등)에 대한 기본적인 구현을 제공
# 이를 오버라이드하여 원하는 기능을 구현 가능
# 그래서 APIView를 사용
class Boards(View):
    def get(self, request):
        form = BoardForm()
        return render(request, 'board/create_board.html', {'form': form})

    def post(self, request):
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            # board.author
            board.save()

            return redirect('/board/list/')

    def delete(self, request, board_id):
        Board.objects.get(board_id=board_id).delete()
        return redirect('/board/list/')


class BoardList(View):
    def get(self, request):
        if request.method == 'GET':
            boards = Board.objects.all().order_by('-updated_at')
            return render(request, 'board/board_list.html', {'boards': boards})
        return redirect('/board/')


# 게시글 이미지는 나중에 넣기? 관련 뷰가 있던 것 같음
>>>>>>> ad85b2fd6e281c1fbcce8b9c3a927d92031188b2
