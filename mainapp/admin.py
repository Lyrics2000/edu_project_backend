from django.contrib import admin
from .models import (
    ExtraInfo,
    EmployerDetails,
    SchoolAttended,
    Scholarship,
    Application,
    Feedback,
    Response,
    Slider,
    AboutSection,
    UserProfile
)

# Register your models here.
admin.site.register(ExtraInfo)
admin.site.register(EmployerDetails)
admin.site.register(SchoolAttended)
admin.site.register(Scholarship)
admin.site.register(Application)
admin.site.register(Feedback)
admin.site.register(Response)
admin.site.register(Slider)
admin.site.register(AboutSection)
admin.site.register(UserProfile)
