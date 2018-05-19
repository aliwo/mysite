from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>[a-z]+)/$', views.areas), # 한글을 입력받으려면 가-힣 사용
    url(r'^areas/(?P<area>[a-z]+)/results$', views.results), #\d로 숫자만 입력받습니다.
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^candidates/(?P<name>[a-z]+)/$', views.candidates),
]