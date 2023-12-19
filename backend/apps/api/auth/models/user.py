from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .common_users_manager import CommonUsersManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Пользователь
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, "
            "digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    patronymic = models.CharField(
        _("Отчество"), max_length=150, blank=True, null=True
    )
    email = models.EmailField(_("email address"), blank=True)

    user_image = models.ImageField(
        _("Фотография пользователя"),
        upload_to="user/img",
        blank=True,
        null=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_manager_department = models.BooleanField(
        default=False, verbose_name=_("Заведующий кафедры")
    )
    manager_department = models.ForeignKey(
        "reference.Department",
        blank=True,
        null=True,
        verbose_name=_("Кафедра"),
        on_delete=models.SET_NULL,
    )

    is_manager_faculty = models.BooleanField(
        default=False, verbose_name=_("Декан факультета")
    )
    manager_faculty = models.ForeignKey(
        "reference.Faculty",
        blank=True,
        null=True,
        verbose_name=_("Факультет"),
        on_delete=models.SET_NULL,
    )

    is_expert = models.BooleanField(default=False, verbose_name=_("Эксперт"))
    category_expert = models.ForeignKey(
        "reference.MainCategory",
        blank=True,
        null=True,
        verbose_name=_("Категория эксперта"),
        on_delete=models.SET_NULL,
    )

    is_super_expert = models.BooleanField(
        default=False, verbose_name=_("Супер эксперт")
    )

    objects = UserManager()
    common_users = CommonUsersManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Return the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
