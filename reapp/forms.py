from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user_role', 'first_name', 'middle_name', 'last_name', 'emp_id', 'department',
                  'photograph', 'user_name', 'email', 'password', 'confirm_password', 'status']


class LeaveEntitlementForm(forms.ModelForm):
    class Meta:
        model = LeaveEntitlement
        fields = ['employee', 'year', 'entitlement_days']


class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user_role', 'sub_unit',
                   'user_name', 'password', 'confirm_password']


class EmployeeDetailForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['photograph']


class StaffEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['emp_id', 'user_role', 'dob',
                   'user_name', 'password', 'confirm_password', 'status',
                   'relation_name', 'relation_type', 'relation_mobile', 'department', 'joined_date', 'pay_grade',
                   'pay_frequency', 'amount', 'comment_qualify', 'comment_skill', 'joined_date', 'pay_grade']


class AssignedCurrencyForm(forms.ModelForm):
    class Meta:
        model = AssignedCurrency
        fields = '__all__'


class DepartmenttitleForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class JobtitleForm(forms.ModelForm):
    class Meta:
        model = Jobtitle
        fields = '__all__'


class JobcategoryForm(forms.ModelForm):
    class Meta:
        model = Jobcategory
        fields = '__all__'


class GenInformationForm(forms.ModelForm):
    class Meta:
        model = GenInformation
        fields = '__all__'


class LocationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = '__all__'


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = '__all__'


class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = '__all__'


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'


class LeaveTypeForm(forms.ModelForm):
    class Meta:
        model = LeaveType
        fields = '__all__'


class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = '__all__'


# class AddUserForm(forms.ModelForm):
#     class Meta:
#         model = AddUser
#         fields = '__all__'


class LeaveApplyForm(forms.ModelForm):
    class Meta:
        model = LeaveApply
        fields = ['leave_from', 'leave_to', 'leave_reason',
                  'address_during_leave_period', ]


class companyDocumentsForm(forms.ModelForm):
    class Meta:
        model = CompanyDocument
        fields = '__all__'


class PersonalDocumentForm(forms.ModelForm):
    class Meta:
        model = PersonalDocument
        fields = '__all__'


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'


class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = '__all__'


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('in_time', 'out_time', )


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class clientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'


class RecruitmentCandidateForm(forms.ModelForm):
    class Meta:
        model = RecruitmentCandidate
        fields = '__all__'


class LeaveAssignForm(forms.ModelForm):
    class Meta:
        model = LeaveApply
        fields = '__all__'
        exclude = ['email', 'emp_id', 'designation', 'department', 'monthly_leaves',
                   'leave_reason', 'mobile', 'address_during_leave_period', 'status', '']


class ProjectModuleForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = '__all__'


class ProjectSubModuleForm(forms.ModelForm):
    class Meta:
        model = ProjectSubModule
        fields = '__all__'


class ProjectTasksForm(forms.ModelForm):
    class Meta:
        model = ProjectTasks
        fields = '__all__'        


class AssignedUserForm(forms.ModelForm):
    class Meta:
        model = AssignedUser
        fields = '__all__'     


class DialyStatusupdatesForm(forms.ModelForm):
    class Meta:
        model = DialyStatusupdates
        fields = '__all__'     
        
    
class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['images',]
        