from django.db import models
from django.forms import ModelForm, Textarea

# Create your models here.

class Account(models.Model):
    bank = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, default='', blank=True)
    last_name = models.CharField(max_length=100, default='')
    account_no = models.CharField(max_length=20, default='')


    def __str__(self):
        return f"{self.bank} - {self.account_no}"



class Apply(models.Model):
    # gender choice
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    # purpose of travel choice
    PURPOSE = (
        ('PS', 'Postgraduate Study'),
        ('US', 'Undergraduate Study'),
        ('I', 'Immigration'),
        ('V', 'Vacation'),
    )

    APPLICATION = (
        ('Account Opening', 'Account Opening'),
        ('Account Funding', "Account Funding"),
        ('Days to Maturity', 'Days to Maturity'),
        ('Funds Liquidated', 'Funds Liquidated')
    )

    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=50, blank=True,)
    last_name = models.CharField(max_length=50, null=False)
    mobile_number = models.IntegerField(unique=True)
    email_address = models.EmailField(max_length=50, unique=True)
    bvn = models.CharField(max_length=10, null=False)
    gender = models.CharField(max_length=10, null=False, choices=GENDER)
    mother_name = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    state_of_origin = models.CharField(max_length=50,blank=True)
    local_govt_area = models.CharField(max_length=50, blank=True)
    home_town = models.CharField(max_length=50, blank=True)
    residential_address = models.CharField(max_length=100, null=False)
    nok_name = models.CharField(max_length=50, null=False)
    nok_address = models.CharField(max_length=100)
    nok_number = models.IntegerField()
    nok_email = models.EmailField(max_length=50, blank=True)
    loan_amount = models.IntegerField(null=False)
    tenor_in_weeks = models.IntegerField()
    purpose = models.CharField(max_length=30, choices=PURPOSE)
    destination = models.CharField(max_length=50, null=False)
    school = models.CharField(max_length=100, blank=True)
    previous_school = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=100, blank=True)
    human_referral = models.CharField(max_length=50, blank=True)
    id_card = models.ImageField(upload_to='file_upload')
    utility = models.ImageField(upload_to='file_upload')
    passport = models.ImageField(upload_to='file_upload')
    referral_code = models.CharField(max_length=20, blank=True)
    application_status = models.CharField(max_length=30, choices=APPLICATION, default='Account Opening')
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


