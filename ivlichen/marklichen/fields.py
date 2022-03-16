from django import forms

from marklichen.widgets import MarkdownWidget


class MarkdownFormField(forms.CharField):
    """
    Used in FormFields as a Markdown enabled replacement for ``CharField``.
    """

    def __init__(self, *args, **kwargs):
        """
        Arguments are similar to Django's default ``CharField``.

        See Django's `documentations on CharField`_ for additional information.

        .. _docs on Charfield: https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.CharField
        """
        super(MarkdownFormField, self).__init__(*args, **kwargs)

        if issubclass(self.widget.__class__, forms.widgets.MultiWidget):
            is_markdownx_widget = any(
                issubclass(item.__class__, MarkdownFormField)
                for item in getattr(self.widget, 'widgets', list())
            )

            if not is_markdownx_widget:
                self.widget = MarkdownWidget()

        elif not issubclass(self.widget.__class__, MarkdownWidget):
            self.widget = MarkdownWidget()
