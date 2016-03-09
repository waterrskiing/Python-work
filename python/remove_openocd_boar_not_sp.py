import os,sys

process_folder = "D:/mcu-sdk-2.0-origin"
yml_folder = "bin/generator/records/ksdk"
folder_process= [
    "sdk_example",
    "sdk_unittest",
    "usb_example"
]

list_path = [
    "twrk21f120m",
    "twrk21d50m",
    "twrk60d100m",
]

key_word = 'app_cortex_m4f'

old_string = [
'          - templates/kds/$core/Release PNE.launch\n',
'          - templates/kds/$core/Debug CMSISDAP.launch\n',
'          - templates/kds/$core/Release CMSISDAP.launch\n',
]

new_string = [
'          - templates/kds/$core/Release PNE.launch\n',
]

os.chdir(process_folder)
for folder in folder_process:
    target = os.path.realpath(os.path.join(yml_folder, folder))
    # for root, dirs, files in os.walk(target):
    #     for file_name in files:
    for file_name in os.listdir(target):
        if (file_name.replace(".yml", "") in list_path) and file_name.endswith(".yml"):
            file_path = os.path.join(target,file_name)
            file_data = open(file_path,'r').read()
            is_m4f = False
            if file_data.count(key_word):
                is_m4f = True
            if is_m4f:
                file_data = file_data.replace(''.join(old_string).replace('$core', 'app_cortex_m4f'), ''.join(new_string).replace('$core', 'app_cortex_m4f'))
            else:
                file_data = file_data.replace(''.join(old_string).replace('$core', 'app_cortex_m4'), ''.join(new_string).replace('$core', 'app_cortex_m4'))
            print file_path
            write_file = open(file_path,'wb')
            write_file.write(file_data)
            write_file.close()