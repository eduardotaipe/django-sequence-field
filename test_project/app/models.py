from django.db import models
from sequence_field.fields import SequenceField
from app import strings


class TestModel(models.Model):

    sequence = SequenceField(
        verbose_name=strings.TESTMODEL_SEQUENCE,
        key="app.test.sequence.1",
        template="%Y%m%d%(code)s%NNNNN",
        params={"code": "ABC"},
        auto=True,
    )

    created = models.DateTimeField(
        verbose_name=strings.TESTMODEL_CREATED, auto_now_add=True
    )

    updated = models.DateTimeField(
        verbose_name=strings.TESTMODEL_UPDATED, auto_now=True
    )

    class Meta:
        verbose_name = strings.TESTMODEL_MODEL_NAME
        verbose_name_plural = strings.TESTMODEL_MODEL_NAME_PLURAL

    def __str__(self):
        return self.sequence
