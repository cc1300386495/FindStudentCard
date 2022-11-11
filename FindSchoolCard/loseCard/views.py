from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Lose
from findCard.models import Find
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'loseCard/index.html')


def result(request):
    CardId = request.POST['student_id']
    student_email = request.POST['student_email']
    try:  # 检查ID是否在FIind数据库里
        message = Find.objects.get(pk=CardId)
        content = '您好，您的校园卡被放在了[ ' + message.location + \
            ' ]请及时拿回哦~' + '\n' + '捡到的时间为' + str(message.find_day)
        send_mail(
            "您的校园卡招领邮件",
            content,
            'xnbgfrdv69@foxmail.com',
            [student_email],
            auth_user='xnbgfrdv69@foxmail.com',
            auth_password='fynwewotziykgdhb'

        )
        message.delete()
    except Find.DoesNotExist:
        try:  # 如果已经存在
            new_lose = Lose.objects.create(
                student_id=CardId,
                student_email=request.POST['student_email']
            )
            new_lose.save()
        except:
            send_mail(
                "您的校园卡招领邮件",
                '您已经提交过一次了哦~',
                'xnbgfrdv69@foxmail.com',
                [student_email],
                auth_user='xnbgfrdv69@foxmail.com',
                auth_password='fynwewotziykgdhb'

            )
    return HttpResponse("Ok")
