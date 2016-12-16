

# setup

o banco de dados originalmente está instalado em  SQLSERVER,
o sql-server exisge que em sei Model as tablemas estejam mapiadas para
NOME_DO_BANCO].[DBO].[NOME_DA_TABELA

# subindo app localmente
```git clone git@github.com:olivx/webtechsis.git webtechsis```
```cd webtechsis```
```python -m venv .webtechsis```
```source .webtechsis/bin/activete```
```pip install -r requirements.txt```
```cp contrib/env-simple .env```
```python manage.py test --nomigrations```

