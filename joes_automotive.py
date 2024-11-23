# Author: Andrew Bittner
# Date: 11/23/2024
# Program #2: Joe's Automotive

import tkinter as tk

class AutoShopCalculator:
    def __init__(self):
        # Create window elements.
        self.instructions = 'Select the work you want done from the list below. Total total will appear below.'

        self.root = tk.Tk()
        self.root.title('Auto Shop Calculator')

        self.frm_main = tk.Frame(self.root)
        self.frm_total = tk.Frame(self.frm_main)

        self.total = tk.StringVar(value='0.00')
        self.var_chbtn_1 = tk.StringVar(value='0')
        self.var_chbtn_2 = tk.StringVar(value='0')
        self.var_chbtn_3 = tk.StringVar(value='0')
        self.var_chbtn_4 = tk.StringVar(value='0')
        self.var_chbtn_5 = tk.StringVar(value='0')
        self.var_chbtn_6 = tk.StringVar(value='0')
        self.var_chbtn_7 = tk.StringVar(value='0')

        self.chbtn_1 = tk.Checkbutton(self.frm_main, text='Oil change', command= self.oil_change, variable=
                                      self.var_chbtn_1)
        self.chbtn_2 = tk.Checkbutton(self.frm_main, text='Lube job', command=self.lube_job, variable=self.var_chbtn_2)
        self.chbtn_3 = tk.Checkbutton(self.frm_main, text='Radiator flush', command=self.radiator_flush, variable=
                                      self.var_chbtn_3)
        self.chbtn_4 = tk.Checkbutton(self.frm_main, text='Transmission fluid', command=self.transmission_fluid,
                                      variable=self.var_chbtn_4)
        self.chbtn_5 = tk.Checkbutton(self.frm_main, text='Inspection', command=self.inspection, variable=
                                      self.var_chbtn_5)
        self.chbtn_6 = tk.Checkbutton(self.frm_main, text='Muffler replacement', command=self.muffler_replacement,
                                      variable=self.var_chbtn_6)
        self.chbtn_7 = tk.Checkbutton(self.frm_main, text='Tire rotation', command=self.tire_rotation, variable=
                                      self.var_chbtn_7)

        self.msg_instructions = tk.Message(self.frm_main, text=self.instructions, width=256, relief='ridge', borderwidth
                                           =3)
        self.lbl_total_1 = tk.Label(self.frm_total, text='Total cost: $')
        self.lbl_total_2 = tk.Label(self.frm_total, textvariable=self.total)
        self.btn_exit = tk.Button(self.frm_main, text='Exit', command=self.root.destroy, width=8)

        # Setup window.
        self.msg_instructions.grid(row=0, column=0, columnspan=3, pady=(0, 4))
        self.chbtn_1.grid(row=1, column=1, sticky='w', columnspan=1)
        self.chbtn_2.grid(row=2, column=1, sticky='w', columnspan=1)
        self.chbtn_3.grid(row=3, column=1, sticky='w', columnspan=1)
        self.chbtn_4.grid(row=4, column=1, sticky='w', columnspan=1)
        self.chbtn_5.grid(row=5, column=1, sticky='w', columnspan=1)
        self.chbtn_6.grid(row=6, column=1, sticky='w', columnspan=1)
        self.chbtn_7.grid(row=7, column=1, sticky='w', columnspan=1)
        self.lbl_total_1.grid(row=0, column=0)
        self.lbl_total_2.grid(row=0, column=1)
        self.frm_total.grid(row=8, column=0, columnspan=3)
        self.btn_exit.grid(row=9, column=0, columnspan=3, pady=(4, 0))
        self.frm_main.pack(padx=16, pady=16)
        self.root.mainloop()

    # Following 7 functions: Change total price based on different options selected above.
    def oil_change(self):
        if self.var_chbtn_1.get() == '1':
            self.total.set(f'{(float(self.total.get()) + 30.0):.2f}')
        elif self.var_chbtn_1.get() == '0':
            self.total.set(f'{(float(self.total.get()) - 30.0):.2f}')
        print(self.total.get())

    def lube_job(self):
        if self.var_chbtn_2.get() == '1':
            self.total.set(f'{(float(self.total.get()) + 20.0):.2f}')
        if self.var_chbtn_2.get() == '0':
            self.total.set(f'{(float(self.total.get()) - 20.0):.2f}')
        print(self.total.get())

    def radiator_flush(self):
        if self.var_chbtn_3.get() == '1':
            self.total.set(f'{(float(self.total.get()) + 40.0):.2f}')
        if self.var_chbtn_3.get() == '0':
            self.total.set(f'{(float(self.total.get()) - 40.0):.2f}')
        print(self.total.get())

    def transmission_fluid(self):
        if self.var_chbtn_4.get() == '1':
            self.total.set(f'{(float(self.total.get()) + 100.0):.2f}')
        if self.var_chbtn_4.get() == '0':
            self.total.set(f'{(float(self.total.get()) - 100.0):.2f}')
        print(self.total.get())

    def inspection(self):
        if self.var_chbtn_5.get() == '1':
            self.total.set(f'{(float(self.total.get()) + 35.0):.2f}')
        if self.var_chbtn_5.get() == '0':
            self.total.set(f'{(float(self.total.get()) - 35.0):.2f}')
        print(self.total.get())

    def muffler_replacement(self):
        if self.var_chbtn_6.get() == '1':
            self.total.set(f'{(float(self.total.get()) + 200.0):.2f}')
        if self.var_chbtn_6.get() == '0':
            self.total.set(f'{(float(self.total.get()) - 200.0):.2f}')
        print(self.total.get())

    def tire_rotation(self):
        if self.var_chbtn_7.get() == '1':
            self.total.set(f'{(float(self.total.get()) + 20.0):.2f}')
        if self.var_chbtn_7.get() == '0':
            self.total.set(f'{(float(self.total.get()) - 20.0):.2f}')
        print(self.total.get())

if __name__ == '__main__':
    window1 = AutoShopCalculator()