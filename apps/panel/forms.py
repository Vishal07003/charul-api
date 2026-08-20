from django import forms
from django.contrib.auth.forms import AuthenticationForm

from apps.categories.models import Category
from apps.projects.models import Project
from apps.services.models import Service
from apps.home.models import Home
from apps.reviews.models import Review
from apps.contact.models import Contact, Lead
from apps.practice.models import Practice
from apps.stats.models import Stat
from apps.process.models import Process


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "field-input",
                "placeholder": "Username",
                "autocomplete": "username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "field-input",
                "placeholder": "Password",
                "autocomplete": "current-password",
            }
        )
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "order"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "field-input"}),
            "order": forms.NumberInput(attrs={"class": "field-input"}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "image",
            "description",
            "location",
            "year",
            "scope",
            "category",
            "order",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "field-input"}),
            "image": forms.ClearableFileInput(attrs={"class": "field-file"}),
            "description": forms.Textarea(attrs={"class": "field-input", "rows": 5}),
            "location": forms.TextInput(attrs={"class": "field-input"}),
            "year": forms.NumberInput(attrs={"class": "field-input"}),
            "scope": forms.TextInput(attrs={"class": "field-input"}),
            "category": forms.Select(attrs={"class": "field-input"}),
            "order": forms.NumberInput(attrs={"class": "field-input"}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "description", "order"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "field-input"}),
            "description": forms.Textarea(attrs={"class": "field-input", "rows": 5}),
            "order": forms.NumberInput(attrs={"class": "field-input"}),
        }


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ["image", "order"]
        widgets = {
            "image": forms.ClearableFileInput(attrs={"class": "field-file"}),
            "order": forms.NumberInput(attrs={"class": "field-input"}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "type", "photo", "video", "description", "order"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "field-input"}),
            "type": forms.Select(attrs={"class": "field-input", "id": "id_type"}),
            "photo": forms.ClearableFileInput(attrs={"class": "field-file"}),
            "video": forms.ClearableFileInput(attrs={"class": "field-file"}),
            "description": forms.Textarea(attrs={"class": "field-input", "rows": 5}),
            "order": forms.NumberInput(attrs={"class": "field-input"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        review_type = cleaned_data.get("type")
        photo = cleaned_data.get("photo")
        video = cleaned_data.get("video")

        if not photo and not (self.instance.pk and self.instance.photo):
            self.add_error("photo", "Photo is required.")

        if review_type == "video":
            has_video = video or (self.instance.pk and self.instance.video)
            if not has_video:
                self.add_error("video", "Video is required for video reviews.")

        if review_type == "text":
            cleaned_data["video"] = None

        return cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["phone", "email", "location", "maps_url", "instagram", "facebook"]
        widgets = {
            "phone": forms.TextInput(attrs={"class": "field-input"}),
            "email": forms.EmailInput(attrs={"class": "field-input"}),
            "location": forms.TextInput(attrs={"class": "field-input"}),
            "maps_url": forms.URLInput(attrs={"class": "field-input", "placeholder": "https://www.google.com/maps/embed?..."}),
            "instagram": forms.URLInput(attrs={"class": "field-input"}),
            "facebook": forms.URLInput(attrs={"class": "field-input"}),
        }


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "field-input"}),
            "email": forms.EmailInput(attrs={"class": "field-input"}),
            "phone": forms.TextInput(attrs={"class": "field-input"}),
            "message": forms.Textarea(attrs={"class": "field-input", "rows": 5}),
        }


class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = ["title", "description", "image", "order"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "field-input"}),
            "description": forms.Textarea(attrs={"class": "field-input", "rows": 5}),
            "image": forms.ClearableFileInput(attrs={"class": "field-file"}),
            "order": forms.NumberInput(attrs={"class": "field-input"}),
        }


class StatForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = ["value", "label", "order"]
        widgets = {
            "value": forms.TextInput(attrs={"class": "field-input"}),
            "label": forms.TextInput(attrs={"class": "field-input"}),
            "order": forms.NumberInput(attrs={"class": "field-input"}),
        }


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ["step", "title", "description"]
        widgets = {
            "step": forms.NumberInput(attrs={"class": "field-input"}),
            "title": forms.TextInput(attrs={"class": "field-input"}),
            "description": forms.Textarea(attrs={"class": "field-input", "rows": 5}),
        }
