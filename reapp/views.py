from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from .decorator import *
from .forms import *
from .models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
# from django.forms import formset_factory
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import logging
from django.forms import modelformset_factory

# Create your views here.


logger = logging.getLogger(__name__)
# logger.warning("Your log message is here")


def safe_run(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            return HttpResponse('System Not Supported')
    return func_wrapper


@safe_run
def home(request):
    # request.session.clear()
    return render(request, 'home.html', {})


@is_authenticated
@safe_run
def admin_dashboard(request):
    employee = Employee.objects.get(id=request.session['pk'])
    # print(asdas)
    if employee.user_role == 'staff':
        request.session.clear()
        return redirect('login')
    return render(request, 'admin_dashboard.html', {'employee': employee})


@is_authenticated
@safe_run
def staff_dashboard(request):
    employee = Employee.objects.get(id=request.session['pk'])
    if not employee.user_role == 'staff':
        request.session.clear()
        return redirect('login')
    return render(request, 'staff_dashboard.html', {'employee': employee})


@is_authenticated
@safe_run
def employee_create(request):
    form = EmployeeForm()
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        password = request.POST['password']
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if not Employee.objects.filter(user_name=user_name).exists():
                if request.POST['password'] != '' and request.POST['confirm_password'] != '':
                    if request.POST['password'] == request.POST['confirm_password']:
                        post.password = make_password(request.POST['password'])
                        post.save()
                        subject = first_name.capitalize() + ' ' + "Your account created with us"
                        message = 'Please find your account details below with credentials:\nFull Name : {}.\nUser Name : {}.\nEmail : {}\nPassword : {}. \n\n\nplease login with your credentials to update your profile!'.format(
                            first_name.capitalize() + ' ' + middle_name.capitalize() + ' ' + last_name.capitalize(), str(user_name), str(email).lower(), str(password))
                        from_email = settings.EMAIL_HOST_USER
                        send_mail(subject, message, from_email, [
                            email], fail_silently=False,)
                        # return redirect('list')
                        return redirect(reverse('employee_edit', kwargs={'pk': int(post.pk)}))
                    else:
                        messages.error(request, "passwords doesn't match")
                else:
                    post.save()
                    # return redirect('list')
                    return redirect(reverse('employee_edit', kwargs={'pk': int(post.pk)}))
            else:
                messages.error(request, "Credentials for this user exists")
    ab = Employee.objects.all()
    deps = Department.objects.all()
    return render(request, 'Employee/create.html', {'form': form, 'department': deps})


# def load_location(request):
#     country_id = request.GET.get('country')
#     state_id = request.GET.get('state')
#     states = State.objects.filter(country_id=country_id).order_by('name')
#     cities = City.objects.filter(state_id=state_id).order_by('name')
#     return render(request, 'Employee/locations.html', {'states': states,
#                                                         'cities': cities})


@is_authenticated
@safe_run
def search(request):
    users = ''
    if request.method == "POST":
        users = Employee.objects.filter(user_name__icontains=request.POST['user_name'],
                                        emp_id__icontains=request.POST['emp_id'],
                                        department__dep_name__icontains=request.POST['department'])
    else:
        users = Employee.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(users, 5)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
    return render(request, 'Employee/list.html', {'users': users})


@is_authenticated
@safe_run
def employee_list(request):
    lists = Employee.objects.filter(
        department__id=request.session['department'])
    return render(request, 'Employee/staff_list.html', {'list': lists})


@is_authenticated
@safe_run
def employee_edit(request, pk):
    obj = Employee.objects.get(pk=pk)
    form = EmployeeEditForm(instance=obj)
    if request.method == 'POST':
        form = EmployeeEditForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list')
    skill = Skills.objects.all()
    language = Languages.objects.all()
    jobtitle = Jobtitle.objects.all()
    jobcategory = Jobcategory.objects.all()
    department = Department.objects.all()
    education = Education.objects.all()
    membership = Membership.objects.all()
    country = Country.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    return render(request, 'Employee/edit_page.html', {
        'form': form, 'values': obj,
        'skill': skill, 'jobtitle': jobtitle,
        'jobcategory': jobcategory, 'department': department,
        'education': education, 'membership': membership,
        'country': country, 'states': states,
        'cities': cities, 'language': language
    }
    )


@is_authenticated
@safe_run
def staff_edit(request, pk):
    staff_edit = Employee.objects.get(pk=pk)
    form = StaffEditForm(instance=staff_edit)
    if request.method == 'POST':
        form = StaffEditForm(request.POST, instance=staff_edit)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse('employee_view', kwargs={'pk': int(post.pk)}))
    langua = Languages.objects.all()
    skil = Skills.objects.all()
    return render(request, 'Employee/staff_edit_page.html', {'form': form,
                                                             'values': staff_edit,
                                                             'language': langua,
                                                             'skill': skil})


@is_authenticated
@safe_run
def employee_view(request, pk):
    try:
        book = get_object_or_404(Employee, pk=pk)
        form = EmployeeDetailForm(request.FILES, instance=book)
        if request.method == 'POST':
            form = EmployeeDetailForm(
                request.POST, request.FILES, instance=book)
            if form.is_valid():
                post = form.save(commit=False)
                post.photograph = request.FILES['file']
                post.save()
    except Exception:
        messages.error(request, 'Please select a single file atleast')
    # employee = Employee.objects.get(id=request.session['pk'])
    return render(request, 'Employee/detailview.html', {'object': book})


@is_authenticated
@safe_run
def employee_delete(request, pk):
    del_obj = Employee.objects.get(pk=pk)
    del_obj.status = False
    del_obj.save()
    return redirect('list')


@is_authenticated
@safe_run
def currency(request):
    morf = AssignedCurrencyForm(request.POST)
    if morf.is_valid():
        morf.save()
    if request.method == 'POST':
        money = request.POST.getlist('currencylist')
        for price in money:
            money_obj = AssignedCurrency.objects.get(id=price)
            money_obj.delete()
    curren = AssignedCurrency.objects.all()
    return render(request, 'Pay_grade/currency.html', {'morf': morf, 'curren': curren})


@is_authenticated
@safe_run
def currency_list(request):
    curren = AssignedCurrency.objects.all()
    return render(request, 'Pay_grade/currency_list.html', {'curren': curren})


@is_authenticated
@safe_run
def currency_edit(request, pk):
    cur = get_object_or_404(AssignedCurrency, pk=pk)
    if request.method == 'POST':
        morf = AssignedCurrencyForm(request.POST, instance=cur)
        if morf.is_valid():
            morf.save()
            return redirect('currency_list')
    else:
        morf = AssignedCurrencyForm(instance=cur)
    return render(request, 'Pay_grade/currency.html', {'morf': morf})


@is_authenticated
@safe_run
def currency_delete(request, pk):
    cur_obj = AssignedCurrency.objects.get(pk=pk)
    cur_obj.delete()
    return redirect('currency_list')


@is_authenticated
@safe_run
def job_add(request):
    form = JobtitleForm()
    if request.method == 'POST':
        form = JobtitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    return render(request, 'Job_title/jobadd.html', {'form': form})


@is_authenticated
@safe_run
def job_list(request):
    jobl = Jobtitle.objects.all()
    return render(request, 'Job_title/joblist.html', {'jobl': jobl})


@is_authenticated
@safe_run
def job_edit(request, pk):
    book = get_object_or_404(Jobtitle, pk=pk)
    if request.method == 'POST':
        form = JobtitleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobtitleForm(instance=book)
    return render(request, 'Job_title/jobadd.html', {'form': form})


@is_authenticated
@safe_run
def job_delete(request, pk):
    form = Jobtitle.objects.get(id=pk)
    form.delete()
    return redirect('job_list')


@is_authenticated
@safe_run
def department_add(request):
    form = DepartmenttitleForm()
    if request.method == 'POST':
        form = DepartmenttitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    return render(request, 'Department/departmentcreate.html', {'form': form})


@is_authenticated
@safe_run
def department_list(request):
    departmentl = Department.objects.all()
    return render(request, 'Department/departmentlist.html', {'departmentl': departmentl})


@is_authenticated
@safe_run
def department_edit(request, pk):
    book = get_object_or_404(departmenttitle, pk=pk)
    if request.method == 'POST':
        form = departmenttitleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = departmenttitleForm(instance=book)
    return render(request, 'Department/departmentcreate.html', {'form': form})


@is_authenticated
@safe_run
def department_delete(request, pk):
    form = Department.objects.get(id=pk)
    form.delete()
    return redirect('department_list')


@is_authenticated
@safe_run
def jobcategory_add(request):
    if request.method == 'POST':
        loki = JobcategoryForm(request.POST)
        if loki.is_valid():
            if request.POST.get('name') != '':
                loki.save()
            return redirect('jobcategory_list')
    else:
        loki = JobcategoryForm()
    raka = Jobcategory.objects.all()
    return render(request, 'Job_category/jobcategory_add.html', {'loki': loki, 'raka': raka})


@is_authenticated
@safe_run
def jobcategory_list(request):
    raka = Jobcategory.objects.all()
    return render(request, 'Job_category/jobcategory_list.html', {'raka': raka})


@is_authenticated
@safe_run
def jobcategory_edit(request, pk):
    book = get_object_or_404(Jobcategory, pk=pk)
    loki = JobcategoryForm(request.POST, instance=book)
    if loki.is_valid():
        loki.save()
        return redirect('jobcategory_add')
    return render(request, 'Job_category/jobcategory_list.html', {'loki': loki})


@is_authenticated
@safe_run
def jobcategory_delete(request, pk):
    loki = Jobcategory.objects.get(pk=pk)
    loki.delete()
    return redirect('jobcategory_add')


@is_authenticated
@safe_run
def genInfo_add_or_create(request):
    book = GenInformation.objects.first()
    form = GenInformationForm(request.GET or None, instance=book)
    if request.method == "POST":
        form = GenInformationForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('genInfo_add_or_create')
    return render(request, 'General_information/create.html', {'form': form})


@is_authenticated
@safe_run
def location_add(request):
    form = LocationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('location_list')
    return render(request, 'Location/locationscreate.html', {'form': form})


# def location_list(request):
#     tata=Locations.objects.all()
#     return render(request, 'locationsedit.html', {'tata': tata})


@is_authenticated
@safe_run
def location_search(request):
    if request.method == 'POST':
        locate = Locations.objects.filter(
            name__icontains=request.POST['name'],
            city__icontains=request.POST['city'],
            country__icontains=request.POST['country'],
        )
    else:
        locate = Locations.objects.all()
        return render(request, 'Location/locationsedit.html', {'tata': locate})


@is_authenticated
@safe_run
def location_edit(request, pk):
    book = get_object_or_404(Locations, pk=pk)
    form = LocationForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect('location_add')
    return render(request, 'Location/locationscreate.html', {'form': form})


@is_authenticated
@safe_run
def location_delete(request, pk):
    form = Locations.objects.get(pk=pk)
    form.delete()
    return redirect('location_list')


@is_authenticated
@safe_run
def skills_create(request):
    form = SkillsForm(request.GET)
    if request.method == 'POST':
        sname = request.POST.get('name')
        if not Skills.objects.filter(name=sname).exists():
            form = SkillsForm(request.POST)
            if form.is_valid():
                skls = form.save(commit=False)
                skls.name.title()
                skls.save()
                return redirect('skills_list')
        else:
            messages.error(
                request, 'the entered skill already exists in the database')
    return render(request, 'Skills/Qualificas_skills.html', {'form': form})


@is_authenticated
@safe_run
def skills_list(request):
    ac = Skills.objects.all()
    if request.method == "POST":
        employee_ids = request.POST.getlist('workstatus')
        for empid in employee_ids:
            emp_object = Skills.objects.get(id=empid)
            emp_object.delete()
    return render(request, 'Skills/Qualificas_skills_list.html', {'ac': ac})


@is_authenticated
@safe_run
def skills_update(request, pk):
    ab = get_object_or_404(Skills, pk=pk)
    form = SkillsForm(request.POST, instance=ab)
    if form.is_valid():
        form.save()
        return redirect('skills_list')
    return render(request, 'Skills/Qualificas_skills.html', {'form': form})


@is_authenticated
@safe_run
def skills_delete(request, pk):
    ad = Skills.objects.get(pk=pk)
    ad.delete()
    return redirect('skills_list')


@is_authenticated
@safe_run
def education_create(request):
    form = EducationForm()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            if request.POST.get('Level') != '':
                form.save()
            return redirect('education_list')
    ao = Education.objects.all()
    return render(request, 'Education/education_create.html', {'form': form, 'ao': ao})


@is_authenticated
@safe_run
def education_list(request):
    az = Education.objects.all()
    return render(request, 'Education/education_list.html', {'az': az})


@is_authenticated
@safe_run
def education_edit(request, pk):
    ab = get_object_or_404(Education, pk=pk)
    form = EducationForm(request.POST, instance=ab)
    if form.is_valid():
        form.save()
        return redirect('Education')
    return render(request, 'Education/education_create.html', {'form': form})


@is_authenticated
@safe_run
def education_delete(request, pk):
    ad = Education.objects.get(pk=pk)
    ad.delete()
    return redirect('education_list')


@is_authenticated
@safe_run
def license_create(request):
    form = LicenseForm()
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('license_list')
    raka = License.objects.all()
    return render(request, 'License/license_add.html', {'form': form, 'raka': raka})


@is_authenticated
@safe_run
def license_list(request):
    raka = License.objects.all()
    return render(request, 'License/license_list.html', {'raka': raka})


@is_authenticated
@safe_run
def license_edit(request, pk):
    greel = get_object_or_404(License, pk=pk)
    form = LicenseForm(request.POST, instance=greel)
    if form.is_valid():
        form.save()
        return redirect('license_list')
    return render(request, 'License/license_list.html', {'form': form})


@is_authenticated
@safe_run
def language_add(request):
    kal = LanguagesForm()
    if request.method == 'POST':
        lname = request.POST.get('name')
        if not Languages.objects.filter(name=lname).exists():
            kal = LanguagesForm(request.POST)
            if kal.is_valid():
                kals = kal.save(commit=False)
                kals.name.title()
                kals.save()
                return redirect('language_list')
        else:
            messages.error(request, 'language already exists in the data')
    return render(request, 'Language/language_add.html', {'kal': kal})


@is_authenticated
@safe_run
def language_list(request):
    lang = Languages.objects.all()
    if request.method == 'POST':
        ba = request.POST.getlist('langlist')
        for b in ba:
            bas = Languages.objects.get(id=b)
            bas.delete()
    return render(request, 'Language/language_list.html', {'lang': lang})


@is_authenticated
@safe_run
def language_edit(request, pk):
    bash = get_object_or_404(Languages, pk=pk)
    kal = LanguagesForm(request.POST, instance=bash)
    if kal.is_valid():
        kal.save()
        return redirect('language_list')
    return render(request, 'Language/language_add.html', {'kal': kal})


@is_authenticated
@safe_run
def membership_add(request):
    form = MembershipForm(request.POST)
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership_list')
    return render(request, 'Membership/membership_add.html', {'form': form})


@is_authenticated
@safe_run
def membership_list(request):
    ac = Membership.objects.all()
    if request.method == 'POST':
        hik = request.POST.getlist('memberlist')
        for h in hik:
            hiks = Membership.objects.get(id=h)
            hiks.delete()
    return render(request, 'Membership/membership_list.html', {'ac': ac})


@is_authenticated
@safe_run
def membership_edit(request, pk):
    ab = get_object_or_404(Membership, pk=pk)
    form = MembershipForm(request.POST, instance=ab)
    if form.is_valid():
        form.save()
        return redirect('membership_list')
    return render(request, 'Membership/membership_add.html', {'form': form})


@is_authenticated
@safe_run
def reporting_add(request):
    form = ReportingMethodForm()
    if request.method == 'POST':
        form = ReportingMethodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reporting_list')
    reports = ReportingMethod.objects.all()
    return render(request, 'Reporting_methods/reportingCreate.html', {'form': form, 'repo': reports})


@is_authenticated
@safe_run
def reporting_list(request):
    reports = ReportingMethod.objects.all()
    if request.method == 'POST':
        repo1 = request.POST.getlist('repo_list')
        for repo23 in repo1:
            repo2 = ReportingMethod.objects.get(id=repo23)
            repo2.delete()
    return render(request, 'Reporting_methods/reportingList.html', {'repo': reports})


@is_authenticated
@safe_run
def reporting_edit(request, pk):
    repoed = get_object_or_404(ReportingMethod, pk=pk)
    form = ReportingMethodForm(request.POST, instance=repoed)
    if form.is_valid():
        form.save()
        return redirect('reporting_list')
    return render(request, 'Reporting_methods/reportingCreate.html', {'form': form})


@is_authenticated
@safe_run
def reporting_delete(request, pk):
    repo_obj = ReportingMethod.objects.get(pk=pk)
    repo_obj.delete()
    return redirect('reporting_list')


@is_authenticated
@safe_run
def leaveentitlement_add(request):
    form = LeaveEntitlementForm()
    if request.method == 'POST':
        employee = request.POST['employee']
        year = request.POST['year']
        form = LeaveEntitlementForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if not LeaveEntitlement.objects.filter(employee=employee, year=year).exists():
                post.save()
                return redirect('leave_list')
            else:
                messages.error(
                    request, 'Leaves for given User already Entitled')
    lists = LeaveEntitlement.objects.all()
    leavetype = LeaveType.objects.all()
    emp = Employee.objects.all()
    return render(request, 'Leave_entitlement/leaveentitlement_add.html', {'form': form,
                                                                           'list': lists,
                                                                           'leave': leavetype,
                                                                           'employee': emp})


@is_authenticated
@safe_run
def leave_list(request):
    lists = LeaveEntitlement.objects.all()
    return render(request, 'Leave_entitlement/leave_list.html', {'list': lists})


@is_authenticated
@safe_run
def leave_edit(request, pk):
    leave_edit = get_object_or_404(LeaveEntitlement, pk=pk)
    if form.is_valid():
        form = LeaveEntitlementForm(request.POST, instance=leave_edit)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveEntitlementForm()
    return render(request, 'Leave_entitlement/leaveentitlement_add.html', {'form': form})


@is_authenticated
@safe_run
def leave_delete(request, pk):
    leave_obj = LeaveEntitlement.objects.get(pk=pk)
    leave_obj.delete()
    return redirect('leave_list')


@is_authenticated
@safe_run
def leaveTypeCreate(request):
    form = LeaveTypeForm()
    if request.method == 'POST':
        form = LeaveTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leaveTypeList')
    return render(request, 'Leave_type/leaveTypeCreate.html', {'form': form})


@is_authenticated
@safe_run
def leaveTypeList(request):
    leavelist = LeaveType.objects.all()
    return render(request, 'Leave_type/leaveTypeList.html', {'leavelist': leavelist})


@is_authenticated
@safe_run
def leaveTypeEdit(request, pk):
    leaveEdit = get_object_or_404(LeaveType, pk=pk)
    form = LeaveTypeForm(request.POST, instance=leaveEdit)
    if form.is_valid():
        form.save()
        return redirect('leaveTypeList')
    else:
        form = LeaveTypeForm(instance=leaveEdit)
    return render(request, 'Leave_type/leaveTypeCreate.html', {'form': form})


@is_authenticated
@safe_run
def leaveTypeDelete(request, pk):
    leave_obj = LeaveType.objects.get(pk=pk)
    leave_obj.delete()
    return redirect('leaveTypeList')


@is_authenticated
@safe_run
def holidayCreate(request):
    form = HolidayForm()
    if request.POST == 'POST':
        form = HolidayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('holiday_list')
    h123 = Holiday.objects.all()
    return render(request, 'Holiday/holidayCreate.html', {'form': form, 'h1': h123})


@is_authenticated
@safe_run
def staff_holiday_list(request):
    # if request.method == 'POST':
    #     scanner = Holiday.objects.filter(
    #         date__icontains=request.POST['from_date'])
    # else:
    scanner = Holiday.objects.all()
    return render(request, 'Holiday/holidaylist2.html', {'list12': scanner})


@is_authenticated
@safe_run
def holidayEdit(request, pk):
    hlidedit = get_object_or_404(Holiday, pk=pk)
    if request.POST == 'POST':
        form = HolidayForm(request.POST, instance=hlidedit)
        if form.is_valid():
            form.save()
            return redirect('holiday_list')
    form = HolidayForm(instance=hlidedit)
    return render(request, 'Holiday/holidayCreate.html', {'form': form})


@is_authenticated
@safe_run
def holidayDelete(requestpk):
    holidlt = Holiday.objects.get(pk=pk)
    holidlt.delete()
    return redirect('holiday_list')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        try:
            user = Employee.objects.get(user_name=user_name)
        except:
            user = False
            messages.error(request, 'Invalid User Name')
            return redirect('login')
        match = check_password(password, user.password)
        if match:
            request.session['pk'] = user.pk
            request.session['user_name'] = user.user_name
            if user.user_role == 'staff':
                request.session['department'] = user.department.id
                return redirect('staff')
            else:
                return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid Password')
            return redirect('login')
    return render(request, 'login.html', {})


@is_authenticated
@safe_run
def logout(request):
    try:
        del request.session['pk']
    except:
        pass
    return redirect('/')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = Employee.objects.get(email=email)
        except:
            user = False
        if user:
            request.session['user_name'] = user.user_name
            otp = randint(1000, 99999)
            print(otp)
            request.session['otp'] = otp
            request.session.set_expiry(120)
            subject = 'OTP Requested for forgotten password'
            message = "We received a for got password request from your account.\nMake sure not to share your OTP with anyone.\n OTP :{}.\n\n\nplease verify your account if it's not you".format(
                str(otp))
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email,
                      [email], fail_silently=False)
            return redirect('otp')
        else:
            messages.error(request, 'Enter valid Registered Email or ')
            messages.error(request, 'Your profile data is Incomlete ')
            return redirect('forgot_password')
    return render(request, 'forgot_password.html', {})


def otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if int(request.session['otp']) == int(otp):
            return redirect('reset_password')
        else:
            messages.error(request, 'Your otp expired or')
            messages.error(request, 'invalid OTP, try again')
            return redirect('otp')
    return render(request, 'otp.html', {})


def reset_password(request):
    rocks12 = Employee.objects.get(user_name=request.session['user_name'])
    if request.method == 'POST':
        email = rocks12.email
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            rocks12.password = make_password(password)
            rocks12.save()
            subject = request.session['user_name'].capitalize(
            ) + "Your Password reset"
            message = 'Please find your account details below with credentials after password reset \nEmail :{}\nUser Name :{}\nPassword :{}'.format(
                email.lower(), request.session['user_name'], str(password))
            from_email = settings.EMAIL_HOST_USER
            send_mail(
                subject,
                message,
                from_email,
                [email],
                fail_silently=False,
            )
            return redirect('login')
        else:
            messages.error(request, 'password mis match')
            return redirect('reset_password')
    return render(request, 'reset_password.html', {})


@is_authenticated
@safe_run
def leaveform_create(request):
    form = LeaveApplyForm()
    if request.method == 'POST':
        emp = Employee.objects.get(id=request.session['pk'])
        x = request.POST['leave_from']
        y = request.POST['leave_to']
        a = datetime.strptime(str(x), "%Y-%m-%d")
        b = datetime.strptime(str(y), "%Y-%m-%d")
        z = abs((a-b).days)+1
        form = LeaveApplyForm(request.POST)
        if form.is_valid():
            loki = form.save(commit=False)
            loki.monthly_leaves = z
            loki.employee = emp
            loki.email = emp.email
            loki.emp_id = emp.emp_id
            loki.department = emp.department
            loki.mobile = emp.mobile
            loki.save()
            return redirect('leaveform_list')
    return render(request, 'Leave_form_apply/leaveform_create.html', {'form': form, })


@is_authenticated
@safe_run
def leaveform_list(request):
    lst = LeaveApply.objects.filter(employee__id=request.session['pk'])
    return render(request, 'Leave_form_apply/leaveform_list.html', {'list': lst})


@is_authenticated
@safe_run
def leaveadmin_list(request):
    lst = LeaveApply.objects.all()
    if request.method == "GET" and request.is_ajax():
        lv = LeaveApply.objects.get(id=request.GET.get('pk'))
        lv.status = request.GET.get('apprs')
        lv.save()
        return HttpResponse('success')
    return render(request, 'Leave_form_apply/leaveadmin_list.html', {'list': lst})


@is_authenticated
@safe_run
def leaveform_edit(request, pk):
    obj = LeaveApply.objects.get(pk=pk)
    if obj.status == "Approved":
        pass
    else:
        form = LeaveForm(instance=obj)
        if request.method == 'POST':
            form = LeaveApplyForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('leaveform_list')
    return render(request, 'Leave_form_apply/leaveform_edit.html', {'form': form, 'values': obj})


@is_authenticated
@safe_run
def leaveform_delete(request, pk):
    del_obj = LeaveApply.objects.get(pk=pk)
    if del_obj.department.head_dep:
        del_obj.delete()
    return redirect('leaveform_list')


# companyDocumentsForm views :
# ...........................................

@is_authenticated
@safe_run
def companyDocuments_create(request):
    form = companyDocumentsForm()
    if request.method == 'POST':
        form = companyDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('companyDocuments_list')
    ac = CompanyDocument.objects.all()
    return render(request, 'company_docx/comdocx.html', {'form': form, 'ac': ac})


@is_authenticated
@safe_run
def companyDocuments_list(request):
    az = CompanyDocument.objects.all()
    return render(request, 'company_docx/comdocs_list.html', {'az': az})


@is_authenticated
@safe_run
def companyDocuments_edit(request, pk):
    ab = get_object_or_404(CompanyDocument, pk=pk)
    if request.method == 'POST':
        form = companyDocumentsForm(request.POST, request.FILES, instance=ab)
        if form.is_valid():
            form.save()
            return redirect('companyDocuments_list')
    form = companyDocumentsForm(instance=ab)
    return render(request, 'company_docx/comdocx.html', {'form': form})


@is_authenticated
@safe_run
def companyDocuments_delete(request, pk):
    ad = CompanyDocument.objects.get(pk=pk)
    ad.delete()
    return redirect('companyDocuments_list')

# personal documents :


@is_authenticated
@safe_run
def personalDocuments_create(request):
    form = PersonalDocumentForm()
    if request.method == 'POST':
        form = PersonalDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('personalDocuments_list')
    ac = CompanyDocument.objects.all()
    return render(request, 'personal_docx/personal_create.html', {'form': form, 'ac': ac})


@is_authenticated
@safe_run
def personalDocuments_list(request):
    az = PersonalDocument.objects.all()
    return render(request, 'personal_docx/personal_list.html', {'az': az})


@is_authenticated
@safe_run
def personalDocuments_edit(request, pk):
    ab = get_object_or_404(PersonalDocument, pk=pk)
    if request.method == 'POST':
        form = PersonalDocumentForm(request.POST, request.FILES, instance=ab)
        if form.is_valid():
            form.save()
            return redirect('personalDocuments_list')
    form = PersonalDocumentForm(instance=ab)
    return render(request, 'personal_docx/personal_create.html', {'form': form})


@is_authenticated
@safe_run
def personalDocuments_delete(request, pk):
    ad = PersonalDocument.objects.get(pk=pk)
    ad.delete()
    return redirect('personalDocuments_list')

 ############################ ANNOUNCEMENT VIEW ######################


@is_authenticated
@safe_run
def announcement_create(request):
    form = AnnouncementForm(request.GET)
    emp = Employee.objects.all().values('email')
    res = [sub['email'] for sub in emp]
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('announcement_title')
            message = form.cleaned_data.get('message')
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, res, fail_silently=False,)
            return redirect('announcement_create')
    lst = Announcement.objects.all()
    return render(request, 'Announcement/announcement-create.html', {'form': form, 'list': lst})


@is_authenticated
# @safe_run
def review_crate(request):
    form = PerformanceReviewForm()
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    if request.method == 'GET' and request.is_ajax():
        empl = Employee.objects.get(id=request.GET.get('emp_id'))
        emp_dep = empl.department.head_dep
        empl.save()
        return HttpResponse(emp_dep)
    emp = Employee.objects.all()
    return render(request, 'Performance_review/review_create.html', {'form': form, 'employee': emp})


@is_authenticated
# @safe_run
def review_list(request):
    review_list = PerformanceReview.objects.all()
    return render(request, 'Performance_review/review_list.html', {'list': review_list})


@is_authenticated
# @safe_run
def staff_review_list(request):
    staf = PerformanceReview.objects.get(employee__id=request.session['pk'])
    return render(request, 'Performance_review/staff_review_list.html', {'list': staf})


@is_authenticated
@safe_run
def review_edit(request, pk):
    review_edit = get_object_or_404(PerformanceReview, pk=pk)
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST, instance=review_edit)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = PerformanceReviewForm(instance=review_edit)
    return render(request, 'Performance_review/review_create.html', {'form': form})


@is_authenticated
@safe_run
def review_delete(request):
    review_del = PerformanceReview.objects.all()
    return redirect('review_list')


@is_authenticated
@safe_run
def asset_create(request):
    form = AssetForm()
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    deps = Department.objects.all()
    return render(request, 'Asset/asset_create.html', {'form': form, 'department': deps})


@is_authenticated
@safe_run
def asset_list(request):
    asset_list = Asset.objects.all()
    return render(request, 'Asset/asset_list.html', {'list': asset_list})


@is_authenticated
@safe_run
def asset_edit(request, pk):
    asset_edit = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset_edit)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset_edit)
    return render(request, 'Asset/review_create.html', {'form': form})


@is_authenticated
@safe_run
def asset_delete(request):
    asset_del = Asset.objects.all()
    asset_del.delete()
    asset_del.save()
    return redirect('asset_list')


@is_authenticated
@safe_run
def attendance_create(request):
    import datetime
    form = AttendanceForm()
    if request.method == 'POST':
        emp = Employee.objects.get(id=request.session['pk'])
        loc = request.POST['location']
        if loc != '':
            if request.POST.get('in_time') == 'on':

                if Attendance.objects.filter(employee__id=emp.id, in_time__date=datetime.datetime.today()):
                    x = Attendance.objects.filter(
                        employee__id=emp.id, in_time__date=datetime.datetime.today())
                    x.in_time = datetime.datetime.now()
                    x.location = loc
                    x.save()
                else:
                    Attendance.objects.create(
                        employee=emp, in_time=datetime.datetime.now(), location=loc)
            elif request.POST.get('out_time') == 'on':
                if Attendance.objects.filter(employee__id=emp.id, out_time__date=datetime.datetime.today()):
                    x = Attendance.objects.filter(
                        employee__id=emp.id, out_time__date=datetime.datetime.today())
                    x.out_time = datetime.datetime.now()
                    x.note = x.out_time.hour-x.in_time.hour
                    x.save()
                else:
                    x = Attendance.objects.filter(
                        employee=emp, in_time__date=datetime.datetime.today()).first()
                    x.out_time = datetime.datetime.now()
                    x.note = x.out_time.hour-x.in_time.hour
                    x.save()
        else:
            return redirect('attendance_create')
    emp = Employee.objects.all()
    return render(request, 'Attendance/attendance_create.html', {'form': form, 'employee': emp})


@is_authenticated
@safe_run
def attendance_list(request):
    attendance_list = Attendance.objects.all()
    return render(request, 'Attendance/attendance_list.html', {'list': attendance_list})


@is_authenticated
@safe_run
def attendance_edit(request, pk):
    attendance_edit = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance_edit)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance_edit)
    return render(request, 'Attendance/attendance_create.html', {'form': form})


@is_authenticated
@safe_run
def attendance_delete(request):
    attendance_del = Attendance.objects.all()
    attendance_del.delete()
    attendance_del.save()
    return redirect('attendance_list')


@is_authenticated
@safe_run
def project_create(request):
    form = ProjectForm()
    if request.method == 'POST':
        if request.POST.get('name'):
            Client.objects.create(name=request.POST.get(
                'name'), description=request.POST.get('description'))
            return redirect('project_create')
        elif request.POST.get('client_name'):
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
    emp_dep = Employee.objects.all()
    client = Client.objects.all()
    return render(request, 'Project/project_create.html', {'form': form, 'employee': emp_dep, 'client': client})


@is_authenticated
@safe_run
def project_list(request):
    project_list = Project.objects.all()
    return render(request, 'Project/project_list.html', {'list': project_list})


@is_authenticated
@safe_run
def project_edit(request, pk):
    project_edit = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project_edit)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project_edit)
    return render(request, 'Project/project_create.html', {'form': form})


@is_authenticated
@safe_run
def project_delete(request):
    project_delete = Project.objects.all()
    project_delete.delete()
    project_delete.save()
    return redirect('project_list')


# client view:
@is_authenticated
@safe_run
def Client_create(request):
    if request.method == 'POST':
        form = clientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Client_list')
    else:
        form = clientForm()
    return render(request, 'Client/Client_create.html', {'form': form})


@is_authenticated
@safe_run
def Client_list(request):
    ac = Client.objects.all()
    return render(request, 'Client/Client_list.html', {'ac': ac})


@is_authenticated
@safe_run
def Client_update(request, pk):
    ab = get_object_or_404(Client, pk=pk)
    form = clientForm(request.POST, instance=ab)
    if form.is_valid():
        form.save()
        return redirect('Client_list')
    return render(request, 'Client/Client_create.html', {'form': form})


@is_authenticated
@safe_run
def Client_delete(request, pk):
    ad = Client.objects.get(pk=pk)
    ad.delete()
    return redirect('Client_list')


@is_authenticated
@safe_run
def reports_all(request):
    return render(request, 'Reports/reports_all.html', {})


@is_authenticated
@safe_run
def employee_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Employee_list Report.csv"'
    employees = Employee.objects.all()
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Employee Id',
                     'User Name', 'Date of birth', 'gender'])
    for employee in employees:
        writer.writerow([employee.first_name, employee.emp_id,
                         employee.user_name, employee.dob, employee.gender])
    return response


@is_authenticated
@safe_run
def leave_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Employee_leave_list Report.csv"'
    leaves = LeaveApply.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Employee Name', 'Employee Id', 'Designation',
                     'Department', 'Leave From', 'Leave To', 'Leave Reason', 'Status'])
    for leave in leaves:
        writer.writerow([leave.employee, leave.emp_id,
                         leave.designation, leave.department, leave.leave_from,
                         leave.leave_to, leave.leave_reason, leave.status])
    return response


@is_authenticated
@safe_run
def perform_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Employee_Performance Report.csv"'
    performance = PerformanceReview.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Employee Name', 'Department Head',
                     'Review Date', 'Description'])
    for perform in performance:
        writer.writerow([perform.employee, perform.co_ordinator,
                         perform.review_date, perform.description])
    return response


@is_authenticated
@safe_run
def attendance_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Employee_Attendance Report.csv"'
    attendance = Attendance.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Employee Name', 'In Time',
                     'Out Time', 'Note', 'Location'])
    for attend in attendance:
        writer.writerow([attend.employee, attend.in_time,
                         attend.out_time, attend.note, attend.location])
    return response


@is_authenticated
@safe_run
def assets_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Assets Report.csv"'
    assets = Asset.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Asset Name', 'Department', 'Description'])
    for asset in assets:
        writer.writerow(
            [asset.asset_name, asset.asset_department, asset.asset_description])
    return response


@is_authenticated
@safe_run
def leave_assign_create(request):
    form = LeaveAssignForm()
    if request.method == 'POST':
        p = request.POST['leave_from']
        q = request.POST['leave_to']
        l = datetime.strptime(str(p), "%Y-%m-%d")
        m = datetime.strptime(str(q), "%Y-%m-%d")
        s = abs((l-m).days)
        form = LeaveAssignForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.remarks = s
            post.leave_balance = LeaveEntitlement.objects.filter(
                entitlement_days__id=request.POST['pk'])
            post.save()
            return redirect('leave_assign_list')
    return render(request, 'Leave_assign/leave_assign_create.html', {'form': form})


@is_authenticated
@safe_run
def leave_assign_list(request):
    assign_list = LeaveApply.objects.all()
    return render(request, 'Leave_assign/leave_assign_list.html', {'list': assign_list})


@is_authenticated
@safe_run
def leave_assign_edit(request, pk):
    assign_edit = get_object_or_404(LeaveApply, pk=pk)
    form = LeaveAssignForm(instance=assign_edit)
    if request.method == 'POST':
        form = LeaveAssignForm(instance=assign_edit)
        if form.is_valid():
            form.save()
            return redirect('leave_assign_list')
    return render(request, 'Leave_assign/leave_assign_create.html', {'form': form})


@is_authenticated
@safe_run
def leave_assign_delete(request, pk):
    assign_del = LeaveApply.objects.all()
    assign_del.delete()
    assign_del.save()
    return redirect('leave_assign_list')


@is_authenticated
@safe_run
def candidate_create(request):
    if request.method == 'POST':
        form = RecruitmentCandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = RecruitmentCandidateForm()
    vaca = Vacancy.objects.all()
    emp = Employee.objects.all()
    return render(request, 'Candidate/candidate_create.html', {'form': form, 'vacancy': vaca, 'employee': emp})


@is_authenticated
@safe_run
def candidate_list(request):
    candidate_list = RecruitmentCandidate.objects.all()
    return render(request, 'Candidate/candidate_list.html', {'candidate': candidate_list})


@is_authenticated
@safe_run
def candidate_update(request, pk):
    form = RecruitmentCandidateForm()
    edit = get_object_or_404(RecruitmentCandidate, pk=pk)
    if request.method == 'POST':
        form = RecruitmentCandidateForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    return render(request, 'Candidate/candidate_create.html', {'form': form})


@is_authenticated
@safe_run
def candidate_delete(request, pk):
    candi_del = RecruitmentCandidate.objects.get(pk=pk)
    candi_del.delete()
    return redirect('candidate_list')


@is_authenticated
@safe_run
def vacancy_create(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm()
    job = Jobtitle.objects.all()
    emp = Employee.objects.all()
    return render(request, 'Vacancy/vacancy_create.html', {'form': form, 'jobtitle': job, 'employee': emp})


@is_authenticated
@safe_run
def vacancy_list(request):
    vacancy_list = Vacancy.objects.all()
    return render(request, 'Vacancy/vacancy_list.html', {'list': vacancy_list})


@is_authenticated
@safe_run
def vacancy_update(request, pk):
    vacancy_edit = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy_edit)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm(instance=vacancy_edit)
    return render(request, 'Vacancy/vacancy_create.html', {'form': form})


@is_authenticated
@safe_run
def vacancy_delete(request, pk):
    vaca_del = Vacancy.objects.get(pk=pk)
    vaca_del.delete()
    return redirect('vacancy_list')


@is_authenticated
@safe_run
def pay_roll(request):
    emp = Employee.objects.values('user_name', 'amount')
    leave = LeaveApply.objects.values('monthly_leaves')
    entitle = LeaveEntitlement.objects.values('entitlement_days')
    mylist = zip(emp, leave, entitle)
    context = {'mylist': mylist}
    return render(request, 'Payroles/pay-list.html', context)


@is_authenticated
@safe_run
def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events": all_events,
    }
    return render(request, 'Calender/calender.html', context)


@is_authenticated
@safe_run
def calender_add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    event = Events.objects.all()
    datas = {}
    datas['events'] = serializers.serialize("json", event)
    print(datas)
    return JsonResponse(datas)


@is_authenticated
@safe_run
def calender_update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()

    event = Events.objects.all()
    datas = {}
    datas['events'] = serializers.serialize("json", event)
    print(datas)
    return JsonResponse(datas)


@is_authenticated
@safe_run
def calender_remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

    # ProjectModule views or functions


@is_authenticated
# @safe_run
def project_module_create(request):
    form = ProjectModuleForm()
    if request.method == 'POST':
        form = ProjectModuleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if post.task_status == 'Closed':
                post.status = False
                post.save()
            else:
                post.save()
            return redirect('Pro_module_list')
    return render(request, 'Project/project_module_create.html', {'form': form})


@is_authenticated
# @safe_run
def project_module_list(request):
    module_list = ProjectModule.objects.all()
    return render(request, 'Project/project_module_list.html', {'list': module_list})


@is_authenticated
# @safe_run
def project_module_update(request, pk):
    project_module_edit = get_object_or_404(ProjectModule, pk=pk)
    if request.method == 'POST':
        form = ProjectModuleForm(request.POST, instance=project_module_edit)
        if form.is_valid():
            form.save()
            return redirect('Pro_module_list')
    else:
        form = ProjectModuleForm(instance=project_module_edit)
    return render(request, 'Project/project_module_create.html', {'form': form})


@is_authenticated
# @safe_run
def project_module_delete(request, pk):
    del_obj = ProjectModule.objects.get(pk=pk)
    del_obj.delete()
    return redirect('Pro_module_list')


###  project_sub_module_create views por functions:#########################

@is_authenticated
# @safe_run
def project_sub_module_create(request):
    form = ProjectSubModuleForm()
    if request.method == 'POST':
        form = ProjectSubModuleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if post.task_status == 'Closed':
                post.status == False
                post.save()
            else:
                post.save()
            return redirect('project_sub_module_list')
    return render(request, 'Project/project_sub_module_create.html', {'form': form})


@is_authenticated
# @safe_run
def project_sub_module_list(request):
    project_sub_module_list = ProjectSubModule.objects.all()
    return render(request, 'Project/project_sub_module_list.html', {'list': project_sub_module_list})


@is_authenticated
# @safe_run
def project_sub_module_update(request, pk):
    project_sub_module_edit = get_object_or_404(ProjectSubModule, pk=pk)
    if request.method == 'POST':
        form = ProjectSubModuleForm(
            request.POST, instance=project_sub_module_edit)
        if form.is_valid():
            form.save()
            return redirect('project_sub_module_list')
    else:
        form = ProjectSubModuleForm(instance=project_sub_module_edit)
    return render(request, 'Project/project_sub_module_create.html', {'form': form})


@is_authenticated
# @safe_run
def project_sub_module_delete(request, pk):
    del_obj = ProjectSubModule.objects.get(pk=pk)
    del_obj.delete()
    return redirect('project_sub_module_list')

########################## ProjectTasks views or functions :  ############################


@is_authenticated
# @safe_run
def Project_tasks_create(request):
    imageFormSet = modelformset_factory(ProjectImage,
                                        form=ProjectImageForm, extra=3)
    if request.method == 'POST':
        task_form = ProjectTasksForm(request.POST)
        image_form = imageFormSet(
            request.POST, request.FILES, queryset=ProjectImage.objects.none())
        try:
            if task_form.is_valid() and image_form.is_valid():
                post = task_form.save(commit=False)
                post.save()

                for form in image_form.cleaned_data:
                    images = form['images']
                    photos = ProjectImage(project_task=post, images=images)
                    photos.save()
                return redirect('Project_tasks_list')
        except:
            if task_form.is_valid():
                post = task_form.save(commit=False)
                post.save()
                return redirect('Project_tasks_list')
    else:
        task_form = ProjectTasksForm()
        image_form = imageFormSet(queryset=ProjectImage.objects.none())
    projects = Project.objects.all()
    module = ProjectModule.objects.all()
    sub_module = ProjectSubModule.objects.all()
    deps = Department.objects.all()
    emps = Employee.objects.all()
    return render(request, 'Project/Project_tasks_create.html', {'task_form': task_form, 'image_form': image_form, 'projects': projects,
                                                                 'module': module, 'submodule': sub_module,
                                                                 'department': deps, 'employee': emps})


@is_authenticated
# @safe_run
def Project_tasks_list(request):
    project_tasks_list = ProjectTasks.objects.all()
    photos = ProjectImage.objects.all()
    mylist = zip(photos, project_tasks_list)
    return render(request, 'Project/Project_tasks_list.html', {'list': mylist})


@is_authenticated
# @safe_run
def Project_tasks_update(request, pk):
    project_sub_module_edit = get_object_or_404(ProjectTasks, pk=pk)
    if request.method == 'POST':
        form = ProjectTasksForm(
            request.POST, request.FILES, instance=project_sub_module_edit)
        if form.is_valid():
            form.save()
            return redirect('Project_tasks_list')
    else:
        form = ProjectTasksForm(
            request.FILES, instance=project_sub_module_edit)
    return render(request, 'Project/Project_tasks_create.html', {'form': form})


@is_authenticated
# @safe_run
def Project_tasks_delete(request, pk):
    del_obj = ProjectTasks.objects.get(pk=pk)
    del_obj.delete()
    return redirect('Project_tasks_list')


#################### AssignedUser VIEW OR FUNCTIONS : ####################################

@is_authenticated
# @safe_run
def assin_user(request):
    form = AssignedUserForm()
    if request.method == 'POST':
        form = AssignedUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asssined_user_list')
    return render(request, 'Project/assin_user.html', {'form': form})


@is_authenticated
# @safe_run
def asssined_user_list(request):
    asssined_user_list = AssignedUser.objects.all()
    return render(request, 'Project/asssined_user_list.html', {'list': asssined_user_list})


@is_authenticated
# @safe_run
def asssined_user_update(request, pk):
    asssined_user_edit = get_object_or_404(AssignedUser, pk=pk)
    if request.method == 'POST':
        form = AssignedUserForm(request.POST, instance=asssined_user_edit)
        if form.is_valid():
            form.save()
            return redirect('asssined_user_list')
    else:
        form = AssignedUserForm(instance=asssined_user_edit)
    return render(request, 'Project/assin_user.html', {'form': form})


@is_authenticated
# @safe_run
def asssined_user_delete(request, pk):
    del_obj = AssignedUser.objects.get(pk=pk)
    del_obj.delete()
    return redirect('asssined_user_list')

######## DialyStatusupdates VIEW OR FUNCTION : ###########################


@is_authenticated
# @safe_run
def DialyStatusUpdates_Create(request):
    form = DialyStatusupdatesForm()
    if request.method == 'POST':
        form = DialyStatusupdatesForm(request.POST)
        if form.is_valid():
            form.save()
    project = Project.objects.all()
    daily_status = DialyStatusupdates.objects.all()
    return render(request, 'Project/DialyStatusUpdates_Create.html', {'form': form, 'project': project,
                                                                                        'daily_status': daily_status})


@is_authenticated
# @safe_run
def DialyStatusUpdates_list(request):
    Dialy_Status_updates_list = DialyStatusupdates.objects.all()
    return render(request, 'Project/DialyStatusUpdates_list.html', {'list': Dialy_Status_updates_list})


@is_authenticated
# @safe_run
def DialyStatusUpdates_update(request, pk):
    asssined_user_edit = get_object_or_404(DialyStatusupdates, pk=pk)
    form = DialyStatusupdatesForm(instance=asssined_user_edit)
    if request.method == 'POST':
        form = DialyStatusupdatesForm(
            request.POST, instance=asssined_user_edit)
        if form.is_valid():
            form.save()
            return redirect('DialyStatusUpdates_list')
    return render(request, 'Project/DialyStatusUpdates_Create.html', {'form': form})


@is_authenticated
# @safe_run
def DialyStatusUpdates_delete(request, pk):
    del_obj = DialyStatusupdates.objects.get(pk=pk)
    del_obj.delete()
    return redirect('DialyStatusUpdates_list')
