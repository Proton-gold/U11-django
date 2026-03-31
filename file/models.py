from fileinput import filename

from django.contrib.admindocs.utils import docutils_is_available
from django.db import models

from common.models import Basemodel


def user_upload(instance, filename):
    if instance.created_by:
        return f'{instance.created_by.user_id}/{filename}'
    else:
        return (
            f'all_users/'
            f'/{filename}'

        )


class Document(Basemodel):
    title = models.CharField(max_length=60)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
