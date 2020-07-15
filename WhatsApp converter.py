if __name__ == "__main__":
    import os
    import re
    import pkg_resources.py2_warn
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    from tkinter.filedialog import asksaveasfile

    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(title = "Select the text file to convert")  # show an "Open" dialog box and return the path to the selected file
    with open('{}'.format(filename), 'r', encoding="utf-8") as f:

        f = ''.join(f.read())

        regex_date = re.compile(r'\d\d[\/]\d\d[\/]\d\d')
        matches = regex_date.finditer(f)
        matches_1 = regex_date.finditer(f)
        matches_list = regex_date.findall(f)
        date_start_is = [x.end() for x in matches]
        date_end_is = [x.start() for x in matches_1]
        from collections import defaultdict

        data_dic = defaultdict(list)

        index = []
        texts = []
        name_t = []
        date_start = matches_list[0]
        date_end = matches_list[-1]

        for i in range(len(matches_list) - 1):

            data = f[date_start_is[i]:date_end_is[i + 1]]
            check = data.split()

            check[0] = matches_list[i]

            try:
                nak = (' '.join(check[3:])).split(':')

                name = nak[0]
                if ('Messages' in name):
                    name = ''
                if (name == ''):
                    pass
                else:
                    name_t.append(name.strip())

            except IndexError:
                name = ' '
            try:
                time = check[1]
            except IndexError:
                time = '00:00'
            if (len(name.split()) > 1):
                text = ' '.join(check[5:])
            else:
                text = ' '.join(check[4:])

            datat = [time, name, text]
            index.append([check[0], time, name])

            texts.append(text)
            data_dic[check[0]].append(datat)

            date = check[0]
    name_t = set(name_t)
    name_t = list(name_t)
    text_length = len(texts)
    import pandas as pd
    import numpy as np

    index = pd.MultiIndex.from_tuples(index, names=['DATE', 'TIME', 'NAME'])
    hey = pd.DataFrame(texts, index)
    hey.columns = ['TEXTS']

    from tkinter import *
    from tkinter import ttk
    import tkinter as tk
    import time
    import tkinter
    from tkinter import messagebox

    # hide main window
    root = tkinter.Tk()
    root.withdraw()

    msg = ("WhatsApp Document Created",
           "Your total text exchanged between {} and {} from date {} to date {} are {} \n Kindly Save the document".format(
               name_t[0], name_t[1], date_start, date_end, text_length))

    import tkinter as tk
    from tkinter import messagebox


    def savethefile():
        from tkinter.filedialog import asksaveasfile

        files = [('Excel File', '*.csv')]

        file = asksaveasfile(title = "Choose where to save the file",filetypes=files, defaultextension=files)

        hey['TEXTS'] = hey['TEXTS'].map(lambda x: x.encode('unicode-escape').decode('utf-8'))
        hey.to_csv(file, header=True, encoding="utf-8")


    canvas1 = tk.Canvas(root, width=300, height=300)
    canvas1.pack()

    MsgBox = tk.messagebox.askquestion("WhatsApp Document Created",
                                       "Your total text exchanged between {} and {} from date {} to date {} are {} \nWould you like to Save the document ?".format(
                                           name_t[0], name_t[1], date_start, date_end, text_length), icon='warning')
    if MsgBox == 'no':
        root.destroy()
    else:
        savethefile()












