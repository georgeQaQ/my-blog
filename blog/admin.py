from django.contrib import admin
from .models import Post,PostAdmin

admin.site.register(Post,PostAdmin)
