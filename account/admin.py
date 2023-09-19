from django.contrib import admin
from .models import User, Members, Task

# Register your models here.
# admin.site.register(User)
# admin.site.register(taskcomplete)

class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'name')
    # list_filter = ('status',)
admin.site.register(User, PostAdmin)

# class Register(admin.ModelAdmin):
#     list_display= ('name', 'user', 'department')
# admin.site.register(register_table, Register)

class Member_Details(admin.ModelAdmin):
    list_display= ('name','email', 'department', 'year', 'contact_number', 'updated_on', 'domain' )
admin.site.register(Members, Member_Details)

class Tasks(admin.ModelAdmin):
    list_display= ( 'id','task', 'taskcom', 'user','completion_date' )
admin.site.register(Task, Tasks)

