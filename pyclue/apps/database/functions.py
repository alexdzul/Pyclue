# -*- coding: utf-8 -*-
__author__ = 'alex'
import os
import sys
import traceback
from pyclue.appSettings import DB_NAME, PROJECT_DIR, get_backup_path, get_data_path
from pyclue.apps.settings.functions import get_settings
from pyclue.apps.database.models import database
import datetime
import shutil


"""
Obtiene el path de la base de datos
"""
def get_db_path():
    try:
        path = os.path.join(PROJECT_DIR, DB_NAME)
        path = os.path.normpath(path)
        return path
    except:
        message = "Error" + str(sys.exc_info()[0]) + " " +\
                  str(sys.exc_info()[1]) + " " + \
                  str(sys.exc_info()[2]) + " " + traceback.format_exc()
        return None


"""
Crea la base de datos pyclue
"""
def create_db():
    try:
        db = database()
        db.syncdb()
    except:
        pass


def generate_backup():
    """
    Valida si se requiere generar un nuevo backup
    :return: None
    """
    settings = get_settings()
    if settings:
        if settings.deactivate_backup:
            #No hace nada porque está desactivado por el usuario
            pass
        else:
            #Inicia el proceso de backup porque está activado.
            if settings.last_backup == None or settings.last_backup == "":
            # Aqui entra cuando es primera vez
                create_backup_file(settings)
            else:
                need_to_create_backup = need_backup(settings)
                if need_to_create_backup:
                    create_backup_file(settings)
                else:
                    pass


def create_backup_file(settings):
    today = datetime.datetime.today()
    file_sufix_backup = today.strftime(".%d%m%y%M%S.bak") # Genera el sufijo correcto para el backup
    file_name_backup = "%s%s"%(settings.file_name_backup, # Genera el nombre completo del archivo backup
                               file_sufix_backup)
    path_to_backup = "%s/%s"%(get_backup_path(),file_name_backup) #Genera la ruta donde se almacenará el backup
    data_to_copy = get_data_path() # Ubica el archivo de la base de datos a respaldar.
    try:
        shutil.copy2(data_to_copy,path_to_backup) # Copia el respaldo
        settings.last_backup = datetime.datetime.today().date() # actualiza la hora y fecha del ultimo respaldo
        settings.save() # Guarda los settings
        return True
    except:
        return False


def get_days_between_backup(settings):
    if settings.deactivate_backup: # Si está desactivado entonces devolvemos 0.
        return 0
    else: # Si están activos los backups entonces consultamos los días entre cada backup.
        if settings.period_backup == "Monthly":
            return 30
        if settings.period_backup == "Weekly":
            return 7
        else:
            return 0


def need_backup(settings):
    """
    Función que valida si ya es necesario realizar on backup o no.
    :param settings: objeto MainSettings
    :return: True or False
    """
    if settings.deactivate_backup:
        #Usuario ha desactivado el respaldo.
        return False
    else:
        #Se encuentra activa la función de respaldos.
        from dateutil.parser import parse
        #Convertimos a objetos tipo date
        last_backup = parse(str(settings.last_backup))
        today = parse((str(datetime.datetime.today().date())))
        #Sumamos al ultimo backup los días entre cada respaldo
        print("Días identificados por cada respaldo:",get_days_between_backup(settings))
        nextDateBackup = last_backup + datetime.timedelta(days=get_days_between_backup(settings))
        #Validamos si ya se requiere y retornamos True o False.
        print("último respaldo:", settings.last_backup)
        print("Siguiente respaldo:", nextDateBackup)
        if nextDateBackup <= today:
            return True
        else:
            return False
