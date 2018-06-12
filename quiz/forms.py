from django import forms

class QuizForm(forms.Form):
    new_question = forms.CharField(
                    label='Add Question',
                    max_length=100,
                    widget=forms.TextInput(attrs={'placeholder':'Enter your own question'}))
    yes_answer = forms.BooleanField(label="Yes", required=False)
    no_answer = forms.BooleanField(label="No", required=False)
