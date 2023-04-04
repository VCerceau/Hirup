#from typing_extensions import ParamSpecKwargs
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from compliance.models import CnilReference
import uuid

class Country(models.Model):
    name = models.CharField(max_length=140, null=True)
    available = models.BooleanField(default=True)
    alpha_3 = models.CharField(max_length=4, null=True)
    country_code = models.IntegerField(null=True)
    flag = models.CharField(max_length=14, null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class DeptProfile(models.Model):
    level = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return '{}'.format(self.name)


class Service(models.Model):
    dept = models.ForeignKey(DeptProfile, related_name='services_attached', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class JobProfile(models.Model):
    service = models.ForeignKey(Service, related_name='job_attached', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, related_name='profile_job', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.title)

class OrgaStatus(models.Model):
    status = models.CharField(max_length=100, blank=True, null=True)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.status
    
class OrgaType(models.Model):
    typo = models.CharField(max_length=100, blank=True, null=True)
    online = models.BooleanField(default=True)

    def __str__(self):
        return self.typo
    
        
class Doc_Type(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    ref_cnil = models.ForeignKey(CnilReference, related_name='ref_cnil', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    online = models.BooleanField(default=True)
    valid = models.BooleanField(default=False) 
    removed = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    # Metadata
    class Meta(object):
        ordering = ['ref_cnil']

    def __str__(self):
        return '{}'.format(self.ref_cnil)


# class Organisation(models.Model):
#     company_status = models.ForeignKey(OrgaStatus, on_delete=models.CASCADE, null=True) # 
#     company_typo = models.ManyToManyField(OrgaType, related_name='company_typologie', blank=True) 
#     departement = models.ManyToManyField(DeptProfile, related_name='departement', blank=True) # Internal / Organigramme

#     logo = models.ImageField(upload_to='organisation/logos/', blank=True,  height_field="", width_field="", default='orga/logos/default_logo.png')
#     company_name = models.CharField(max_length=150, blank=True, null=True)
#     rcs = models.CharField(max_length=200, blank=True, null=True)
#     address = models.CharField(max_length=100, blank=True, null=True)
#     phone = models.CharField(max_length=12, blank=True, null=True)
#     zipcode = models.CharField(max_length=10, blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    
#     archived = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, null=True)

#     # Metadata
#     class Meta(object):
#         ordering = ['company_name']

#     def __str__(self):
#         return '{}'.format(self.company_name)


# def supplyer_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/DOCS/mag_<mag_number>/<filename>
#     return 'SUPPLIERS{0}/ACCOUNTABILITY/{1}'.format(instance.mandat.id, filename)

class OrgaProfile(models.Model):
    company_type = models.ForeignKey(OrgaType, on_delete=models.CASCADE, null=True)
    departement = models.ManyToManyField(DeptProfile, related_name='orga', blank=True) # Internal / Organigramme
    supplier = models.ManyToManyField("self", blank=True) # Provide Services To self (DON'T KEEP the datas)
    # supplier = models.ManyToManyField("self", related_name='suppliers', blank=True) # Provide Services To self (DON'T KEEP the datas)
    # external = models.ManyToManyField("self", related_name='externals', blank=True) # Provide Services To self (KEEP the datas event if the relation is broken)
    external = models.ManyToManyField("self", blank=True) # Provide Services To self (KEEP the datas event if the relation is broken)
    
    logo = models.ImageField(upload_to='orga/logos/', blank=True,  height_field="", width_field="", default='orga/logos/default_logo.png')
    company_name = models.CharField(max_length=150, blank=True, null=True)
    rcs = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    # Metadata
    class Meta(object):
        ordering = ['company_name']

    # Methods

    def get_by_user(user):
        user_roles = User_Role.objects.filter(user=user).values('orga')
        user_roles = OrgaProfile.objects.filter(pk__in=user_roles)
        # TODO Utiliser la fonction de nouma en dessous
        from projects.models import Project
        orga_roles = Project.objects.filter(user_project_roles__user=user)

        orgas = OrgaProfile.objects.filter(orgas__in=orga_roles)
        
        orgas |= user_roles

        return orgas

    def get_suppliers(self):
        return OrgaProfile.objects.filter(company_type=3).order_by('company_name').count()
    
    def get_nber_of_mandates(self):
        return Mandate.objects.filter(company_id__supplier=self).count()

    def get_nber_of_docs(self):
        from suppliers.models import SupplierAttachementsFile
        return SupplierAttachementsFile.objects.filter(supplier_id=self).count()

    def get_progress_audit(self):
        from suppliers.models import AuditSupplier, Question
        nber_of_q_in_the_thematic = AuditSupplier.objects.filter(supplier_id=self).count()
        answer_01 = AuditSupplier.objects.filter(archived=False, answer=1, supplier_id=self).count()
        answer_02 = AuditSupplier.objects.filter(archived=False, answer=2, supplier_id=self).count()
        answer_03 = AuditSupplier.objects.filter(archived=False, answer=3, supplier_id=self).count()
        questions = Question.objects.all().count()
        total_question_available = questions - answer_03
        if total_question_available > 0:
            progress = (answer_01 / total_question_available) * 100
        else:
            progress = 0
        return progress

    def get_pa_attached_to_external(self):
        from processactivity.models import PA_CategoriesOfRecipients
        external = PA_CategoriesOfRecipients.objects.filter(typo=4, hidded=False, external=self)
        #print(more_datas)
        return external

    def get_pa_attached_to_suppliers(self):
        from processactivity.models import PA_CategoriesOfRecipients
        
        suppliers = PA_CategoriesOfRecipients.objects.filter(typo=3, hidded=False, supplier=self).distinct()
        #print(more_datas_2)
        return suppliers
    
    def __str__(self):
        return '{}'.format(self.company_name)

        
# def mandate_contract_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/DOCS/mag_<mag_number>/<filename>
#     return 'MANDAT_{2}_{0}/CONTRACT/{1}'.format(instance.mandat.company, filename, instance.mandat.id)

class Mandate(models.Model):
    company = models.ForeignKey(OrgaProfile, related_name='mandate', on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True) 
    owner = models.ForeignKey(User, related_name='mandated', on_delete=models.CASCADE)
    date_start = models.DateField(blank=True, null=True)
    mandate_length = models.CharField(max_length=150, blank=True, null=True)
    
    dpo = models.ForeignKey(User, related_name='dpo', on_delete=models.CASCADE, blank=True, null=True)
    rt = models.ForeignKey(User, related_name='Rt', on_delete=models.CASCADE, blank=True, null=True)
    
    online = models.BooleanField(default=True)
    valid = models.BooleanField(default=True) 
    removed = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    # Metadata
    class Meta(object):
        ordering = ['company']

    def __str__(self):
        return '{}'.format(self.company)


def document_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/DOCS/mag_<mag_number>/<filename>
    return 'MANDAT_{0}/ACCOUNTABILITY/{1}'.format(instance.mandat.id, filename)

class MandateDocument(models.Model):
    mandat = models.ForeignKey(Mandate, related_name='mandate', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    doc_uploaded = models.FileField(upload_to=document_directory_path, validators=[FileExtensionValidator(['pdf'])])

    online = models.BooleanField(default=True)
    valid = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, related_name='doc_added_by', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self) -> str:
        return(self.name)

class User_Role(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    orga = models.ForeignKey('organisations.OrgaProfile', on_delete=models.CASCADE, related_name="roles")
    role = models.ForeignKey('organisations.Role', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return(self.user.username)
    def has_permission_in_orga(user: User, orga: OrgaProfile, edit : bool =False) -> bool:
        """
        
        Check if the user has permission to access or edit the given orga.
        
        Parameters:
            - user (User): The user to check permission for.
            - orga (Organization): The organization to check permission for.
            - edit (bool, optional): Indicates whether to check for edit permission (default is False)
        
        Returns:
        - bool: 
                - True if the user has permission in the orga
                - False if user does not have permission or user_role relation does not exist
        """
        try:
            user_roles = User_Role.objects.get(user=user, orga=orga).role
            # print(user_roles.level)
            # print(edit and user_roles.level > 1)
            if edit and user_roles.level > 1:
                return False
            return True

        except User_Role.DoesNotExist:
            return False

class Compliance_By_Orga(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    mandate = models.ForeignKey(Mandate, related_name='Compliance_By_mandate', on_delete=models.CASCADE, blank=True, null=True)

    pas_all = models.IntegerField(blank=True, null=True)
    dept_all = models.IntegerField(blank=True, null=True) # dept == Project APP
    pas_14 = models.IntegerField(blank=True, null=True)
    pas_21 = models.IntegerField(blank=True, null=True)
    pas_28 = models.IntegerField(blank=True, null=True)
    pas_35 = models.IntegerField(blank=True, null=True)
    pas_42 = models.IntegerField(blank=True, null=True)
    pas_50 = models.IntegerField(blank=True, null=True)
    pas_57 = models.IntegerField(blank=True, null=True)
    pas_64 = models.IntegerField(blank=True, null=True)
    pas_71 = models.IntegerField(blank=True, null=True)
    pas_78 = models.IntegerField(blank=True, null=True)
    pas_85 = models.IntegerField(blank=True, null=True)
    pas_complete = models.IntegerField(blank=True, null=True)

    online = models.BooleanField(default=False)
    calculated_on = models.DateTimeField(auto_now_add=True)
    calculated_by = models.ForeignKey(User, related_name='Compliance_Calculate_By', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(blank=True, null=True)

    # def get_pourcent_less_than_25(self):
    #     calcul = (self.nber_of_pas_less_than_25 / self.nber_of_pas) * 100
    #     result = round(calcul)
    #     return result

    # def get_pourcent_less_than_50(self):
    #     calcul = (self.nber_of_pas_less_than_50 / self.nber_of_pas) * 100
    #     result = round(calcul)
    #     return result

    # def get_pourcent_less_than_75(self):
    #     calcul = (self.nber_of_pas_less_than_75 / self.nber_of_pas) * 100
    #     result = round(calcul)
    #     return result

    # def get_pourcent_more_than_75(self):
    #     calcul = (self.nber_of_pas_more_75 / self.nber_of_pas) * 100
    #     result = round(calcul)
    #     return result

    def get_completed_pas(self):
        calcul = (self.nber_of_pas_complete / self.nber_of_pas) * 100
        result = round(calcul)
        return result