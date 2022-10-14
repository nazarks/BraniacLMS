from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from mainapp.managers.news_manager import CoursesManager


class News(models.Model):

    title = models.CharField(max_length=256, verbose_name=_("Title"))
    preambule = models.CharField(max_length=1024, verbose_name=_("Preambule"))
    body = models.TextField(blank=True, null=True, verbose_name=_("Body"))
    body_as_markdown = models.BooleanField(default=False, verbose_name=_("As markdown"))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, editable=False, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ("-created",)


class Courses(models.Model):
    objects = CoursesManager()

    name = models.CharField(max_length=256, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name=_("As markdown"), default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Cost"), default=0)
    cover = models.CharField(max_length=25, default="no_image.svg", verbose_name=_("Cover"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Edited"))
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")


class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name=_("Lesson number"))
    title = models.CharField(max_length=256, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name=_("As markdown"), default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"), editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Edited"), editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ("course", "num")
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")


class CourseTeachers(models.Model):
    course = models.ManyToManyField(Courses)
    name_first = models.CharField(max_length=128, verbose_name=_("Name"))
    name_second = models.CharField(max_length=128, verbose_name=_("Surname"))
    day_birth = models.DateField(verbose_name=_("Birth date"))
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.name_second, self.name_first)

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")


class CourseFeedback(models.Model):
    RATING = ((5, "⭐⭐⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (3, "⭐⭐⭐"), (2, "⭐⭐"), (1, "⭐"))
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name=_("Course"))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    feedback = models.TextField(default=_("No feedback"), verbose_name=_("Feedback"))
    rating = models.SmallIntegerField(choices=RATING, default=5, verbose_name=_("Rating"))
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course} ({self.user})"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["course", "user"], name="course_user_unique"),
        ]
