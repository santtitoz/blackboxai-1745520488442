# Sistema de Biblioteca Django

Um projeto Django simples para demonstrar operações CRUD usando o Django ORM.

## Estrutura do Projeto

O projeto contém dois modelos principais:
- **Autor**: Armazena informações sobre autores
- **Livro**: Armazena informações sobre livros

## Funcionalidades

- Cadastro de autores e livros
- Listagem de autores e livros
- Edição de registros
- Exclusão de registros
- Interface administrativa Django

## Como Usar

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Inicie o servidor:
```bash
python manage.py runserver
```

7. Acesse o admin em: http://localhost:8000/admin

## Exemplos de Uso do ORM Django

Abra o shell do Django:
```bash
python manage.py shell_plus
```

### Criar um Autor
```python
autor = Author.objects.create(
    name='Nome do Autor',
    email='autor@email.com'
)
```

### Criar um Livro
```python
from datetime import date

livro = Book.objects.create(
    title='Título do Livro',
    author=autor,
    description='Descrição do livro',
    published_date=date.today(),
    is_available=True
)
```

### Consultas Básicas
```python
# Listar todos os autores
Author.objects.all()

# Buscar autor por email
Author.objects.get(email='autor@email.com')

# Listar livros disponíveis
Book.objects.filter(is_available=True)

# Buscar livros de um autor específico
autor.books.all()  # usando related_name
# ou
Book.objects.filter(author=autor)
```

### Atualizar Registros
```python
livro.title = 'Novo Título'
livro.save()

# ou
Book.objects.filter(id=1).update(title='Novo Título')
```

### Deletar Registros
```python
livro.delete()
# ou
Book.objects.filter(id=1).delete()
```

## Campos dos Modelos

### Autor (Author)
- name: Nome do autor (CharField)
- email: E-mail do autor (EmailField, único)
- created_at: Data de criação (DateTimeField, automático)

### Livro (Book)
- title: Título do livro (CharField)
- author: Autor do livro (ForeignKey -> Author)
- description: Descrição do livro (TextField)
- published_date: Data de publicação (DateField)
- is_available: Disponibilidade (BooleanField)
- created_at: Data de criação (DateTimeField, automático)
- updated_at: Data de atualização (DateTimeField, automático)
