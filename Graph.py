import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import dateutil

from tkinter import *

resolution = '400x300'


class ErrorWindow(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master

		self.init_window()

	def init_window(self):

		self.master.title("Error Message")
		self.pack(side='top', fill=BOTH, expand=1)

		my_menu = Menu(self.master)
		self.master.config(menu=my_menu)

		file = Menu(my_menu)
		file.add_command(label='Save')
		file.add_command(label='Exit', command=self.client_exit)
		my_menu.add_cascade(label='File', menu=file)

		if wrong_num_values:
			text = Label(self, text='Mismatch in number of entries')
			text.pack()
		else:
			text = Label(self, text='Incorrect format of values')
			text.pack()

		ok_button = Button(self, text="OK", command=self.ok_command, fg='red', bg='black')
		ok_button.pack()

	@staticmethod
	def ok_command():
		root.destroy()

	@staticmethod
	def client_exit():
		root.destroy()


class MainWindow(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master

		self.input_data = None
		self.data = None

		# Start of Background colour options

		self.col_back_dict = dict()

		self.col_back_dict['white'] = BooleanVar()
		self.col_back_dict['white'].set(1)

		self.col_back_dict['red'] = BooleanVar()
		self.col_back_dict['red'].set(0)

		self.col_back_dict['green'] = BooleanVar()
		self.col_back_dict['green'].set(0)

		self.col_back_dict['blue'] = BooleanVar()
		self.col_back_dict['blue'].set(0)

		self.col_back_dict['black'] = BooleanVar()
		self.col_back_dict['black'].set(0)

		for key in self.col_back_dict:
			if self.col_back_dict[key].get():
				self.back_colour = key

		# End of Background colour options

		# Start of Point Arrow colour options

		self.col_v_point_dict = dict()

		self.col_v_point_dict['w'] = BooleanVar()
		self.col_v_point_dict['w'].set(0)

		self.col_v_point_dict['r'] = BooleanVar()
		self.col_v_point_dict['r'].set(0)

		self.col_v_point_dict['g'] = BooleanVar()
		self.col_v_point_dict['g'].set(0)

		self.col_v_point_dict['b'] = BooleanVar()
		self.col_v_point_dict['b'].set(0)

		self.col_v_point_dict['k'] = BooleanVar()
		self.col_v_point_dict['k'].set(1)

		for key in self.col_v_point_dict:
			if self.col_v_point_dict[key].get():
				self.v_point_colour = key

		# End of Point Arrow colour options

		# Start of Point Dot colour options

		self.col_point_dict = dict()

		self.col_point_dict['w'] = BooleanVar()
		self.col_point_dict['w'].set(0)

		self.col_point_dict['r'] = BooleanVar()
		self.col_point_dict['r'].set(0)

		self.col_point_dict['g'] = BooleanVar()
		self.col_point_dict['g'].set(0)

		self.col_point_dict['b'] = BooleanVar()
		self.col_point_dict['b'].set(0)

		self.col_point_dict['k'] = BooleanVar()
		self.col_point_dict['k'].set(1)

		for key in self.col_point_dict:
			if self.col_point_dict[key].get():
				self.point_colour = key

		# End of Point Dot colour options

		self.init_window()

		root.protocol('WM_DELETE_WINDOW', self.save_exit)

	def init_window(self):

		self.master.title("Input for Plot")
		self.pack(side='top', fill=BOTH, expand=1)

		my_menu = Menu(self.master, tearoff=False)

		self.master.config(menu=my_menu)

		file = Menu(my_menu, tearoff=False)
		# file.add_command(label='Save')
		file.add_command(label='Exit', command=self.client_exit)
		my_menu.add_cascade(label='File', menu=file)

		edit = Menu(my_menu, tearoff=False)
		sub_back_colour = Menu(edit, tearoff=False)
		sub_v_point_colour = Menu(edit, tearoff=False)
		sub_point_colour = Menu(edit, tearoff=False)

		edit.add_cascade(label='Colour of Background', menu=sub_back_colour)
		sub_back_colour.add_checkbutton(label='White', command=self.back_colour_set,
		                                variable=self.col_back_dict['white'])
		sub_back_colour.add_checkbutton(label='Red', command=self.back_colour_set,
		                                variable=self.col_back_dict['red'])
		sub_back_colour.add_checkbutton(label='Green', command=self.back_colour_set,
		                                variable=self.col_back_dict['green'])
		sub_back_colour.add_checkbutton(label='Blue', command=self.back_colour_set,
		                                variable=self.col_back_dict['blue'])
		sub_back_colour.add_checkbutton(label='Black', command=self.back_colour_set,
		                                variable=self.col_back_dict['black'])

		edit.add_cascade(label='Colour of Arrow Points', menu=sub_v_point_colour)
		sub_v_point_colour.add_checkbutton(label='White', command=self.v_point_colour_set,
		                                 variable=self.col_v_point_dict['w'])
		sub_v_point_colour.add_checkbutton(label='Red', command=self.v_point_colour_set,
		                                 variable=self.col_v_point_dict['r'])
		sub_v_point_colour.add_checkbutton(label='Green', command=self.v_point_colour_set,
		                                 variable=self.col_v_point_dict['g'])
		sub_v_point_colour.add_checkbutton(label='Blue', command=self.v_point_colour_set,
		                                 variable=self.col_v_point_dict['b'])
		sub_v_point_colour.add_checkbutton(label='Black', command=self.v_point_colour_set,
		                                 variable=self.col_v_point_dict['k'])

		edit.add_cascade(label='Colour of Dot Points', menu=sub_point_colour)
		sub_point_colour.add_checkbutton(label='White', command=self.point_colour_set,
		                                 variable=self.col_point_dict['w'])
		sub_point_colour.add_checkbutton(label='Red', command=self.point_colour_set,
		                                 variable=self.col_point_dict['r'])
		sub_point_colour.add_checkbutton(label='Green', command=self.point_colour_set,
		                                 variable=self.col_point_dict['g'])
		sub_point_colour.add_checkbutton(label='Blue', command=self.point_colour_set,
		                                 variable=self.col_point_dict['b'])
		sub_point_colour.add_checkbutton(label='Black', command=self.point_colour_set,
		                                 variable=self.col_point_dict['k'])

		my_menu.add_cascade(label='Edit', menu=edit)

		text = Label(self, text='Input Data Format:\n[Time] [BP] [Heart Rate]')
		text.pack()

		self.input_data = Text(self, width=30, height=10)
		self.input_data.pack(expand=False)

		# text = Label(self, text='Input Time Values')
		# text.pack()

		# input_time = Entry(self, textvariable=time_var)
		# input_time.insert(END, '10 20 30 40 50 60 70 80 90 100 110 120 130 140 150')
		# input_time.pack(side='bottom', fill='x')

		ok_button = Button(self, text="OK", command=self.ok_command, fg='white', bg='gray')
		ok_button.pack()

	def back_colour_set(self):
		if self.col_back_dict['white'].get() and self.back_colour != 'white':
			self.back_colour = 'white'
			self.back_colour_tick_del()
			self.col_back_dict['white'].set(1)
		elif self.col_back_dict['red'].get() and self.back_colour != 'red':
			self.back_colour = 'red'
			self.back_colour_tick_del()
			self.col_back_dict['red'].set(1)
		elif self.col_back_dict['green'].get() and self.back_colour != 'green':
			self.back_colour = 'green'
			self.back_colour_tick_del()
			self.col_back_dict['green'].set(1)
		elif self.col_back_dict['blue'].get() and self.back_colour != 'blue':
			self.back_colour = 'blue'
			self.back_colour_tick_del()
			self.col_back_dict['blue'].set(1)
		elif self.col_back_dict['black'].get() and self.back_colour != 'black':
			self.back_colour = 'black'
			self.back_colour_tick_del()
			self.col_back_dict['black'].set(1)

	def back_colour_tick_del(self):
		self.col_back_dict['white'].set(0)
		self.col_back_dict['red'].set(0)
		self.col_back_dict['green'].set(0)
		self.col_back_dict['blue'].set(0)
		self.col_back_dict['black'].set(0)

	def v_point_colour_set(self):
		if self.col_v_point_dict['w'].get() and self.v_point_colour != 'w':
			self.v_point_colour = 'w'
			self.v_point_colour_tick_del()
			self.col_v_point_dict['w'].set(1)
		elif self.col_v_point_dict['r'].get() and self.v_point_colour != 'r':
			self.v_point_colour = 'r'
			self.v_point_colour_tick_del()
			self.col_v_point_dict['r'].set(1)
		elif self.col_v_point_dict['g'].get() and self.v_point_colour != 'g':
			self.v_point_colour = 'g'
			self.v_point_colour_tick_del()
			self.col_v_point_dict['g'].set(1)
		elif self.col_v_point_dict['b'].get() and self.v_point_colour != 'b':
			self.v_point_colour = 'b'
			self.v_point_colour_tick_del()
			self.col_v_point_dict['b'].set(1)
		elif self.col_v_point_dict['k'].get() and self.v_point_colour != 'k':
			self.v_point_colour = 'k'
			self.v_point_colour_tick_del()
			self.col_v_point_dict['k'].set(1)

	def v_point_colour_tick_del(self):
		self.col_v_point_dict['w'].set(0)
		self.col_v_point_dict['r'].set(0)
		self.col_v_point_dict['g'].set(0)
		self.col_v_point_dict['b'].set(0)
		self.col_v_point_dict['k'].set(0)

	def point_colour_set(self):
		if self.col_point_dict['w'].get() and self.point_colour != 'w':
			self.point_colour = 'w'
			self.point_colour_tick_del()
			self.col_point_dict['w'].set(1)
		elif self.col_point_dict['r'].get() and self.point_colour != 'r':
			self.point_colour = 'r'
			self.point_colour_tick_del()
			self.col_point_dict['r'].set(1)
		elif self.col_point_dict['g'].get() and self.point_colour != 'g':
			self.point_colour = 'g'
			self.point_colour_tick_del()
			self.col_point_dict['g'].set(1)
		elif self.col_point_dict['b'].get() and self.point_colour != 'b':
			self.point_colour = 'b'
			self.point_colour_tick_del()
			self.col_point_dict['b'].set(1)
		elif self.col_point_dict['k'].get() and self.point_colour != 'k':
			self.point_colour = 'k'
			self.point_colour_tick_del()
			self.col_point_dict['k'].set(1)

	def point_colour_tick_del(self):
		self.col_point_dict['w'].set(0)
		self.col_point_dict['r'].set(0)
		self.col_point_dict['g'].set(0)
		self.col_point_dict['b'].set(0)
		self.col_point_dict['k'].set(0)

	def ok_command(self):
		global should_plot
		should_plot = True

		self.data = self.input_data.get("1.0", END)
		root.destroy()

	@staticmethod
	def client_exit():
		root.destroy()
		global done
		done = True

	def save_exit(self):
		self.data = self.input_data.get("1.0", END)
		root.destroy()

done = False

try:
	with open('Saved Data.txt', 'r') as read_save:
		colour_line = read_save.readline()
		# print(colour_line)
		back_colour, v_point_colour, point_colour = colour_line.split()
		# print(back_colour)
		# print(v_point_colour)
		# print(point_colour)

		data = read_save.read()

except FileNotFoundError:
	myfile = open('Saved Data.txt', 'w+')
	myfile.close()

	data = ''
	back_colour = None
	v_point_colour = None
	point_colour = None

except ValueError:
	data = ''
	back_colour = None
	v_point_colour = None
	point_colour = None


while not done:
	should_plot = False
	invalid_data = False
	wrong_num_values = False

	root = Tk()
	root.iconbitmap('Graph Icon.ico')
	root.geometry(resolution)

	app_main = MainWindow(root)

	app_main.input_data.insert(0.0, data[:-1])

	if back_colour is None:
		back_colour = app_main.back_colour
		v_point_colour = app_main.v_point_colour
		point_colour = app_main.point_colour
	else:
		app_main.back_colour = back_colour
		app_main.v_point_colour = v_point_colour
		app_main.point_colour = point_colour

		# print(back_colour)

		for col_back in app_main.col_back_dict:
			if col_back == back_colour:
				app_main.col_back_dict[col_back].set(1)
			else:
				app_main.col_back_dict[col_back].set(0)

		for col_v_point in app_main.col_v_point_dict:
			if col_v_point == v_point_colour:
				app_main.col_v_point_dict[col_v_point].set(1)
			else:
				app_main.col_v_point_dict[col_v_point].set(0)

		for col_point in app_main.col_point_dict:
			if col_point == point_colour:
				app_main.col_point_dict[col_point].set(1)
			else:
				app_main.col_point_dict[col_point].set(0)

	root.mainloop()

	back_colour = app_main.back_colour
	v_point_colour = app_main.v_point_colour
	point_colour = app_main.point_colour
	data = app_main.data

	if should_plot:
		try:
			data = app_main.data

			upper_points = []
			lower_points = []
			time = []
			heart_rate = []

			format_data = []

			line_data = data.replace('/ ', '/').replace(', ', ' ').replace(',', ' ').split('\n')
			# print(line_data)

			for i in line_data:
				format_data.append(i.split())
			# print(format_data)

			for i in range(len(format_data)):
				for v in range(len(format_data[i])):
					if '/' in format_data[i][v]:
						a = format_data[i][v].split('/')
						del format_data[i][v]
						c = []
						for b in a:
							b = float(b)
							c.append(b)
						format_data[i].append(c)
			# print(format_data)

			for i in range(len(format_data)):
				if format_data[i]:
					if '.' in format_data[i][0]:
						format_data[i][0] = format_data[i][0].replace('.', ':')
					heart_rate.append(float(format_data[i][1]))
					upper_points.append(format_data[i][2][0])
					lower_points.append(format_data[i][2][1])
					format_data[i][2].append('Error Catcher')
					if '+' in format_data[i][0]:
						add_time = format_data[i][0][1:]

						if not time:
							prev_time = '00:00'
						else:
							prev_time = time[-1]

						add_hour, add_min = add_time.split(':')
						add_hour = int(add_hour)
						add_min = int(add_min)

						prev_hour, prev_min = prev_time.split(':')
						prev_hour = int(prev_hour)
						prev_min = int(prev_min)

						new_hour = prev_hour + add_hour
						new_min = prev_min + add_min

						if new_min >= 60:
							new_hour += new_min // 60
							new_min %= 60

						new_hour = str(new_hour)
						new_min = str(new_min)

						new_time = new_hour + ':' + new_min

						time.append(new_time)

					else:
						time.append(format_data[i][0])

			# print(time)
			# print(heart_rate)
			# print(upper_points)
			# print(lower_points)
		except (AttributeError, TypeError, IndexError):
			wrong_num_values = True
		except ValueError:
			invalid_data = True

		if not (invalid_data or wrong_num_values) and \
				(len(upper_points) ==
					 len(time) ==
					 len(lower_points) ==
					 len(heart_rate)) and time:

			# plt.plot(time, upper_points, app_main.v_point_colour + 'v', label='First Line')
			# plt.plot(time, lower_points, app_main.v_point_colour + '^', label='Second Line')
			plt.xlabel('Time')
			plt.ylabel('BP Readings')
			plt.title('Vitals Chart')
			# plt.legend(loc=1)
			plt.grid(linewidth=1)
			# plt.ylim([0, 260])
			plt.yticks(np.arange(0, max(upper_points) + 1, 25))
			ax = plt.gca()
			ax.set_facecolor(app_main.back_colour)
			ax.xaxis_date()

			times = [dateutil.parser.parse(s) for s in time]

			fake_times = [dateutil.parser.parse(s) for s in ['1:05', '22:55']]
			fake_data = [0, 260]

			xfmt = md.DateFormatter('%H:%M')
			ax.xaxis.set_major_formatter(xfmt)

			plt.plot_date(times, upper_points, app_main.v_point_colour + 'v')
			plt.plot_date(times, lower_points, app_main.v_point_colour + '^')
			plt.plot_date(times, heart_rate, app_main.point_colour + '.')

			# This is an invisible set of data to stretch out the axes
			plt.plot_date(fake_times, fake_data, alpha=0)

			ax.xaxis.set_major_locator(md.HourLocator())

			graph_shown = True

			plt.show()
		else:
			root = Tk()
			root.iconbitmap('Graph Icon.ico')
			root.geometry(resolution)

			app_error = ErrorWindow(root)

			root.mainloop()
	# print(data)
	else:
		with open('Saved Data.txt', 'w') as write_save:
			colours = back_colour + ' ' + v_point_colour + ' ' + point_colour
			write_save.write(colours)
			if data is None:
				data = ''
			write_save.write('\n' + data)

		done = True
