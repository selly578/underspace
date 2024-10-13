from django.shortcuts import render,redirect,get_object_or_404
from markdown import markdown 
from .models import Board,Post,Comment,Announcement
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

def rule(request):
    # print(rule)
    rule = Announcement.objects.filter(title="Peraturan").first()
    rule_content = rule.content
    rule_author = rule.author 

    if not rule_content:
        rule_content = ""
    rule_content = markdown(rule_content)
    return render(request,"rule.html",{"title": "Peraturan","rule_content": rule_content,"author": rule_author})


def about(request):
    about = Announcement.objects.filter(title="Tentang").first()
    if not about:
        about = ""
    about = markdown(about)
    return render(request,"rule.html",{"title": "Tentang website ini","rule_content": about,"author": None})