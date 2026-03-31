from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from common.email import send_email_in_thread


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f'Creating user {instance}')
        if instance.email:
            print(f'User dont have email {instance.email}')
            send_email_in_thread(
                subject="Welcome",
                message=f"Hi ms, {instance.username} Your account has been created!",
                recipient=instance.email
            )
        else:
            print(f"User dont have email {instance.username}")
    else:
        print(f'Congratulations for updating {instance}')
