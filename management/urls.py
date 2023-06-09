"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emp_data import views
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings 
from django.conf.urls.static import static 
from emp_data.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings

# django admin customization
admin.site.site_header = "LeadSoc Admin "
admin.site.site_title = "Welcome to Admin Dashboard"
admin.site.index_title = "Welcome to LeadSoc Technologies PVT LTD."


    
urlpatterns = [        
    path('admin/', admin.site.urls),
    path("simple_upload",views.simple_upload),
    path("customer_data_upload",views.customer_data_upload),
    
    #path('admin_login/',admin.site.urls),
    #path('admin_login',views.admin_login),
    # user signup path
    #path('signup',views.signup),
    path("home",views.home),
   # customer requirements details
    path("show_cust_requirements", views.show_cust_requirements),
    path('add_cust_requirements',views.add_cust_requirements),
    path('job_description',views.job_description), 
    path('add_candidate',views.add_candidate),
    path('show_candidate',views.show_candidate),
    path('savedvalues',views.savedvalues),
    #path('candidate_search',views.candidate_search),
     #Customer paths 
    path('comp', views.comp),
    path('show', views.show),
    path('edit/<str:cName>', views.edit),
    path('update/<str:cName>', views.update),
    path('delete/<str:cName>', views.delete), 

    #employee paths
    path('emp', views.emp),
    path('showemp', views.showemp),
    path('deleteEmp/<str:eFname>', views.deleteEmp),
    path('editemp/<str:eFname>', views.editemp), 
    path('updateEmp/<str:eFname>', views.updateEmp),
    

    #Homepage path
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('PasswordChangeDoneView', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('PasswordChangeView', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_resetPasswordResetCompleteView', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('PasswordResetConfirmView/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm.html'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),

    #inbuilt login path
    path('accounts/', include('django.contrib.auth.urls')),
    
]
#for Media Storage 
if settings.DEBUG: 
        urlpatterns += static(settings.STATIC_URL,
                               document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 