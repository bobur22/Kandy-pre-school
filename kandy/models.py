from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .validators import validate_email, PhoneValidator, validate_f_name, valid_url_extension
from django.utils import timezone


# class Worker(models.Model):


class Career(models.Model):
    f_name = models.CharField(max_length=50, help_text=_("Required. The full name of the worker."),
                              validators=[validate_f_name])
    email = models.EmailField(_("email address"),
                              help_text=_("Required. Your gmail address."),
                              error_messages={"unique": _("A user with that email already exists")},
                              validators=[validate_email])
    p_number = models.CharField(max_length=13, blank=True, null=True,
                                help_text=_('Enter phone number'
                                            ' e.g: +998123456789'),
                                verbose_name='phone number',
                                error_messages={'invalid': _('Please enter a valid phone')},
                                validators=[PhoneValidator()])
    message = models.TextField(blank=True, null=True,
                               help_text=_("Tell us what you can do."))
    career_img = models.ImageField(upload_to='career/', blank=True, null=True, help_text=_(
        "Please upload your cv or report file about your career.(.jpg, .jpeg, .png only)!"),
                                   validators=[valid_url_extension])

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.f_name

    class Meta:
        verbose_name = "Career"
        verbose_name_plural = "Careers"


class Application(models.Model):
    Gender_Choice = (('M', 'Male'), ('F', 'Female'))

    parent_fname = models.CharField(max_length=50, help_text=_("Required. The full name of the parrent."),
                                    validators=[validate_f_name])
    parent_address = models.CharField(max_length=50, help_text=_("Required. The address of the parrent."))
    email = models.EmailField(_("email address"),
                              help_text=_("Required. Your gmail address."),
                              error_messages={"unique": _("A user with that email already exists")},
                              validators=[validate_email])
    home_phone = models.CharField(max_length=13, blank=True, help_text=_("Enter phone number"
                                                                         " e.g: +998123456789"),
                                  verbose_name="phone number",
                                  error_messages={
                                      'unique': _("A user with that phone number already exists"),
                                      'invalid': _("Please enter a valid phone")},
                                  validators=[PhoneValidator()])
    cell_phone = models.CharField(max_length=13, help_text=_("Enter phone number"
                                                             " e.g: +998123456789"),
                                  verbose_name='phone number',
                                  error_messages={
                                      "unique": _("A user with that phone number already exists"),
                                      "invalid": _("Please enter a valid phone")},
                                  validators=[PhoneValidator()])
    child_fname = models.CharField(max_length=50, help_text=_("Required. The full name of the child name."),
                                   validators=[validate_f_name])
    gender = models.CharField(max_length=1, choices=Gender_Choice, default='M',
                              help_text=_("Required. Choose child's gender."))
    date_of_birth = models.DateField(null=True, blank=True, default=timezone.now,
                                     help_text=_("Required. Child's birth date."))
    child_address = models.CharField(null=True, blank=True, max_length=50,
                                     help_text=_("The additional address of the child"))
    child_img = models.ImageField(upload_to="children_photo/", null=True, blank=True,
                                  help_text=_("'Your child's picture. .jpg, .jpeg, .png only!'"),
                                  validators=[valid_url_extension])
    child_text = models.TextField(null=True, blank=True,
                                  help_text=_("Enter your address here. e.g: 45/9 Sergeli 7, Tashkent Shahar"))

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.parent_fname

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"
