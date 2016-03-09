import os, re
from collections import OrderedDict

ls_keys_to_bypass = ['AIPS', 'CAU', 'FMC', 'GPIO', 'LLWU', 'MCG', 'MCM', 'NV',\
                    'OSC', 'PMC', 'RCM', 'RFSYS', 'RFVBAT', 'SIM', \
                    'SMC', 'USBDCD', 'WDOG', 'ROM', 'AXBS','XBAR', \
                    'MTB', 'MTBDWT', 'MMAU','LCD', 'UART0', 'FGPIO', 'CAN',\
                    'LMEM', 'SDRAM', 'USBPHY']

path_repo = 'd:\hubs_doing\mcu-sdk-2.0-origin'
list_soc_name = ['MKL02Z4', 'MKL03Z4', 'MKL25Z4','MK21DA5', 'MK24F25612', 'MK60D10', 'MKM34Z7',\
                    'MK64F12', 'MK65F18']

class ParseClockFile:

    def __init__(self, root):
        self.CLOCK_FORMAT = r"([A-Z 0-9 _]* CLK_GATE_DEFINE[A-Z 0-9 _]*)"
        self.CLOCK_IP_ARRAY_FORMAT = r"([A-Z 0-9 _]*_BASE_ADDRS )"
        self.root = root

    def get_fsl_clock(self, board):
        fsl_clock_file = os.path.join(self.root, "devices", board.upper(), "fsl_clock.h")
        return self.get_fsl_clock_by_path(fsl_clock_file)

    def get_fsl_clock_by_path(self, path):
        fsl_clock_file = path
        clock = {}
        with open(fsl_clock_file, 'r') as _file:
            lines = _file.read().split("\n")
            for line in lines:
                m = re.search(self.CLOCK_FORMAT, line)
                if m:
                    while "  " in line:
                        line = line.replace("  ", " ")
                    if line.startswith(" "):
                        line = line[1:]
                    define = line.split(" ")
                    if not define[0] in clock:
                        clock[define[0]] = define[2]
        return clock

    def get_ip_clock_array(self, board):
        fsl_clock_file = os.path.join(self.root, "devices", board.upper(), "%s.h" % board.upper())
        return self.get_ip_clock_array_by_path(fsl_clock_file)

    def get_ip_clock_array_by_path(self, path):
        fsl_clock_file = path
        dic_data = {}
        with open(fsl_clock_file, 'r') as _file:
            lines = _file.read().split("\n")
            for line in lines:
                m = re.search(self.CLOCK_IP_ARRAY_FORMAT, line)
                if m:
                    while "  " in line:
                        line = line.replace("  ", " ")
                    if line.startswith(" "):
                        line = line[1:]
                    define = line.split(" ")
                    if re.search("0u", line):
                        dic_data[(define[1][:define[1].find('_BASE_ADDRS')])] = line.count(',')
                    else:
                        dic_data[(define[1][:define[1].find('_BASE_ADDRS')])] = line.count(',') + 1
            if 'UART0' in dic_data:
                if 'UART' in dic_data:
                    dic_data['UART'] = dic_data['UART'] + 1
            bypass_keys(dic_data)
            dic_data = change_name_keys(dic_data)
        return dic_data

def change_name_keys(dic_):
    if 'ADC16' in dic_:
        dic_['ADC'] = dic_.pop('ADC16')
    if 'I2S' in dic_:
        dic_['SAI'] = dic_.pop('I2S')
    if 'RNG' in dic_:
        dic_['RNGA'] = dic_.pop('RNG')
    if 'DSPI' in dic_:
        dic_['SPI'] = dic_.pop('DSPI')
    if 'USB' in dic_:
        dic_['USBFS'] = dic_.pop('USB')
    if 'EDMA' in dic_:
        dic_['DMA'] = dic_.pop('EDMA')
    if 'FB' in dic_:
        dic_['FLEXBUS'] = dic_.pop('FB')
    if 'FTFL' in dic_:
        dic_['FTF'] = dic_.pop('FTFL')
    if 'FTFE' in dic_:
        dic_['FTF'] = dic_.pop('FTFE')
    if 'FTFA' in dic_:
        dic_['FTF'] = dic_.pop('FTFA')
    return dic_

def bypass_keys(dic_):
    for ls_key in ls_keys_to_bypass:
        if ls_key in dic_:
            del dic_[ls_key]

def capitalize_keys(dic_in):
    result = {}
    for key, value in dic_in.items():
        upper_key = key.upper()
        result[upper_key] = result.get(upper_key, 0) + value
    return result

if __name__ == "__main__":
    parse = ParseClockFile(r'%s' %path_repo)
    for soc_name_in_list in list_soc_name:
        dic_clock = {}
        result_fsl_clock = parse.get_fsl_clock(soc_name_in_list)
        for old_key_of_clock in result_fsl_clock.keys():
            if old_key_of_clock[0] == 'k':
                new_key_of_clock = old_key_of_clock[7:]
                new_key_of_clock = new_key_of_clock[:(len(new_key_of_clock)-1)]
                if new_key_of_clock in dic_clock.keys():
                    dic_clock[new_key_of_clock] += 1
                else:
                    dic_clock[new_key_of_clock] = 1
        #upper case for keys  of dictionary
        dic_clock = capitalize_keys(dic_clock)
        dic_clock = OrderedDict(sorted(dic_clock.items()))

        result_ip_clock_array = parse.get_ip_clock_array(soc_name_in_list)
        result_ip_clock_array = OrderedDict(sorted(result_ip_clock_array.items()))

        ##### Compare "device_name.h" to "fsl_clock.h"
        print "#######Report for %s#######" %(soc_name_in_list)
        bit_check = 1
        for key in result_ip_clock_array.keys():
            if key in dic_clock:
                if dic_clock[key] != result_ip_clock_array[key]:
                    print "Wrong define: kClock_%s (in %s: %i # %i in fsl_clock.h)" \
                                %(key, soc_name_in_list ,result_ip_clock_array[key], dic_clock[key])
                    bit_check = 0
            else:
                print "Miss clock gate name: %s" %key
        if bit_check == 1:
            print "It's OK! No differences was found!"

        del dic_clock
        del result_ip_clock_array
        print "#######End for %s#######\r\n" %(soc_name_in_list)

        ##### Compare "clock ip name array" with "clock gate" in fsl_clock.h
