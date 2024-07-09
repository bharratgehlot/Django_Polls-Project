from django.contrib import admin
from .models import Question, Choice, Responses, User

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Responses)
admin.site.register(User)
