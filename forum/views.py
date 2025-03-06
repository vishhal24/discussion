from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Comment
from .forms import TopicForm, CommentForm

def topic_list(request):
    topics = Topic.objects.all().order_by('-created_at')
    return render(request, 'forum/topic_list.html', {'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    comments = topic.comments.all()
    comment_form = CommentForm()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.topic = topic
            comment.save()
            return redirect('topic_detail', topic_id=topic.id)
    
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'comments': comments, 'comment_form': comment_form})

def create_topic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic_list')
    else:
        form = TopicForm()
    return render(request, 'forum/create_topic.html', {'form': form})
