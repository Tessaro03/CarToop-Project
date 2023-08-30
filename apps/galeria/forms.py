from django import forms
from galeria.models import Veiculo, Foto

class VeiculoForms(forms.ModelForm):
    class Meta:
        model = Veiculo
        exclude = ['user']
        fields = '__all__'
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control-long '}),
            'marca':forms.Select(attrs={'class':'form-control-long'}),
            'ano':forms.TextInput(attrs={'class':'form-control-mini'}),
            'km':forms.TextInput(attrs={'class':'form-control-mini'}),
            'tipo':forms.Select(attrs={'class':'form-control-mini'}),        
            'portas':forms.TextInput(attrs={'class':'form-control-mini'}),
            'motor':forms.TextInput(attrs={'class':'form-control-mini'}),
            'cor':forms.TextInput(attrs={'class':'form-control-mini'}),
            'câmbio':forms.Select(attrs={'class':'form-control-mini'}),
            'combustivel':forms.Select(attrs={'class':'form-control-long'}),        
            'valor':forms.TextInput(attrs={'class':'form-control-long'}),
            'legenda':forms.Textarea(attrs={'class':'form-control-big'}),
            }
        
class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        exclude = ['veiculo']
        fields = '__all__'
        widgets = {
            'posicao': forms.TextInput(attrs={'class': 'form-control-foto'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-foto'}),
        }
