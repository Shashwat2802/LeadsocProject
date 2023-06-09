from ctypes import wstring_at
from pkgutil import get_data
import queue
import quopri
from django.shortcuts import render,redirect
from emp_data.models import Customer,Employee,Customer_Requirements
from .resources import EmployeeResource
from emp_data.forms import CustomerForm,EmployeeForm,loginForm,UploadFileForm
from django.contrib import messages
from django.contrib.auth.models import auth
from emp_data.models import *
from tablib import Dataset
from .models import Customer
from django.template import loader
import xlwt
from django.http import HttpResponse
from django.db.models import Q


def loginCheck(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/emp")
        else:
            messages.info(request, 'invalid credentials')
            return redirect("/emp")



    else:
        form = loginForm()
        return render(request, "regsitration/login.html")



#Home page
def home(request):
    return render(request,"home.html")
'''
def admin_login(request):
    return render(request, 'admin_login.html')
'''
# To create Customer

def comp(request):
    if request.method == "POST":

        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Company Details saved successfully')
                return redirect("/show")
            except:
                pass
    else:
        form = CustomerForm()
    return render(request, "index.html", {'form':form})


# add company details
'''
def comp(request):
    if request.method == "POST":
        print("Hi Anil")
        cName = request.POST['cName']
        cEmail = request.POST['cEmail']
        cLogo = request.POST['cLogo']
        cUrl = request.POST['cUrl']
        ins=Customer(cName=cName,cEmail=cEmail,cLogo=cLogo,cUrl=cUrl)
        ins.save()

        print(cName)
    return render(request, 'index.html')
'''

def emp(request):
    if request.method == "POST":
        
        eFname = request.POST['eFname']
        eLname = request.POST['eLname']
        refer_Customer_no = request.POST['refer_Customer']
        eEmail = request.POST['eEmail']
        ePhone = int(request.POST['ePhone'])
        eExperience =request.POST['eExperience']
        eskills = request.POST['eskills']
        eRole = request.POST['eRole']
        eMP_Type = request.POST['eMP_Type']
        estatus = request.POST['estatus']
        leadsoc_joining_date = request.POST['leadsoc_joining_date']
        customer_start_date = request.POST['customer_start_date']
        remarks = request.POST['remarks']
        ins=Employee(eFname=eFname, eLname=eLname, refer_Customer_id=refer_Customer_no, eEmail=eEmail, ePhone=ePhone, 
                     eExperience=eExperience,eskills=eskills,eRole=eRole,eMP_Type=eMP_Type,estatus=estatus,
                     leadsoc_joining_date=leadsoc_joining_date,customer_start_date=customer_start_date,remarks=remarks)
        ins.save()
        return redirect('/showemp')
        
    return render(request, 'addemp.html')

def add_cust_requirements(request):
    if request.method == "POST":
        
        Requirement_Id = request.POST['Requirement_Id']
        customers = request.POST['customers']
        Customer_Requirement_id = request.POST['Customer_Requirement_id']
        Required_skills = request.POST['Required_skills']
        Job_Description = request.POST['Job_Description']
        Required_Experience =request.POST['Required_Experience']
        Open_positions = request.POST['Open_positions']
        remain_positions = request.POST['remain_positions'] 
        Position_Status = request.POST['Position_Status']        
        Sales_Incharge = request.POST['Sales_Incharge']
        bu_head = request.POST['bu_head']        
        cust_require_data=Customer_Requirements(Requirement_Id=Requirement_Id,customers_id=customers,Customer_Requirement_id=Customer_Requirement_id, 
                                                Required_skills=Required_skills, Job_Description=Job_Description, Required_Experience=Required_Experience,
                                                   Open_positions =Open_positions, remain_positions=remain_positions, Position_Status=Position_Status,
                                                    Sales_Incharge=Sales_Incharge, bu_head=bu_head)
        cust_require_data.save()
        return redirect('/show_cust_requirements.html')
    else:
        return render(request, 'addcustrequirements.html')

# To retrieve Customer details
def show(request):
    companies = Customer.objects.all()
    return render(request, "show.html", {'companies':companies})

# To Edit Customer details
def edit(request, cName):
    customer = Customer.objects.get(cName=cName)
    return render(request, "edit.html", {'customer':customer})

# To Update Customer
def update(request, cName):
    customer = Customer.objects.get(cName=cName)
    form = CustomerForm(request.POST, instance= customer)
    if form.is_valid():
         form.save()
         return redirect("/show")
    return render(request, "edit.html", {'customer': customer})

# To Delete Customer details
def delete(request, cName):
    
    customer = Customer.objects.get(cName=cName)
    customer.delete()       

    return redirect("/show")

# show customer_requirements details
def show_cust_requirements(request):
    customer_requirements = Customer_Requirements.objects.all()
    return render(request, "show_cust_requirements.html", {'customer_requirements':customer_requirements})

def job_description(request):
    job_desc = Customer_Requirements.objects.values('Job_Description')
    #print(job_desc)
    return render(request,"job_description.html",{'job_desc':job_desc})

# adding candidate details in customer_requirement page
def add_candidate(request):
    if request.method == 'POST':
        candidate_name = request.POST['candidate_name']
        interview_status = request.POST['interview_status']
        candidate_data  = CandidateList(candidate_name=candidate_name,interview_status=interview_status)
        candidate_data.save()        
        return redirect("/show_candidate.html")
    else:
        return render(request,"add_candidates.html")
'''
def show_candidate(request):
    candidate = CandidateList.objects.all()
    return render(request,"show_candidate.html",{'candidate':candidate})'''
'''
def show_candidate(request):
    candidate = Employee.objects.filter(estatus ='Free').values()
    return render(request,"show_candidate.html",{'candidate':candidate})'''
# search and show the data
def show_candidate(request):
    form = Employee.objects.filter(estatus ='Free').values()
    #form = Employee.objects.all()
    
    if request.method == "GET":   
        free = Employee.objects.filter(estatus ='Free').values()              
        skills = request.GET.get('searchskill')        
        #f = Employee.objects.values_list('eskills')
        if skills == free:  
        #if skills != f:
            form = Employee.objects.filter(eskills__icontains= skills).filter(estatus__icontains= free)
            #above eskills form column name with double underscore icontain inbuilt attribute
    return render(request,'show_candidate.html',{'form':form})

def checkbox(request):
    if request.method == 'POST':
        empName=request.POST.getlist("check")
        print(empName)

    return redirect("/show_candidate")


from .forms import addEmpToCustomerForm

def addempcustomer(request):
    if request.method == 'POST':
        form = addEmpToCustomerForm(request.POST or None)

        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = addEmpToCustomerForm()

    context = {'form': form}
    return render(request, 'show_candidate.html', context)

def savedvalues(request):
    if request.method == 'POST':
        if request.POST.getlist('eFname'):  
            print("sunil")
            savedata = addEmpToCustomer()
            savedata.eFname=request.POST.getlist('eFname')
            savedata.save()
            print(savedata)
            #return render(request,'show_candidate.html')
    else:
        return render(request,'show_candidate.html')

        
  
  
  
# To create employee
'''
def emp(request):
    if request.method == "POST":
        
        form = EmployeeForm(request.POST)
        if form.is_valid():
            
            try:
                form.save()
                return redirect("/showemp.html")
            except:
                pass
    else:
        
        form = EmployeeForm()
        print("sunil")
    return render(request, "addemp.html", {'form':form})
'''

# To show employee details
def showemp(request):
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})

# To delete employee details
def deleteEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")

# To edit employee details
def editemp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    return render(request, "editemployee.html", {'employee':employee})

# To update employee details
def updateEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    form = EmployeeForm(request.POST, instance= employee)
    
    if form.is_valid():
        
        form.save()
        return redirect("/showemp")
    return render(request, "editemployee.html", {'employee': employee})


# this is working upload employee data to model
def simple_upload(request):
    
    if request.method == "POST":
        
        #Employee_Resource = EmployeeResource()
        dataset = Dataset()
        new_employee = request.FILES['myfile']

        if not new_employee.name.endswith('xlsx'):
            messages.info(request,'Wrong format of file')
            return render(request,'upload.html')
        
        imported_data = dataset.load(new_employee.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = Employee(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13]
                )
            value.save()
        return redirect("/showemp")
        
    return render(request,'upload.html')

# upload customer data to model
def customer_data_upload(request):
    
    if request.method == "POST":
        
        #Employee_Resource = EmployeeResource()
        dataset = Dataset()
        new_customer = request.FILES['myfile']

        if not new_customer.name.endswith('xlsx'):
            messages.info(request,'Wrong format of file')
            return render(request,'upload.html')
        
        imported_data = dataset.load(new_customer.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = Customer(
                data[0],
                data[1],
                data[2], 
                data[3]                            
                )
            value.save()
        return redirect("/show")
    
    return render(request,'upload.html')

# upload customer requirement data the model
def customer_requirement_file(request):
    
    if request.method == "POST":
        
        #Employee_Resource = EmployeeResource()
        dataset = Dataset()
        new_Requirements = request.FILES['file']

        if not new_Requirements.name.endswith('xlsx'):
            messages.info(request,'Wrong format of file')
            return render(request,'customer_requirement_data.html')
        
        imported_data = dataset.load(new_Requirements.read(), format='xlsx')
        for data in imported_data:
            print(data[1])
            value = Customer_Requirements(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11]
                )
            value.save()
        return redirect("/show_cust_requirements")
        
    return render(request,'customer_requirement_data.html')



# download employee excel file
'''
def download_excel_data(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')

	#decide file name
	response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')

	#adding sheet
	ws = wb.add_sheet("sheet1")

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names, you can use your own headers here
	columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4','Column 5','Column 6',
            'Column 7','Column 8','Column 9','Column 10','Column 11','Column 12','Column 13' ]

	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	#get your data, from database or from a text file...
	data = get_data() #dummy method to fetch data.
	for my_row in data:                           
	    row_num = row_num + 1
	    ws.write(row_num, 0, my_row.eFame, font_style)
        ws.write(row_num, 1, my_row.eLname, font_style)
	    ws.write(row_num, 2, my_row.refer_Customer, font_style)
	    ws.write(row_num, 4, my_row.eEmail, font_style)
        ws.write(row_num, 5, my_row.ePhone, font_style)
        ws.write(row_num, 6, my_row.eExperience, font_style)
        ws.write(row_num, 7, my_row.eskills, font_style)
        ws.write(row_num, 8, my_row.eMP_Type, font_style)
        ws.write(row_num, 9, my_row.estatus, font_style)
        ws.write(row_num, 10, my_row.leadsoc_joining_date, font_style)
        ws.write(row_num, 11, my_row.customer_start_date, font_style)
        ws.write(row_num, 12, my_row.remarks, font_style)
        

	wb.save(response)
	return response
'''
#Reset and login views

from urllib.parse import urlparse, urlunparse

from django.conf import settings

# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

UserModel = get_user_model()


class RedirectURLMixin:
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url_allowed_hosts = set()

    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name, self.request.GET.get(self.redirect_field_name)
        )
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ""

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        raise ImproperlyConfigured("No URL to redirect to. Provide a next_page.")


class LoginView(RedirectURLMixin, FormView):
    """
    Display the login form and handle the login action.
    """

    form_class = AuthenticationForm
    authentication_form = None
    template_name = "registration/login.html"
    redirect_authenticated_user = False
    extra_context = None

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return resolve_url(settings.LOGIN_REDIRECT_URL)

    def get_form_class(self):
        return self.authentication_form or self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update(
            {
                self.redirect_field_name: self.get_redirect_url(),
                "site": current_site,
                "site_name": current_site.name,
                **(self.extra_context or {}),
            }
        )
        return context


class LogoutView(RedirectURLMixin, TemplateView):
    """
    Log out the user and display the 'You are logged out' message.
    """

    http_method_names = ["post", "options"]
    template_name = "registration/logged_out.html"
    extra_context = None

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        auth_logout(request)
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            # Redirect to target page once the session has been cleared.
            return HttpResponseRedirect(redirect_to)
        return super().get(request, *args, **kwargs)

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        elif settings.LOGOUT_REDIRECT_URL:
            return resolve_url(settings.LOGOUT_REDIRECT_URL)
        else:
            return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update(
            {
                "site": current_site,
                "site_name": current_site.name,
                "title": _("Logged out"),
                "subtitle": None,
                **(self.extra_context or {}),
            }
        )
        return context


def logout_then_login(request, login_url=None):
    """
    Log out the user if they are logged in. Then redirect to the login page.
    """
    login_url = resolve_url(login_url or settings.LOGIN_URL)
    return LogoutView.as_view(next_page=login_url)(request)


def redirect_to_login(next, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Redirect the user to the login page, passing the given 'next' page.
    """
    resolved_url = resolve_url(login_url or settings.LOGIN_URL)

    login_url_parts = list(urlparse(resolved_url))
    if redirect_field_name:
        querystring = QueryDict(login_url_parts[4], mutable=True)
        querystring[redirect_field_name] = next
        login_url_parts[4] = querystring.urlencode(safe="/")

    return HttpResponseRedirect(urlunparse(login_url_parts))


# Class-based password reset views
# - PasswordResetView sends the mail
# - PasswordResetDoneView shows a success message for the above
# - PasswordResetConfirmView checks the link the user clicked and
#   prompts for a new password
# - PasswordResetCompleteView shows a success message for the above


class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {"title": self.title, "subtitle": None, **(self.extra_context or {})}
        )
        return context


class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name = "registration/password_reset_email.html"
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = reverse_lazy("password_reset_done")
    template_name = "registration/password_reset_form.html"
    title = _("Password reset")
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)


INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"


class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = "/password_reset_done.html"
    title = _("Password reset sent")


class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = "set-password"
    success_url = reverse_lazy("password_reset_complete")
    template_name = "password_reset/password_reset_confirm.html"
    title = _("Enter new password")
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        if "uidb64" not in kwargs or "token" not in kwargs:
            raise ImproperlyConfigured(
                "The URL path must contain 'uidb64' and 'token' parameters."
            )

        self.validlink = False
        self.user = self.get_user(kwargs["uidb64"])

        if self.user is not None:
            token = kwargs["token"]
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(
                        token, self.reset_url_token
                    )
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            UserModel.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context["validlink"] = True
        else:
            context.update(
                {
                    "form": None,
                    "title": _("Password reset unsuccessful"),
                    "validlink": False,
                }
            )
        return context


class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_reset_complete.html"
    title = _("Password reset complete")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = resolve_url(settings.LOGIN_URL)
        return context


class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    #success_url = reverse_lazy("password_change_done")
    #template_name = "registration/password_change_form.html"
    #template_name = "password_reset/password_change.html"
    title = _("Password change")

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    #template_name = "password_reset/password_change_done.html"
    template_name = "home.html"
    title = _("Password Change Successful")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)












