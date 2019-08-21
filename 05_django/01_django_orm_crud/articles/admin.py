from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성한다.
    list_display = ('pk', 'title', 'content', 'updated_at', 'created_at',)
    list_filter = ('created_at',)
    list_display_links = ('content',)
    list_editable = ('title',)
    # 기본값 = 1000
    list_per_page = 2

admin.site.register(Article, ArticleAdmin)
