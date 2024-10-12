from django.shortcuts import render,redirect,get_object_or_404
from .models import Board,Post,Comment
from .forms import PostForm,CommentForm

# Create your views here.

def index(request):
    boards = Board.objects.all()
    return render(request,"index.html",{"boards": boards,"title": "Underspace - Tempat cerita tanpa batas"})

def board(request,name):
    posts = Post.objects.filter(board__name__contains=name).all()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            board = Board.objects.filter(name=name).first()
            post = form.save(commit=False)
            post.board = board
            post.save()
            return redirect("post",name=name,id=post.id)
    return render(request,"board.html",{"posts": posts,"title": name,"form": form})

def post(request,name,id):
    post = get_object_or_404(Post,id=id)
    form  = CommentForm()
    comments = Comment.objects.filter(post=id).all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect("post",name=name,id=id)
    return render(request,"post.html",{"post": post,"form": form,"title": post.title,"comments": comments})