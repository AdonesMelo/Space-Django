# 🚀 Alura Space

Aplicação web desenvolvida com **Django 5.2** para gerenciamento de uma galeria de fotografias do espaço. O projeto permite que usuários se cadastrem, façam login e naveguem por uma coleção de imagens astronômicas organizadas por categorias como Nebulosa, Estrela, Galáxia e Planeta.

---

## 📋 Funcionalidades

### 🔐 Autenticação de Usuários
- **Cadastro** de novos usuários com validação de formulário (nome sem espaços, confirmação de senha)
- **Login** e **Logout** com sistema de mensagens de feedback
- Proteção de rotas — apenas usuários autenticados acessam a galeria

### 🖼️ Galeria de Fotografias
- **Listagem** de fotografias ordenadas por data (mais recentes primeiro)
- **Visualização** detalhada de cada fotografia (nome, legenda, descrição)
- **Cadastro** de novas fotografias via formulário
- **Edição** de fotografias existentes
- **Exclusão** de fotografias
- **Busca** por nome da fotografia
- **Filtro por categoria**: Nebulosa, Estrela, Galáxia, Planeta

### ⚙️ Painel Administrativo
- Interface de administração personalizada com listagem, busca, filtros e edição em linha
- Campos exibidos: ID, Nome, Legenda, Publicada
- Filtro por categoria e usuário

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Descrição |
|---|---|---|
| **Python** | 3.x | Linguagem principal |
| **Django** | 5.2.7 | Framework web |
| **SQLite** | — | Banco de dados (desenvolvimento) |
| **Pillow** | 12.0.0 | Processamento de imagens |
| **django-storages** | 1.14.6 | Integração com armazenamento externo |
| **boto3** | 1.40.61 | SDK AWS para upload no S3 |
| **python-dotenv** | 1.1.1 | Gerenciamento de variáveis de ambiente |

---

## 📁 Estrutura do Projeto

```
Space-Django/
├── apps/
│   ├── galeria/              # App principal da galeria
│   │   ├── admin.py          # Configuração do Django Admin
│   │   ├── forms.py          # Formulário de cadastro/edição de fotos
│   │   ├── models.py         # Modelo Fotografia
│   │   ├── urls.py           # Rotas da galeria
│   │   └── views.py          # Views (CRUD + busca + filtro)
│   └── usuarios/             # App de autenticação
│       ├── forms.py          # Formulários de Login e Cadastro
│       ├── urls.py           # Rotas de autenticação
│       └── views.py          # Views (login, cadastro, logout)
├── setup/
│   ├── settings.py           # Configurações do Django
│   ├── urls.py               # URLs raiz do projeto
│   ├── static/
│   │   ├── assets/           # Imagens, ícones e logo
│   │   └── styles/           # Arquivos CSS
│   ├── wsgi.py
│   └── asgi.py
├── templates/
│   ├── shared/
│   │   └── base.html         # Template base (layout principal)
│   ├── partials/
│   │   ├── _menu.html        # Menu lateral de navegação
│   │   ├── _footer.html      # Rodapé
│   │   └── _alertas.html     # Mensagens de alerta
│   ├── galeria/
│   │   ├── index.html        # Página principal com cards
│   │   ├── imagem.html       # Detalhe da fotografia
│   │   ├── nova_imagem.html  # Formulário de nova foto
│   │   └── editar_imagem.html# Formulário de edição
│   └── usuarios/
│       ├── login.html        # Página de login
│       └── cadastro.html     # Página de cadastro
├── scripts/
│   └── secret_key_generator.py  # Gerador de SECRET_KEY
├── manage.py
├── requirements.txt
├── .env                      # Variáveis de ambiente (não versionado)
└── .gitignore
```

---

## 🔗 Rotas da Aplicação

### Galeria

| Método | Rota | Nome | Descrição |
|---|---|---|---|
| GET | `/` | `index` | Página principal com todas as fotos |
| GET | `/imagem/<id>` | `imagem` | Detalhe de uma fotografia |
| GET | `/buscar?buscar=<termo>` | `buscar` | Busca por nome |
| GET/POST | `/nova-imagem` | `nova_imagem` | Cadastrar nova foto |
| GET/POST | `/editar-imagem/<id>` | `editar_imagem` | Editar foto existente |
| GET | `/deletar-imagem/<id>` | `deletar_imagem` | Deletar foto |
| GET | `/filtro/<categoria>` | `filtro` | Filtrar por categoria |

### Usuários

| Método | Rota | Nome | Descrição |
|---|---|---|---|
| GET/POST | `/login` | `login` | Página de login |
| GET/POST | `/cadastro` | `cadastro` | Página de cadastro |
| GET | `/logout` | `logout` | Efetuar logout |

---

## 🗃️ Modelo de Dados

### Fotografia

| Campo | Tipo | Descrição |
|---|---|---|
| `nome` | CharField(100) | Nome da fotografia |
| `legenda` | CharField(150) | Legenda curta |
| `categoria` | CharField(150) | Categoria (Nebulosa, Estrela, Galáxia, Planeta) |
| `descricao` | TextField | Descrição detalhada |
| `foto` | ImageField | Imagem (upload organizado por data) |
| `publicada` | BooleanField | Visibilidade na galeria |
| `data_fotografia` | DateTimeField | Data do registro |
| `usuario` | ForeignKey(User) | Usuário que cadastrou |

---

## ☁️ Armazenamento na AWS S3

O projeto utiliza **Amazon S3** para armazenar arquivos estáticos e mídia em produção:

- **Arquivos estáticos** → pasta `static/` no bucket
- **Arquivos de mídia** (uploads) → pasta `media/` no bucket
- Cache configurado para 1 dia (`max-age=86400`)
- Proteção contra sobrescrita de arquivos com mesmo nome

---

## ⚡ Como Rodar o Projeto

### Pré-requisitos

- Python 3.10+
- pip

### 1. Clone o repositório

```bash
git clone https://github.com/AdonesMelo/Space-Django.git
cd Space-Django
```

### 2. Crie e ative o ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SECRET_KEY=sua_secret_key_aqui
AWS_ACCESS_KEY_ID=sua_access_key
AWS_SECRET_ACCESS_KEY=sua_secret_key
AWS_STORAGE_BUCKET_NAME=nome_do_bucket
AWS_S3_REGION_NAME=regiao_do_bucket
```

> 💡 Use o script `python scripts/secret_key_generator.py` para gerar uma `SECRET_KEY` segura.

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📝 Licença

Este projeto foi desenvolvido durante o curso da [Alura](https://www.alura.com.br/) como parte do aprendizado em Django.

---

## 👤 Autor

**Adones Melo** — [GitHub](https://github.com/AdonesMelo)
