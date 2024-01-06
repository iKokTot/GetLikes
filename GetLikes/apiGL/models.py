from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class UserProfile (models.Model):
    vk_user_id = models.PositiveIntegerField(unique=True)
    access_token = models.CharField(max_length=255, verbose_name='токен')
    email = models.EmailField(verbose_name='email пользователя')
    wallet = models.IntegerField(default=0,  verbose_name='Время жизни')

class Subscription (models.Model):
    class Status(models.IntegerChoices):
        not_signet = 0, 'Не подписан'
        signet = 1, 'Подписан'
    id_subscriber = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='uesr_subscriber', verbose_name='id подписчика')
    subscription = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.not_signet, blank=False, verbose_name='Подписка')
    subscription_time = models.DateTimeField(auto_now=True, verbose_name='Время подписки')

class Balance (models.Model):
    makings = models.IntegerField(blank=False, verbose_name="Общий доход пользователей")
    expenditure = models.IntegerField(blank=False, verbose_name="Общий расход пользователей")

class Service (models.Model):
    name = models.CharField(blank=False, verbose_name="Название")
    price = models.IntegerField(blank=False, verbose_name='цена')

class History (models.Model):
    id_customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='customer_history', verbose_name='id заказчика')
    id_fulfiller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='fulfiller_history', verbose_name='id оценившего')
    id_service = models.ForeignKey(Service,on_delete=models.CASCADE, related_name='service_history', verbose_name='id услуги')
    album = models.CharField(blank=True, verbose_name="Альбом фотографии")
    photo = models.CharField(blank=True, verbose_name="фотография")

class Orders (models.Model):
    id_customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='customer_orders', verbose_name='id покупателя')
    id_service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='service_orders', verbose_name='id услуги')
    count = models.IntegerField(blank=True, verbose_name='количество')
    album = models.CharField(blank=True, verbose_name="Альбом фотографии")
    photo = models.CharField(blank=True, verbose_name="фотография")