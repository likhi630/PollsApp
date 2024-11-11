from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone
from .models import Poll

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Assuming that the voting logic updates the question's votes or does some processing
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()

    # Redirect to the results page after voting
    return redirect('polls:results', pk=question.id)
def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})