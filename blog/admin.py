from django.contrib import admin

from blog.models import Mahsulot, Haridor, Mol

from blog.models import Rasm

# Register your models here.

admin.site.register(Mahsulot)

admin.site.register(Rasm)

admin.site.register(Haridor)
admin.site.register(Mol)