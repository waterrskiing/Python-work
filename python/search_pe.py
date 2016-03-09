import os,sys

process_folder = "D:/mcu-sdk-2.0-origin\\bin\generator\\templates\mdk"

os.chdir(process_folder)
for root, dirs, files in os.walk(process_folder):
    for files in files:
        if files.count("pemicro_connection_settings.ini"):
            file_path = os.path.join(root,files)
            file_dirname = os.path.dirname(file_path)
            if not file_dirname.count('virtual'):
                file_dirname = file_dirname.replace(process_folder+'\\'+'app_','')
                print file_dirname
