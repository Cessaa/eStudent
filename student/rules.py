from django.contrib import messages


class InfoMessageMixin:
    """
    Add a info message on successful form submission.
    """
    info_message = ""

    def form_valid(self, form):
        response = super().form_valid(form)
        info_message = self.get_info_message(form.cleaned_data)

        if info_message:
            messages.info(self.request, info_message)
        return response

    def get_info_message(self, cleaned_data):
        return self.info_message % cleaned_data
