from django.db.models.base import Model
from apps.posts.models import Post
from django.forms import ModelForm, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_content']
        widgets = {
            'post_content': Textarea(attrs={'cols': 50, 'rows': 2, 'resize':'none' , 'class':'form-control'}),
        }

        labels = {
                'post_content': '',
                # 'post_content': 'Contenido del Post',
        }

