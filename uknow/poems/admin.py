from django.contrib import admin

from poems.models import Poem
from poems.models import Tag
from poems.models import Stock

class PoemAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class StockAdmin(admin.ModelAdmin):
    pass

admin.site.register(Poem, PoemAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Stock, StockAdmin)
