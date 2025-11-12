from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_ticket_email(ticket_id, email):
    subject = f"Ticket #{ticket_id} Created"
    message = "Your ticket has been created successfully."
    send_mail(subject, message, "support@example.com", [email])
