import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import *
from PIL import Image
import os

class file_counter(object):
	def __init__(self):
		self.position = self.size = 0

	def seek(self, offset, whence=0):
		if whence == 1:
			offset += self.position
		elif whence == 2:
			offset += self.size
		self.position = min(offset, self.size)

	def tell(self):
		return self.position

	def write(self, string):
		self.position += len(string)
		self.size = max(self.size, self.position)

class master():
	def __init__(self):
		self.m = tk.Tk(className="图片压缩（版本1.0）")
		self.file = StringVar()
		self.path = StringVar()
		self.size = StringVar()
		self.outputmessage = StringVar()
		Label(self.m, text="输入文件", font=24, width=20, height=3).grid(row=0)
		Label(self.m, text="输出路径", font=24, width=20, height=3).grid(row=1)
		Label(self.m, text="图片大小（MB）", font=24, width=20, height=3).grid(row=2)
		Label(self.m, text="消息", font=24, width=20, height=3).grid(row=3)
		self.inputfile = Entry(self.m, textvariable=self.file, width=80)
		self.inputfile.grid(row=0, column=1)
		self.outputpath = Entry(self.m, textvariable=self.path, width=80)
		self.outputpath.grid(row=1, column=1)
		self.SIZE = Entry(self.m, textvariable=self.size, width=80)
		self.SIZE.grid(row=2, column=1)
		Button(self.m, text="选择图片文件", width=20, font=24, command=self.selectFile, bg="white").grid(row=0, column=2)
		Button(self.m, text="选择输出文件夹", width=20, font=24, command=self.SelectPath, bg="white").grid(row=1, column=2)
		Button(self.m, text="执行压缩", width=20, font=24, command=lambda: self.smaller_than(self.inputfile.get(),
																							  self.SIZE.get(), self.outputpath.get())).grid(
			row=2, column=2)
		Entry(self.m, textvariable=self.outputmessage, width=80).grid(row=3, column=1)

	def selectFile(self):
		file_ = askopenfilename()
		self.file.set(file_)

	def SelectPath(self):
		path_ = askdirectory()
		self.path.set(path_)

	def smaller_than(self, inputfile, size, outputpath, guess=70, subsampling=1, low=1, high=100):
		inputpath, filename = os.path.split(inputfile)
		outputfile = outputpath + "/" + "new_" + filename

		if not os.path.exists(inputfile) or not os.path.exists(outputpath):
			self.outputmessage.set("Error : input image or output path don't exist")
			return
		else:
			if os.path.splitext(inputfile)[-1] != ".jpg":
				self.outputmessage.set("Error : input image isn't a jpg")
				return
			else:
				if size == "" or float(size)<=0:
					self.outputmessage.set("Please input a correct image size!")
				else:
					print(inputfile, outputfile)
					if inputfile == outputfile:
						self.outputmessage.set(
							"Warn : both path and filename of input and output are same ! input image will be covered!")
					else:
						self.outputmessage.set("Compress successfully")
					im = Image.open(inputfile)
					while low < high:
						counter = file_counter()
						im.save(counter, format='JPEG', subsampling=subsampling, quality=guess)
						if counter.size < float(size) * 1024 * 1024:
							low = guess
						else:
							high = guess - 1
						guess = (low + high + 1) // 2
					im.save(outputfile, format="JPEG", quality=low)
					return self.outputmessage

	def start(self):
		self.m.mainloop()


if __name__ == "__main__":
	m = master()
	m.start()

