from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusEnum(models.IntegerChoices):
    CHECKED = 1, _("Checked")
    UNCHECKED = 0, _("Unchecked")
