from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_course_update_email(recipient_email, course_name):
    subject = f'Обновление курса: {course_name}'
    message = f'Материалы курса "{course_name}" были обновлены. Проверьте новые уроки!'
    send_mail(subject, message, 'no-reply@example.com', [recipient_email])
