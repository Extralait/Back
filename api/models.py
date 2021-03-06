from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    # Custom User Class
class userProfile(AbstractUser):
    username = None
    first_name = None
    last_name = None

    class RoleChoices(models.TextChoices):
        PARENT = 'parent', 'Родитель'
        ENROLLEE = 'enrollee', 'Абитуриент'

    status = models.CharField('Статус', max_length=10, choices=RoleChoices.choices)
    SNILS = models.IntegerField('СНИЛС', null=True)
    full_name = models.CharField('ФИО', max_length=100)
    email = models.EmailField('Email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Авторизированный'
        verbose_name_plural = 'Авторизированные'

    def __str__(self):
        return self.full_name



class Event(models.Model):
    organizer = models.CharField("Организатор", max_length=60)
    time = models.DateTimeField('Время' ,null=True,blank=True)
    link = models.CharField('Ссылка', unique=True, db_index=True, max_length=200)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.organizer

class User(models.Model):
    class RoleChoices(models.TextChoices):
        PARENT = 'parent', 'Родитель'
        ENROLLEE = 'enrollee', 'Абитуриент'

    status = models.CharField('Статус', max_length=12, choices=RoleChoices.choices)
    name = models.CharField("Фио", max_length=60)
    email = models.CharField('email' ,unique=True, max_length=40)
    number = models.IntegerField('Номер', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name

class Achievements(models.Model):
    text = models.TextField("Текст")
    photo = models.ImageField('Фото',blank=True, null=True, upload_to='achievements')

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.text

class BestStudent(models.Model):
    avatar = models.ImageField('Аватар',blank=True, null=True, upload_to='students')
    name = models.CharField('ФИО', max_length=60)
    achievements = models.TextField('Достижения', blank=True, null=True)

    class Meta:
        verbose_name = 'Лучший студент'
        verbose_name_plural = 'Лучшие студенты'
    def __str__(self):
        return self.name

class Photo(models.Model):
    class CategoryChoices(models.TextChoices):
        WEEKDAYS = 'weekdays', 'Будни студента'
        CAMPUS = 'campus', 'Кампус ДВФУ'
        EVENTS = 'events', 'Студенческие события'
        PREMISES = 'premises', 'Учебные помещения'
        LIBRARY = 'library', 'Библиотека'
        CREATIVE_CENTER = 'creative_center', 'Творческий центр'
        SPORT_LIFE = 'sport_life', 'Спортивная жизнь студентов'
        LABORATORIES = 'laboratories', 'Лаборатории'
        CENTER_NTI = 'center_nti', 'Центр НТИ'
        INTERNATIONAL_ACTIVITY = 'international_activity', 'Международная деятельность'
    category = models.CharField('Категория', max_length=30, choices=CategoryChoices.choices)
    img = models.ImageField('Фото',blank=True, null=True, upload_to=f'gallery')
    title = models.TextField('Описание',blank=True,null=True)
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
    def __str__(self):
        return self.title[:30]


class Organization(models.Model):
    name = models.CharField('Название направления', max_length=200, unique=True)
    school = models.CharField('Школа', blank=True, null=True, max_length=80)
    number = models.CharField('Код направления', blank=True, null=True,max_length=20)
    place = models.IntegerField('Бюджетных мест', blank=True, null=True)
    price = models.IntegerField('Цена обучения', blank=True, null=True)
    jsons = models.JSONField('Прочее', blank=True, null=True)
    best_students = models.ManyToManyField(BestStudent,verbose_name='Лучшие студенты', blank=True)
    offer = models.ManyToManyField('self', verbose_name='Предложение', blank=True)
    event = models.ForeignKey(Event, verbose_name='Вебинар', on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField('Логотип',blank=True, null=True, upload_to='org_logo')
    org_detail = models.TextField('Код направления', blank=True, null=True)
    video_link = models.TextField('Ссылка на видео',blank=True,null=True)
    plan = models.TextField('Учебный план',blank=True,null=True)
    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name