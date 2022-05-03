import time

from api.public.snap import snap_t
from api.read_md.tool.public.zzy_tostr.zzy_tostr import data2str

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
rules3 = {'bef_each_start': {'1': '-1', '3': '-1'},'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules4 = {'bef_each_start': {'0': '-1', '5': '-1'},'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules5 = {'aft_each_start': {'2': '---', '4': '---'},'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules6 = {'bef_each_end': {'0': '///', '3': '///'},'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
rules7 = {'aft_each_end': {'0': '+++', '4': '+++'},'start': 'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}

test_data = [[{'data_list': data_list, 'rules': {}}, 'smock', 'a1b1c1d1e1f1'],
             [{'data_list': data_list, 'rules': rules1}, 'half_easy', 'start||a1||each_endb1||each_endc1||each_endd1||each_ende1||each_endf1||each_end'],
             [{'data_list': data_list, 'rules': rules2}, 'easy', 'start||each_start||a1||each_endeach_start||b1||each_endeach_start||c1||each_endeach_start||d1||each_endeach_start||e1||each_endeach_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules3}, 'bef_each_start_1', 'start||each_start||a1||each_end-1each_start||b1||each_endeach_start||c1||each_end-1each_start||d1||each_endeach_start||e1||each_endeach_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules4}, 'bef_each_start_0', 'start||-1each_start||a1||each_endeach_start||b1||each_endeach_start||c1||each_endeach_start||d1||each_endeach_start||e1||each_end-1each_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules5}, 'aft_each_start_2', 'start||each_start||a1||each_endeach_start||b1||each_endeach_start||---c1||each_endeach_start||d1||each_endeach_start||---e1||each_endeach_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules6}, 'bef_each_end03', 'start||each_start||a1///||each_endeach_start||b1||each_endeach_start||c1||each_endeach_start||d1///||each_endeach_start||e1||each_endeach_start||f1||each_end||end||'],
             [{'data_list': data_list, 'rules': rules7}, 'aft_each_end04', 'start||each_start||a1||each_end+++each_start||b1||each_endeach_start||c1||each_endeach_start||d1||each_endeach_start||e1||each_end+++each_start||f1||each_end||end||']
             ]



@zzy_ddt('md2data')
def test_md2data(test_data):
    return data2str(test_data['data_list'], test_data['rules']).str

class _:

    def smock(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        snap_t({'data':data_list},acc_data={'data': ['a1', 'b1', 'c1', 'a1', 'b1', 'c1']}, msg='tm11_look_data')

    def h_easy(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'start': 'start||',
                 'each_end': '||each_end',
                 'end': '||end||'}
        res = data2str(data_list, rules).str
        return res

    def easy(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'start': 'start||',
                 'each_start': 'each_start||',
                 'each_end': '||each_end',
                 'end': '||end||'}
        res = data2str(data_list, rules).str
        return res
        # snap_t(res,acc_data='start||each_start||a1||each_endeach_start||b1||each_endeach_start||c1||each_endeach_start||a1||each_endeach_start||b1||each_endeach_start||c1||each_end||end', msg='tm16_easy')

    def bef_each_start(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'bef_each_start': {'1': '-1',
                                    '3': '-1'},
                 'start':'start||',
                 'each_start': 'each_start||',
                 'each_end':'||each_end',
                 'end':'||end||'}
        # acc = 'start||start||each_start||a1||each_end||end||start||-1each_start||b1||each_end||end||start||each_start||c1||each_end||end||start||-1each_start||d1||each_end||end||start||each_start||e1||each_end||end||start||each_start||f1||each_end||end||'
        return data2str(data_list, rules)
        # snap_t(data2str(data_list, rules).str,acc_data=acc, msg='bef_each_start')

    def aft_each_start(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'aft_each_start': {'1': '-1',
                                    '3': '-1'},
                 'start':'start||',
                 'each_start': 'each_start||',
                 'each_end':'||each_end',
                 'end':'||end||'}
        acc = 'start||start||each_start||a1||each_end||end||start||each_start||-1b1||each_end||end||start||each_start||c1||each_end||end||start||each_start||-1d1||each_end||end||start||each_start||e1||each_end||end||start||each_start||f1||each_end||end||'

        snap_t(data2str(data_list, rules).str,acc_data=acc, msg="aft_each_start_{'aft_each_start': {'1': '-1','3': '-1'},'start':'start||','each_start': 'each_start||','each_end':'||each_end','end':'||end||'}")

    def bef_each_end(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'bef_each_end': {'1': '-1',
                                    '3': '-1'},
                 'start':'start||',
                 'each_start': 'each_start||',
                 'each_end':'||each_end',
                 'end':'||end||'}
        acc = 'start||start||each_start||a1||each_end||end||start||each_start||b1-1||each_end||end||start||each_start||c1||each_end||end||start||each_start||d1-1||each_end||end||start||each_start||e1||each_end||end||start||each_start||f1||each_end||end||'

        snap_t(data2str(data_list, rules).str,acc_data=acc, msg='bef_each_end')

    def aft_each_end(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'bef_each_end': {'1': '-1',
                                    '3': '-1'},
                 'start':'start||',
                 'each_start': 'each_start||',
                 'each_end':'||each_end',
                 'end':'||end||'}
        acc = 'start||start||each_start||a1||each_end||end||start||each_start||b1||each_end-1||end||start||each_start||c1||each_end||end||start||each_start||d1||each_end-1||end||start||each_start||e1||each_end||end||start||each_start||f1||each_end||end||'

        snap_t(data2str(data_list, rules).str,acc_data=acc, msg='aft_each_end')


    def hard(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'insert_data': {'1': '-1', '3': '-1'},'start':'start||', 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
        return snap_t(data2str(data_list, rules).str)

    def hard_bef_each_start(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'bef_each_start':{'0':'---'},'insert_data': {'0': '-1', '3': '-1'},'start':'start||',
                 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
        return snap_t(data2str(data_list, rules).str)

    def hard_aft_each_start(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'aft_each_start':{'0':'---'},'insert_data': {'0': '-1', '3': '-1'},'start':'start||',
                 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
        return snap_t(data2str(data_list, rules).str)

    def hard_bef_each_end(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'bef_each_end':{'0':'---'},'insert_data': {'0': '-1', '3': '-1'},'start':'start||',
                 'each_start': 'each_start||', 'each_end': '||each_end', 'end': '||end||'}
        return snap_t(data2str(data_list, rules).str)

    def hard_aft_each_end(self):
        data_list = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1']
        rules = {'aft_each_end':{'0':'---','3':'+++'},'insert_data': {'0': '-1', '3': '-1'},'start':'start||', 'end':'end||','each_start':'each_start||','each_end':'||each_end', 'end':'||end||'}
        return snap_t(data2str(data_list, rules).str)

def basics():
    t = _()
    t.smock()



if __name__ == '__main__':
    # basics()
    test_md2data(test_data)