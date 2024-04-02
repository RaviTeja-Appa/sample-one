from .models import Comment
from .models import Board  # Assuming Board model is in the same app
from django.forms import forms, ModelForm, ModelChoiceField

from .models import Image_Posting, Board, Comment, Following

from .models import Image_Posting, Board, Comment, Following, Save_Post

from django import forms


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
        }


# class BoardChoiceField(forms.ModelChoiceField):
#     def __init__(self, user, **kwargs):
#         super().__init__(queryset=Board.objects.none(), **kwargs)
#         self.user = user

#     def to_label(self, obj):
#         return obj.name

#     def get_queryset(self):
#         if self.user:
#             return self.user.board_set.all()
#         else:
#             return Board.objects.none()


class PinCreationForm(forms.ModelForm):
    image_Post = forms.ImageField(label='Image', widget=forms.ClearableFileInput(
        attrs={'placeholder': 'Upload Image'}))

    def clean_image_Post(self):
        image = self.cleaned_data['image_Post']
        # Optional image validation logic here
        return image

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            # Filter boards based on user's ownership using queryset
            boards = Board.objects.filter(user=user)
            self.fields['board'] = forms.ModelChoiceField(
                queryset=boards, label='Select Board')
        else:
            # Set empty choices if no user provided
            self.fields['board'] = forms.ModelChoiceField(
                queryset=Board.objects.none(), label='Select Board')

    class Meta:
        model = Image_Posting
        fields = ['title', 'image_description', 'board',
                  'image_tagged_topics', 'image_Post']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Title'}),
            'image_description': forms.Textarea(attrs={'class': 'form-field-textarea', 'placeholder': 'Image Description'}),
            'image_tagged_topics': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Tagged Topics'}),

            'board': forms.Select(attrs={'class': 'form-field', 'placeholder': 'Select Board', 'style': 'width: 300px'}),

            'board': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Board', 'style': 'width: 80%'}),


        }


class PinUpdateForm(forms.ModelForm):
    class Meta:
        model = Image_Posting
        fields = ['title', 'image_description', 'board',
                  'image_tagged_topics', 'image_Post']


class LikePostForm(forms.Form):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class followingForm(forms.ModelForm):
    class Meta:
        model = Following
        fields = []


class Save_Form(forms.ModelForm):
    class Meta:
        model = Save_Post
        fields = []
