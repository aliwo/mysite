from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=10) # 길이 10인 문자열 필드입니다.
    introduction = models.TextField() # 길이 제한 없는 문자열이에요
    area = models.CharField(max_length=15) # 지역구를 나타내요
    party_number = models.IntegerField(default=0)
    # 기호를 나타내는 정수 필드입니다.
    # 나: 원래 사칙연산이 의미가 없는 숫자는 문자로 표현하는게 맞음.

    def __str__(self):
        return self.name

class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length = 15) # 지역구

class Choice(models.Model):
    poll = models.ForeignKey(Poll) #Poll 모델의 id를 이용
    candidate = models.ForeignKey(Candidate) # 후보자 테이블도 가져와요
    votes = models.IntegerField(default = 0) # 지지자 수