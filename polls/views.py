from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice
from django.http import Http404
import logging

logger = logging.getLogger(__name__)

def index(request):
    '''latest_question_list=list(reversed(Question.objects.order_by("-pub_date")[:7]))
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}'''
    return render(request, "polls/main_page.html")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Знаходимо наступне питання
    next_question = Question.objects.filter(pk__gt=question_id).first()
    next_question_id = next_question.id if next_question else None

    return render(request, "polls/Questions.html", {
        "question": question,
        "next_question_id": next_question_id
    })


logger = logging.getLogger(__name__)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/Questions.html', {
            'question': question,
            'error_message': "Виберіть варіант відповіді.",
        })
    else:
        # Оновлюємо бали у сесії
        if 'score' not in request.session:
            request.session['score'] = 0
        request.session['score'] += selected_choice.points

        # Переходимо до наступного питання або результатів
        next_question = Question.objects.filter(pk__gt=question_id).first()
        if next_question:
            return redirect('polls:detail', question_id=next_question.id)
        else:
            return redirect('polls:results')  # Перехід до сторінки результату


def results(request):
    # Отримуємо бали із сесії
    score = request.session.get('score', 0)
    
    # Очищаємо бали після перегляду результатів
    if 'score' in request.session:
        del request.session['score']
    
    return render(request, 'polls/results.html', {'score': score})



