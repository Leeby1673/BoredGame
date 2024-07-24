from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "標題"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "內容", "rows": 10}
            ),
        }

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Div(
    #             Field("title", wrapper_class="form-floating"),
    #             css_class="mb-3",
    #             id="div_id_title",
    #         ),
    #         Div(
    #             Field("content"),
    #             css_class="mb-3",
    #             id="div_id_content",
    #         ),
    #         Submit("submit", "Submit", css_class="btn btn-primary"),
    #     )
