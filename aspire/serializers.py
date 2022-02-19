from rest_framework import serializers
from .models import Apply, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = []


class ApplySerializer(serializers.ModelSerializer):
    # serializer method 1
    # account_name = serializers.CharField(source='account.name')
    # account_number = serializers.IntegerField(source='account.account_no')
    # account = serializers.SerializerMethodField()

    # serializer method 2
    account = AccountSerializer()

    # serializer method 3
    # def get_account(self, obj):
    #     account = None
    #     if obj.account:
    #         account = dict()
    #         account['name'] = obj.account.name
    #         account['acct_number'] = obj.account.account_no
    #         # account = AccountSerializer(obj.account).data
    #     return account

    class Meta:
        model = Apply
        exclude = ['id','middle_name','bvn','gender','mother_name','place_of_birth','nationality','state_of_origin','local_govt_area',
                   'home_town','residential_address','nok_name','nok_address','nok_number','nok_email','tenor_in_weeks',
                   'loan_amount','purpose','destination','school','previous_school','course','human_referral','id_card',
                   'utility','passport','referral_code','created_on','updated_on']
        # depth = 1

