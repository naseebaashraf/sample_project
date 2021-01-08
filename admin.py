from django.contrib import admin

# Register your models here.
from.models import user_login, pic_pool,student

admin.site.register(user_login)
admin.site.register(pic_pool)
admin.site.register(student)

