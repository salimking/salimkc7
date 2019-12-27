from django.contrib import admin
from .models import Doctor
from .models import order
from .models import products
from .models import kart
from .models import Confirm
from .models import users
from .models import Report
from .models import File

from .models import Patient




admin.site.register(Doctor)
admin.site.register(order)
admin.site.register(products)
admin.site.register(kart)
admin.site.register(Confirm)
admin.site.register(users)

admin.site.register(File)
admin.site.register(Patient)