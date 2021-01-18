
from django.contrib import admin
from .models import Product
from .models import Teachingstaff
from .models import nonTeachingstaff
from .models import others
from .models import collegenotices
# Register your models here.

admin.site.register(Teachingstaff)
admin.site.register(nonTeachingstaff)
admin.site.register(others)
admin.site.register(collegenotices)