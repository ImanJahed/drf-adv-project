from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.timezone import now

# Create your models here.
USER = get_user_model()


class Ad(models.Model):
    date_added = models.DateTimeField(_('Date Publish'), default=now)
    title = models.CharField(_('Title'), max_length=100)
    image = models.ImageField(_('Image'), upload_to='image')
    caption = models.TextField(_('Caption'))
    is_published = models.BooleanField(_('Is Published'), default=True, help_text=_(
        'Public Ads will be displayed in the api views.'))
    publisher = models.ForeignKey(USER, on_delete=models.CASCADE,
                                  related_name='%(class)s', blank=True, null=True, verbose_name=_('Publisher'))

    class Meta:
        ordering = ('-date_added',)
        get_latest_by = 'date_added'
        verbose_name = 'ad'
        verbose_name_plural = 'ads'

    def __str__(self):
        return self.title
