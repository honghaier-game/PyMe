import tkinter

import tkinter.ttk

def SetupStyle():

    style = tkinter.ttk.Style()

    style.configure(".TLabel",background="#333333",foreground="#b8860b",relief="flat")

    style.configure(".TButton",background="#333333",foreground="#b8860b",activebackground="#000000",activeforeground="#b8860b",relief="raised")

    style.configure(".TEntry",background="#333333",foreground="#b8860b")

    style.configure(".TText",background="#333333",foreground="#b8860b")

    style.configure(".TProgressbar",background="#333333",foreground="#b8860b")

    style.configure(".TPanedWindow",background="#333333",foreground="#b8860b",highlightthickness=0,bordercolor="#333333",bd=0)

    style.configure(".TLabelframe",background="#333333",foreground="#b8860b")

    style.configure(".TListbox",background="#333333",foreground="#b8860b",highlightthickness=0)

    style.configure(".TCanvas",background="#333333",highlightthickness=0)

    style.configure(".TCheckbutton",background="#333333",foreground="#b8860b",activebackground="#333333",activeforeground="#b8860b",relief="flat")

    style.configure(".TRadiobutton",background="#333333",foreground="#b8860b",activebackground="#333333",activeforeground="#b8860b",relief="flat")

    style.configure(".TSpinbox",background="#333333",foreground="#b8860b",activebackground="#333333",activeforeground="#b8860b",relief="flat")

    style.configure(".TScale",background="#333333",foreground="#b8860b",relief="flat",highlightthickness=0,bordercolor="#333333",bd=0)

    style.configure(".TFrame",background="#333333",highlightthickness=0)
    
    style.theme_create('combostyle', parent='alt',

                            settings={'TCombobox':

                                        {'configure':

                                            {

                                                'foreground': '#b8860b',

                                                'selectbackground': 'black',   # 选择后的背景颜色   

                                                'fieldbackground': '#333333',  #  下拉框颜色

                                                'background': '#333333',     # 背景颜色

                                                "font":10,   # 字体大小

                                                "font-weight": "bold"

                                            }

                                        },

                                      'Treeview':

                                        {'configure':

                                            {

                                                # 'foreground': 'white',

                                                'selectbackground': 'black',   # 选择后的背景颜色

                                                'fieldbackground': '#333333',  #  下拉框颜色

                                                'background': '#333333',     # 背景颜色

                                                "font":10,   # 字体大小

                                                "font-weight": "bold"

                                            }

                                        },

                                      'TNotebook':

                                        {'configure':

                                            {

                                                # 'foreground': 'white',

                                                'selectbackground': 'black',   # 选择后的背景颜色

                                                'fieldbackground': '#333333',  #  下拉框颜色

                                                'background': '#333333',     # 背景颜色

                                                "font":10,   # 字体大小

                                                "font-weight": "bold"

                                            }

                                        }



                                     }

                            )

    style.theme_use('combostyle')

    

    return style

