from django.db import models
from django.utils.translation import gettext as _


class WorkingDay(models.Model):
    date = models.DateField(_("Date"))

    def __str__(self):
        return str(self.date)
