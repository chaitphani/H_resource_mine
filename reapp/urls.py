from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('staff_dashboard', views.staff_dashboard, name='staff'),

    # Employee urls
    path('create', views.employee_create, name='create'),
    # path('ajax/load_location/', views.load_location, name='ajax_load_location'),
    path('list', views.search, name='list'),
    path('staff_list', views.employee_list, name='staff_list'),
    path('edit/<int:pk>', views.employee_edit, name='employee_edit'),
    path('staff_edit/<int:pk>', views.staff_edit, name='staff_edit'),
    path('employee_view/<int:pk>', views.employee_view, name='employee_view'),
    path('delete/<int:pk>', views.employee_delete, name='employee_delete'),

    # department
    path('department_add', views.department_add, name='department_add'),
    path('department_list', views.department_list, name='department_list'),
    path('department_edit/<int:pk>', views.department_edit, name='department_edit'),
    path('department_delete/<int:pk>',
         views.department_delete, name='department_delete'),

    # Currency urls
    path('currency', views.currency, name='currency'),
    path('currency_list', views.currency_list, name='currency_list'),
    path('currency_edit/<int:pk>', views.currency_edit, name='currency_edit'),
    path('currency_delete/<int:pk>', views.currency_delete, name='currency_delete'),

    # Job_Title urls
    path('job_add', views.job_add, name='job_add'),
    path('job_list', views.job_list, name='job_list'),
    path('job_edit/<int:pk>', views.job_edit, name='job_edit'),
    path('job_delete/<int:pk>', views.job_delete, name='job_delete'),


    # Job_Category urls
    path('jobcategory_add', views.jobcategory_add, name='jobcategory_add'),
    path('jobcategory_list', views.jobcategory_list, name='jobcategory_list'),
    path('jobcategory_edit/<int:pk>',
         views.jobcategory_edit, name='jobcategory_edit'),
    path('jobcategory_delete/<int:pk>',
         views.jobcategory_delete, name='jobcategory_delete'),

    # General_Information urls
    path('genInfo_add_or_create', views.genInfo_add_or_create,
         name='genInfo_add_or_create'),

    # Location urls
    path('location_add', views.location_add, name='location_add'),
    path('list', views.location_search, name='location_search'),
    path('location_edit/<int:pk>', views.location_edit, name='location_edit'),
    path('location_delete/<int:pk>', views.location_delete, name='location_delete'),

    # Skills urls
    path('skills_create', views.skills_create, name='skills_create'),
    path('skills_list', views.skills_list, name='skills_list'),
    path('skills_update/<int:pk>', views.skills_update, name='skills_update'),
    path('skills_delete/<int:pk>', views.skills_delete, name='skills_delete'),

    # Education urls
    path('education_create', views.education_create, name='education_create'),
    path('education_list', views.education_list, name='education_list'),
    path('education_edit/<int:pk>', views.education_edit, name='education_edit'),
    path('education_delete/<int:pk>',
         views.education_delete, name='education_delete'),

    # License urls
    path('license_create', views.license_create, name='license_create'),
    path('license_list', views.license_list, name='license_list'),
    path('license_edit/<int:pk>', views.license_edit, name='license_edit'),

    # Language urls
    path('language_add', views.language_add, name='language_add'),
    path('language_list', views.language_list, name='language_list'),
    path('language_edit/<int:pk>', views.language_edit, name='language_edit'),

    # Membership urls
    path('membership_add', views.membership_add, name='membership_add'),
    path('membership_list', views.membership_list, name='membership_list'),
    path('membership_edit/<int:pk>', views.membership_edit, name='membership_edit'),


    # Reporting_Method urls
    path('reporting_add', views.reporting_add, name='reporting_add'),
    path('reporting_list', views.reporting_list, name='reporting_list'),
    path('reporting_edit/<int:pk>', views.reporting_edit, name='reporting_edit'),
    path('reporting_delete/<int:pk>',
         views.reporting_delete, name='reporting_delete'),



    # Leave_Type urls
    path('leaveTypeCreate', views.leaveTypeCreate, name='leaveTypeCreate'),
    path('leaveTypeList', views.leaveTypeList, name='leaveTypeList'),
    path('leaveTypeEdit/<int:pk>', views.leaveTypeEdit, name='leaveTypeEdit'),
    path('leaveTypeDelete/<int:pk>', views.leaveTypeDelete, name='leaveTypeDelete'),

    # Holiday urls
    path('holidayCreate', views.holidayCreate, name='holidayCreate'),
    path('holiday_list', views.staff_holiday_list, name='staff_holiday_list'),
    path('holidayEdit/<int:pk>', views.holidayEdit, name='holidayEdit'),
    path('holidayDelete/<int:pk>', views.holidayDelete, name='holidayDelete'),

    path('leaveentitlement_add', views.leaveentitlement_add, name='leaveentitlement_add'),
    path('leaveentitlement_list', views.leave_list, name='leave_list'),
    path('leaveentitlement_edit/<int:pk>', views.leave_edit, name='leave_edit'),
    path('leaveentitlement_delete/<int:pk>', views.leave_delete, name='leave_delete'),


    # LEAVE FORM urls
    path('leaveform_create', views.leaveform_create, name='leaveform_create'),
    path('leaveform_list', views.leaveform_list, name='leaveform_list'),
    path('leaveadmin_list', views.leaveadmin_list, name='leaveadmin_list'),
    path('leaveform_edit/<int:pk>', views.leaveform_edit, name='leaveform_edit'),
    path('leaveform_delete/<int:pk>',
         views.leaveform_delete, name='leaveform_delete'),

    path('companyDocuments_create', views.companyDocuments_create,
         name='companyDocuments_create'),
    path('companyDocuments_list', views.companyDocuments_list,
         name='companyDocuments_list'),
    path('companyDocuments_edit/<int:pk>',
         views.companyDocuments_edit, name='companyDocuments_edit'),
    path('companyDocuments_delete/<int:pk>',
         views.companyDocuments_delete, name='companyDocuments_delete'),

    path('personalDocuments_create', views.personalDocuments_create,
         name='personalDocuments_create'),
    path('personalDocuments_list', views.personalDocuments_list,
         name='personalDocuments_list'),
    path('personalDocuments_edit/<int:pk>',
         views.personalDocuments_edit, name='personalDocuments_edit'),
    path('personalDocuments_delete/<int:pk>',
         views.personalDocuments_delete, name='personalDocuments_delete'),

    # announcement urls
    path('Announcement', views.announcement_create,
         name='announcement_create'),

    # Review urls
    path('review_create', views.review_crate, name='review_create'),
    path('review_list', views.review_list, name='review_list'),
    path('review_edit/<int:pk>', views.review_edit, name='review_edit'),
    path('review_delete/<int:pk>', views.review_delete, name='review_delete'),
    path('staff_review_list', views.staff_review_list, name='staff_review_list'),

	

    path('asset_create', views.asset_create, name='asset_create'),
    path('asset_list', views.asset_list, name='asset_list'),
    path('asset_edit/<int:pk>', views.asset_edit, name='asset_edit'),
    path('asset_delete/<int:pk>', views.asset_delete, name='asset_delete'),

    path('attendance_create', views.attendance_create, name='attendance_create'),
    path('attendance_list', views.attendance_list, name='attendance_list'),
    path('attendance_edit/<int:pk>', views.attendance_edit, name='attendance_edit'),
    path('attendance_delete/<int:pk>',
         views.attendance_delete, name='attendance_delete'),

    path('project_create', views.project_create, name='project_create'),
    path('project_list', views.project_list, name='project_list'),
    path('project_edit/<int:pk>', views.project_edit, name='project_edit'),
    path('project_delete/<int:pk>', views.project_delete, name='project_delete'),

    path('Client_create', views.Client_create, name='Client_create'),
    path('Client_list', views.Client_list, name='Client_list'),
    path('Client_update/<int:pk>', views.Client_update, name='Client_update'),
    path('Client_delete/<int:pk>', views.Client_delete, name='Client_delete'),

    path('leave_assign_create', views.leave_assign_create, name='leave_assign_create'),
    path('leave_assign_list', views.leave_assign_list, name='leave_assign_list'),
    path('leave_assign_edit/<int:pk>', views.leave_assign_edit, name='leave_assign_edit'),
    path('leave_assign_delete/<int:pk>', views.leave_assign_delete, name='leave_assign_delete'),

    path('candidate_create', views.candidate_create, name='candidate_create'),
    path('candidate_list', views.candidate_list, name='candidate_list'),
    path('candidate_update/<int:pk>', views.candidate_update, name='candidate_update'),
    path('candidate_delete/<int:pk>', views.candidate_delete, name='candidate_delete'),

    path('vacancy_create', views.vacancy_create, name='vacancy_create'),
    path('vacancy_list', views.vacancy_list, name='vacancy_list'),
    path('vacancy_update/<int:pk>', views.vacancy_update, name='vacancy_update'),
    path('vacancy_delete/<int:pk>', views.vacancy_delete, name='vacancy_delete'),


    # admin Report urls here
    path('Reports', views.reports_all, name='reports'),
    path('employee', views.employee_report, name='emp_report'),
    path('leave', views.leave_report, name='leave_report'),
    path('performance', views.perform_report, name='perform_report'),
    path('attendance', views.attendance_report, name='attendance_report'),
    path('assets', views.assets_report, name='assets_report'),

    path('pay_roll', views.pay_roll, name='pay_roll'),

    path('calendar', views.calendar, name='calendar'),
    path('calender_add_event', views.calender_add_event, name='calender_add_event'),
    path('calender_update/<int:pk>', views.calender_update, name='calender_update'),
    path('calender_remove/<int:pk>', views.calender_remove, name='calender_remove'),

    path('Project_Module_add', views.project_module_create, name='Pro_module_create'),
    path('project_module_list', views.project_module_list, name='Pro_module_list'),
    path('project_module_add/<int:pk>', views.project_module_update, name='Pro_module_edit'),
    path('project_module_add/<int:pk>', views.project_module_delete, name='pro_module_del'),


    path('project_sub_module_create', views.project_sub_module_create, name='project_sub_module_create'),
    path('project_sub_module_list', views.project_sub_module_list, name='project_sub_module_list'),
    path('project_sub_module_update/<int:pk>', views.project_sub_module_update, name='project_sub_module_update'),
    path('project_Sub_module_add/<int:pk>', views.project_sub_module_delete, name='project_sub_module_delete'),


    path('Project_tasks_create', views.Project_tasks_create, name='Project_tasks_create'),
    path('Project_tasks_list', views.Project_tasks_list, name='Project_tasks_list'),
    path('Project_tasks_update/<int:pk>', views.Project_tasks_update, name='Project_tasks_update'),
    path('Project_tasks_delete/<int:pk>', views.Project_tasks_delete, name='Project_tasks_delete'),


    path('assin_user', views.assin_user, name='assin_user'),
    path('asssined_user_list', views.asssined_user_list, name='asssined_user_list'),
    path('asssined_user_update/<int:pk>', views.asssined_user_update, name='asssined_user_update'),
    path('asssined_user_delete/<int:pk>', views.asssined_user_delete, name='asssined_user_delete'),

    path('DialyStatusUpdates_Create', views.DialyStatusUpdates_Create, name='DialyStatusUpdates_Create'),
    path('DialyStatusUpdates_list', views.DialyStatusUpdates_list, name='DialyStatusUpdates_list'),
    path('DialyStatusUpdates_update/<int:pk>', views.DialyStatusUpdates_update, name='DialyStatusUpdates_update'),
    path('DialyStatusUpdates_delete/<int:pk>', views.DialyStatusUpdates_delete, name='DialyStatusUpdates_delete'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
