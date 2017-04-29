#!/bin/bash
# Diretorio e arquivo de log
set -e
LOGFILE=/home/olivx/www/pytech/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
# Numero de processo simultaneo, modifique de acordo com seu processador
NUM_WORKERS=3
# Usuario/Grupo que vai rodar o gunicorn
USER=olivx
#GROUP=root
# Endereço local que o gunicorn irá rodar
ADDRESS=0.0.0.0:8000
# Ativando ambiente virtual e executando o gunicorn para este projeto
. /home/olivx/www/pytech/.venv/bin/activate
cd /home/olivx/www/pytech/
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -w $NUM_WORKERS --bind=$ADDRESS --user=$USER --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE websistesis.wsgi:application
websistesis.wsgi:application