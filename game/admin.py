from django.contrib import admin

from game.models import *


# Register your models here.

class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)


admin.site.register(TaskType, TaskTypeAdmin)


class GameRoundUserInLine(admin.TabularInline):
    model = GameRoundUser
    list_display = ('user', 'name')


class GameRoundAdmin(admin.ModelAdmin):
    list_display = ('datetime',)
    inlines = [GameRoundUserInLine]


admin.site.register(GameRound, GameRoundAdmin)
