from django import forms
from .models import DatosGestante,ActividadGestante,SeguimientoGestante,SoporteGestante, CargueMensual

class DatosGestanteForm(forms.ModelForm):
    class Meta:
        model = DatosGestante  
        fields = [
    
            'tipdoc',
            'nro_doc',
            'fecha_parto',
  
        ]
        widgets = {
            'fecha_parto': forms.DateInput(attrs={'type': 'date'}),
        }

class ActividadGestanteForm(forms.ModelForm):
    class Meta:
        model = ActividadGestante
        fields = [
    
            'fecha_parto',
            'cod_cups',
            'finalidad',
            'clas_ries_ges',
            'clas_ries_precl',
            'suministro_asa',
            'suministro_acido',
            'suministro_sulfato',
            'suministro_calcio',
            'fecha_suministro',
            'suministro_antic',
            'fecha_salida',
   
          
        ]
        widgets = {
            'fecha_parto': forms.DateInput(attrs={'type': 'date'}),
            'fecha_suministro': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
        }

class SeguimientoGestanteForm(forms.ModelForm):
    class Meta:
        model = SeguimientoGestante
        fields = [

            'tipo_caso',
            'fecha_seguimiento',
            'tipo_seguimiento',
            'asig_cita_pm',
            'asig_cita_me',
            'referencia_inst',
            'can_entrega_med',
            'entrega_med',
            'info_ciudado_sal',
     
          
        ]
        widgets = {
            'fecha_seguimiento': forms.DateInput(attrs={'type': 'date'})
        }

class SoporteGestanteForm(forms.ModelForm):
    class Meta:
        model = SoporteGestante
        fields = ['tipo_arch', 'soporte']

    def clean_soporte(self):
        soporte = self.cleaned_data.get('soporte')

        if soporte:
            file_extension = soporte.name.split('.')[-1].lower()
            if file_extension != 'pdf':
                raise forms.ValidationError('El archivo debe ser en formato PDF.')

        return soporte
    

class CargueMensualForm(forms.ModelForm):
    class Meta:
        model = CargueMensual
        fields = ['soporte_excel']

    def clean_soporte_excel(self):
        soporte_excel = self.cleaned_data.get('soporte_excel')
        if soporte_excel:
            ext = soporte_excel.name.split('.')[-1].lower()
            if ext not in ['xls', 'xlsx']:
                raise forms.ValidationError("Por favor, suba un archivo Excel válido (xlsx o xls).")
        return soporte_excel


