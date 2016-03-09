import os

ksdk_path = "D:\Prj\work3-origin\mcu-sdk-2.0-origin"

result_file_path = 'D:\Prj\work3-origin\\result.txt'

folder_process = 'devices'

str_sign = '#define $IP_CLOCKS'

def getModuleFeature(file_data):
    result = {}
    for line in file_data:
        if '#define FSL_FEATURE_SOC' in line:
            tmp_arr = line.split(' ')
            new_key = tmp_arr[1].replace('FSL_FEATURE_SOC_', '').replace('_COUNT', '')
            new_value = tmp_arr[2].replace('(', '').replace(')', '').strip()
            if result.get(new_key, 0) < new_value:
                result[new_key] = new_value
    return result
def checkValid(dict_input, file_path):
    file_data = []
    result = []
    try:
        file_data = open(file_path, 'rb').read()
    except IOError:
        return result
    tmp_arr = file_data.split('\n\n')

    for key in dict_input.keys():
        for block in tmp_arr:
            if block.count('#define') and block.count('CLOCKS') and block.count(str_sign.replace('$IP', key)):
                if block.count('kCLOCK_') != int(dict_input[key]):
                    result.append(str(key) + ' ')

    return result

data_to_write = open(result_file_path, 'a')

temp_str = [
'$board\n'
'   Not valid module: $module\n'
]

os.chdir(ksdk_path)
for root, dirs, files in os.walk(folder_process):
    for file_name in files:
        if 'features' in file_name and file_name.endswith('.h'):
            file_path = os.path.join(root, file_name)
            clock_file_path = os.path.join(os.path.dirname(file_path), 'fsl_clock.h')
            file_data = open(file_path, 'rb').readlines()
            tmp_dict = {}
            tmp_dict = getModuleFeature(file_data)
            tmp_result = []
            tmp_result = checkValid(tmp_dict, clock_file_path)
            if len(tmp_result):
                str_wr = ''.join(temp_str).replace('$board', file_name.replace('_features', '')).replace('$module', ''.join(tmp_result))
                data_to_write.write(str_wr)

data_to_write.close()


