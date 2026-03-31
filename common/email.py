from django.core.mail import send_mail
import threading

def send_simple_email(subject, message, recipient_list, fail_silently=False):
    send_mail(
        subject=subject,
        message=message,
        from_email="sultonovshoxrux98@gmail.com",
        recipient_list=recipient_list,
        fail_silently=fail_silently,
    )


def send_email_in_thread(subject, message, recipient):
    thread = threading.Thread(
        target=send_simple_email,
        args=(subject, message, [recipient]),
        daemon=True
    )
    thread.start()
