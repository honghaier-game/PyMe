import tkinter

import tkinter.ttk

def SetupStyle():

    style = tkinter.ttk.Style()

    style.configure(".TLabel",background="#46a1ef",foreground="#ffffff",relief="flat")

    style.configure(".TButton",background="#46a1ef",foreground="#ffffff",activebackground="#eeeeee",activeforeground="#ffffff",relief="raised")

    style.configure(".TEntry",background="#46a1ef",foreground="#ffffff")

    style.configure(".TText",background="#46a1ef",foreground="#ffffff")

    style.configure(".TProgressbar",background="#46a1ef",foreground="#ffffff")

    style.configure(".TPanedWindow",background="#46a1ef",foreground="#ffffff",highlightthickness=0,bordercolor="#46a1ef",bd=0)

    style.configure(".TLabelframe",background="#46a1ef",foreground="#ffffff")

    style.configure(".TListbox",background="#46a1ef",foreground="#ffffff",highlightthickness=0)

    style.configure(".TCanvas",background="#46a1ef",highlightthickness=0)

    style.configure(".TCheckbutton",background="#46a1ef",foreground="#ffffff",activebackground="#46a1ef",activeforeground="#ffffff",relief="flat")

    style.configure(".TRadiobutton",background="#46a1ef",foreground="#ffffff",activebackground="#46a1ef",activeforeground="#ffffff",relief="flat")

    style.configure(".TSpinbox",background="#46a1ef",foreground="#ffffff",activebackground="#46a1ef",activeforeground="#ffffff",relief="flat")

    style.configure(".TScale",background="#46a1ef",foreground="#ffffff",relief="flat",highlightthickness=0,bordercolor="#46a1ef",bd=0)

    style.configure(".TFrame",background="#46a1ef",highlightthickness=0)

    style.theme_create('combostyle', parent='alt',

                            settings={'TCombobox':

                                        {'configure':

                                            {

                                                'foreground': '#ffffff',

                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色   

                                                'fieldbackground': '#46a1ef',  #  下拉框颜色

                                                'background': '#46a1ef',     # 背景颜色

                                                "font":10,   # 字体大小

                                                "font-weight": "bold"

                                            }

                                        },

                                      'Treeview':

                                        {'configure':

                                            {

                                                # 'foreground': 'white',

                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色

                                                'fieldbackground': '#46a1ef',  #  下拉框颜色

                                                'background': '#46a1ef',     # 背景颜色

                                                "font":10,   # 字体大小

                                                "font-weight": "bold"

                                            }

                                        },

                                      'TNotebook':

                                        {'configure':

                                            {

                                                # 'foreground': 'white',

                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色

                                                'fieldbackground': '#46a1ef',  #  下拉框颜色

                                                'background': '#46a1ef',     # 背景颜色

                                                "font":10,   # 字体大小

                                                "font-weight": "bold"

                                            }

                                        }



                                     }

                            )

    style.theme_use('combostyle')

    

    return style

