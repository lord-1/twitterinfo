from django.shortcuts import render
import tweepy
import sys
from collections import Counter
from .forms import nameform
from django.http import HttpResponse
from django.template import loader
from .models import tweets
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
	try:#try for authentication
		#authentication begin
		auth= tweepy.OAuthHandler('3aubzHcBB8lesUUnzVhKqqh1h','zHW2L0ghwOYxSPcBduc5CHtfOpmatC1aCa54BQ3OWHpbMrReIX')
		auth.set_access_token('4622562707-q9dZK6DDmBHVafKaRDaAwFWpJ5yF7LY3ttRZsnb','2H01iMM6K1jQzjRoiQZSqAzn9KkGpxv3CRHQppg4poOC7')
		resp= tweepy.API(auth)
		#auth complete
		count=0
		number=""
		arr=[]
		hashtags=[]
		try:#try for user exists or not
			subject = resp.get_user(request.GET['username'])
			tweets.objects.all().delete()
			#getting statuses
			for status in tweepy.Cursor(resp.user_timeline,id=request.GET['username']).items(200):
					li=status.text.encode("utf8")
					t = tweets(tweet=li)
					t.save()
					terra = li.split()
					for s in terra:
						if s[0]=='@' and s[len(s)-1]==":":#getting people
								arr.append(s[0:len(s)-1])
					for s in terra:#getting hashes
						if s[0]=='#':
							hashtags.append(s[0:len(s)])
			cnt1 = Counter()
			cnt2 = Counter()
			lix=[]
			liy=[]
			#counters to get the top elements
			for always in arr:
				cnt1[always]+=1
			for comm,comm2 in cnt1.most_common(5):
				lix.append(comm)
			for always in hashtags:
				cnt2[always]+=1
			for comm,comm2 in cnt2.most_common(5):
				liy.append(comm)
			tweet_list = tweets.objects.all()
			template = loader.get_template("tweetlist.html")
			context = {
				'tweet_list':tweet_list,
				'common':lix,
				'hash_tags':liy,
				'number':number, #user exists or not
				
			}
			return HttpResponse(template.render(context,request))
		except:#in case user doesnt exist
			if request.GET['username']!="":
				number="User doesnot exist "
			else:
				number = ""
			template = loader.get_template('index.html')
			context = {
				'number':number,
			}
			return HttpResponse(template.render(context,request))
	except :#incase the authentication fails
		template = loader.get_template('index.html')
		number = ""
		context = {
			'latest_question_list': latest_question_list,
			'number':number,
		}
		return HttpResponse(template.render(context, request))
