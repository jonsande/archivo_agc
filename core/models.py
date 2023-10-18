from django.db import models

# Create your models here.

class HomeConfig(models.Model):
    titulo = models.TextField(max_length=48, null=False, blank=False, default='Archivo de Tertulias de ¿Agustín García Calvo?')
    subtitulo = models.TextField(max_length=64, null=False, blank=False, default='Bienvenidos al Archivo de Tertulias de Agustín García Calvo')
    texto_portada = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Texto de bienvenida', default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam at tempor lectus. Etiam pharetra, sem a sagittis blandit, tortor odio euismod risus, eu tristique est nisi id sem. Pellentesque sodales est a diam aliquet commodo. Duis lobortis ante nec eros luctus, a lacinia dolor feugiat. Fusce sollicitudin, felis tempus placerat imperdiet, turpis lacus placerat justo, eu ullamcorper lacus metus ut felis. Aenean fringilla et tortor at rutrum. Etiam at est eget nunc accumsan sagittis in vel orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin quis hendrerit tortor.")

    class Meta:
        verbose_name = 'Configuración de la página web'
        verbose_name_plural = 'Configuración de la página web'
    
    def __str__(self):
        #return self.titulo
        return "Página de inicio"
    
    
    """
    Un enfoque efectivo para convertir el modelo en un singleton. 
    Al sobrescribir los métodos save y delete y forzar el pk a 1, 
    aseguras que solo exista una instancia de HomeConfig en la base 
    de datos, y así evitas la creación de instancias adicionales desde 
    el panel de administración de Django.
    """
    def save(self, *args, **kwargs):
        self.pk = 1
        super(HomeConfig, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj