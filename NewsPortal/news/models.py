from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.core.cache import cache


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Авторы")
    ratingAuthor = models.SmallIntegerField(default=0, verbose_name="Рейтинг автора")

    def __str__(self):
        return '{}'.format(self.authorUser)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        comRat = 0
        comRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + comRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Категория")
    subscribers = models.ManyToManyField(User, through='Subscriber')

    def __str__(self):
        return self.name

    def get_subscribers(self):
        return ",\n".join([str(p) for p in self.subscribers.all()])


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Авторы")

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE, verbose_name="Тип")
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    postCategory = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0, verbose_name="Рейтинг")

    def __str__(self):
        return '{}'.format(self.pk)

    def get_absolute_url(self):
        return reverse('news detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class Subscriber(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )