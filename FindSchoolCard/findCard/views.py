from django.shortcuts import render, HttpResponse
from .models import Find
from django.utils import timezone
from loseCard.models import Lose
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request, 'findCard/index.html')


def result(request):
    find_id = request.POST['student_id']
    location = request.POST['location']
    find_day = timezone.now()
    try:
        message = Lose.objects.get(pk=find_id)
        student_email = message.student_email
        content = '您好，您的校园卡被放在了[ ' + location + \
            ' ]请及时拿回哦~' + '\n' + '捡到的时间为' + str(find_day)
        send_mail(
            "您的校园卡招领邮件",
            content,
            'xnbgfrdv69@foxmail.com',
            [student_email],
            auth_user='xnbgfrdv69@foxmail.com',
            auth_password='fynwewotziykgdhb'

        )
        message.delete()
    except Lose.DoesNotExist:
        try:
            new_find = Find.objects.create(
                student_id=find_id, location=location, find_day=find_day)
            new_find.save()
        except:
            print("用于测试git")
    return HttpResponse("提交成功，感谢你的帮助哦~")
