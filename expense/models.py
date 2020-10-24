from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
from django.db.models.signals import post_save
from django.urls import reverse
from six import text_type


# Create your models here.


class Expense(models.Model):
    expense_id = models.CharField(
        max_length=120, primary_key=True, default=str(uuid.uuid4())
    )
    rent = models.FloatField(verbose_name="Rent")
    physio = models.FloatField(verbose_name="Physio")
    family = models.FloatField(verbose_name="Family")
    personal = models.FloatField(verbose_name="Personal")
    dependent = models.FloatField(verbose_name="Dependent")
    misc = models.FloatField(verbose_name="Miscallenaous")
    doctor = models.FloatField(verbose_name="Doctor")
    gym = models.FloatField(verbose_name="Gym")
    saving = models.FloatField(verbose_name="Saving")
    extra = models.TextField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True, verbose_name="Total")
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Expense Detail")
        verbose_name_plural = _("Expense Details")
        unique_together = ("month", "year")

    def __str__(self):
        return "{}".format(self.expense_id)

    def __get_label(self, field):
        return text_type(self._meta.get_field(field).verbose_name)

    def get_year(self):
        return self.created_at.year

    def get_month(self):
        return self.created_at.month

    def get_absolute_url(self):
        return reverse("expense:expense_detail", args=[str(self.expense_id)])

    @property
    def rent_label(self):
        return self.__get_label("rent")

    @property
    def physio_label(self):
        return self.__get_label("physio")

    @property
    def family_label(self):
        return self.__get_label("family")

    @property
    def dependent_label(self):
        return self.__get_label("dependent")

    @property
    def saving_label(self):
        return self.__get_label("saving")

    @property
    def misc_label(self):
        return self.__get_label("misc")

    @property
    def doctor_label(self):
        return self.__get_label("doctor")

    @property
    def gym_label(self):
        return self.__get_label("gym")

    @property
    def extra_label(self):
        return self.__get_label("extra")

    @property
    def personal_label(self):
        return self.__get_label("personal")

    @property
    def total_label(self):
        return self.__get_label("total")


def update_date_year(sender, instance, **kwargs):
    Expense.objects.filter(expense_id=instance.expense_id).update(
        month=instance.get_month(),
        year=instance.get_year(),
        total=instance.rent
        + instance.physio
        + instance.family
        + instance.personal
        + instance.dependent
        + instance.misc
        + instance.doctor
        + instance.gym
        + instance.saving,
    )


post_save.connect(update_date_year, sender=Expense)
