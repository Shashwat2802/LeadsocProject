from django.db import models
from datetime import datetime
# Create your models here.

class Customer(models.Model):
    cName = models.CharField(max_length=50,null=True)
    cEmail = models.EmailField(null=True)
    cUrl = models.CharField(max_length=50,null=True)
    
    class Meta:     
        db_table = "customer"

    def __str__(self):
        return str(self.cName)
    

class Employee(models.Model):
    eFname = models.CharField(max_length=50,null=True)
    eLname = models.CharField(max_length=50,null=True)
    refer_Customer = models.ForeignKey(Customer, on_delete = models.CASCADE,db_column='cName',null=True)
    eEmail = models.EmailField(max_length=200,null=True)
    ePhone = models.CharField(max_length=50,null=True)
    eExperience = models.IntegerField(default=0,null=True)
    eskills = models.CharField(max_length=100,null=True)
    eRole = models.CharField(max_length=50,null=True) # designation
    eMP_Type = models.CharField(max_length=30,null=True) # either sales,software engineer, account
    estatus = models.CharField(max_length=100,null=True) # either free or deployed
    leadsoc_joining_date = models.DateField(null=True)
    customer_start_date = models.DateField(null=True)
    remarks = models.CharField(max_length=30,null=True) # about employee

    class Meta:
        db_table = "employee"

    def __str__(self):
        return str(self.eFname)
         
        

class Customer_Requirements(models.Model):
    Requirement_Id = models.IntegerField(primary_key=True, unique=True)
    customers = models.ForeignKey(Customer, on_delete = models.CASCADE,db_column='cName',blank=True)
    Customer_Requirement_id = models.IntegerField(default=0)
    Required_skills = models.TextField()
    Job_Description = models.TextField()
    Required_Experience = models.IntegerField(default=0)
    Open_positions = models.IntegerField(default=0)
    remain_positions = models.IntegerField(default=0)
    Position_Status = models.CharField(max_length=10) # active or closed        
    Sales_Incharge = models.CharField(max_length=50) # name of the person
    #Candidate_List = models.CharField(max_length=100,null=True) # need candidate list
    Bu_head = models.CharField(max_length=50,null=True)

    class Meta:
        db_table = "customer_requirements"

    def __str__(self):
        return self.customers
    
class CandidateList(models.Model):
    candidate_name = models.CharField(max_length=100,default="",editable=False,primary_key=True)
    interview_status = models.CharField(max_length=100,null=True)
    
    class Meta:
        db_table = "candidate_list"
    
    def __str__(self):
        return self.candidate_name

class addEmpToCustomer(models.Model):
    eFname = models.CharField(max_length=100,null=True)
    eLname = models.CharField(max_length=100, null=True)
    refer_Customer = models.ForeignKey(Customer, on_delete = models.CASCADE,db_column='cName',null=True)
    eskills = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = "addemptocustomer"

    def __str__(self):
        return str(self.eFname)

class Employee_Details(models.Model):
    pass

class UploadFile(models.Model):
    specifications = models.FileField(upload_to='router_specifications')
    
class Login(models.Model):
    UserName = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    
    class Meta:
        db_table = "login"



