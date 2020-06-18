from django import forms
from .models import Movie
class MovieForm(forms.ModelForm):
    title = forms.CharField(
        max_length=300,
        label='한글 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '한글 제목을 입력하세요.'
            }
        )
    )
    title_en = forms.CharField(
        max_length=300,
        label='영문 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '영문 제목을 입력하세요.'
            }
        )
    )
    audience = forms.IntegerField(
        label='관객수',
        widget=forms.NumberInput (
            attrs={
                'placeholder' : '관객수를 입력하세요'
            }
        )
    )
    open_date = forms.DateField(
        label='개봉일',
        widget=forms.DateInput(
            attrs={
                'placeholder' : '개봉일을 입력하세요'
            }
        )
    )
    genre = forms.CharField(
        max_length=100,
        label='장르',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '장르를 입력하세요'
            }
        )
    
    )
    watch_grade = forms.CharField(
        max_length=50,
        label='관람가',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '관람가를 입력하세요'
            }
        )
    )
    score = forms.FloatField(
        label='평점',
        widget=forms.NumberInput(
            attrs={
                'placeholder' : '평점를 입력하세요'
            }
        )
    )
    poster_url = forms.CharField(
        widget=forms.Textarea,
        label='포스터URL',
    )
    description = forms.CharField(
        widget=forms.Textarea,
        label='줄거리',
        
    )

    class Meta:
        model = Movie
        fields = '__all__'
