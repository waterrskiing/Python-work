import os, sys

process_folder = "D:\Backup\mcu-sdk-2.0-origin\devices"

key_word = ''

module2 = ""

def count_module(module_name, file_path, index_module):
    file_data = open(file_path,'rb').readlines()
    for index, line in enumerate (file_data):
        if (module_name in line) and ('kCLOCK' in file_data[index+2]):
            # print file_data[index+2],
            index_clock =file_data[index+2].count(",") +1
            # print index_clock
            # print file_data2
            # index_clock = index_clock +1
            # print index_clock
            if index_module != index_clock:
                fail_path = root + ":" + module_name.replace('#define ','').replace('_CLOCKS','')
                print fail_path

os.chdir(process_folder)
for root, dirs, files in os.walk(process_folder):
    # module_dict = {}
    module_list = []
    module_value = []
    for file_name in files:
        if 'features.h' in file_name:
            file_path = os.path.join(root,file_name)
            file_data = open(file_path,'rb').readlines()
            for line_data in file_data:
                if '#define FSL_FEATURE_SOC' in line_data:
                    line_data = line_data.split('_')
                    module = line_data[3]
                    module2 = "#define %s_CLOCKS" % module
                    # print module2
                    index_module = line_data[4][7:8]
                    module_list.append(module2)
                    module_value.append(int(index_module))
                    # module_dict[module2] = int(index_module)
                    # print index_module
                    data_new = module+" "+index_module
                    # print data_new
    # module_list = module_dict.keys()
    # module_list.sort()
    file_path = os.path.join(root, "fsl_clock.h")
    if os.path.exists(file_path):
        # for module_name in module_dict:
        #     count_module(module_name, file_path, module_dict[module_name])
        for count in range(len(module_list)):
            count_module(module_list[count], file_path, module_value[count])
    # for file_name in files:
    #     if file_name.count('fsl_clock') and file_name.endswith(".h"):
    #         file_path = os.path.join(root,file_name)
    #         for module_name in module_list:
    #             count_module(module_name, file_path, module_dict[module_name])

