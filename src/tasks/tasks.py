import smtplib
from email.message import EmailMessage

from celery import Celery
from config import settings

celery = Celery("tasks", broker=settings.redis_url)

def get_email_template_dashboard(username: str) -> EmailMessage:
    email = EmailMessage()
    email["Subject"] = "Report"
    email["From"] = settings.smtp_user 
    email["To"] = "to_ev@mail.ru"

    email.set_content(
        f"<h1>Привет, {username}, как дела?</h1>",
        subtype="html"
    )

    return email

@celery.task
def send_email_report_dashboard(username: str) -> None:
    ''' Task for Celery to send email '''
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(settings.smtp_host, settings.smtp_port) as server:
        server.login(
            user=settings.smtp_user, 
            password=settings.smtp_password
        )
        server.send_message(email)

        


