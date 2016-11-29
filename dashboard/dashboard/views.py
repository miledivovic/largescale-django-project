from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.conf.urls.static import static
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from mysite.settings import XMLFILES_FOLDER


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'dashboard/index.html', context)


def dashboard(request):
	json_file = XMLFILES_FOLDER+"/data.json"
	print json_file

	f = open(json_file)
	d = f.readline()
	return render(request, 'dashboard/dashboard.html', {"JSONdata" : d})


def config(request):
    return render(request, 'dashboard/config.html')




# def data(request):
#     json_file = "/Users/clararubin/Desktop/django-sample/mysite/dashboard/static/dashboard/data.json"
#     f = open(json_file)
#     d = f.readline()
#     f.close()
#     return render(request, 'dashboard/data.html', {"data" : d})



# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'dashboard/detail.html', {'question': question})



# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'dashboard/results.html', {'question': question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'dashboard/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('dashboard:results', args=(question.id,)))     


