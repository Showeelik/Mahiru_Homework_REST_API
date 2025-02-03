from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_course_update_email(recipient_email, course_name):
    subject = f'Обновление курса: {course_name}'
    message = f'Материалы курса "{course_name}" были обновлены. Проверьте новые уроки!'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])
