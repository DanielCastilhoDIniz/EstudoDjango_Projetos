
# Projetos em  Django
### Preparação
#### Guide to getting started with Django project.
1. *Criar repositório no gitHub*
 - conectar o git ao gitHub (usar chaves SSH)
```bash
    $ git init
    $ git remote add origin <SSH key>
    $ git remote -v
    $ git add .
    $ git pull --rebase origin main
    $ git status
    $ git push
```
em caso de problemas [acesse](https://github.com/settings/keys).
***

2. *Atualização do python e suas ferramentas.*
   Para ver a versão do python use: ```$ python --version ```
- Atualizando e instalando ferramentas:
   - **pip**  ie o gerenciador de pacotes Python padrão. Ele permite que você instale e gerencie pacotes adicionais que não são parte da biblioteca padrão do Python.
   
   - **setuptools** é uma biblioteca em Python que facilita o download, a construção, a instalação, o upgrade e a desinstalação de pacotes Python.

    - **wheel** é um formato de pacote binário para Python, que permite a distribuição de pacotes de software de maneira pré-compilada. Isso é uma vantagem sobre o formato tradicional de pacote de código-fonte, o sdist, que exige que o usuário final tenha todas as ferramentas necessárias para compilar o software a partir do código-fonte, além das dependências Python necessárias.

    ```bash
        $ python -m pip install pip setuptools wheel --upgrade
    ```
- Criar ambiente vitual:
    ```bash
        $ python -m venv venv
    ```
   ativar o ambiente virtual:
    ```bash
        $ . venv/scripts/activate
    ```

## Django overview

<img src=https://pt-static.z-dn.net/files/d72/7207e1c558cab223c1277de1b956acf7.png>

  1. Um navegador web solicita uma página por sua URL e o servidor web passa a requisição HTTP para o Django.
  2. O Django percorre seus padrões de URL configurados e para no primeiro que corresponde ao
  URL solicitado.
  1. O Django executa a visualização que corresponde ao padrão de URL correspondente.
  2. A exibição potencialmente usa modelos de dados para recuperar informações do banco de dados.
  3. Os modelos de dados fornecem a definição de dados e os comportamentos. Eles são usados para consultar o banco de dados.
  4. A visualização renderiza um modelo (geralmente HTML) para exibir os dados e os retorna com um HTTP
  resposta.
1. *Instalação do Django*
    ```bash
        $ pip install django
    ```
    verificar versão:
    ```bash
        $ python -m django --version
    ```
    Iniciando um projeto. 
    ```bash
        $ django-admin startproject nameproject .
    ```
    criando uma app:
    ```bash
        $ python manage.py startapp nameapp
    ```
    No arquivo ```settings.py``` adicionar o app criado :

    ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'nameapp' # nome do app criado
            ]
    ```
    criar na pasta nameapp um arqurivo ```urls.py ``` e inserir:

    ```python
    from django.urls import path
    from recipes.views import sobre, home, contato

    urlpatterns = [
        path('', home), # exemplo de views criada
        path('sobre/', sobre),
        path('contato/', contato),
    ]
    ```
    Em seguida na pasta nameproject no em ```urls.py ``` adicionar:

    ```python
        from django.contrib import admin
        from django.urls import path, include # include adiconado

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('nameapp.urls')), # adiciona as rotas dentro da pasta nameapp
        ]
    ```
    Para evitar colisões de nomes crie na pasta ```nameapp``` uma pasta chamada ```templates``` com uma subpasta ```nameapp```
            
        C:\nameproject\nameapp\templates\nameapp