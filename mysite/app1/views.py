from django.shortcuts import render
import tweepy
import sys
from .forms import nameform
from django.http import HttpResponse
from django.template import loader
from .models import Question,Choices,tweets
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
	i=0
	try:
		auth= tweepy.OAuthHandler('3aubzHcBB8lesUUnzVhKqqh1h','zHW2L0ghwOYxSPcBduc5CHtfOpmatC1aCa54BQ3OWHpbMrReIX')
		auth.set_access_token('4622562707-q9dZK6DDmBHVafKaRDaAwFWpJ5yF7LY3ttRZsnb','2H01iMM6K1jQzjRoiQZSqAzn9KkGpxv3CRHQppg4poOC7')
		resp= tweepy.API(auth)
		count=0
		arr=[]
		hashtags=[]
		tweets.objects.all().delete()
		for status in tweepy.Cursor(resp.user_timeline,id=request.GET['username']).items(100):
				li=status.text.encode("utf8")
		##trying from here
				t = tweets(tweet=li)
				t.save()
				terra = li.split()
				for s in terra:
					if s[0]=='@':
						if s[len(s)-1]==":":
							arr.append(s[0:len(s)-1])
				for s in terra:
					if s[0]=='#':
						if s[len(s)-1]==":":
							hashtags.append(s[0:len(s)-1])
				# process status here
				#tw=tweets(tweet=li[i])
		##ends here##
		##entries for html
		tweet_list = tweets.objects.all()
		template = loader.get_template("tweetlist.html")
		context = {
			'tweet_list':tweet_list,
			'common':max(set(arr), key=arr.count),
			'hash_tags':max(set(hashtags), key=hashtags.count)
		}
		#
		##end of entries
		#return HttpResponse(max(set(arr), key=arr.count))
		return HttpResponse(template.render(context,request))
	except :
		latest_question_list = Question.objects.order_by('-pub_date')[:5]
		template = loader.get_template('index.html')
		context = {
			'latest_question_list': latest_question_list,
		}
		return HttpResponse(template.render(context, request))
	#return HttpResponse("You're looking at question %s." % question_id)
def detail(request , question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'detail.html', {'question': question})
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse("This is the respose")
def vote(request, question_id):
	try:
		question = get_object_or_404(Question, pk=question_id)
		selected_choice = question.choice_set.get(pk=request.POST[choice])
	except (KeyError, Choices.DoesNotExist):
		return render(
		request,'detail.html',{
			'question':question,
			'error_message':"you did not select a choice",
		})
	else:
		selected_choice+=1
		selected_choice.save()
	return HttpResponseRedirect(reverse('app1:results', args=(question.id,)))
def auth(request):
	try:
		auth= tweepy.OAuthHandler('3aubzHcBB8lesUUnzVhKqqh1h','zHW2L0ghwOYxSPcBduc5CHtfOpmatC1aCa54BQ3OWHpbMrReIX')
		auth.set_access_token('4622562707-q9dZK6DDmBHVafKaRDaAwFWpJ5yF7LY3ttRZsnb','2H01iMM6K1jQzjRoiQZSqAzn9KkGpxv3CRHQppg4poOC7')
		resp= tweepy.API(auth)
		count=0
		for status in tweepy.Cursor(resp.user_timeline,id="ndtvindia").items(2):
				li = status.text.encode("utf8")
				# process status here
		return HttpResponse(li)
	except:
		return HttpResponse(sys.exc_info())
def get(request,username):
	return HttpResponse(username)
#################################################################################333
def get_name(request):
	if request.METHOD=='POST':
		form = nameform(request.POST)
		if form.is_valid():
			return HttpResponse("This is valid")
		else:
			return HttpResponse("This is not valid")
	else:
		return HttpResponse("This was not post method")
	return HttpResponse("Waste method")