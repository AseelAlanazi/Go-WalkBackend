from django.contrib import admin
from .models import Place,FavoritePlace,ReviewAndComments
# Register your models here.

admin.site.register(Place)
admin.site.register(FavoritePlace)
admin.site.register(ReviewAndComments)