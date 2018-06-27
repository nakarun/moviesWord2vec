from django import forms


ACTOR_CHOICES= [
    ('d', 'ドゥニ・ヴィルヌーヴ'),
    ('e', 'エマ・ワトソン'),
    ('s', 'ステイサム'),
]

class ActorForm(forms.Form):
    actor = forms.CharField(label='', widget=forms.Select(choices=ACTOR_CHOICES))

class MyForm(forms.Form):
    text = forms.CharField(max_length=100)
