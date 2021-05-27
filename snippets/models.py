from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


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
    owner = models.ForeignKey('auth.user', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']
    

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title':self.title} if self.title else {}
        formatter = HtmlFormatter(style = self.style, linenos = linenos, full=True, **options)
        self.highlighted = highlight(self.code,lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
    
