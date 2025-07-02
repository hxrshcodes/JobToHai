from django.contrib import admin
from .models import *
# Register your models here.

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1  # Number of empty forms to display

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_no')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [AchievementInline, ExperienceInline, EducationInline, ProjectInline, SkillInline]

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'personal_info')
    search_fields = ('title',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'personal_info', 'start_date', 'end_date')
    search_fields = ('title', 'organization')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'personal_info', 'start_date', 'graduation_date')
    search_fields = ('school', 'degree')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'personal_info')
    search_fields = ('title',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'personal_info')
    search_fields = ('skill',)

@admin.register(UserMaster)
class usermaster_model(admin.ModelAdmin):
    list_display = ('id','email','password','role','is_active','is_verified','is_created','is_updated')

@admin.register(Candidate)
class candidate_model(admin.ModelAdmin):
    list_display = ('user_id','name')

@admin.register(Company)
class company_model(admin.ModelAdmin):
    list_display = ('user_id','name')

