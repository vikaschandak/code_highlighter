from django.db import models
from pygments import styles
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [i for i in get_all_lexers()if i[1]]
LANGUAGES = sorted((i[1][0], i[0])for i in LEXERS)
STYLES = sorted((i,i)for i in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGES, default='python', max_length=100)
    style = models.CharField(choices=STYLES,default='friendly',max_length=100)

    class Meta:
        ordering = ['created']