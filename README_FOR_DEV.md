### Configurando o .gitignore
```
**/__pycache__
.pytest_cache
venv
.env
```
### Instalando ambiente virtual do python
```python
pip3 install virtualenv

python3 -m venv venv
```

### Entrando no ambiente virtual
```
. venv/bin/activate
```

### Atualizando o pip
```
pip install --upgrade pip
```
### Instalando dependencias
```
pip3 install cffi
pip3 install pysus
pip3 install readdbc

pip3 install tables sqlalchemy

```

### configurando o VS CODE para esconter pasta de compilação do python
- crie uma pasta .vscode
- crei um arquivo de configurações (setting.json)


```json
{
  "files.exclude": {
    "**/*.pyc": {"when": "$(basename).py"},
    "**/__pycache__": true,
    "**/*.pytest_cache": true,
  }
}
```


### para usar variaveis de ambiente no projeto
- instalar o python dotenv

```
pip3 install python-dotenv
```

- criar o arquivo .env na raiz do projeto
- no arquivo que vamos usar as variaveis adicionar:
```
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acesse as variáveis de ambiente
dbc_file = os.getenv("DBC_FILE")
csv_file = os.getenv("CSV_FILE")

# Agora você pode usar essas variáveis no seu código!
```