from django.contrib import admin

from game.models import *


# Register your models here.

class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_editable = ('name','url')


admin.site.register(TaskType, TaskTypeAdmin)


class GamePlanTaskTypeInLine(admin.TabularInline):
    model = GamePlanTaskType


class GamePlanAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [GamePlanTaskTypeInLine]


admin.site.register(GamePlan, GamePlanAdmin)
