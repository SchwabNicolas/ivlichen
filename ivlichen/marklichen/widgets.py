from django import forms


class MarkdownWidget(forms.Textarea):
    pass


class SmallMarkdownWidget(MarkdownWidget, forms.TextInput):
    pass
