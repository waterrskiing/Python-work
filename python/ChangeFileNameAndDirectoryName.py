import os, sys, shutil
import sys

#Replace directory's your repo
ksdk_path = "D:\mqx_cloud_repo\ksdk_test"

process_folder = 'boards'

_folders = []
# sign_to_add_postfix = 'dspi_interrupt'
postfix = '_transfer'

# This function changes name of file or directory
# Begin funtion
def Change_name(old_name, new_name):
    os.chdir(ksdk_path)
    for root, dirs, files in os.walk(process_folder):
    # change file name
        for file_name in files:
            # if file_name.count('lpuart'):
            #     continue
            # if file_name.count('buffer'):
            #     continue
            if file_name.count('functional'):
                continue
            if file_name.count('transfer'):
                continue
            # if file_name.count('ptp1588'):
            #     continue
            # if file_name.count('interrupt'):
            #     continue
            # if file_name.count('dma_spi'):
            #     continue
            # if file_name.count('edma'):
            #     continue
            if file_name.count('dspi'):
                continue
            # if file_name.count('qspi'):
            #     continue
            if file_name.count('lpspi'):
                continue
            # if file_name.count('transfer'):
            #     continue
            if file_name.count('lpspi'):
                continue
            # if file_name.count('b2b'):
            #     continue
            # if file_name.count('lpi2c'):
            #     continue
            # if file_name.count('readme'):
            #     continue
            # if file_name.count('.c'):
            #     continue
            # if file_name.count('.meta'):
            #     continue
            if file_name.count('flexio'):
                continue
            # if file_name.count('lpi2c'):
            #     continue
            # if file_name.count('spi'):
            #     continue
            # if file_name.count('lpspi_polling'):
            #     continue
            if file_name.count('123'):
                # continue
                if file_name.count(old_name):
                    file_path = os.path.join(root, file_name)
                    old_file_path = os.path.abspath(file_path)
                    base_name_folder = os.path.dirname(old_file_path)
                    new_file_path = base_name_folder + '\\' + file_name.replace(old_name, new_name)
                    print new_file_path
                    shutil.move(old_file_path, new_file_path)
    print "\n\tChanged file name successfull!\n\n"
    # change folder name
    for root, dirs, files in os.walk(process_folder):
        for _dir in dirs:
    #         # if os.path.join(root, _dir).count('lpuart'):
    #         #     continue
    #         # if os.path.join(root, _dir).count('buffer'):
    #         #     continue
    #         if os.path.join(root, _dir).count('functional'):
    #             continue
    #         if os.path.join(root, _dir).count('transfer'):
    #             continue
    #         if os.path.join(root, _dir).count('dspi'):
    #             continue
    #         # if os.path.join(root, _dir).count('qspi'):
    #         #     continue
    #         if os.path.join(root, _dir).count('lpspi'):
    #             continue
    #         # if os.path.join(root, _dir).count('lpspi'):
    #         #     continue
    #         # if os.path.join(root, _dir).count('b2b'):
    #         #     continue
    #         # if os.path.join(root, _dir).count('edma'):
    #         #     continue
    #         # if os.path.join(root, _dir).count('dma_spi'):
    #         #     continue
    #         # if os.path.join(root, _dir).count('lpi2c'):
    #         #     continue
            if os.path.join(root, _dir).count('flexio'):
                continue
    #         # if os.path.join(root, _dir).count('interrupt'):
    #         #     continue
    #         # if os.path.join(root, _dir).count('ptp1588'):
    #         #     continue
            if os.path.join(root, _dir).count('pdb'):
            #     continue
                if (_dir.count(old_name)):
                    old_path = os.path.abspath(os.path.join(root, _dir))
                    new_path = os.path.dirname(old_path) + '\\' + _dir.replace(old_name, new_name)
                    print new_path
                    os.rename(old_path, new_path)
    # print "\n\tChanged directory name successfull!\n\n"
# End of funtion

# In developing ############################################
# def AddPostfixToName(sign_to_add_postfix):
#     os.chdir(ksdk_path)
#     for root, dirs, files in os.walk(process_folder):
#         for _dir in dirs:
#             if (_dir.count(sign_to_add_postfix)):
#                 old_path = os.path.abspath(os.path.join(root, _dir))
#                 _folders.append(os.path.basename(old_path))
#             print (_folders)
#     for item in _folders:
#         item.append(postfix)
#         print (item)

##################### ##################################################################
# os.chdir(ksdk_path)
# AddPostfixToName(str(sys.argv[1]))

Change_name(str(sys.argv[1]), str(sys.argv[2]))



########################################################################################
#EOF
########################################################################################

# Change_name('dspi_edma_transfer_b2b', 'dspi_edma_b2b_transfer')
# Change_name('dspi_interrupt', 'dspi_int_transfer')
# Change_name('dspi_interrupt_b2b', 'dspi_int_b2b_transfer')
# Change_name('dspi_polling', 'dspi_polling_transfer')
old_name = [
    'dspi_interrupt_b2b'
]
new_name = [
    ''
]