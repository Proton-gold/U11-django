from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()

    class Meta:
        db_table = 'category'


class Question(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'answer'
