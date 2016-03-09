#de bai:vao tat ca cac file .yml trong bin/generator/records/ksdk va thao tac voi tat ca cac
# thu muc trong process_folder thay doi old_string -> new_string

import os, sys, shutil

ksdk_path = "D:/mcu-sdk-2.0-origin"
yml_folder = "bin/generator/records/ksdk/"
process_folder = [
    "sdk_example",
    "sdk_unittest",
    "usb_example"
]

list_path = [
    "frdmkl81z",
    "frdmkl82z",
    "frdmkv10z",
    "frdmkv31f",
    "frdmkw24",
    "frdmkw40z",
    "frdmkw41z",
    "mapsks22",
    "mrbkw01",
    "twrk21d50m",
    "twrk21f120m",
    "twrk22f120m",
    "twrk24f120m",
    "twrk60d100m",
    "twrk64f120m",
    "twrk65f180m",
    "twrk80f150m",
    "twrk81f150m",
    "twrke18f150m",
    "twrkl25z48m",
    "twrkl28t72m",
    "twrkl28z72m",
    "twrkl43z48m",
    "twrkl81z72m",
    "twrkl82z72m",
    "twrkm34z75m",
    "twrkv10z32",
    "twrkv11z75m",
    "twrkv31f120m",
    "twrkv46f150m",
    "twrkv58f220m",
    "twrkw24d512",
    "usbkw40z_kw40z",
    "usbkw41z_kw41z",
    "frdmk22f",
    "frdmk64f",
    "frdmk66f",
    "frdmk82f",
    "frdmke15z",
    "frdmkl02z",
    "frdmkl03z",
    "frdmkl25z",
    "frdmkl26z",
    "frdmkl27z",
    "frdmkl28t",
    "frdmkl28z",
    "frdmkl43z",
    "frdmkl43zkl33z4",
    "frdmkl46z"
]

old_string = '          - templates/iar/general.eww\r\n'

new_string = '          - templates/iar/dni/${board}.dni\r\n          - templates/iar/general.eww\r\n'

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
                file_data = file_data.replace(old_string,new_string)
                print file_path
                with open(file_path, "wb") as write_file:
                    write_file.write(file_data)
