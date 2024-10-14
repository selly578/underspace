from django.contrib import admin
from .models import Board,Post,Comment,Announcement

# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id","name") 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id","title","date_created")

    def has_add_permission(self,*args, **kwargs):
        return False
    
    def has_change_permission(self,*args, **kwargs):
        return False

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","date_created")

    def has_add_permission(self,*args, **kwargs):
        return False
    
    def has_change_permission(self,*args, **kwargs):
        return False

@admin.register(Announcement)
class AnnoucementAdmin(admin.ModelAdmin):
    list_display = ("title","date_created","author")
    readonly_fields = ("author",)
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('admin',)
        return self.readonly_fields

    def admin_display(self, obj):
        return obj.admin.username if obj.admin else "Belum Ditentukan"
  
    