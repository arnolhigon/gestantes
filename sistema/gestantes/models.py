from django.db import models
import os
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError



# Create your models here.


def user_directory_path(instance, filename):
    ruta = 'SOPORTES_GESTANTES'
    return '{0}/{1}/{2}/{3}/{4}/{5}'.format(ruta, instance.regional,
                                    instance.prestador,
                                    instance.tipdoc,
                                    instance.identificacion,
                                    instance.tipoar,
                                    filename)



class DatosGestante(models.Model):

    TIPDOC = (
        ('CC', 'CEDULA DE CIUDA'),
        ('CE', 'CEDULA DE EXTR.'),
        ('MS', 'MENOR SIN IDENT'),
        ('NU', 'N.UNICO IDENT'),
        ('PA', 'PASAPORTE'),
        ('RC', 'REGISTRO CIVIL'),
        ('TI', 'TARJETA IDENT.'),
        ('PE', 'PERMISO PERMANE'),
        ('CN', 'NACIDO VIVO'),
        ('SC', 'SALVO CONDUTO'),
        ('AS', 'ADULTO SIN IDEN'),
        ('PT', 'PER PROTEC TEMP'),
    )

    tipo_archivo = models.IntegerField('Tipo archivo', default=2)
    tipdoc = models.CharField('Tipo de documento', max_length=2, null=True, blank=True)
    nro_doc = models.CharField("Documento de identificación", max_length=25, db_index=True)
    fecha_parto = models.DateField('Fecha de parto')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    objects = models.Manager()

    def __str__(self):
        return str(self.nro_doc)

    class Meta:
        ordering = ["nro_doc"]


class ActividadGestante(models.Model):

    CLASIF = (
        ('4', 'Alto riesgo'),
        ('5', 'Bajo riesgo'),
        ('21', 'Riesgo no evaluado'),
    )

    SUMIN = (
        ('0', 'No aplica'),
        ('1', 'Si se suministra'),
        ('21', 'Riesgo no evaluado'),
    )

    SUMAC = (
        ('0', 'No aplica'),
        ('1', 'Dispositivo intrauterino'),
        ('2', 'Dispositivo intrauterino y preservativo'),
        ('3', 'implante sudérmico'),
        ('4', 'implante sudérmico y preservativo '),
        ('5', 'Oral'),
        ('6', 'Oral y preservativo'),
        ('7', 'Inyectable mensual'),
        ('8', 'Inyectable mensual y preservativo'),
        ('9', 'Inyectable trimestral'),
        ('10', 'Inyectable trimestral y preservativo'),
        ('13', 'Esterilización'),
        ('14', 'Esterilización y preservativo'),
        ('15', 'Preservativo'),
    )

    tipo_archivo = models.IntegerField('Tipo archivo', default=2)
    fecha_parto = models.DateField('Fecha de parto')
    cod_cups = models.CharField('codigo cups', max_length=25, null=True, blank=True, db_index=True)
    finalidad = models.CharField('Finalidad tecnologia salud', max_length=2, null=True, blank=True)
    clas_ries_ges = models.CharField('Clasificación riesgo gestacional', max_length=2, choices=CLASIF)
    clas_ries_precl = models.CharField('Clasificación riesgo preclampsia', max_length=2, choices=CLASIF)
    suministro_asa = models.CharField('Suministro asa', max_length=2, choices=SUMIN)
    suministro_acido = models.CharField('Suministro acido folico', max_length=2, choices=SUMIN)
    suministro_sulfato = models.CharField('Suministro sulfato ferroso', max_length=2, choices=SUMIN)
    suministro_calcio = models.CharField('Suministro calcio ', max_length=2, choices=SUMIN)
    fecha_suministro = models.DateField('Fecha suministro')
    suministro_antic = models.CharField('Suministro anticonceptivo ', max_length=2, choices=SUMAC)
    fecha_salida = models.DateField('Fecha salida atención parto cesarea')
    datosgestante = models.ForeignKey(DatosGestante, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    objects = models.Manager()

    def __str__(self):
        return str(self.cod_cups)

    class Meta:
        ordering = ["cod_cups"]


class SeguimientoGestante(models.Model):

    TIPOCA = (
        ('1', 'Mayor de 95 años'),
        ('2', 'Alteraciones nutricionales'),
        ('3', 'Consulta a servicios de urgencias'),
        ('4', 'Hospitalización'),
        ('5', 'Laboratorios alterados'),
        ('6', 'Antecendes de preeclampsia'),
        ('7', 'Riesgo de preeclampsia'),
        ('8', 'Menos de cuatro controles prenatales mediando la semana gestacional 30'),
        ('9', 'Morbilidad materna externa'),
        ('10', 'Riesgo de tromboembolismo'),
        ('10', 'Diagnóstico de enfermedad del colágeno'),
        ('10', 'Diagnóstico de algún tipo de cáncer'),

    )

    SUMIN = (
        ('0', 'No aplica'),
        ('1', 'Si se suministra'),
        ('21', 'Riesgo no evaluado'),
    )

    RPTA = (
        ('1', 'SI'),
        ('2', 'NO'),

    )

    TSEGUI = (
        ('1', 'Contacto telefónico'),
        ('2', 'Visita domiciliaria'),
        ('3', 'Visita de auditor concurrente en hospitalización'),
        ('4', 'Otro'),

    )

    tipo_archivo = models.IntegerField('Tipo archivo', default=2)
    tipo_caso = models.CharField('Tipo caso', max_length=2, choices=TIPOCA)
    fecha_seguimiento = models.DateField('Fecha de seguimiento')
    tipo_seguimiento = models.CharField('Tipo de seguimiento', max_length=2, choices=TSEGUI)
    asig_cita_pm = models.CharField('Asignación cita profesional medicina', max_length=2, choices=RPTA)
    asig_cita_me = models.CharField('Asignación cita medicina especializada', max_length=2, choices=RPTA)
    referencia_inst = models.CharField('Referencia mayor complejidad', max_length=2, choices=RPTA)
    can_entrega_med = models.CharField('Canalización entrega de medicamentos', max_length=2, choices=RPTA)
    entrega_med = models.CharField('Entrega de medicamentos', max_length=2, choices=RPTA)
    info_ciudado_sal = models.CharField('Información cuidado salud', max_length=2, choices=RPTA)
    datosgestante = models.ForeignKey(DatosGestante, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    objects = models.Manager()

    def __str__(self):
        return str(self.tipo_caso)


class SoporteGestante(models.Model):
    TIPOCA = (
    ('IC', 'Inicio de control'),
    ('VH', 'VIH'),
    ('SF', 'Sifilis'),
    ('HC', 'Historia clinica'),
    )
    tipo_arch = models.CharField('Tipo archivo', max_length=2, choices=TIPOCA)
    soporte = models.FileField('Soporte',
                               validators=[FileExtensionValidator(['pdf'])])
    datosgestante = models.ForeignKey(DatosGestante, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    objects = models.Manager()

    def __str__(self):
        return str(self.soporte)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.soporte.path):
            os.remove(self.soporte.path)
        super(SoporteGestante, self).delete(*args, **kwargs)



def validate_excel_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError("Por favor, suba un archivo Excel válido (xlsx o xls).")

class CargueMensual(models.Model):
    soporte_excel = models.FileField('Soporte Excel', validators=[validate_excel_file_extension])
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.soporte_excel



class InformacionGestante(models.Model):
    OBSERVACIONES_PARA_SEGUIMIENTO = models.TextField('OBSERVACIONES PARA SEGUIMIENTO')
    RESPONSABLE_DE_LA_ZONA = models.CharField('RESPONSABLE DE LA ZONA',max_length=255)
    PUNTO_O_CENTRO_DE_ATENCION = models.CharField('PUNTO O CENTRO DE ATENCION',max_length=255)
    ATENCION_PRECONCEPCIONAL = models.CharField('ATENCIÓN PRECONCEPCIONAL',max_length=255)
    APELLIDO = models.CharField('APELLIDO',max_length=255)
    APELLIDO2 = models.CharField('APELLIDO 2',max_length=255)
    NOMBRE1 = models.CharField('NOMBRE 1',max_length=255)
    cargue_mensual = models.ForeignKey(CargueMensual, on_delete=models.CASCADE, related_name='informacion_gestante')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    objects = models.Manager()


class InformacionMensual(models.Model):
    var1 = models.TextField('Observaciones Seguimiento', null=True, blank=True)
    var2 = models.CharField('Responsable zona', max_length=50, null=True, blank=True)
    var3 = models.CharField('Punto Atencion', max_length=60, null=True, blank=True)
    var4 = models.CharField('Atencion_Preconcepcional', max_length=50, null=True, blank=True)
    var5 = models.CharField("Primer nombre", max_length=60, null=True, blank=True)
    var6 = models.CharField("Segundo nombre", max_length=60, null=True, blank=True)
    var7 = models.CharField("Primer apellido", max_length=60, null=True, blank=True)
    var8 = models.CharField("Segundo apellido", max_length=60, null=True, blank=True)
    var9 = models.CharField('Tipo de documento', max_length=2, null=True, blank=True)
    var10 = models.CharField("Documento de identificación", max_length=25, null=True, blank=True, db_index=True)
    var11 = models.CharField("Estado Civil", max_length=20, null=True, blank=True)
    var12 = models.CharField("Ocupacion", max_length=50, null=True, blank=True)
    var13 = models.CharField('Fecha de nacimiento',max_length=10, null=True, blank=True)
    var14 = models.CharField("Edad actual", max_length=60, null=True, blank=True)
    var15 = models.CharField('Fecha Identificacion Gestante',max_length=10, null=True, blank=True)
    var16 = models.CharField("Efectividad Demanda", max_length=50, null=True, blank=True)
    var17 = models.CharField("Novedad Momento Captacion", max_length=50, null=True, blank=True)
    var18 = models.CharField('Fecha Consulta PrimeraVez CPN',max_length=10, null=True, blank=True)
    var19 = models.CharField("Regimen", max_length=20, null=True, blank=True)
    var20 = models.CharField("Aseguradora", max_length=50, null=True, blank=True)
    var21 = models.CharField("Municipio Residencia", max_length=50, null=True, blank=True)
    var22 = models.CharField("Zona Residencia", max_length=20, null=True, blank=True)
    var23 = models.CharField("Vereda y/o Barrio", max_length=50, null=True, blank=True)
    var24 = models.CharField("Direcion", max_length=50, null=True, blank=True)
    var25 = models.CharField("Resguardo", max_length=50, null=True, blank=True)
    var26 = models.CharField("Telefono", max_length=50, null=True, blank=True)
    var27 = models.CharField("Tipo Etnia", max_length=50, null=True, blank=True)
    var28 = models.CharField("Pueblo Indigena", max_length=50, null=True, blank=True)
    var29 = models.CharField("Estudios", max_length=50, null=True, blank=True)
    var30 = models.CharField("Uso Sustancias Psicoactivas", max_length=32, null=True, blank=True)
    var31 = models.CharField("Embarazo Aceptado Deseado", max_length=2, null=True, blank=True)
    var32 = models.CharField("Apoyo Familiar", max_length=2, null=True, blank=True)
    var33 = models.CharField("Nivel Socioeconomico Bajo", max_length=2, null=True, blank=True)
    var34 = models.CharField("Ansiedad", max_length=2, null=True, blank=True)
    var35 = models.CharField("Grupo Poblacional Especial", max_length=30, null=True, blank=True)
    var36 = models.CharField("Victima Violencia Genero", max_length=2, null=True, blank=True)
    var37 = models.CharField("Riesgo Psicosocial", max_length=30, null=True, blank=True)
    var38 = models.CharField("Antecedente Hipertension Inducida por Embarazo", max_length=2, null=True, blank=True)
    var39 = models.CharField("Antecedente Placenta Previa", max_length=2, null=True, blank=True)
    var41 = models.CharField("Antecedente Peso Bebe Menor A 2500", max_length=2, null=True, blank=True)
    var42 = models.CharField("Antecedente Peso Bebe Mayor A 4000", max_length=2, null=True, blank=True)
    var43 = models.CharField("Antecedente Parto Pretermino", max_length=2, null=True, blank=True)
    var44 = models.CharField("Antecedente Trabajo Parto Prolongado", max_length=2, null=True, blank=True)
    var45 = models.CharField("Antecedente Fliar Preeclamsia", max_length=2, null=True, blank=True)
    var46 = models.CharField("Antecedente Gravida", max_length=2, null=True, blank=True)
    var47 = models.CharField("Antecedente Partos", max_length=2, null=True, blank=True)
    var48 = models.CharField("Antecedente Abortos", max_length=2, null=True, blank=True)
    var49 = models.CharField("Antecedente Tres Abortos Seguidos", max_length=2, null=True, blank=True)
    var51 = models.CharField("Antecedente Cesareas", max_length=2, null=True, blank=True)
    var52 = models.CharField("Antecedente Obito Fetal Muerte Perinatal", max_length=2, null=True, blank=True)
    var53 = models.CharField("Antecedente Embarazo Ectopico Recanalizacion", max_length=2, null=True, blank=True)
    var54 = models.CharField("Antecedente Embarazo Molar", max_length=2, null=True, blank=True)
    var55 = models.CharField("Antecedente_ Muerte_Neonatal_Tardia", max_length=2, null=True, blank=True)
    var56 = models.CharField("Tiene_VIH_Pregestacional", max_length=2, null=True, blank=True)
    var57 = models.CharField("Tiene_Epilepsia", max_length=2, null=True, blank=True)
    var58 = models.CharField("Tiene_Enfermedades_Autoinmunes", max_length=2, null=True, blank=True)
    var59 = models.CharField("Tiene_Diabetes_Mellitus", max_length=2, null=True, blank=True)
    var61 = models.CharField("Tiene_Enfermedad_Cardiaca", max_length=2, null=True, blank=True)
    var62 = models.CharField("Tiene_HTA_Cronica", max_length=2, null=True, blank=True)
    var63 = models.CharField("Tiene_Enfermedad_Renal_Cronica", max_length=2, null=True, blank=True)
    var64 = models.CharField("Embarazo_Actual_Enfermedades_Infecciosas", max_length=2, null=True, blank=True)
    var65 = models.CharField("Embarazo_Actual_Reproduccion_Asistida", max_length=2, null=True, blank=True)
    var66 = models.CharField("Embarazo_Actual_Anomalia_Congenita", max_length=2, null=True, blank=True)
    var67 = models.CharField("Embarazo_Actual_Hemorragia_Vaginal_", max_length=2, null=True, blank=True)
    var68 = models.CharField("Embarazo_Actual_Hemorragia_Vaginal", max_length=2, null=True, blank=True)
    var69 = models.CharField('Fecha_Terminacion_ultimo_Embarazo',max_length=10, null=True, blank=True)
    var71 = models.CharField('Fum Por Amenorrea',max_length=10, null=True, blank=True)
    var72 = models.CharField("Fum_Formula_Confiable", max_length=20, null=True, blank=True)
    var73 = models.CharField("Periodo Intergenesico", max_length=10, null=True, blank=True)
    var74 = models.CharField('Fum Por Eco',max_length=10, null=True, blank=True)
    var75 = models.CharField("Semanas Gestacion al Ingreso", max_length=10, null=True, blank=True)
    var76 = models.CharField("Trimestre Ingreso", max_length=10, null=True, blank=True)
    var77 = models.CharField("Semanas Gestacion Actualizadas", max_length=10, null=True, blank=True)
    var78 = models.CharField("Tipo Eco Uno", max_length=50, null=True, blank=True)
    var79 = models.CharField('Fecha Eco Uno',max_length=10, null=True, blank=True)
    var80 = models.CharField("Semanas Gestacion Eco Uno", max_length=10, null=True, blank=True)
    var81 = models.CharField("Tipo Eco Dos", max_length=50, null=True, blank=True)
    var82 = models.CharField('Fecha Eco Dos',max_length=10, null=True, blank=True)
    var83 = models.CharField("Semanas Gestacion Eco Dos", max_length=10, null=True, blank=True)
    var84 = models.CharField("Embarazo_Actual_Restriccion_Crecimiento", max_length=2, null=True, blank=True)
    var85 = models.CharField("Embarazo_Multiple_Actual", max_length=2, null=True, blank=True)
    var86 = models.CharField("Presentacion_Feto", max_length=15, null=True, blank=True)
    var87 = models.CharField("Polihidramnios", max_length=2, null=True, blank=True)
    var88 = models.CharField("Momento Peso al ingreso CPN", max_length=13, null=True, blank=True)
    var89 = models.CharField("Talla_Metros", max_length=5, null=True, blank=True)
    var90 = models.CharField("Peso_Kilogramos_Ingreso_Pregestacional", max_length=6, null=True, blank=True)
    var91 = models.CharField("IMC", max_length=6, null=True, blank=True)
    var92 = models.CharField("Clasificación_Nutricional_Ingreso", max_length=15, null=True, blank=True)
    var93 = models.CharField('Fecha_Ultimo_Control',max_length=10, null=True, blank=True)
    var94 = models.CharField("Peso_Kilogramos", max_length=4, null=True, blank=True)
    var95 = models.CharField("IMC_Ultimo_CPN", max_length=5, null=True, blank=True)
    var96 = models.CharField("Semanas_Gestacion_Ultimo_CPN", max_length=5, null=True, blank=True)
    var97 = models.CharField("Clasificacion_Curva_Atalah_Ultimo_CPN", max_length=20, null=True, blank=True)
    var98 = models.CharField("Altura_Uterina", max_length=5, null=True, blank=True)
    var99 = models.CharField("Alarma_ Altura_Uterina", max_length=30, null=True, blank=True)
    var100 = models.CharField("TA_Sistolica_Antes_Semana_Doce", max_length=4, null=True, blank=True)
    var101 = models.CharField("TA_Diastolica_Antes_Semana_Doce", max_length=4, null=True, blank=True)
    var102 = models.CharField("Alarma_Uno_TA_Antes_Doce_Semanas", max_length=50, null=True, blank=True)
    var103 = models.CharField("TA_Sistolica_Semana_Veinte_VeintiSeis", max_length=4, null=True, blank=True)
    var104 = models.CharField("TA_Diastolica_Semana_20 y 26", max_length=5, null=True, blank=True)
    var105 = models.CharField("Alarma_Dos_TA_Entre_Semana_20_A_Veintiseis", max_length=50, null=True, blank=True)
    var106 = models.CharField("TA_Sistolica_Sem_Treinta_A_TreintayCuatro", max_length=5, null=True, blank=True)
    var107 = models.CharField("TA_Diastolica_Sem_Treinta_A_TreintayCuatro", max_length=5, null=True, blank=True)
    var108 = models.CharField("Alarma_Tres_TA_Semana_Treinta_A_TreintayCuatro", max_length=50, null=True, blank=True)
    var109 = models.CharField("TA_Sistolica", max_length=5, null=True, blank=True)
    var110 = models.CharField("TA_Diastolica", max_length=5, null=True, blank=True)
    var111 = models.CharField("Alarma_TA_Mensual", max_length=50, null=True, blank=True)
    var112 = models.CharField("Fecha_Lactancia_Materna_Durante_CPN",max_length=10, null=True, blank=True)
    var113 = models.CharField("Fecha_Asesoria_Anticoncepcion_Durante_CPN",max_length=10, null=True, blank=True)
    var114 = models.CharField('Fecha_C2',max_length=10, null=True, blank=True)
    var115 = models.CharField('Fecha_C3',max_length=10, null=True, blank=True)
    var116 = models.CharField('Fecha_C4',max_length=10, null=True, blank=True)
    var117 = models.CharField('Fecha_C5',max_length=10, null=True, blank=True)
    var118 = models.CharField('Fecha_C6',max_length=10, null=True, blank=True)
    var119 = models.CharField('Fecha_C7',max_length=10, null=True, blank=True)
    var120 = models.CharField('Fecha_C8',max_length=10, null=True, blank=True)
    var121 = models.CharField('Fecha_C9',max_length=10, null=True, blank=True)
    var122 = models.CharField('Fecha_C10',max_length=10, null=True, blank=True)
    var123 = models.CharField('Fecha_C11',max_length=10, null=True, blank=True)
    var124 = models.CharField('Fecha_C12',max_length=10, null=True, blank=True)
    var125 = models.CharField('Fecha_C13',max_length=10, null=True, blank=True)
    var126 = models.CharField("Curso_Maternidad_Paternidad", max_length=2, null=True, blank=True)
    var127 = models.CharField('Fecha_Concentracion_Plan_Parto', max_length=2, null=True, blank=True)
    var128 = models.CharField("Acuerdo_Posible_Lugar_Nacimiento", max_length=50, null=True, blank=True)
    var129 = models.CharField("Alerta_Plan_Parto", max_length=15, null=True, blank=True)
    var130 = models.CharField("Gestante_Actuales", max_length=20, null=True, blank=True)
    var131 = models.CharField("Cita_Proximo_Control", max_length=20, null=True, blank=True)
    var132 = models.CharField("Alerta_Seguiimiento", max_length=20, null=True, blank=True)
    var133 = models.CharField('Fecha_Ultimo_CPN',max_length=10, null=True, blank=True)
    var134 = models.CharField("Edad_Gestacional_Ultimo_CPN", max_length=5, null=True, blank=True)
    var135 = models.CharField("Total_Controles", max_length=2, null=True, blank=True)
    var136 = models.CharField("Adherencia_al_CPN", max_length=2, null=True, blank=True)
    var137 = models.CharField("Controles_Programados", max_length=4, null=True, blank=True)
    var138 = models.CharField("Porcentaje_Cumplimiento_Individual", max_length=5, null=True, blank=True)
    var139 = models.CharField("Fecha_Remision_Psicologia",max_length=10, null=True, blank=True)
    var140 = models.CharField('Fecha_Asistencia_Consulta_Psicologia',max_length=10, null=True, blank=True)
    var141 = models.CharField('Fecha_Remision_Nutricion',max_length=10, null=True, blank=True)
    var142 = models.CharField('Fecha_Asistencia_Consulta_Nutricion',max_length=10, null=True, blank=True)
    var143 = models.CharField('Fecha_Remision_Ginecologo',max_length=10, null=True, blank=True)
    var144 = models.CharField('Fecha_Asistencia_Primera_Vez_Ginecologia',max_length=10, null=True, blank=True)
    var145 = models.CharField('Fecha_Ultima_Asistencia_Consulta_Gineco',max_length=10, null=True, blank=True)
    var146 = models.CharField("Numero_Consultas_Ginecologo", max_length=10, null=True, blank=True)
    var147 = models.CharField("Resultado_Hemogl Antes_Tercer_Trimestre", max_length=5, null=True, blank=True)
    var148 = models.CharField('Fecha_Resultado_HB',max_length=10, null=True, blank=True)
    var149 = models.CharField("Edad_Gestacional_HB", max_length=4, null=True, blank=True)
    var150 = models.CharField("Conducta_Hemoglobina", max_length=50, null=True, blank=True)
    var151 = models.CharField("Trimestre_Gestacion_Toma_Examen", max_length=10, null=True, blank=True)
    var152 = models.CharField("Resultado_Hemoglobina_Semana_Veintiocho", max_length=6, null=True, blank=True)
    var153 = models.CharField('Fecha_Resultado_HB_Semana_Veintiocho',max_length=10, null=True, blank=True)
    var154 = models.CharField("Edad_Gestacional_HB_Semana_Veintiocho", max_length=5, null=True, blank=True)
    var155 = models.CharField("Conducta_Hemoglobina_Diez", max_length=50, null=True, blank=True)
    var156 = models.CharField("Resultado_Hemoclasificacion_RH_Riesgo_", max_length=20, null=True, blank=True)
    var157 = models.CharField('FECHA RESULTADO DE HEMOCL',max_length=10, null=True, blank=True)
    var158 = models.CharField('Fecha_Aplicación_Rhesuman',max_length=10, null=True, blank=True)
    var159 = models.CharField("Edad_Gestacional_Hemoclasificacion_RH", max_length=5, null=True, blank=True)
    var160 = models.CharField("Observacion_Resultado_De_Hemoclasificacion_RH_", max_length=50, null=True, blank=True)
    var161 = models.CharField("Glicemia_Pre", max_length=5, null=True, blank=True)
    var162 = models.CharField('Fecha_Glicemia',max_length=10, null=True, blank=True)
    var163 = models.CharField("Edad_Gestacional_Glicemia", max_length=5, null=True, blank=True)
    var164 = models.CharField("PTOG_Carga_SeteintayCinco_Pre_Valor", max_length=10, null=True, blank=True)
    var165 = models.CharField("PTOG_Carga_SeteintayCinco_Uno_Hora_Valor", max_length=10, null=True, blank=True)
    var166 = models.CharField("PTOG_Carga_SeteintayCinco_Dos_Hora_Valor", max_length=10, null=True, blank=True)
    var167 = models.CharField("PTOG_Carga_SeteintayCinco_Resultado", max_length=30, null=True, blank=True)
    var168 = models.CharField('Fecha_Toma_Examen_PTOG',max_length=10, null=True, blank=True)
    var169 = models.CharField("Edad_Gestacional_PTOG", max_length=6, null=True, blank=True)
    var170 = models.CharField("Tamizaje_Para_Sifilis_Segun_GPC_Sifilis_", max_length=30, null=True, blank=True)
    var171 = models.CharField('Fecha_Resultado_Primer_Trimestre',max_length=10, null=True, blank=True)
    var172 = models.CharField("Alarma_Tamizaje_Sifilis_Primer_Trimestre", max_length=7, null=True, blank=True)
    var173 = models.CharField("Tamizaje_Sifilis_Segun_GPC_Sifilis_Segundo_Trimestre", max_length=40, null=True, blank=True)
    var174 = models.CharField('Fecha_Resultado_PR_Segundo_Trimestre',max_length=10, null=True, blank=True)
    var175 = models.CharField("Alarma_Tamizaje_Sifilis_Segundo_Trimestre_", max_length=6, null=True, blank=True)
    var176 = models.CharField("Tamizaje_Sifilis_Segun_GPC_Sifilis_Tercer_", max_length=50, null=True, blank=True)
    var177 = models.CharField('Fecha_Resultado_PR_Tercer_Trimestre',max_length=10, null=True, blank=True)
    var178 = models.CharField("Alarma_Tamizaje_Sifilis_Tercer_Trimest", max_length=25, null=True, blank=True)
    var179 = models.CharField("Tamizaje_Sifilis_Segun_GPC_Sifilis_", max_length=40, null=True, blank=True)
    var180 = models.CharField('Fecha_Resultado_PR_Intraparto',max_length=10, null=True, blank=True)
    var181 = models.CharField("Alarma_Consolidada_Casos_Sifilis_", max_length=50, null=True, blank=True)
    var182 = models.CharField("Resultado_Urocultivo", max_length=20, null=True, blank=True)
    var183 = models.CharField('Fecha_Resultado_Urocultivo',max_length=10, null=True, blank=True)
    var184 = models.CharField("Edad_Gestacional_Uroculltivo", max_length=6, null=True, blank=True)
    var185 = models.CharField("Tamizaje_VIH_Primer_Trimestre", max_length=40, null=True, blank=True)
    var186 = models.CharField('Fecha_Resultado_Tamizaje_VIH_Primer_Trimestre',max_length=10, null=True, blank=True)
    var187 = models.CharField("Alarma_Tamizaje_VIH_Primer_Trimestre", max_length=30, null=True, blank=True)
    var188 = models.CharField("Tamizaje_VIH_Segundo_Trimestre", max_length=30, null=True, blank=True)
    var189 = models.CharField('Fecha_Resultado_Tamizaje_VIH_Segundo_',max_length=10, null=True, blank=True)
    var190 = models.CharField("Alarma_Tamizaje_VIH_Segundo_Trimestre", max_length=50, null=True, blank=True)
    var191 = models.CharField("Tamizaje_VIH_Tercer_Trimestre", max_length=30, null=True, blank=True)
    var192 = models.CharField('Fecha_Resultado_Tamizaje_VIH_Tercer_',max_length=10, null=True, blank=True)
    var193 = models.CharField("Alarma_Tamizaje_VIH_Tercer_Trimestre", max_length=30, null=True, blank=True)
    var194 = models.CharField("Tamizaje_VIH_Intraparto_Segun_GPC", max_length=30, null=True, blank=True)
    var195 = models.CharField('Fecha_Resultado_Tamizaje_Intraparto',max_length=10, null=True, blank=True)
    var196 = models.CharField("Segunda_Prueba_PR_Definir_Diagnostico_VIH_Segun_", max_length=30, null=True, blank=True)
    var197 = models.CharField('Fecha_Resultado_Segunda_Prueba_Elisa_PR_Definir_',max_length=10, null=True, blank=True)
    var198 = models.CharField("Resultado_Carga_Viral_Segun_Protocolo_INS", max_length=50, null=True, blank=True)
    var199 = models.CharField('Fecha_Resultado_Carga_Viral_Segun_Protocolo_INS',max_length=10, null=True, blank=True)
    var200 = models.CharField("Resultado_HEP_B_Antigeno_Sperficie", max_length=30, null=True, blank=True)
    var201 = models.CharField('Fecha_Resultado_HASB',max_length=10, null=True, blank=True)
    var202 = models.CharField("Edad_Gestacional_Dieciocho", max_length=6, null=True, blank=True)
    var203 = models.CharField("Resultado_Toxoplasma_IgG", max_length=20, null=True, blank=True)
    var204 = models.CharField("Resultado_Confir_Toxoplasma_IgM", max_length=20, null=True, blank=True)
    var205 = models.CharField("Alarma_Toxoplasmosis", max_length=35, null=True, blank=True)
    var206 = models.CharField('Fecha_Resultado_Toxo',max_length=10, null=True, blank=True)
    var207 = models.CharField("Edad_Gestacional_Veinituno", max_length=6, null=True, blank=True)
    var208 = models.CharField("Trimestre_Gestacion_Toma_Examen_CincuentayDos", max_length=10, null=True, blank=True)
    var209 = models.CharField("Resultado_Toxoplasmosis_Ultimo_IgM_Si_", max_length=20, null=True, blank=True)
    var210 = models.CharField("Numero_Veces_Toma_Toxoplasma_IgM_Control", max_length=10, null=True, blank=True)
    var211 = models.CharField("Resultado_Ultima_Citologia", max_length=40, null=True, blank=True)
    var212 = models.CharField("Tamizaje_Para_Chagas", max_length=70, null=True, blank=True)
    var213 = models.CharField('Fecha_Resultado_Tamizaje_Chagas',max_length=10, null=True, blank=True)
    var214 = models.CharField("Tamizaje_Inicial_Gota_Gruesa_Malaria", max_length=70, null=True, blank=True)
    var215 = models.CharField('Fecha_Resultado_Tamizaje_Inicial_Gota_Gruesa',max_length=10, null=True, blank=True)
    var216 = models.CharField("Resultado_Ultimo_Tamizaje_Gota_Gruesa", max_length=70, null=True, blank=True)
    var217 = models.CharField("Numero_Tamizajes_Tomados_Gota_Gruesa_Malaria", max_length=10, null=True, blank=True)
    var218 = models.CharField("Diagnostico_Positivo_Covid_Infeccion_SARS", max_length=50, null=True, blank=True)
    var219 = models.CharField("Enfermedades_Propias_Culturales", max_length=70, null=True, blank=True)
    var220 = models.CharField("Otros_Factores_Riesgo", max_length=70, null=True, blank=True)
    var221 = models.CharField("Riesgo_Biopsicosocial", max_length=40, null=True, blank=True)
    var222 = models.CharField("Motivos_Clasificacion_Riesgo_Biopsicosocial", max_length=70, null=True, blank=True)
    var223 = models.CharField("Alarma_Factores_Riesgo_Complicaciones_", max_length=40, null=True, blank=True)
    var224 = models.CharField("Alarma_Seguimiento_Cifras_Presion_Arterial_", max_length=50, null=True, blank=True)
    var225 = models.CharField("Alerta_Seguimiento_Dos", max_length=50, null=True, blank=True)
    var226 = models.CharField("Gestantes_Actuales_VeintiDos", max_length=50, null=True, blank=True)
    var227 = models.CharField("Clasificacion_Riesgo_Adecuada", max_length=2, null=True, blank=True)
    var228 = models.CharField("Suministro_ASA_Segun_GPC", max_length=20, null=True, blank=True)
    var229 = models.CharField('Fecha_Inicio_Suministro_ASA',max_length=10, null=True, blank=True)
    var230 = models.CharField("Alerta_Suministro_ASA", max_length=30, null=True, blank=True)
    var231 = models.CharField('Fecha_Inicio_Suministro_Calcio',max_length=10, null=True, blank=True)
    var232 = models.CharField("Suministro_Calcio", max_length=50, null=True, blank=True)
    var233 = models.CharField('Fecha_Inicio_Suministro_Acido_Folico',max_length=10, null=True, blank=True)
    var234 = models.CharField("Suministro_Acido_Folico", max_length=35, null=True, blank=True)
    var235 = models.CharField('Fecha_Inicio_Suministro_Sulfato_Ferroso',max_length=10, null=True, blank=True)
    var236 = models.CharField("Suministro_Sulfato_Ferroso", max_length=50, null=True, blank=True)
    var237 = models.CharField('Fecha_Consulta_Primera_Vez_Odontologia',max_length=10, null=True, blank=True)
    var238 = models.CharField("Semanas de gestacion al cnslta odontol", max_length=50, null=True, blank=True)
    var239 = models.CharField("Manejo_Odontologico_Durante_Gestacion", max_length=2, null=True, blank=True)
    var240 = models.CharField("Vacunacion_Covid", max_length=30, null=True, blank=True)
    var241 = models.CharField('Fecha_Vacuna_Anti_Influenza',max_length=10, null=True, blank=True)
    var242 = models.CharField("Fecha_Vacuna_DPT_Acelular", max_length=50, null=True, blank=True)
    var243 = models.CharField("Alarma_DPT_Acelular", max_length=50, null=True, blank=True)
    var244 = models.CharField('Fecha_Vacuna_TD',max_length=10, null=True, blank=True)
    var245 = models.CharField('FPP2',max_length=10, null=True, blank=True)
    var246 = models.CharField("Días_Parto_Dos", max_length=7, null=True, blank=True)
    var247 = models.CharField("Alerta_Parto_Tres", max_length=30, null=True, blank=True)
    var248 = models.CharField('Fecha_Ultima_Remision_URG',max_length=10, null=True, blank=True)
    var249 = models.CharField("Sale_Programa_Por", max_length=25, null=True, blank=True)
    var250 = models.CharField("Eventos_Interes_Salud_Publica_Madre", max_length=50, null=True, blank=True)
    var251 = models.CharField("Eventos_Interes_Salud_Publica_RecienNacido", max_length=60, null=True, blank=True)
    var252 = models.CharField('Fecha_Salida_Programa',max_length=10, null=True, blank=True)
    var253 = models.CharField("Lugar_Atencion_Parto", max_length=20, null=True, blank=True)
    var254 = models.CharField("Edad_Gestacional_Salida_Programa", max_length=6, null=True, blank=True)
    var255 = models.CharField("Nombre_Institucion_Atendio_Parto", max_length=80, null=True, blank=True)
    var256 = models.CharField("Nivel_Complejidad_Atencion_Institucion_Atencion", max_length=15, null=True, blank=True)
    var257 = models.CharField("Profesional_Atencion_Parto", max_length=50, null=True, blank=True)
    var258 = models.CharField("Inicio_Trabajo_Parto", max_length=50, null=True, blank=True)
    var259 = models.CharField("Acompañamiento_Persona_Confianza_Durante", max_length=10, null=True, blank=True)
    var260 = models.CharField("Diligenciamiento_Partograma", max_length=10, null=True, blank=True)
    var261 = models.CharField("Manejo_Activo_Tercer_Periodo_Parto", max_length=10, null=True, blank=True)
    var262 = models.CharField("Contacto_Piel_A_Piel", max_length=10, null=True, blank=True)
    var263 = models.CharField("Inicio_Lactancia_Materna_Durante_Contacto", max_length=10, null=True, blank=True)
    var264 = models.CharField("Monitoria_Cada_Quince_Minutos_Signos_Vitales", max_length=10, null=True, blank=True)
    var265 = models.CharField("Complicaciones_Postparto", max_length=30, null=True, blank=True)
    var266 = models.CharField("Numero_Nacidos_Vivos", max_length=12, null=True, blank=True)
    var267 = models.CharField("Sexo_RN", max_length=12, null=True, blank=True)
    var268 = models.CharField("Peso_RN_Gramos", max_length=12, null=True, blank=True)
    var269 = models.CharField("Peso_Nacer", max_length=50, null=True, blank=True)
    var270 = models.CharField('Fecha_Toma_TSH',max_length=10, null=True, blank=True)
    var271 = models.CharField("Resultado_TSH", max_length=10, null=True, blank=True)
    var272 = models.CharField('Fecha_Resultado_TSH',max_length=10, null=True, blank=True)
    var273 = models.CharField("Aplicacion_VIT_K", max_length=10, null=True, blank=True)
    var274 = models.CharField("Grupo_Sanguineo_RN", max_length=4, null=True, blank=True)
    var275 = models.CharField('Fecha_Aplicacion_Vacuna_HepatitisB',max_length=10, null=True, blank=True)
    var276 = models.CharField('Fecha_Aplicacion_Vacuna_BCG',max_length=10, null=True, blank=True)
    var277 = models.CharField("Sexo_RN_Dos", max_length=20, null=True, blank=True)
    var278 = models.CharField("Peso_RN_Dos", max_length=50, null=True, blank=True)
    var279 = models.CharField("Peso_Nacer_Edad_Gestacional_RN_Dos", max_length=35, null=True, blank=True)
    var280 = models.CharField('Fecha_Toma_TSH_Dos',max_length=10, null=True, blank=True)
    var281 = models.CharField("Resultado_TSH_Dos", max_length=10, null=True, blank=True)
    var282 = models.CharField('Fecha_Resultado_TSH_Dos1',max_length=10, null=True, blank=True)
    var283 = models.CharField("Aplicacion_VIT_K_Dos", max_length=10, null=True, blank=True)
    var284 = models.CharField("Grupo_Sanguineo_RN_Dos", max_length=10, null=True, blank=True)
    var285 = models.CharField('Fecha_Resultado_TSH_Dos',max_length=10, null=True, blank=True)
    var286 = models.CharField('Fecha_Aplicacion_Vacuna_BCG_Dos',max_length=10, null=True, blank=True)
    var287 = models.CharField('Control_RN_Fecha_Asistio',max_length=2, null=True, blank=True)
    var288 = models.CharField("Alarma_Uno_Control_RN", max_length=25, null=True, blank=True)
    var289 = models.CharField('Control_Puerperio_Fecha',max_length=10, null=True, blank=True)
    var290 = models.CharField("Alarma_Control_Puerperio", max_length=25, null=True, blank=True)
    var291 = models.CharField("Asesoria_Lactancia_Materna_Exlusiva_", max_length=10, null=True, blank=True)
    var292 = models.CharField("Asesoria_Planificacion_Familiar_PostEvento_", max_length=10, null=True, blank=True)
    var293 = models.CharField("Puerpera_Planificacion_Familiar_PostEvento_", max_length=10, null=True, blank=True)
    var294 = models.CharField('Fecha_Inscripcion_Planificacion_Familiar_Dos',max_length=10, null=True, blank=True)
    var295 = models.CharField("Metodo_Anticonceptivo_Inciado_Postparto", max_length=50, null=True, blank=True)
    var296 = models.CharField("Tipo_Apoyo_Realizado_Por_EPS", max_length=20, null=True, blank=True)
    var297 = models.CharField("Tipo_Apoyo_Realizado_Por_IPS_Primaria", max_length=30, null=True, blank=True)
    var298 = models.CharField('Fecha_Seguimiento_Inicial_Por_Personal_Salud_Terreno',max_length=10, null=True, blank=True)
    var299 = models.CharField('Fecha_Ultimo_Seguimiento',max_length=10, null=True, blank=True)
    var300 = models.CharField("Numero_Seguimientos_CPN", max_length=15, null=True, blank=True)
    var301 = models.TextField("Hallazgo_Gestacion_Seguimiento_Visita_Domiciliaria", null=True, blank=True)
    var302 = models.CharField('Fecha_Seguimientos_Telefonicos',max_length=2, null=True, blank=True)
    var303 = models.CharField("Numero_Seguimientos_Telefonicos", max_length=20, null=True, blank=True)
    var304 = models.TextField("Observacion_Seguimientos_Telefonicos", null=True, blank=True)
    var305 = models.CharField('Fecha_Seguimiento_Personal_Salud_Terreno_Puerperio',max_length=10, null=True, blank=True)
    var306 = models.TextField("Hallazgos_Acompañamiento_Personal_Salud__Puerpera", null=True, blank=True)
    var307 = models.TextField("Hallazgos_Acompañamiento_Personal_Salud__", null=True, blank=True)
    var308 = models.CharField('Fecha_Ultimo_Seguimiento_Personal_Salud_Terreno',max_length=10, null=True, blank=True)
    var309 = models.CharField("Numero_Seguimiento_Puerperio", max_length=10, null=True, blank=True)
    var310 = models.CharField('Fecha_Primer_Acompañamiento_SabedorAncestral',max_length=10, null=True, blank=True)
    var311 = models.CharField("Tipo_Sabedor", max_length=30, null=True, blank=True)
    var312 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Uno", max_length=50, null=True, blank=True)
    var313 = models.TextField("Actividad_Ritualidad_Realizada_Uno", null=True, blank=True)
    var314 = models.CharField('Fecha_Acompañamiento_Sabedor_Ancestral_Dos',max_length=10, null=True, blank=True)
    var315 = models.CharField("Tipo_Sabedor_Dos", max_length=20, null=True, blank=True)
    var316 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Dos", max_length=50, null=True, blank=True)
    var317 = models.TextField("Actividad_Ritualidad_Realizada_Dos", null=True, blank=True)
    var318 = models.CharField('Fecha_Acompañamiento_Sabedor_Ancestral_Tres',max_length=10, null=True, blank=True)
    var319 = models.CharField("Tipo_Sabedor_Tres", max_length=30, null=True, blank=True)
    var320 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Tres", max_length=25, null=True, blank=True)
    var321 = models.TextField("Actividad_Ritualidad_Realizada_Cuatro", null=True, blank=True)
    var322 = models.CharField('Fecha_Acompañamiento_Sabedor_Ancestral_Cuatro',max_length=10, null=True, blank=True)
    var323 = models.CharField("Tipo_Sabedor_Cuatro", max_length=30, null=True, blank=True)
    var324 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Cuatro", max_length=50, null=True, blank=True)
    var325 = models.TextField("Actividad_Ritualidad_Realizada_Cinco", null=True, blank=True)
    var326 = models.CharField('Fecha_Acompañamiento_Sabedor_Ancestral_Cinco',max_length=10, null=True, blank=True)
    var327 = models.CharField("Tipo_Sabedor_Cinco", max_length=30, null=True, blank=True)
    var328 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Cinco", max_length=50, null=True, blank=True)
    var329 = models.TextField("Actividad_Ritualidad_Realizada_Seis", null=True, blank=True)
    var330 = models.CharField('Fecha_Acompañamiento_Sabedor_Ancest',max_length=10, null=True, blank=True)
    var331 = models.CharField("Tipo_Sabedor_Seis", max_length=30, null=True, blank=True)
    var332 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Seis", max_length=50, null=True, blank=True)
    var333 = models.TextField("Actividad_Ritualidad_Realizada_Siete", null=True, blank=True)
    var334 = models.CharField('Fecha_Acompañamiento_Sabedor_Puerperio',max_length=10, null=True, blank=True)
    var335 = models.CharField("Tipo_Sabedor_Siete", max_length=30, null=True, blank=True)
    var336 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Siete", max_length=50, null=True, blank=True)
    var337 = models.TextField("Actividad_Ritualidad_Realizada_Ocho", null=True, blank=True)
    var338 = models.CharField('Fecha_Acompañamiento_Sabedor_Puerperio22',max_length=10, null=True, blank=True)
    var339 = models.CharField("Tipo_Sabedor_Ocho", max_length=30, null=True, blank=True)
    var340 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Ocho", max_length=50, null=True, blank=True)
    var341 = models.TextField("Actividad_Ritualidad_Realizada_Nueve", null=True, blank=True)
    var342 = models.CharField('Fecha_Acompañamiento_Sabedor_Ancestral1',max_length=10, null=True, blank=True)
    var343 = models.CharField("Tipo_Sabedor_Nueve", max_length=30, null=True, blank=True)
    var344 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Nueve", max_length=50, null=True, blank=True)
    var345 = models.TextField("Actividad_Ritualidad_Realizada_Diez", null=True, blank=True)
    var346 = models.CharField('Fecha_Acompañamiento_Sabedor_Ancestral',max_length=10, null=True, blank=True)
    var347 = models.CharField("Tipo_Sabedor_Diez", max_length=30, null=True, blank=True)
    var348 = models.CharField("Necesidad_Desarmonia_Desde_Lo_Propio_Diez", max_length=50, null=True, blank=True)
    var349 = models.TextField("Actividad_Ritualidad_Realizada_Once", null=True, blank=True)
    mensual = models.ForeignKey(CargueMensual, on_delete=models.CASCADE, related_name='informacion_gestantes')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    objects = models.Manager()

