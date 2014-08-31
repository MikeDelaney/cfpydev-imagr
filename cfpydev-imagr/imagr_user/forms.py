from django import forms
from imagr_user.models import ImagrUser
from registration.forms import RegistrationForm


class ImagrUserRegistrationForm(RegistrationForm):
    def clean_username(self):
        """Validate that the username is alphanumeric and is not already in use.
        """
        existing = ImagrUser.objects.filter(
            username__iexact=self.cleaned_data['username']
        )
        if existing.exists():
            raise forms.ValidationError(
                "A user with that username already exists."
            )
        else:
            return self.cleaned_data['username']

    def save(self, commit=True):
        # Save password in hashed format
        user = super(ImagrUserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
