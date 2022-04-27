class data2str:
    def __init__(self, *args, **kwargs):
        self.each_end = ""
        self.each_start = ""
        self.end = ""
        self.start = ""
        if len(args)>0:
            self.value = args[0]
        else:
            if 'value' in kwargs:
                self.value = kwargs['value']
            else:
                raise
        if 'each_end' in kwargs:
            self.each_end = kwargs['each_end']
        if 'each_start' in kwargs:
            self.each_start = kwargs['each_start']
        if 'end' in kwargs:
            self.end = kwargs['end']
        if 'start' in kwargs:
            self.start = kwargs['start']

    @property
    def str(self):
        return "".join([self.start, self.each_start,
                 ("".join([self.each_end , self.each_start]))
                       .join(self.value),self.each_end, self.end])