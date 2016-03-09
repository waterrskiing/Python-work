import os,sys

process_folder = "D:/mcu-sdk-2.0-origin"
yml_folder = "bin/generator/records/ksdk"
folder_process= [
    "sdk_example",
    "sdk_unittest",
]
folder_process2 = [    "usb_example"]

list_path = [
"twrkl81z72m",
"twrkl82z72m",
"frdmkl81z",
"frdmkl82z"
]

old_string = [
'          - templates/mdk/app_$board/$board.uvprojx\n',
'      kds:\n'
]

new_string = [
'          - templates/mdk/app_$board/$board.uvprojx\n',
'          - templates/mdk/app_$board/pemicro_connection_settings.ini\n',
'      kds:\n'
]

old_string_usb = [
'      mdk:\r\n',
'        project-templates:\r\n',
'          - templates/mdk/app_$board/$board.uvprojx\r\n'
]

new_string_usb = [
'      mdk:\r\n',
'        project-templates:\r\n',
'          - templates/mdk/app_$board/$board.uvprojx\r\n',
'          - templates/mdk/app_$board/pemicro_connection_settings.ini\r\n'
]
os.chdir(process_folder)
for folder in folder_process:
    target = os.path.realpath(os.path.join(yml_folder, folder))
    # for root, dirs, files in os.walk(target):
    #     for file_name in files:
    for file_name in os.listdir(target):
        if (file_name.replace(".yml", "") in list_path) and file_name.endswith(".yml"):
            file_name2 = file_name.replace(".yml", "")
            file_path = os.path.join(target,file_name)
            file_data = open(file_path,'r').read()
            file_data = file_data.replace(''.join(old_string).replace('$board', file_name2), ''.join(new_string).replace('$board', file_name2))
            print file_path
            write_file = open(file_path,'wb')
            write_file.write(file_data)
            write_file.close()
for folder2 in folder_process2:
    target2 = os.path.realpath(os.path.join(yml_folder, folder2))
    for root, dirs, files in os.walk(target2):
        for board2 in list_path:
            if root.count(board2):
                for files in files:
                    file_path_usb = os.path.join(root,files)
                    file_data_usb = open(file_path_usb,'rb').read()
                    file_data_usb = file_data_usb.replace(''.join(old_string_usb).replace('$board', board2), ''.join(new_string_usb).replace('$board', board2))
                    print file_path_usb
                    write_file2 = open(file_path_usb,'wb')
                    write_file2.write(file_data_usb)
                    write_file2.close()