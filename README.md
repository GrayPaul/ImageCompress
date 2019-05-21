# ImageCompress
## Motivation
In many cases, we need to upload an image with the specified number of bytes. For example, we post an article on WeChat that requires the size of the image to be no more than 2 Mbytes.
## Goal
Compress jpg image to a specific bytes by python GUI  
python GUI编程实现图片压缩（目前只针对JPG文件）
## Method
1、When we look up the detail information of a jpg image in winsows system , the bytes of the image are usually not equal to the number of pixels multiply the bytes per pixel. The reason is jpg used to be compressed, while we cannot find the compress  ratio in windows system .   
2、In Pillow, when we save a image ,we can specify a quality, the bigger quality the more bytes
```Python  
im.save(counter, format='JPEG', subsampling=subsampling, quality=quality)
```
3、So, in order to convert the JPG image to specific bytes, we should find the  suitable qulity using Binary Search  
4、Tkinter is used to show the graphical interfaces  
5、pyinstaller is used to make a *.exe file 
