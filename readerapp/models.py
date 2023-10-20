from django.db import models
# El error /Import "ckeditor.fields" could not be resolved/ se debe
# a que visual estudio no está corriendo con el venv.
# Ckeditor está instalado en el venv. No hay pués que preocuparse por
# este error.
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify

# Para la generación de pdf
#from io import BytesIO
#from django.core.files import File
#from .utils import render_to_pdf


# Create your models here.


class Slug(models.Model):
    slug = models.SlugField(verbose_name=u'URL amigable', unique=True, blank=True, max_length=255)

    def __str__(self):
        return str(self.slug)

'''
class Category(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
'''
    
class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Etiquetas')
    parent = models.ForeignKey(
        "self",
        related_name="subcategories",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Padre',
    )

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    #def __str__(self):
    #    return self.name
    
    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
 

STATUS_CHOICES = (('NR', 'No revisada'), ('BR', 'Bronce'), ('PL', 'Plata'), ('OR', 'Oro'))
#SOURCES_STATE_CHOICES = (('I', 'Incompleta'), ('C', 'Completa'))

class Article(models.Model):

    # INFORMACIÓN BÁSICA
    title = models.CharField(max_length=34, verbose_name='Título')
    old_cod = models.IntegerField(unique=True, verbose_name='Referencia antigua', null=True, blank=True, help_text="Dejar en blanco en caso de no tener número de referencia antigua.")
    new_cod = models.DateField(verbose_name='Referencia (Fecha)', unique=True)
    
    cuerpo = RichTextUploadingField(verbose_name='Cuerpo')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='No revisada', verbose_name='Estado de revisión')
    abstract = RichTextUploadingField(verbose_name='Resumen', blank=True, null=True)
    categories = models.ManyToManyField(Category, verbose_name='Etiquetas', default='Sin etiquetas', blank=True)
    #etiquetas = models.ManyToManyField(Etiqueta)
    #etiquetas = models.CharField()
    #audio

    # INFORMACIÓN SOBRE LAS FUENTES
    transcriber = models.CharField(verbose_name='Trascriptor', max_length=255, null=True, blank=True)
    transcrip_info = models.TextField(verbose_name='Formato del texto original', blank=True, help_text='Digital/Papel, otras observaciones')
    recording_info = models.TextField(verbose_name='Información sobre la grabación', null=True, blank=True)
    #sources_state = models.CharField(max_length=10, choices=SOURCES_STATE_CHOICES, default='Incompleta', verbose_name='Información sobre las fuentes')

    # OTROS
    comments = models.TextField(verbose_name='Observaciones', null=True, blank=True)
    revision_log = models.TextField(verbose_name='Historial de revisiones', blank=True, default='Autor (acciones); Fecha (dd/mm/aaaa)')
    
    created = models.DateField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateField(auto_now_add=True, verbose_name='Actualizado')
    slug = models.OneToOneField(Slug, verbose_name=u'URL amigable', blank=True, null=True, editable=False, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.id and self.slug_id == None:
            try:
                id = self.__class__.objects.latest("id").id + 1
            except:
                id = 1
            slug = Slug(slug=slugify(self.title))
            qs = Slug.objects.filter(slug=slug)
            if qs.exists():
                slug = Slug(slug=slugify(self.title)+"-%s" % str(id))
            else:
                slug = Slug(slug=slugify(self.title))
            slug.save()
                
            self.slug = slug
        super(Article, self).save( *args, **kwargs)

    class Meta:
        verbose_name = 'tertulia'
        verbose_name_plural = 'tertulias'

    def __str__(self):
        return self.title