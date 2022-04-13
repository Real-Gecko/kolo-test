from django.forms import BaseForm

BaseForm.use_required_attribute = False

super_base_form_init = BaseForm.__init__


def base_form_init(self, *args, **kwargs):
    if len(args) == 8:
        args = list(args)
        args[6] = ""
    super_base_form_init(self, *args, **kwargs)


# For form to properly work with Kolo this must be commented
BaseForm.__init__ = base_form_init
