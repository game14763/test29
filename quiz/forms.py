from django import forms
from quiz.models import Quiz

class QuizForm(forms.ModelForm):
    question = forms.CharField(
                    label='Add Question',
                    max_length=100,
                    widget=forms.TextInput(attrs={'placeholder':'Enter your own question'}))
    yes_answer = forms.BooleanField(label="Yes", required=False)
    no_answer = forms.BooleanField(label="No", required=False)
    class Meta():
        model = Quiz
        fields = '__all__'
