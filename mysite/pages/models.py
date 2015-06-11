from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class User(models.Model):
    """docstring for User"""
    class Meta:
        verbose_name = "使用者"

    account = models.CharField("帳號", max_length=30)
    name = models.CharField("名稱", max_length=20)

    def __str__(self):
        return "%s(%s)" % (self.account, self.name)

class PageItem(models.Model):
    """docstring for Page"""
    class Meta:
        verbose_name = "Facebook 專頁"

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, related_name='created_page_items',
    )
    name = models.CharField("名稱", max_length=20)
    fb_id = models.BigIntegerField("Facebook 專頁編號")
    add_time = models.DateTimeField("加入時間", auto_now_add=True, editable=False)
    last_access_time = models.DateTimeField("上次存取時間", auto_now=True)
    last_like_count = models.IntegerField("上次粉絲人數")
    picture_url = models.CharField("大頭貼", max_length=250)
    notes = models.TextField("備註", blank=True, default="")


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('page_item_detail', kwargs={'pk': self.pk})


    def can_user_delete(self, user):
        if not self.creator or self.creator == user:
            return True
        if user.has_perm('pages.page_item_delete'):
            return True
        return False
