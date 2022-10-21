from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

User = get_user_model()


class Post(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('draft', 'Draft')
    )

    user = models.ForeignKey(
        verbose_name='Автор поста',
        to=User,
        on_delete=models.CASCADE,
        related_name='publications'
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, primary_key=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images')
    status = models.CharField(
        max_length=12, 
        choices=STATUS_CHOICES, 
        default='draft')
    tag = models.ManyToManyField(
        to='Tag',
        related_name='publications',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('created_at', )


class Tag(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(primary_key=True, blank=True, max_length=35)

    def __str__(self):
        return self.title