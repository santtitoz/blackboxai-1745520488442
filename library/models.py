from django.db import models

class Author(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['name']

class Book(models.Model):
    title = models.CharField('Título', max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Autor',
        related_name='books'
    )
    description = models.TextField('Descrição', blank=True)
    published_date = models.DateField('Data de Publicação')
    is_available = models.BooleanField('Disponível', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author.name}"

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['-created_at']
