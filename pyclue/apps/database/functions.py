# -*- coding: utf-8 -*-
__author__ = 'alex'
import os, sys, traceback
from pyclue.appSettings import DB_NAME, PROJECT_DIR, get_backup_path, get_data_path
from pyclue.apps.settings.functions import get_settings
from pyclue.apps.database.models import database


"""
Obtiene el path de la base de datos
"""
def get_db_path():
    try:
        path = os.path.join(PROJECT_DIR,DB_NAME)
        path = os.path.normpath(path)
        print path
        return path
    except:
        message = "Error" + str(sys.exc_info()[0]) + " " +\
                      str(sys.exc_info()[1]) + " " + \
                      str(sys.exc_info()[2])  + " " + traceback.format_exc()
        print message
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
    print settings.last_backup
    if settings.last_backup == None or settings.last_backup == "": # Aqui entra cuando es primera vez
        create_backup_file(settings)
    else:
        pass


def create_backup_file(settings):
    from datetime import datetime
    import shutil
    today = datetime.today()
    file_sufix_backup = today.strftime(".%d%m%y%M%S.bak") # Genera el sufijo correcto para el backup
    file_name_backup = "%s%s"%(settings.file_name_backup, # Genera el nombre completo del archivo backup
                               file_sufix_backup)
    path_to_backup = "%s/%s"%(get_backup_path(),file_name_backup) #Genera la ruta donde se almacenará el backup
    data_to_copy = get_data_path() # Ubica el archivo de la base de datos a respaldar.
    try:
        shutil.copy2(data_to_copy,path_to_backup) # Copia el respaldo
        settings.last_backup = datetime.today() # actualiza la hora y fecha del ultimo respaldo
        settings.save() # Guarda los settings
        return True
    except:
        return False