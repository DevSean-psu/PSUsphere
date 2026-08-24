from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('college_name', 'created_at', 'updated_at')
    search_fields = ('college_name',)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('prog_name', 'college', 'created_at', 'updated_at')
    search_fields = ('prog_name',)
    list_filter = ('college',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('college',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'lastname',
        'firstname',
        'middlename',
        'program',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'student_id',
        'lastname',
        'firstname',
        'middlename',
    )
    list_filter = ('program',)


@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'organization',
        'date_joined',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'student__student_id',
        'student__lastname',
        'student__firstname',
        'organization__name',
    )
    list_filter = ('organization', 'date_joined')