from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import TEXT_DISPLAY_LENGTH, TITLE_DISPLAY_LENGTH

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=200,
    )
    slug = models.SlugField(unique=True)
    description = models.TextField('Описание',)

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title[:TITLE_DISPLAY_LENGTH]


class Post(models.Model):
    text = models.TextField('Текст',)
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Изображение',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа',
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.text[:TEXT_DISPLAY_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Публикация',
    )
    text = models.TextField('Текст',)
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (f'Комментарий: {self.text[:TEXT_DISPLAY_LENGTH]}, '
                f'автора: {self.author}, '
                f'к публикации: {self.post}')
