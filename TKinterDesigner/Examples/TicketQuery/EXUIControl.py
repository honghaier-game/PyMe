# 版权声明：本文参考CSDN博主「我的眼_001」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/wodeyan001/article/details/86703034
# -*- coding: utf-8 -*- 
import calendar
import tkinter
datetime = calendar.datetime.datetime
timedelta = calendar.datetime.timedelta
#日历控件
class Calendar:
    def __init__(self, widget):
        self.master = widget
        fwday = calendar.SUNDAY
        year = datetime.now().year
        month = datetime.now().month
        locale = None
        self.Btn_callbackFun = None
        self.classname = None
        self.widgetname = None
        self.datebar_bg = 'black'
        self.datebar_fg = 'white'
        self.sel_bg = '#ecffc4'
        self.sel_fg = '#05640e'
        self._date = datetime(year, month, 1)
        self._selection = None # 设置为未选中日期
        self.G_Frame = widget
        self._cal = self.__get_calendar(locale, fwday)
        self.__setup_styles()       # 创建自定义样式
        self.__place_widgets()      # pack/grid 小部件
        self.__config_calendar()    # 调整日历列和安装标记
        # 配置画布和正确的绑定，以选择日期。
        self.__setup_selection()
        # 存储项ID，用于稍后插入。
        self._items = [self._calendar.insert('', 'end', values='') for _ in range(6)]
        # 在当前空日历中插入日期
        self._update()
    def keepbgColor(self):
        frame_bg = self.master.cget('bg')
        self.hframe.configure(bg=frame_bg)
        self.gframe.configure(bg=frame_bg)
        self.bframe.configure(bg=frame_bg)
        self.YearLabel.configure(bg=frame_bg)
        self.MonthLabel.configure(bg=frame_bg)

    #设置日期栏的背景色
    def setDatebarBgColor(self,bgcolor):
        self.datebar_bg = bgcolor
        self._calendar.tag_configure('header', background=self.datebar_bg,foreground=self.datebar_fg)
    #设置日期栏的前景色
    def setDatebarFgColor(self,fgColor):
        self.datebar_fg = fgColor
        self._calendar.tag_configure('header', background=self.datebar_bg,foreground=self.datebar_fg)
    #设置选中时的背景色
    def setSelectedBgColor(self,bgColor):
        self.sel_bg = bgColor
        self.__setup_selection()
    #设置选中时的前景色
    def setSelectedFgColor(self,fgColor):
        self.sel_fg = fgColor
        self.__setup_selection()
    #设置点击确定时的回调函数
    def setBtnCallBackFunction(self,callBackFun,classname,widgetname):
        self.Btn_callbackFun = callBackFun
        self.classname = classname
        self.widgetname = widgetname
    def __get_calendar(self, locale, fwday):
        # 实例化适当的日历类
        if locale is None:
            return calendar.TextCalendar(fwday)
        else:
            return calendar.LocaleTextCalendar(fwday, locale)
    def __setitem__(self, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            self._canvas['background'] = value
        elif item == 'selectforeground':
            self._canvas.itemconfigure(self._canvas.text, item=value)
        else:
            self.G_Frame.__setitem__(self, item, value)
    def __getitem__(self, item):
        if item in ('year', 'month'):
            return getattr(self._date, item)
        elif item == 'selectbackground':
            return self._canvas['background']
        elif item == 'selectforeground':
            return self._canvas.itemcget(self._canvas.text, 'fill')
        else:
            r = tkinter.ttk.tclobjs_to_py({item: tkinter.ttk.Frame.__getitem__(self, item)})
            return r[item]
    def __setup_styles(self):
        # 自定义TTK风格
        style = tkinter.ttk.Style(self.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))
    def __place_widgets(self):
        # 标头框架及其小部件
        Input_judgment_num = self.master.register(self.Input_judgment)  # 需要将函数包装一下，必要的
        frame_bg = self.master.cget('bg')
        self.hframe = tkinter.Frame(self.G_Frame,bg=frame_bg)
        self.gframe = tkinter.Frame(self.G_Frame,bg=frame_bg)
        self.bframe = tkinter.Frame(self.G_Frame,bg=frame_bg)
        self.hframe.pack(in_=self.G_Frame, side='top', pady=5, anchor='center')
        self.gframe.pack(in_=self.G_Frame, fill=tkinter.X, pady=5)
        self.bframe.pack(in_=self.G_Frame, side='bottom', pady=5)
        lbtn = tkinter.ttk.Button(self.hframe, style='L.TButton', command=self._prev_month)
        lbtn.grid(in_=self.hframe, column=0, row=0, padx=12)
        rbtn = tkinter.ttk.Button(self.hframe, style='R.TButton', command=self._next_month)
        rbtn.grid(in_=self.hframe, column=5, row=0, padx=12)
        self.CB_year = tkinter.ttk.Combobox(self.hframe, width = 5, values = [str(year) for year in range(datetime.now().year, datetime.now().year-11,-1)], validate = 'key', validatecommand = (Input_judgment_num, '%P'))
        self.CB_year.current(0)
        self.CB_year.grid(in_=self.hframe, column=1, row=0)
        self.CB_year.bind('<KeyPress>', lambda event:self._update(event, True))
        self.CB_year.bind("<<ComboboxSelected>>", self._update)
        self.YearLabel = tkinter.Label(self.hframe, text = 'Year', justify = 'left',bg=frame_bg)
        self.YearLabel.grid(in_=self.hframe, column=2, row=0, padx=(0,5))
        self.CB_month = tkinter.ttk.Combobox(self.hframe, width = 3, values = ['%02d' % month for month in range(1,13)], state = 'readonly')
        self.CB_month.current(datetime.now().month - 1)
        self.CB_month.grid(in_=self.hframe, column=3, row=0)
        self.CB_month.bind("<<ComboboxSelected>>", self._update)
        self.MonthLabel = tkinter.Label(self.hframe, text = 'Month', justify = 'left',bg=frame_bg)
        self.MonthLabel.grid(in_=self.hframe, column=4, row=0)
        # 日历部件
        self._calendar = tkinter.ttk.Treeview(self.gframe, show='', selectmode='none', height=7)
        self._calendar.pack(expand=1, fill='both', side='bottom', padx=5)
        tkinter.ttk.Button(self.bframe, text = 'OK', width = 6, command = lambda: self._exit(True)).grid(row = 0, column = 0, sticky = 'ns', padx = 20)
        tkinter.ttk.Button(self.bframe, text = 'Cancel', width = 6, command = self._exit).grid(row = 0, column = 1, sticky = 'ne', padx = 20)
        tkinter.Frame(self.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 0, rely = 0, relwidth = 1, relheigh = 2/200)
        tkinter.Frame(self.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 0, rely = 198/200, relwidth = 1, relheigh = 2/200)
        tkinter.Frame(self.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 0, rely = 0, relwidth = 2/200, relheigh = 1)
        tkinter.Frame(self.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 198/200, rely = 0, relwidth = 2/200, relheigh = 1)
    def __config_calendar(self):
        # cols = self._cal.formatweekheader(3).split()
        cols = ['SUN','MON','TUE','WED','THU','FRI','SAT']
        self._calendar['columns'] = cols
        self._calendar.tag_configure('header', background=self.datebar_bg,foreground=self.datebar_fg)
        self._calendar.insert('', 'end', values=cols, tag='header')
        # 调整其列宽
        font = tkinter.font.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='center')
    def __setup_selection(self):
        def __canvas_forget(evt):
            canvas.place_forget()
            self._selection = None
        self._font = tkinter.font.Font()
        self._canvas = canvas = tkinter.Canvas(self._calendar, background=self.sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=self.sel_fg, anchor='w')
        canvas.bind('<Button-1>', __canvas_forget)
        self._calendar.bind('<Configure>', __canvas_forget)
        self._calendar.bind('<Button-1>', self._pressed)
    def _build_calendar(self):
        year, month = self._date.year, self._date.month
        # update header text (Month, YEAR)
        header = self._cal.formatmonthname(year, month, 0)
        # 更新日历显示的日期
        cal = self._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            self._calendar.item(item, values=fmt_week)
    def _show_select(self, text, bbox):
        """为新的选择配置画布。"""
        x, y, width, height = bbox
        textw = self._font.measure(text)
        canvas = self._canvas
        canvas.configure(width = width, height = height)
        canvas.coords(canvas.text, (width - textw)/2, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self._calendar, x=x, y=y)
    def _pressed(self, evt = None, item = None, column = None, widget = None):
        """在日历的某个地方点击。"""
        if not item:
            x, y, widget = evt.x, evt.y, evt.widget
            item = widget.identify_row(y)
            column = widget.identify_column(x)
        if not column or not item in self._items:
            # 在工作日行中单击或仅在列外单击。
            return
        item_values = widget.item(item)['values']
        if not len(item_values): # 这个月的行是空的。
            return
        text = item_values[int(column[1]) - 1]
        if not text: # 日期为空
            return
        bbox = widget.bbox(item, column)
        if not bbox: # 日历尚不可见
            self.master.after(20, lambda : self._pressed(item = item, column = column, widget = widget))
            return
        # 更新，然后显示选择
        text = '%02d' % text
        self._selection = (text, item, column)
        self._show_select(text, bbox)
    def _prev_month(self):
        """更新日历以显示前一个月。"""
        self._canvas.place_forget()
        self._selection = None
        self._date = self._date - timedelta(days=1)
        self._date = datetime(self._date.year, self._date.month, 1)
        self.CB_year.set(self._date.year)
        self.CB_month.set(self._date.month)
        self._update()
    def _next_month(self):
        """更新日历以显示下一个月。"""
        self._canvas.place_forget()
        self._selection = None
        year, month = self._date.year, self._date.month
        self._date = self._date + timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        self._date = datetime(self._date.year, self._date.month, 1)
        self.CB_year.set(self._date.year)
        self.CB_month.set(self._date.month)
        self._update()
    def _update(self, event = None, key = None):
        """刷新界面"""
        if key and event.keysym != 'Return': return
        year = int(self.CB_year.get())
        month = int(self.CB_month.get())
        if year == 0 or year > 9999: return
        self._canvas.place_forget()
        self._date = datetime(year, month, 1)
        self._build_calendar() # 重建日历
        if year == datetime.now().year and month == datetime.now().month:
            day = datetime.now().day
            for _item, day_list in enumerate(self._cal.monthdayscalendar(year, month)):
                if day in day_list:
                    item = 'I00' + str(_item + 2)
                    column = '#' + str(day_list.index(day)+1)
                    self.master.after(100, lambda :self._pressed(item = item, column = column, widget = self._calendar))
    def _exit(self, confirm = False):
        if  self.Btn_callbackFun != None:
            self.Btn_callbackFun(self.classname,self.widgetname,confirm,self.selection())
        """退出窗口"""
        # if not confirm: self._selection = None
        # self.master.destroy()
    def selection(self):
        """返回表示当前选定日期的日期时间。"""
        if not self._selection: return None
        year, month = self._date.year, self._date.month
        return str(datetime(year, month, int(self._selection[0])))[:10]
    def Input_judgment(self, content):
        """输入判断"""
        # 如果不加上==""的话，就会发现删不完。总会剩下一个数字
        if content.isdigit() or content == "":
            return True
        else:
            return False
