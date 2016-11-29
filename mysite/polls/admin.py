from django.contrib import admin

from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

    def get_extra(self, request, obj=None, **kwargs):
        if obj == None:
            return self.extra
        elif obj.choice_set.count() >= 3:
            return 1
        else:
            return self.extra - obj.choice_set.count()

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

