from django import forms  
from insta.models import Post , HashTag 
# from django.shortcuts import c



# choice_list = []


# for item in choices:
#     choice_list.append(item)
class PostForm(forms.ModelForm):
    # choicelist = HashTag.
    choices = HashTag.objects.all().values_list('name','name')
    # hash_tag = forms.Select(choices=choices,attrs={'class':'form-control'}),
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','hash_tag','body', 'image')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'hash_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
       
        }

        def clean_hash_tag(self):
            data  = self.cleaned_data['hash_tag']
            print(data)
            return data
            


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),


        }