from django.db.models.base import Model
from apps.posts.models import Post
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_content']
        labels = {
                'post_content': '',
                # 'post_content': 'Contenido del Post',
        }

