from django.db import models

# Create your models here.
gender_status = (
    ('Male', 'Male'),
    ('Fe Male', 'FeMale'),
)

marital_status = (
    ('Married', 'Married'),
    ('Un Married', 'Un Married'),
)

pay_frequency_status = (
    ('BiWeekly', 'BiWeekly'),
    ('Hourly', 'Hourly'),
    ('Monthly', 'Monthly'),
    ('Semi Monthly', 'Semi Monthly'),
    ('Weekely', 'Weekely'),
)

account_type_status = (
    ('Savings', 'Savings'),
    ('Checking', 'Checking'),
    ('Other', 'Other'),
)

fluency_choices = (
    ('Writing', 'Writing'),
    ('Speaking', 'Speaking'),
    ('Reading', 'Reading'),
)

competency_choices = (
    ('Poor', 'Poor'),
    ('Basic', 'Basic'),
    ('Good', 'Good'),
    ('Mother Tongue', 'Mother Tongue'),
)


class AssignedCurrency(models.Model):
    currency_name = models.CharField(max_length=120)
    minimum_salary = models.IntegerField(null=True, blank=True)
    maximum_salary = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.currency_name)


class Jobtitle(models.Model):
    job_title = models.CharField(max_length=200, null=True, blank=True)
    job_descriptions = models.CharField(max_length=255, null=True, blank=True)
    job_specification = models.FileField(
        upload_to="docx", null=True, blank=True)
    note = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.job_title)


class Jobcategory(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)


class GenInformation(models.Model):
    organisation_Name = models.CharField(max_length=120, null=True, blank=True)
    tax_id = models.CharField(max_length=120, null=True, blank=True)
    number_of_employees = models.IntegerField(null=True, blank=True)
    registration_number = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    address_street_1 = models.CharField(max_length=120, null=True, blank=True)
    address_street_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    state_Province = models.CharField(max_length=120, null=True, blank=True)
    zip_postal_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    note = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)


class Locations(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    fax = models.IntegerField(null=True, blank=True)
    notes = models.TextField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)


class Skills(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)


class Education(models.Model):
    Level = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.Level)


class License(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)



class Languages(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)


class Membership(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)


class LeaveType(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    is_entitlement_situational = models.BooleanField(
        default=False, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)


DAY_CHOICES = (
    ('Full day', 'FULL DAY'),
    ('Half day', 'HALF DAY'),
)

class Holiday(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    repeats_annually = models.BooleanField(default=False)
    full_day_half_day = models.CharField(
        max_length=120, choices=DAY_CHOICES, null=True, blank=True, default='--select--')
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)


class Department(models.Model):
    dep_name = models.CharField(max_length=120, null=True, blank=True)
    head_dep = models.ForeignKey(
        'Employee', on_delete=models.CASCADE, related_name='head_depart', null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.dep_name)


class Country(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

class State(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='emp_state', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

class City(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='emp_city', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

USER_CHOICES = (
    ('admin', 'ADMIN'),
    ('staff', 'staff'),
)

class Employee(models.Model):
    # personal Details
    first_name = models.CharField(max_length=120, null=True, blank=True)
    middle_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    emp_id = models.IntegerField(null=True, blank=True)
    user_role = models.CharField(
        max_length=100, choices=USER_CHOICES, default='--select--', null=True, blank=True)
    photograph = models.ImageField(upload_to='media', null=True, blank=True)
    gender = models.CharField(
        max_length=120, choices=gender_status, default='-select--', null=True, blank=True)
    marital_status = models.CharField(
        max_length=120, choices=marital_status, default='-select--', null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    user_name = models.CharField(
        max_length=120, unique=True, null=True, blank=True)
    password = models.CharField(max_length=120, null=True, blank=True)
    confirm_password = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    # Contact details
    address_streer1 = models.CharField(max_length=120, null=True, blank=True)
    address_streer2 = models.CharField(max_length=120, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    email = models.EmailField(
        max_length=120, null=True, blank=True, unique=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='city_emp', null=True, blank=True)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='state_emp', null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='country_emp', null=True, blank=True)
    # Emergency Contacts
    relation_name = models.CharField(max_length=120, null=True, blank=True)
    relation_type = models.CharField(max_length=120, null=True, blank=True)
    relation_mobile = models.IntegerField(null=True, blank=True)
    relation_email = models.EmailField(
        max_length=120, null=True, blank=True, unique=True)
    # Dependents details
    dependant_name = models.CharField(max_length=120, null=True, blank=True)
    dependent_relation = models.CharField(
        max_length=120, null=True, blank=True)
    dependent_dob = models.DateField(null=True, blank=True)
    # Job details
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='dep_emp', null=True, blank=True)
    job_title = models.ForeignKey(
        Jobtitle, on_delete=models.CASCADE, null=True, blank=True)
    job_category = models.ForeignKey(
        Jobcategory, on_delete=models.CASCADE, null=True, blank=True)
    joined_date = models.DateField(null=True, blank=True)
    releave_date = models.DateField(null=True, blank=True)
    location = models.ForeignKey(
        Locations, on_delete=models.CASCADE, null=True, blank=True)
    # Salary details
    pay_frequency = models.CharField(
        choices=pay_frequency_status, max_length=120, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    bank_name = models.CharField(max_length=120, null=True, blank=True)
    ifsc_code = models.IntegerField(null=True, blank=True)
    # on_button_click these must be shown
    account_number = models.IntegerField(null=True, blank=True)
    account_type = models.CharField(
        max_length=120, choices=account_type_status, null=True, blank=True)
    # Assigned Supervisor details
    supervisor_name = models.CharField(max_length=120, null=True, blank=True)
    # Assigned Subordinates details
    subordinate_name = models.CharField(max_length=120, null=True, blank=True)
    # Qualifications details
    # work Experience
    company = models.CharField(max_length=120, null=True, blank=True)
    jobtitle = models.CharField(max_length=120, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    # eductaion details
    level = models.ForeignKey(
        Education, on_delete=models.CASCADE, null=True, blank=True)
    institue = models.CharField(max_length=120, null=True, blank=True)
    specialization = models.CharField(max_length=120, null=True, blank=True)
    year = models.CharField(max_length=120, null=True, blank=True)
    GPA_Score = models.CharField(max_length=120, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    # skills details
    skill = models.ManyToManyField(Skills)
    years_of_experience = models.IntegerField(null=True, blank=True)
    language = models.ManyToManyField(Languages)
    fluency = models.CharField(
        max_length=120, choices=fluency_choices, null=True, blank=True)
    competency = models.CharField(
        max_length=120, choices=competency_choices, null=True, blank=True)
    # license details
    license_type = models.ForeignKey(
        Membership, on_delete=models.CASCADE, null=True, blank=True)
    license_number = models.IntegerField(null=True, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.user_name)


import datetime
YEAR_CHOICES = []
for r in range(2018, (datetime.datetime.now().year+10)):
    YEAR_CHOICES.append((r,r))

class LeaveEntitlement(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    year = models.IntegerField(('year'),choices=YEAR_CHOICES,default=datetime.datetime.now().year,null=True, blank=True)
    entitlement_days = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)   

    def __str__(self):
        return str(self.employee)


STATUS_CHOICES = (
    ('approved', 'Approved'),
    ('not_approved', 'Not Approved'),
    ('approved_with_conditions', 'Approved With Conditions'),
)


class LeaveApply(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(
        max_length=120, null=True, blank=True, unique=True)
    emp_id = models.IntegerField(null=True, blank=True)
    designation = models.CharField(max_length=120, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='depe_emp', null=True, blank=True)
    monthly_leaves = models.IntegerField(null=True, blank=True)
    leave_from = models.DateField(null=True, blank=True)
    leave_to = models.DateField(null=True, blank=True)
    leave_reason = models.CharField(
        max_length=120, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    address_during_leave_period = models.CharField(
        max_length=300, null=True, blank=True)
    leave_balance = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="Not Approved", null=True, blank=True)
    remarks = models.CharField(max_length=250, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.employee)
        

class CompanyDocument(models.Model):
    document_name = models.CharField(max_length=120, null=True, blank=True)
    company_document = models.FileField(
        upload_to='documents/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.document_name)


class PersonalDocument(models.Model):
    document_name = models.CharField(max_length=120, null=True, blank=True)
    personal_document = models.FileField(upload_to='documents/personal')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.document_name)
        

class Announcement(models.Model):
    announcement_title = models.CharField(
        max_length=120, null=True, blank=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(upload_to='documents/announcement')
    announcement_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.announcement_title)


class Vacancy(models.Model):
    jobtitle = models.ForeignKey(
        Jobtitle, on_delete=models.CASCADE, null=True, blank=True)
    vacancy_name = models.CharField(max_length=120, null=True, blank=True)
    hiring_manager = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    number_of_positions = models.IntegerField(
        default='0', null=True, blank=True)
    description = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.vacancy_name)


class RecruitmentCandidate(models.Model):
    jobvacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, null=True, blank=True)
    candidate_name = models.CharField(max_length=120, null=True, blank=True)
    hiring_manager = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(
        max_length=70, blank=True, null=True, unique=True)
    contact_number = models.IntegerField(default='0', null=True, blank=True)
    resume = models.FileField(upload_to='media', null=True, blank=True)
    key_skills = models.CharField(max_length=120, null=True, blank=True)
    comments = models.CharField(max_length=120, null=True, blank=True)
    date_of_application = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.candidate_name)


class Client(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    client_name = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.CharField(max_length=120, null=True, blank=True)
    project_manager = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.project_name)


class Asset(models.Model):
    asset_name = models.CharField(max_length=120, null=True, blank=True)
    asset_department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)
    asset_description = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.asset_name)


class Attendance(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    in_time = models.DateTimeField(null=True, blank=True)
    out_time = models.DateTimeField(null=True, blank=True)
    note = models.CharField(max_length=120, null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.employee.user_name)


class PerformanceReview(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employeename', null=True, blank=True)
    co_ordinator = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employeecoordinator', null=True, blank=True)
    review_date = models.DateTimeField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True) 

    def __str__(self):
        return str(self.employee)


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return str(self.name)


task_status = (
    ('Open', 'Open'),
    ('In-Process', 'In-Process'),
    ('Pending', 'Pending'),
    ('Closed', 'Closed'),
    ('Re-opened', 'Re-opened'),
)

testing_status = (
    
    ('Open', 'Open'),
    ('In-Process', 'In-Process'),
    ('Pending', 'Pending'),
    ('Closed', 'Closed'),
)

class ProjectModule(models.Model):
    code = models.CharField(max_length=120, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    module_name = models.CharField(max_length=120, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    status = models.BooleanField(default=True)
    task_status = models.CharField(max_length=120, choices=task_status, null=True, blank=True, default='--select--')
    testing_status = models.CharField(max_length=120, choices=testing_status, null=True, blank=True, default='--select--')

    def __str__(self):
        return str(self.module_name)


class ProjectSubModule(models.Model):
    code = models.CharField(max_length=120, null=True, blank=True)
    project_module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE, null=True, blank=True)
    sub_module_name = models.CharField(max_length=120, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    status = models.BooleanField(default=True)
    task_status = models.CharField(max_length=120, choices=task_status, null=True, blank=True, default='--select--')
    testing_status = models.CharField(max_length=120, choices=testing_status, null=True, blank=True, default='--select--')



    def __str__(self):
        return str(self.sub_module_name)


priority_choices = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
)

task_category = (
    ('New', 'New'),
    ('Issue', 'Issue'),
    ('Customization', 'Customization'),
)
class ProjectTasks(models.Model):
    code = models.CharField(max_length=120, null=True, blank=True)
    task_name = models.CharField(max_length=120, null=True, blank=True)
    task_description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    project_module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE, null=True, blank=True)
    project_sub_module = models.ForeignKey(ProjectSubModule, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    priority_level = models.CharField(max_length=120, choices=priority_choices, null=True, blank=True, default='--select--')
    task_status = models.CharField(max_length=120, choices=task_status, null=True, blank=True, default='--select--')
    testing_status = models.CharField(max_length=120, choices=testing_status, null=True, blank=True, default='--select--')
    task_category = models.CharField(max_length=120, choices=task_category, null=True, blank=True, default='--select--')
    raised_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    raised_by_user = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    expected_days = models.PositiveSmallIntegerField(null=True, blank=True)
    start_date = models.DateField(auto_now=True,null = True,blank = True)
    end_date = models.DateField(auto_now=True,null = True,blank = True)
    status = models.BooleanField(default=True)
    is_closed = models.BooleanField(default=False)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.task_name)    


class ProjectImage(models.Model):
    project_task = models.ForeignKey(ProjectTasks, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to='media/project_tasks', null=True, blank=True)

    def __str__(self):
        return str(self.project_task) 

user_status = (
    ('Open', 'Open'),
    ('In-Process', 'In-Process'),
    ('Pending', 'Pending'),
    ('Closed', 'Closed'),
)

class AssignedUser(models.Model):
    task_id = models.ForeignKey(ProjectTasks, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    assigned_date = models.DateField(auto_now=True,null = True,blank = True)
    user_status = models.CharField(max_length=120, choices=user_status, null=True, blank=True, default='--select--')
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.employee)    


class DialyStatusupdates(models.Model):
    task_id = models.ForeignKey(ProjectTasks, on_delete=models.CASCADE, null=True, blank=True)
    updates = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    user_status = models.CharField(max_length=120, choices=user_status, null=True, blank=True, default='--select--')
    testing_status = models.CharField(max_length=120, choices=testing_status, null=True, blank=True, default='--select--')
    priority = models.CharField(max_length=120, null=True, blank=True)
    task_status = models.CharField(max_length=120, null=True, blank=True)
    image1 = models.ImageField(upload_to='media/status_updates', null=True, blank=True)
    image2 = models.ImageField(upload_to='media/status_updates', null=True, blank=True)

    def __str__(self):
        return str(self.task_id.task_name)   