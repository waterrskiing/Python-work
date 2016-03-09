import os,sys
tmp_arr = []
module_arr =[]
module_path ="D:\Backup\mcu-sdk-2.0-origin\platform\drivers"
file_folder = "D:\\map_driver2examples.yml"
process_folder = "D:\Backup\mcu-sdk-2.0-origin\\bin\generator\\records\ksdk\sdk_example\common"
module_arr+=os.listdir(module_path)
# print '\n'.join(module_arr)

os.chdir(process_folder)
for file_name in os.listdir(process_folder):
    if "virtual" in file_name:
        continue
    else:
        path = os.path.join(os.path.realpath(process_folder),file_name)
    data = sorted(open(path,"rb").readlines())

    for line in data:
        if line[0].isalpha() == True:
            if line.count('lwip'):
                tmp_arr.append(line)
                data_lwip = "    %s : True\n"%'enet'
                tmp_arr.append(data_lwip)
                continue
            if line.count('emv'):
                tmp_arr.append(line)
                data_emv = "    %s : True\n"%'emvl1'
                tmp_arr.append(data_emv)
                continue
            if line.count('touch'):
                tmp_arr.append(line)
                data_gpio = "    %s : True\n"%'gpio'
                tmp_arr.append(data_gpio)
                continue
            if 'core' in line or 'benchmark' in line or 'selftest' in line:
                tmp_arr.append(line)
                data_core = "    %s : True\n"%'port'
                tmp_arr.append(data_core)
                continue
            if 'power_manager' in line or 'power_mode_switch' in line:
                tmp_arr.append(line)
                data_lptm = "    %s : True\n    %s :True\n"%('llwu','sim')
                tmp_arr.append(data_lptm)
                continue
            else:
                tmp_arr.append(line)
                module_in_ex = line.strip().replace(':','').split('_')
                module_output = []
                for module in module_in_ex:
                    if module in module_arr:
                        module_output.append(module.strip())
                for count in range(len(module_output)):
                    data2 = "    %s : True\n"%module_output[count]
                    tmp_arr.append(data2)
print "Create map_file finished"

write_file = open(file_folder, 'wb')
write_file.write(''.join(((tmp_arr))))
write_file.close()
