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
    show_change_link = True


class GameRoundAdmin(admin.ModelAdmin):
    list_display = ('name', 'game_plan', 'date_time', 'fake_user_count', 'complete')
    inlines = [GameRoundUserInLIne]


admin.site.register(GameRound, GameRoundAdmin)






class GameRoundUserTaskInLine(admin.TabularInline):
    model = GameRoundUserTask
    fields = ('dim_percent','score','start_time','score_log','complete')
    readonly_fields = ('start_time','score_log','complete')


class GameRoundUserAdmin(admin.ModelAdmin):
    fields = ('game_round','fake_user','user')
    readonly_fields = ('game_round',)
    inlines = [GameRoundUserTaskInLine]


admin.site.register(GameRoundUser, GameRoundUserAdmin)
