from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Choice, Question

# <HINT> Register QuestionInline and ChoiceInline classes here


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 3


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]


# <HINT> Register Question and Choice models here
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'question_grade', 'lesson']
    list_filter = ['question_text']
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text']
    list_filter = ['choice_text', 'is_correct']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
