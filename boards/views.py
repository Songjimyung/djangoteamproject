from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, DeleteView
from .models import Board
from django.urls import reverse_lazy
from .forms import BoardForm
from django.http import HttpResponse

# Create your views here.
# 추후 로그인 리콰이어


def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            # board.author
            board.save()

            return HttpResponse('작성 성공')
            # return render(request, 'board/board.html')
    else:
        form = BoardForm()
    return render(request, 'board/create_board.html', {'form': form})


def board_list(request):
    if request.method == 'GET':
        boards = Board.objects.all()

        return render(request, 'board/board_list.html', {'boards': boards})


def board_delete(request, board_id):
    Board.objects.filter(board_id=board_id).delete()
    return redirect('/board/list/')


# class Board(View):
#     def get(self, request):
#         boards = Board.objects.all()
#         return render(request, "board.html", {'boards': boards})

#     def post(self, request):
#         # user_id
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         board = Board.objects.create(title=title, contnet=content)

#         return redirect('/board/')

# class BoardCreate(View):
#     def get(self):
#         return redirect("/board_create.html")


# class BoardListView(ListView):
#     model = Board
#     template_name = 'board_list.html'
#     context_object_name = 'board_list'

# class BoardDelete(DeleteView):
#     model = Board
#     template_name = 'board_detail.html'
#     # URL 문자열을 동적을 생성하기 위해 reverse_lazy()를 쓴다
#     success_url = reverse_lazy('board')

# 추후 로그인 리콰이어, 나누게 된다면 쓰일 듯
# class BoardCreate(CreateView):
#     model = Board
#     fields = ['title', 'content'] # user_id
#     template_name = 'board_create.html'
#     success_url = '/board/'

# 게시글 이미지는 나중에 넣기? 관련 뷰가 있던 것 같음
