def diff(a, b):
    if type(a) != type(b):
        # print(1)
        return False
    # elif type(a) == str or type(a) == int or type(a) == bytes:
    elif type(a) == int:
        if a == b:
            # print(2)
            return True
        else:
            # print(a,b,3)
            # print(type(a), type(b), 3)
            return False
    elif type(a) == str:
        #  or bytes
        if a in b:
            return True
        else:
            return False
    elif type(a) == dict:
            for i in a:
                # snap_t((a[i], b[i], diff(a[i], b[i])), msg=i)
                if diff(a[i], b[i]) == False:
                    # print(4)
                    return False
    elif type(a) == list:
        for i in a:
            res = False
            for j in b:
                if diff(i, j) == True:
                    res = True
                    break
            if res == False:
                return False
        return True


    # print(6)
    return True
numb=1


def run_fn(fun):
    def in_fun_fn(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            return e
    return in_fun_fn

def get_res(fun):
    try:
        return fun
    except Exception as e:
        return e



def snap_t(*args, **kwargs):
    def inn_snap(data):
        if type(data) == list:
            data_list = []
            for i in data:
                try:
                    if i.__dict__ != {}:
                        data_list.append(i.__dict__)
                    else:
                        data_list.append(i)
                except:
                    data_list.append(i)
            return data_list
        elif type(data) == dict:
            data_dict = {}
            for i in data:
                data_dict[i] = inn_snap(data[i])
            return data_dict
        elif type(data) == str or type(data) == int:
            return data

    if 'msg' in kwargs:
        my_msg = kwargs['msg']
    else:
        my_msg = ""
    res = {}

    if len(args) == 1:
        has_data = True
        arg_data = args[0]

    elif len(args) == 0:
        has_data = False
        arg_data = ""


    def show_data(orgi_data_dict="",white_log_list="",black_log_list=""):
        if white_log_list == "":
            if black_log_list=="":
                res = orgi_data_dict
            else:
                res = {}
                for i in orgi_data_dict:
                    if i not in black_log_list:
                        res[i] = orgi_data_dict[i]

        else:
            res = {}
            for i in orgi_data_dict:
                if i in white_log_list:
                    res[i] = orgi_data_dict[i]

        return res


    res['data'] = ""

    if has_data == True:
        res['orgi_data'] = inn_snap(arg_data)

        if 'show' in kwargs:
            show_config = kwargs['show']
        else:
            show_config = ""
        if 'hide' in kwargs:
            hide_config = kwargs['hide']
        else:
            hide_config = ""
        is_list = False
        if type(res['orgi_data']) == list:
            is_list = True
            res_list = []
            for i in res['orgi_data']:
               res_list.append(show_data(orgi_data_dict=i,white_log_list=show_config,black_log_list=hide_config))
            res['data'] = res_list
        elif type(res['orgi_data']) == dict:
            res['data'] = show_data(orgi_data_dict=res['orgi_data'], white_log_list=show_config, black_log_list=hide_config)
        else:
            res['data'] = res['orgi_data']
        my_acc = 'not_title'
        # print(f'orgi_data--{res["orgi_data"]}--')

    elif has_data == False:
        res['data'] = ""
        my_acc = 'title'
    elif has_data == False:
        pass

    if 'acc_data' in kwargs:
        res['acc_data'] = kwargs['acc_data']
        has_acc_data = True
    else:
        has_acc_data = False
    if has_acc_data == True:
        if my_acc != 'title':
            my_acc = diff(res['acc_data'], res['data'])
    elif has_acc_data == False:
        if my_acc == 'title':
            pass
        if my_acc != 'title':
            if res['data'] == None:
                my_acc = 'msg'
            else:
                my_acc = 'info'
    if 'msg' in kwargs:

        if 'run' in kwargs and kwargs['run'] in ['nomal', 'n']:
            if my_acc == 'title':
                print(f'\033[0;34m{my_msg}'.ljust(45, '-') + f'complete\033[0m')

        else:
            if my_acc == True:
                print(f'\033[0;32m[{my_msg}]'.ljust(50, '-')+f'{my_acc}\033[0m')
            elif my_acc == False:
                print(f'\033[0;31m[{my_msg}]'.ljust(50, '-')+f'{my_acc}\033[0m')
                print(f'\033[0;31m{type(res["data"])}|{res["data"]}\033[0m')
                print(f'\033[0;31m{type(res["acc_data"])}|{res["acc_data"]}\033[0m')
            elif my_acc == 'msg':
                print(f'\033[0;32m{my_msg}'.ljust(45, '-')+f'complete\033[0m')
            elif my_acc == "info":
                if is_list == True:
                    for i in res['data']:
                        print(f'\033[0;34m{my_msg}'.ljust(50, '-')+f'info\033[0m')
                        print(f'\033[0;34m{type(i)}|{i}\033[0m')
                else:
                    print(f'\033[0;34m{my_msg}'.ljust(50, '-') + f'info\033[0m')
                    print(f'\033[0;34m{type(res["data"])}|{res["data"]}\033[0m')
            elif my_acc == 'title':
                print(f'\033[0;34m' + f'{my_msg}'.rjust(43, "=") + f'{"".ljust(43, "=")}\033[0m')
    else:
        pass

    if res['data']:
        return res['data']
    else:
        None



class test_snap:


    def test_title(self):
        snap_t(msg='test_title')

    def test_true(self):
        snap_t('aa', acc_data='aa', msg='test_true')

    def test_false(self):
        snap_t('aa', acc_data='bb', msg='test_false')

    def test_info(self):
        snap_t('aa', msg='test_info')

    def test_msg(self):
        snap_t(None, msg='test_msg')
    @run_fn
    def err_fn(self):
        raise AssertionError('aa')

    def test_err(self):
        try:
            self.err_fn()
        except Exception as e:
            print('--', e)

    def tt(self, *args):
        return len(args)

if __name__ == '__main__':
    test_snap().test_title()
    test_snap().test_true()
    test_snap().test_false()
    test_snap().test_info()
    test_snap().test_msg()
    snap_t(test_snap().err_fn(), msg='test_err')
    # # # try:
    # # #     arg_data =test_snap().err_fn()
    # # #
    # # # except Exception as e:
    # # #     arg_data = e
    # # # print('==',arg_data,'==')
    # try:
    #     ff=test_snap().err_fn()
    # except Exception as e:
    #     print('--',e)
