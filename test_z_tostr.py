import time

from api.public.snap import snap_t
from api.read_md.tool.public.z_tostr.z_tostr import data2str


def zzy_ddt(msg1):
    def in_zzy_ddt(fn):
        def in_fn(*args):
            for i in args[0]:
                if type(i) == list:
                    if len(i) == 1:
                        try:
                            snap_t(fn(i[0]),msg=f'{msg1}--{i[0]}')
                        except:
                            print(f'{msg1}--{i[0]}\n{fn(i[0])}')
                    elif len(i) == 2:
                        try:
                            snap_t(fn(i[0]),msg=f'{msg1}--{i[1]}--{i[0]}')
                        except:
                            print(f'{msg1}--{i[1]}--{i[0]}\n{fn(i[0])}')
                    elif len(i) == 3:
                        try:
                            snap_t(fn(i[0]),msg=f'{msg1}--{i[1]}--{i[0]}',acc_data=i[2])
                        except:
                            print(f'{msg1}--{i[1]}--{i[0]}\n{fn(i[0])}')
                else:
                    try:
                        snap_t(fn(i),msg=f'{i}{msg1}')
                    except:
                        print(f'{i}--{msg1}\n{fn(i)}')
        return in_fn
    return in_zzy_ddt

def add_dict(dict1,dict2):
    temp = dict(dict1)
    temp.update(dict2)
    return temp

data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
rules1 = {'start': 'start||','each_end': '||each_end'}
rules2 = {'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules3 = {'bef_each_start': {'1': '-1', '3': '-1'}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules4 = {'bef_each_start': {'0': '-1', '5': '-1'}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules5 = {'aft_each_start': {'2': '---', '4': '---'}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules6 = {'bef_each_end': {'0': '///', '3': '///'}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules7 = {'aft_each_end': {'0': '+++', '4': '+++'}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules8 = {'bef_each_start': {'0': '--1', '5': '--1', '*': '???'}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules9 = {'insert_data': {'0': 'ddd','3':['fff','eee']}, 'bef_each_start': {'1': '-1', '3': '-1', '*': ')))'}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules10 = {'bef_each_start': {'0': '-1', '5': '-1', '*': '==='}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules11 = {'aft_each_start': {'2': '---', '4': '---', '*': '***'}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules12 = {'bef_each_end': {'0': '///', '3': '///', '*': ';;;'}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules13 = {'aft_each_end': {'0': '+++', '4': '+++', '*': '[[['}, 'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}


test_data = [[{'data_list': data_list, 'rules': {}}, 'smock', 'a1b1c1d1e1f1'],
             [{'data_list': data_list, 'rules': rules1}, '1_half_easy', 'start||a1||each_endb1||each_endc1||each_endd1||each_ende1||each_endf1||each_end'],
             [{'data_list': data_list, 'rules': rules2}, '2_easy', 'start||each_start||a1||each_endeach_start||b1||each_endeach_start||c1||each_endeach_start||d1||each_endeach_start||e1||each_endeach_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules3}, '3_bef_each_start_1', 'start||each_start||a1||each_end-1each_start||b1||each_endeach_start||c1||each_end-1each_start||d1||each_endeach_start||e1||each_endeach_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules4}, '4_bef_each_start_0', 'start||-1each_start||a1||each_endeach_start||b1||each_endeach_start||c1||each_endeach_start||d1||each_endeach_start||e1||each_end-1each_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules5}, '5_aft_each_start_2', 'start||each_start||a1||each_endeach_start||b1||each_endeach_start||---c1||each_endeach_start||d1||each_endeach_start||---e1||each_endeach_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules6}, '6_bef_each_end03', 'start||each_start||a1///||each_endeach_start||b1||each_endeach_start||c1||each_endeach_start||d1///||each_endeach_start||e1||each_endeach_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules7}, '7_aft_each_end04', 'start||each_start||a1||each_end+++each_start||b1||each_endeach_start||c1||each_endeach_start||d1||each_endeach_start||e1||each_end+++each_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules8}, '8_bef_each_start0_5_*','start||--1each_start||a1||each_end???each_start||b1||each_end???each_start||c1||each_end???each_start||d1||each_end???each_start||e1||each_end--1each_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules9}, '9_insert_bef_each_start1_3_*'],
             [{'data_list': data_list, 'rules': rules10}, '10_bef_each_start0_5_*'],
             [{'data_list': data_list, 'rules': rules11}, '11_aft_each_start2_4_*'],
             [{'data_list': data_list, 'rules': rules12}, '12_bef_each_end0_3_*'],
             [{'data_list': data_list, 'rules': rules13}, '13_aft_each_end0_4_*']
             ]



@zzy_ddt('md2data')
def test_md2data(test_data):
    return data2str(test_data['data_list'], test_data['rules']).str


if __name__ == '__main__':
    test_md2data(test_data)