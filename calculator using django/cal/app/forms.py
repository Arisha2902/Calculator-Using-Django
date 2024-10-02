from django import forms



class calc(forms.Form):
    num1=forms.CharField(max_length=100)
    num2=forms.CharField(max_length=100)
    operator1 = forms.ChoiceField(choices=  [
            ('+', 'add'),
            ('-', 'sub'),
            ('*', 'mul'),

 ])
    



