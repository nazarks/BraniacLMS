from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models

# from authapp import models as authapp_models
# get_user_model()


@admin.register(get_user_model())
class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "is_staff", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["is_active", "is_staff"]


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]
    list_display = ["id", "title", "deleted"]
    list_editable = ["deleted"]
    list_filter = ["created"]


@admin.register(mainapp_models.Courses)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["name", "description"]
    list_display = ["id", "name", "deleted"]
    list_editable = ["deleted"]
    list_filter = ["created", "cost"]
    actions = ["set_free"]

    def set_free(self, request, queryset):
        queryset.update(cost=0)

    set_free.short_description = _("Set cost 0")


@admin.register(mainapp_models.CourseFeedback)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "rating", "user", "feedback", "course", "deleted"]
    list_editable = ["deleted"]
    list_filter = ["created"]
    ordering = ["rating"]
    list_per_page = 5


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 5
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted"]
    search_fields = ["title", "description"]
    list_editable = ["deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(mainapp_models.CourseTeachers)
class CourseTeachersAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "get_courses"]
    list_select_related = True

    def get_courses(self, obj):
        return ", ".join((i.name for i in obj.course.all()))

    get_courses.short_description = _("Courses")
