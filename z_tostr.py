import uuid


class data2str:
    def __init__(self, input_data, rules):
        self.value_snap_list = self.value_chain.snip_list
        self.value_dict = self.value_chain.dict
        self.value_chain = toChain(self.value, self.__dict__)
        easy_rule = ['start', 'end', 'each_end', 'each_start']
        nomal_rule = ['bef_each_start', 'aft_each_start', 'bef_each_end', 'aft_each_end']
        hard_rule = ['insert_data']
        self.degree = 'easy'
        # self.rules
        for i in rules:
            if i in hard_rule:
                if self.degree != 'hard':
                    self.degree = 'hard'
            elif i in nomal_rule:
                if self.degree == 'easy':
                    self.degree = 'normal'
            elif i in easy_rule:
                if self.degree == 'easy':
                    pass
            else:
                print('===', i, '===')
                raise UserWarning(f'rule里{i}没有设置')
        self.each_start = ""
        self.each_end = ""
        self.end = ""
        self.start = ""
        self.bef_each_start = {}
        self.bef_each_end = {}
        self.aft_each_start = {}
        self.aft_each_end = {}
        self.insert_data = {}
        if 'each_start' in rules:
            self.each_start = rules.get('each_start')
        if 'each_end' in rules:
            self.each_end = rules.get('each_end')
        if 'end' in rules:
            self.end = rules.get('end')
        if 'start' in rules:
            self.start = rules.get('start')
        if 'bef_each_start' in rules:
            self.bef_each_start = rules.get('bef_each_start')
        if 'bef_each_end' in rules:
            self.bef_each_end = rules.get('bef_each_end')
        if 'aft_each_start' in rules:
            self.aft_each_start = rules.get('aft_each_start')
        if 'aft_each_end' in rules:
            self.aft_each_end = rules.get('aft_each_end')
        if 'insert_data' in rules:
            self.insert_data = rules.get('insert_data')
        self.value = input_data

    @property
    def str(self):
        if self.degree == 'easy':
            # print('easy')
            return "".join([self.start, self.each_start,
                            ("".join([self.each_end, self.each_start])).join(self.value), self.each_end, self.end])
        elif self.degree == 'normal':
            # print('normal')
            res_list = []
            res_list.append(self.start)

            for i in range(len(self.value)):
                bef_each_start = ""
                aft_each_start = ""
                bef_each_end = ""
                aft_each_end = ""

                if self.bef_each_start.get(f'{i}') is not None:
                    bef_each_start = self.bef_each_start.get(f'{i}')

                if self.aft_each_start.get(f'{i}') is not None:
                    aft_each_start = self.aft_each_start.get(f'{i}')

                if self.bef_each_end.get(f'{i}') is not None:
                    bef_each_end = self.bef_each_end.get(f'{i}')

                if self.aft_each_end.get(f'{i}') is not None:
                    aft_each_end = self.aft_each_end.get(f'{i}')

                res_list.append(self.start)

                res_list.append("".join([bef_each_start, self.each_start,
                                         aft_each_start, self.value[i], bef_each_end, self.each_end, aft_each_end]))
                res_list.append(self.end)
            res = "".join(res_list)

            return res
        elif self.degree == 'hard':
            for i in self.insert_data:
                self.value_chain.insert_data(self.insert_data[i], int(i))
            res = "".join([i['value'] for i in self.value_chain.new_list])

            return res


class toChain:
    def __init__(self, data_list, orgi_dict):
        self.tid = "home"
        self.fid = ""
        self.res_dict = {}
        self.res_list = []
        self.orgi_dict = orgi_dict
        self.bef_each_start = orgi_dict.get('bef_each_start')
        self.each_start = orgi_dict.get('each_start')
        self.aft_each_start = orgi_dict.get('aft_each_start')
        self.bef_each_end = orgi_dict.get('bef_each_end')
        self.each_end = orgi_dict.get('each_end')
        self.aft_each_end = orgi_dict.get('aft_each_end')
        for i in range(len(data_list)):
            eid = uuid.uuid4().hex
            bef_each_start = ""
            aft_each_start = ""
            bef_each_end = ""
            aft_each_end = ""
            if self.bef_each_start is not None and self.aft_each_start is not None and self.bef_each_end != None and self.aft_each_end != None:
                if f'{i}' in self.bef_each_start:
                    bef_each_start = self.bef_each_start[f'{i}']
                if f'{i}' in self.aft_each_start:
                    aft_each_start = self.aft_each_start[f'{i}']
                if f'{i}' in self.bef_each_end:
                    bef_each_end = self.bef_each_end[f'{i}']
                if f'{i}' in self.aft_each_end:
                    aft_each_end = self.aft_each_end[f'{i}']
            # snap_t({'err':data_list},msg='--err--')
            self.res_dict[eid] = {'id': eid, 'value': "".join([bef_each_start,
                                                               self.each_start,
                                                               aft_each_start,
                                                               data_list[i],
                                                               bef_each_end,
                                                               self.each_end,
                                                               aft_each_end])}
            if self.tid == 'home':
                self.fid = eid
                self.res_dict[eid]['pid'] = 'home'
            else:
                self.res_dict[eid]['pid'] = self.tid
                self.res_dict[self.tid]['cid'] = eid
            if i == len(data_list) - 1:
                self.res_dict[eid]['cid'] = self.fid
                self.res_dict[self.fid]['pid'] = eid
            self.res_list.append(eid)
            self.tid = eid

    def insert_data(self, inst_data, inst_index):
        if type(inst_data) == str:
            inst_data = [inst_data]
        not_each = ['bef_each_start', 'bef_each_end', 'aft_each_start', 'aft_each_end']
        inst_dict = {}
        for i in self.orgi_dict:
            if i not in not_each:
                inst_dict[i] = self.orgi_dict[i]
        inst_data = toChain(inst_data, inst_dict)
        inst_data_dict = inst_data.dict
        inst_data_list = inst_data.snip_list
        first_data = inst_data_dict[inst_data_list[0]]
        end_data = inst_data_dict[inst_data_list[-1]]
        if inst_index == 0:
            self.fid = first_data['id']
        elif inst_index == len(self.res_list):
            inst_index = 0
        elif inst_index > len(self.res_list):
            raise IOError(f'{inst_index}>{len(self.res_list)}  inst_index不能大于列表长度')
        inst_index_uid = self.res_list[inst_index]
        aft_data = self.res_dict[inst_index_uid]
        bef_data = self.res_dict[aft_data['pid']]

        bef_data['cid'] = first_data['id']
        first_data['pid'] = bef_data['id']
        end_data['cid'] = aft_data['id']
        aft_data['pid'] = end_data['id']
        self.res_dict.update(inst_data_dict)

    @property
    def new_list(self):
        res = []
        while len(res) < len(self.res_dict):
            if len(res) == 0:
                res.append(self.res_dict[self.fid])
            else:
                res.append(self.res_dict[res[-1]['cid']])
        return res

    @property
    def new_pay_list(self):
        temp = []
        res = []
        while len(res) < len(self.res_dict):
            if len(res) == 0:
                temp.append(self.res_dict[self.fid])
                res.append(temp[-1]['id'])
            else:
                temp.append(self.res_dict[temp[-1]['cid']])
                res.append(temp[-1]['id'])
        return res

    @property
    def dict(self):
        return self.res_dict

    @dict.setter
    def dict(self, value):
        self.res_dict = value

    @property
    def snip_list(self):
        return self.res_list

    @snip_list.setter
    def snip_list(self, value):
        self.res_list = value

    @property
    def first_id(self):
        return self.fid

    @first_id.setter
    def first_id(self, value):
        self.first_id = value
