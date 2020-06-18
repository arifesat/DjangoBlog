from django.contrib import admin
# Own Code
from .models import Article,Comment
# Register your models here.
# Own Code
admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]

    #Django böyle yap diyor. 
    class Meta:
        model = Article