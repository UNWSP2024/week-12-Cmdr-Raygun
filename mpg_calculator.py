# Author: Andrew Bittner
# Date: 11/23/2024
# Program #1: MPG Calculator

import tkinter as tk
import tkinter.messagebox

class MPGCalculator:
    def __init__(self):
        # Create window elements.
        self.instructions = ('Input gas tank capacity and mileage from a full tank (integers only), then press '
                             '"Calculate".')
        self.root = tk.Tk()
        self.root.title('MPG Calculator')
        self.frm_main = tk.Frame(self.root)
        self.frm_sub_1 = tk.Frame(self.frm_main)
        self.frm_sub_2 = tk.Frame(self.frm_main)
        self.msg_instructions = tk.Message(self.frm_main, text=self.instructions, width=256, relief='ridge', borderwidth
                                           =3)
        self.tank_capacity = tk.StringVar()
        self.full_tank_mileage = tk.StringVar()
        self.lbl_tank_capacity = tk.Label(self.frm_main, text='Tank capacity:')
        self.lbl_full_tank_mileage = tk.Label(self.frm_main, text='Full tank mileage:')
        self.entry_tank_capacity = tk.Entry(self.frm_main, textvariable=self.tank_capacity, borderwidth=2)
        self.entry_full_tank_mileage = tk.Entry(self.frm_main, textvariable=self.full_tank_mileage, borderwidth=2)
        self.btn_calc = tk.Button(self.frm_sub_1, text='Calculate', command=self.calc_mpg, width=8)
        self.btn_exit = tk.Button(self.frm_sub_1, text='Exit', command=self.root.destroy, width=8)

        # Setup window.
        self.msg_instructions.grid(row=0, column=0, columnspan=3, padx=8, pady=8)
        self.entry_tank_capacity.grid(row=1, column=1, columnspan=1, padx=8, pady=8)
        self.entry_full_tank_mileage.grid(row=2, column=1, columnspan=1, padx=8, pady=8)
        self.lbl_tank_capacity.grid(row=1, column=0, sticky='e', pady=8)
        self.lbl_full_tank_mileage.grid(row=2, column=0, sticky='e', pady=8)
        self.btn_calc.pack(side='left', padx=4)
        self.btn_exit.pack(side='left', padx=4)
        self.frm_sub_1.grid(row=3, column=0, columnspan=3, padx=8, pady=8)
        self.frm_sub_2.grid(row=2, column=0, columnspan=3, padx=8, pady=8)
        self.frm_main.pack(padx=16, pady=16)
        self.root.mainloop()


    def calc_mpg(self):
        try:
            tkinter.messagebox.showinfo(title='MPG', message=f'{int(self.full_tank_mileage.get()) / int(self.tank_capacity.get()):.1f} miles per gallon')
        except ValueError as err:
            tkinter.messagebox.showinfo(title='Error', message='Please enter a valid value.')
        return

if __name__ == '__main__':
    window1 = MPGCalculator()