import time

from api.public.snap import snap_t
from api.read_md.tool.md2data import data2str


class _:
    def smock(self):
        data_list = ['a1', 'b1', 'c1', 'a1', 'b1', 'c1']
        snap_t({'data':data_list},acc_data={'data': ['a1', 'b1', 'c1', 'a1', 'b1', 'c1']}, msg='tm11_smock')

    def easy(self):
        data_list = ['a1', 'b1', 'c1', 'a1', 'b1', 'c1']
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
        acc = 'start||start||each_start||a1||each_end||end||start||-1each_start||b1||each_end||end||start||each_start||c1||each_end||end||start||-1each_start||d1||each_end||end||start||each_start||e1||each_end||end||start||each_start||f1||each_end||end||'
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

        snap_t(data2str(data_list, rules).str,acc_data=acc, msg='aft_each_start')

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
    # performance(t.easy(),'t.easy')
    time1 = time.time()
    for i in range(1000):
        t_d = t.easy()
        td = ""
    snap_t(f'data:{t.easy()} \n time:{time.time()-time1}',msg='t.easy')
    time1 = time.time()
    for i in range(1000):
        t_d = t.hard()
        td = ""
    snap_t(f'data:{t.bef_each_start()} \n time:{time.time() - time1}', msg='t.bef_each_data')

    # t.bef_each_start()
    t.aft_each_start()
    t.bef_each_end()

    time1 = time.time()
    for i in range(1000):
        t_d = t.hard()
        td = ""
    snap_t(f'data:{t.hard()} \n time:{time.time()-time1}', msg='t.hard')
    # t.t_insert_data1()

    time1 = time.time()
    for i in range(1000):
        t_d = t.hard_bef_each_start()
        td = ""
    snap_t(f'data:{t.hard_bef_each_start()} \n time:{time.time() - time1}', msg='t.hard_bef_each_start')

    time1 = time.time()
    for i in range(1000):
        t_d = t.hard_aft_each_start()
        td = ""
    snap_t(f'data:{t.hard_aft_each_start()} \n time:{time.time() - time1}', msg='t.hard_aft_each_start')

    time1 = time.time()
    for i in range(1000):
        t_d = t.hard_bef_each_end()
        td = ""
    snap_t(f'data:{t.hard_bef_each_end()} \n time:{time.time() - time1}', msg='t.hard_bef_each_end')

    time1 = time.time()
    for i in range(1000):
        t_d = t.hard_aft_each_end()
        td = ""
    snap_t(f'data:{t.hard_aft_each_end()} \n time:{time.time() - time1}', msg='t.hard_aft_each_end')



if __name__ == '__main__':
    basics()
