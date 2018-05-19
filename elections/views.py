from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum
from .models import Candidate, Poll, Choice
import datetime

# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates' : candidates} #context에 모든 후보에 대한 정보를 저장
    return render(request, 'elections/index.html', context) # context로 html에 모든 후보에 대한 정보를 전달

def areas(request, area):
    today = datetime.datetime.now() # 오늘의 날짜를 가져옵니다.
    try :
        poll = Poll.objects.get(area = area, start_date__lte=today, end_date__gte=today)
        # get에 인자로 조건을 전달해줍니다.
        candidates = Candidate.objects.filter(area = area)
        # Candidate의 area와 매개변수 area가 같은 객체만 불러오기
    except: # 에러가 발생한다면
        poll = None # poll을 가져올 필요 없습니다. None으로 지정.
        candidates = None # candidates도 마찬가지
    context = {'candidates': candidates,
    'area' : area,
    'poll' : poll }
    return render(request, 'elections/area.html', context)

def polls(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    selection = request.POST['choice'] # choice 키의 값을 가져옵니다. 후보자 id가 담겨 있습니다.

    try:
        choice = Choice.objects.get(poll_id = poll_id, candidate_id=selection)
        choice.votes +=1 # choice 레코드의 지지자 수를 1 증가
        choice.save()
    except: # 만약 처음으로 한 투표라면, 새 레코드를 생성해야 합니다.
        choice = Choice(poll_id = poll_id, candidate_id= selection, votes=1)
        choice.save()
    return HttpResponseRedirect("/areas/{}/results".format(poll.area))  # 이걸 추가해주세요

def results(request, area):
    candidates = Candidate.objects.filter(area = area)
    polls = Poll.objects.filter(area = area)
    poll_results = []
    for poll in polls:
        result = {}
        result['start_date'] = poll.start_date
        result['end_date'] = poll.end_date

        #먼저 득표수를 가져옵니다.
        # poll.id(한 여론조사)에 해당하는 전체 투표수
        total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))
        #db에서 import한 sum()은 votes 필드의 값을 전부 더하는 함수입니다.
        #그런데 이 sum()은 딕셔너리를 반환하는데, 이 경우에는 그 key가 votes__sum 입니다.
        # {'votes__sum' : 결과값} 형태로 되어 있는 것이죠. 따라서 결과값을 사용하려면 다음과 같이 합니다.
        result['total_votes'] = total_votes['votes__sum']

        rates = [] #지지율
        for candidate in candidates:
            # choice가 하나도 없는 경우(한 표도 받지 못한 경우입니다.) - 예외처리로 0을 append
            try:
                choice = Choice.objects.get(poll = poll, candidate = candidate)
                #현재 poll 객체와 candidate로 choice 테이블을 쿼리. 여론조사의 결과를 choice에서 가져온다.
                rates.append( round(choice.votes * 100 / result['total_votes'], 1)  )
                #아까 가져온 total_votes는 전체 표 수. 그리고 choice.votes는 현재 후보의 득표수.
                #현재 후보의 득표수 / 전체 득표수 = 지지율이다.
            except :
                rates.append(0)
        result['rates'] = rates # rates는 요소 하나 (지지율 혹은 0) 이 담긴 리스트입니다.
        #rates를 리스트 말고 그냥 변수로 하면 안되나 *?
        poll_results.append(result)

    context = {'candidates':candidates, 'area':area,
    'poll_results' : poll_results}
    return render(request, 'elections/result.html', context)

def candidates(request, name):
    candidate = Candidate.objects.get(name = name)
    return HttpResponse(candidate.name)