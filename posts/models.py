from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify, truncatechars


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(default='slug', max_length=25)

    def __str__(self):
        return self.title

    def post_count(self):
        return self.postByCategory.all().count()

    def save_base(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save_base(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, default='slug')

    def __str__(self):
        return self.title

    def save_base(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save_base(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(default='slug', max_length=20, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='postByCategory')
    slider_post = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='postByTags', blank=True)

    def __str__(self):
        return self.title

    def save_base(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save_base(*args, **kwargs)
