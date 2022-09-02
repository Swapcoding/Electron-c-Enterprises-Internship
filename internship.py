from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import bs4
import requests
from matplotlib.widgets import Button as Bt


def f1():
	marks=[]
	name=[]
	plt.bar(name,marks,color=['red','blue','green',])
	# create buttons area

	clear = plt.axes([0.58, 0.05, 0.15, 0.07])
	subplot = plt.axes([0.70, 0.05, 0.15, 0.07])

	button_clear = Bt(clear, "Clear", color = 'green')
	button_subplot = Bt(subplot, "Subplot", color = 'red')
	plt.xlabel("Name")
	plt.ylabel("Marks")
	plt.title("Batch Information")
	plt.show()

main_window = Tk()
main_window.title("S.M.S")
main_window.geometry("600x600+400+100")
main_window_btn_analysis = Button(main_window, text= "Analysis", font=('Arial', 20, 'bold'), width=10)
main_window_btn_graph = Button(main_window, text= "Graph", font=('Arial', 20, 'bold'), width=10, command=f1)

main_window_btn_analysis.pack(pady=100)
main_window_btn_graph.pack(pady=10)

main_window.mainloop()