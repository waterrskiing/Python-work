import os

ksdk_path = "D:\Prj\work2-origin\mcu-sdk-2.0-origin"

process_folder = 'bin'

dni_folder_path = "D:\Prj\work2-origin\mcu-sdk-2.0-origin\\bin\generator\\templates\iar"
yml_file = "D:\Prj\work2-origin\mcu-sdk-2.0-origin\\bin\generator\\records\ksdk\options\common\debugger_config.yml"

templates_to_add ='$cpu  osjtag:\r\n    $device\r\n'

def getDeviceName(file_path):
    file_data = open(file_path, 'rb').readlines()
    for line in file_data:
        if line.count('device0=_'):
            line = line.replace('device0=_', '')
            line = line.replace('\"', '')
            return line.strip()

def addToYmlFile(file_data, new_item):
#K22FN512M12
    tmp_arr = new_item.split('_')
    sign_check = tmp_arr[2][:4]

    #print new_item
    for index, line in enumerate(file_data):
        if line.count(sign_check.lower()):
            if file_data[index+9].count('osjtag'):
                continue
            tmp = templates_to_add.replace('$cpu', file_data[index+8])
            tmp = tmp.replace('$device', new_item)
            yml_file_data_to_write[index+8] = tmp
            print tmp

yml_file_data = open(yml_file, 'rb').readlines()
yml_file_data_to_write =  yml_file_data[:]
os.chdir(dni_folder_path)
for root, dirs, files in os.walk('dni'):
    for file_name in files:
        if file_name.count('.dni'):
            file_path = os.path.join(root, file_name)
            addToYmlFile(yml_file_data, getDeviceName(file_path))
        else:
            continue

str_to_write = ''.join(yml_file_data_to_write)
write_file = open(yml_file, 'wb')
write_file.write(str_to_write)
write_file.close()
