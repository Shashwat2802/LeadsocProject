from import_export.admin import ImportExportModelAdmin 
from django.contrib import admin
from emp_data import models

#admin.register(models.Employee) 
admin.site.register(models.UploadFile)
#admin.site.register(models.Customer_Requirements)
#admin.site.register(models.Customer)
#admin.site.register(models.Employee)


@admin.register(models.Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('id','cName','cEmail','cUrl')
    search_fields = ['cName']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    

@admin.register(models.Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ('eFname','eLname','refer_Customer','eEmail','ePhone','eExperience','eskills','eRole','eMP_Type','estatus','leadsoc_joining_date','customer_start_date','remarks')
    search_fields = ['eFname','eLname','eEmail','ePhone','eMP_Type','eRole','estatus','eskills']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(models.Customer_Requirements)
class Customer_RequirementsAdmin(ImportExportModelAdmin):
    list_display = ('Requirement_Id','customers','Customer_Requirement_id','Required_skills','Job_Description','Required_Experience','Open_positions','remain_positions','Position_Status','Sales_Incharge','Bu_head')
    search_fields = ['Position_Status','Required_skills']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(models.CandidateList)
class CandidateList(ImportExportModelAdmin):
    list_display = ('candidate_name','interview_status')
    search_fields = ['candidate_name','interview_status']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(models.addEmpToCustomer)
class addEmpToCustomer(ImportExportModelAdmin):
    list_display = ('eFname','eLname','refer_Customer','eskills')
    search_fields = ['eFname','eLname','refer_Customer','eskills']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


    



