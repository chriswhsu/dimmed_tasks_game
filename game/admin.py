from django.contrib import admin

from game.models import *


# Register your models here.

class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_editable = ('name', 'url')


admin.site.register(TaskType, TaskTypeAdmin)


class GamePlanTaskInLine(admin.TabularInline):
    model = GamePlanTask


class GamePlanAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [GamePlanTaskInLine]


admin.site.register(GamePlan, GamePlanAdmin)


class GameRoundUserInLIne(admin.TabularInline):
    model = GameRoundUser


class GameRoundAdmin(admin.ModelAdmin):
    list_display = ('name', 'game_plan', 'date_time', 'fake_user_count', 'complete')
    inlines = [GameRoundUserInLIne]


admin.site.register(GameRound, GameRoundAdmin)


admin.site.register(GameRoundUser)
