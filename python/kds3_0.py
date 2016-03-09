import os, sys, shutil

ksdk_path = "D:/mqx_cloud_repo/ksdk_test"
yml_folder = "bin/generator/records/ksdk/"
process_folder = [
    "sdk_example",
    "sdk_unittest",
    "usb_example"
]
# process_folder = 'sdk_example'
list_path = [
    "frdmk22f",
    "frdmk64f",
    "frdmkl25z",
    "frdmkl26z",
    "frdmkl46z",
    "twrk21d50m",
    "twrk21f120m",
    "twrk22f120m",
    "twrk60d100m",
    "twrk64f120m",
    "twrkl25z48m",
]

key_word = "Debug CMSISDAP.launch"
old_string = [
'          - templates/kds/$core/Release PNE.launch\r\n'
]
new_string = [
'          - templates/kds/$core/Release PNE.launch\r\n'
'          - templates/kds/$core/Debug CMSISDAP.launch\r\n',
'          - templates/kds/$core/Release CMSISDAP.launch\r\n',
]
usb_old_string = [
'          - templates/kds/$core/Release PNE.launch\r\n'
]
usb_new_string = [
'          - templates/kds/$core/Release PNE.launch\r\n'
'          - templates/kds/$core/Debug CMSISDAP.launch\r\n',
'          - templates/kds/$core/Release CMSISDAP.launch\r\n',
]

sign_m4f = [
'templates/kds/app_cortex_m4f/Debug CMSISDAP.launch',
'templates/kds/app_cortex_m4f/Release CMSISDAP.launch'
]
sign_m4 = [
'templates/kds/app_cortex_m4/Debug CMSISDAP.launch',
'templates/kds/app_cortex_m4/Release CMSISDAP.launch'
]
sign_m0p = [
'templates/kds/app_cortex_m0plus/Debug CMSISDAP.launch',
'templates/kds/app_cortex_m0plus/Release CMSISDAP.launch'
]

def add_cmsis(file_path):
    pass

if __name__ == "__main__":
    os.chdir(ksdk_path)
    for folder_process in process_folder:
        target = os.path.realpath(os.path.join(yml_folder, folder_process))
        for root, dirs, files in os.walk(target):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if not file_name.endswith(".yml"):
                    continue
                for board_target in list_path:
                    if file_path.count(board_target):
                        break
                else:
                    continue
                file_path = os.path.join(root, file_name)
                file_data = open(file_path, 'rb').read()
                is_m4f = False
                is_m0p = False
                is_Change = False
                is_usb = False
                if file_name.count('usb_'):
                    is_usb = True
                if file_data.count('app_cortex_m4f'):
                    is_m4f = True
                elif file_data.count('app_cortex_m0plus'):
                    is_m0p = True
                if is_m4f:
                    if file_data.count(sign_m4f[0]):
                        continue
                    else:
                        is_Change = True
                        if is_usb:
                            file_data = file_data.replace(''.join(usb_old_string).replace('$core', 'app_cortex_m4f'), ''.join(usb_new_string).replace('$core', 'app_cortex_m4f'))
                        else:
                            file_data = file_data.replace(''.join(old_string).replace('$core', 'app_cortex_m4f'), ''.join(new_string).replace('$core', 'app_cortex_m4f'))
                elif is_m0p:
                    if file_data.count(sign_m0p[0]):
                        continue
                    else:
                        is_Change = True
                        if is_usb:
                            file_data = file_data.replace(''.join(usb_old_string).replace('$core', 'app_cortex_m0plus'), ''.join(usb_new_string).replace('$core', 'app_cortex_m0plus'))
                        else:
                            file_data = file_data.replace(''.join(old_string).replace('$core', 'app_cortex_m0plus'), ''.join(new_string).replace('$core', 'app_cortex_m0plus'))
                else:
                    if file_data.count(sign_m4[0]):
                        continue
                    else:
                        is_Change = True
                        if is_usb:
                            file_data = file_data.replace(''.join(usb_old_string).replace('$core', 'app_cortex_m4'), ''.join(usb_new_string).replace('$core', 'app_cortex_m4'))
                        else:
                            file_data = file_data.replace(''.join(old_string).replace('$core', 'app_cortex_m4'), ''.join(new_string).replace('$core', 'app_cortex_m4'))
                if is_Change:
                    print file_path
                    with open(file_path, "wb") as write_file:
                        write_file.write(file_data)


# if __name__ == "__main__":
#     os.chdir(ksdk_path)
#     import re, yaml
#     for folder_process in process_folder:
#         target = os.path.realpath(os.path.join(yml_folder, folder_process))
#         for root, dirs, files in os.walk(target):
#             for file_name in files:
#                 if not file_name.endswith(".yml"):
#                     continue
#                 file_path = os.path.join(root, file_name)
#                 if re.search("|".join(list_path), file_path):
#                     # print file_name
#                     board_option = {}
                    # with open(file_path, 'rb') as stream:
                    #     board_option = yaml.load(stream)
                        # if (not "templates/kds/app_cortex_m4f/Debug CMSISDAP.launch" in board_option["__hierarchy__"]["configuration"]["tools"]["kds"]["project-templates"]):
                        #     board_option["__hierarchy__"]["configuration"]["tools"]["kds"]["project-templates"].append("templates/kds/app_cortex_m4f/Debug CMSISDAP.launch")
                        # if (not "templates/kds/app_cortex_m4f/Release CMSISDAP.launch" in board_option["__hierarchy__"]["configuration"]["tools"]["kds"]["project-templates"]):
                        #     board_option["__hierarchy__"]["configuration"]["tools"]["kds"]["project-templates"].append("templates/kds/app_cortex_m4f/Release CMSISDAP.launch")
                    # with open(file_path, 'wb') as stream:
                    #     stream.write(yaml.dump(board_option, default_flow_style=True))
                    # file_data = open(file_path, "rb").read()
                    # if not key_word in file_data:
                    #     file_data = file_data.replace(old_string, new_string)
                    # with open(file_path, "wb") as write_file:
                    #     write_file.write(file_data)

                # for board_name in list_path:
                #     if file_path.count(board_name):
                #         break
                # else:
                #     continue
                # add_cmsis(file_path)

