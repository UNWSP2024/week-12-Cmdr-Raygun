# Author: Andrew Bittner
# Date: 11/23/2024
# Program #3: Long-distance Calls

import tkinter as tk
import tkinter.messagebox

class LDCallCalculator:
    def __init__(self):
        # Create window elements.
        self.instructions = ('Select the time frame for your call, then enter the duration of the call in minutes ('
                             'numbers only). Total cost will appear below.')

        self.root = tk.Tk()
        self.root.title('Long-distance Call Calculator')

        self.frm_main = tk.Frame(self.root)
        self.frm_entry = tk.Frame(self.frm_main)
        self.frm_total = tk.Frame(self.frm_main)

        self.total = tk.StringVar(value='0.00')
        self.minutes = tk.StringVar()
        self.var_rdbtn = tk.IntVar(value=0)

        self.rdbtn_1 = tk.Radiobutton(self.frm_main, text='Daytime (6:00 A.M. through 5:59 P.M.)', command=
                                      self.calc_cost, variable=self.var_rdbtn, value=1)
        self.rdbtn_2 = tk.Radiobutton(self.frm_main, text='Evening (6:00 P.M. through 11:59 P.M.)', command=
                                      self.calc_cost, variable=self.var_rdbtn, value=2)
        self.rdbtn_3 = tk.Radiobutton(self.frm_main, text='Off-peak (12:00 A.M. through 5:59 A.M.)', command=
                                      self.calc_cost, variable=self.var_rdbtn, value=3)
        self.entry_minutes = tk.Entry(self.frm_entry, textvariable=self.minutes, borderwidth=2)
        self.msg_instructions = tk.Message(self.frm_main, text=self.instructions, width=256, relief='ridge', borderwidth
                                           =3)
        self.lbl_minutes = tk.Label(self.frm_entry, text='Enter minutes: ')
        self.lbl_total_1 = tk.Label(self.frm_total, text='Total cost: $')
        self.lbl_total_2 = tk.Label(self.frm_total, textvariable=self.total)
        # self.lbl_total_2 = tk.Label(self.frm_total, text=self.total.get().format(.2))
        self.btn_exit = tk.Button(self.frm_main, text='Exit', command=self.root.destroy, width=8)

        # Setup window.
        self.msg_instructions.grid(row=0, column=0, columnspan=3, pady=(0, 4))
        self.rdbtn_1.grid(row=1, column=1, sticky='w', columnspan=1)
        self.rdbtn_2.grid(row=2, column=1, sticky='w', columnspan=1)
        self.rdbtn_3.grid(row=3, column=1, sticky='w', columnspan=1)
        self.lbl_minutes.pack(side='left')
        self.entry_minutes.pack(side='left')
        self.frm_entry.grid(row=4, column=0, columnspan=3, padx=8, pady=8)
        self.lbl_total_1.grid(row=0, column=0)
        self.lbl_total_2.grid(row=0, column=1)
        self.frm_total.grid(row=5, column=0, columnspan=3)
        self.btn_exit.grid(row=6, column=0, columnspan=3, pady=(4, 0))
        self.frm_main.pack(padx=16, pady=16)
        self.root.mainloop()

    def calc_cost(self):
        # Calculate cost of call based on time of radio button output (time of day).
        if self.var_rdbtn.get() == 1:
            self.total.set(f'{(float(self.minutes.get()) * 0.02):.2f}')
            print(self.total.get())
        elif self.var_rdbtn.get() == 2:
            self.total.set(f'{(float(self.minutes.get()) * 0.12):.2f}')
            print(self.total.get())
        elif self.var_rdbtn.get() == 3:
            self.total.set(f'{(float(self.minutes.get()) * 0.05):.2f}')
            print(self.total.get())
        else:
            tk.messagebox.showinfo(title='Error', message='Please select a time.')
            print(self.total.get())

if __name__ == '__main__':
    window1 = LDCallCalculator()