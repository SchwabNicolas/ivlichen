from django.db import models

from marklichen.fields import MarkdownFormField


class MarkdownField(models.TextField):
    def formfield(self, **kwargs):
        """
        Customising the ``form_class``.
        :return: TextField with a custom ``form_class``.
        :rtype: django.db.models.TextField
        """
        defaults = {'form_class': MarkdownFormField}
        defaults.update(kwargs)
        return super(MarkdownField, self).formfield(**defaults)
