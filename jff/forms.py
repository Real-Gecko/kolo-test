from django import forms

from jff import models


class UpdateReadonlyFieldsFormMixin:
    """Use to make form fields uneditable on update.
    Define desired fields in Form.Meta.update_readonly_fields:
    ```
    class Meta:
        update_readonly_fields = ['username', 'email']
    ```
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        instance = getattr(self, "instance", None)

        if instance and instance.id:
            if self.Meta.update_readonly_fields == "__all__":
                field_list = self.fields
            else:
                field_list = self.Meta.update_readonly_fields

            for field in field_list:
                self.fields[field].disabled = True


class OfficeForm(UpdateReadonlyFieldsFormMixin, forms.ModelForm):
    class Meta:
        model = models.Office
        fields = "__all__"
        update_readonly_fields = ["company"]
