from django.db import models

STATUS_CHOICES = [
    ('active','Активно'),
    ('blocked','Заблокировано')
]

class Record(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, verbose_name='Автор')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active', verbose_name='Активно')
    text = models.TextField(max_length=255,null=False, blank=False, verbose_name='Текст')
    email = models.EmailField(max_length=255, null=False, blank=False, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.author, self.email)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ['-created_at']

