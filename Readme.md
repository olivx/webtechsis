

# setup

o banco de dados originalmente está instalado em  SQLSERVER,
o sql-server exisge que em seu Model as tablemas estejam mapiadas para
NOME_DO_BANCO].[DBO].[NOME_DA_TABELA, nada te empede de usar outro
banco de dados, é só fazer as adaptações necessaria.

# subindo app localmente
```
git clone git@github.com:olivx/webtechsis.git webtechsis
cd webtechsis
python -m venv .webtechsis
source .webtechsis/bin/activete
pip install -r requirements.txt
cp contrib/env-simple .env
```



depois desses passos , existe um arquivo script_init_sql, é só executar ele,
ele foi feito para sql-server , então execute ele no  sql manager studio de
preferencia, para criar as dependecias necessaria.



