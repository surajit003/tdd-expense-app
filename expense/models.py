from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

# Create your models here.


class Expense(models.Model):
    expense_id = models.CharField(
        max_length=120, primary_key=True, default=str(uuid.uuid4())
    )
    rent = models.FloatField()
    physio = models.FloatField()
    family = models.FloatField()
    personal = models.FloatField()
    dependent = models.FloatField()
    misc = models.FloatField()
    doctor = models.FloatField()
    gym = models.FloatField()
    saving = models.FloatField()
    extra = models.TextField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Expense Detail")
        verbose_name_plural = _("Expense Details")

    def __str__(self):
        return "{}-{}".format(self.id, self.total)
