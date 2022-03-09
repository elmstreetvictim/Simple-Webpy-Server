import pygetwindow as gw
import cv2 as cv2
import numpy as np
import pyautogui as gui
from PIL import ImageGrab, Image
#from matplotlib import pyplot as plt

class screenHelper():

	def __init__(self):
		print('Created a screen helper')

	def GetWindowFromName(self, windowName):
		windows = gw.getWindowsWithTitle(windowName)
		if len(windows) > 0:
			return windows[0]
		#return None
	
	def TakeScreenshotOfDesktop(self):
		screen = gui.size()
		grab = ImageGrab.grab(bbox=(0, 0, screen.width, screen.height))
		grab.save('static/Desktop.png')
		
	def TakeScreenshotForWindow(self, windowName, with_filename):
		# this works do not fuck with it
		hsWindow = self.GetWindowFromName(windowName)
		#if hsWindow.isMinimized:
		#	hsWindow.restore()
		if hsWindow is not None:
			hsWindow.activate()
			hs_top = hsWindow.top
			hs_left = hsWindow.left
			hs_right = hsWindow.right
			hs_bottom = hsWindow.bottom
			grab = ImageGrab.grab(bbox=(hs_left, hs_top, hs_right, hs_bottom))
			grab.save(with_filename)

	def GetWindowSize(self, windowNameString):
		window = self.GetWindowFromName(windowNameString)
		if window is not None:
			window.activate()
			left = window.left
			top = window.top
			right = window.right
			bottom = window.bottom
			return (left, top, right, bottom)

	def WatchForTemplateOnScreen(self, templateName, windowName):
		# this works do not fuck with it
		hsWindow = self.GetWindowFromName(windowName)
		#if hsWindow.isMinimized:
		#	hsWindow.restore()
		if hsWindow is not None:
			hsWindow.activate()
			hs_top = hsWindow.top
			hs_left = hsWindow.left
			hs_right = hsWindow.right
			hs_bottom = hsWindow.bottom

			grab = ImageGrab.grab(
				bbox=(hs_left, hs_top, hs_right, hs_bottom)).convert('L')
			img_rgb = np.array(grab)
			template = cv2.imread(templateName, 0)
			height, width = template.shape[::]
			res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
			threshold = 0.8  # For TM_CCOEFF_NORMED, larger values = good fit.
			loc = np.where(res >= threshold)
			locations = []
			for pt in zip(*loc[::-1]):
				locations.append(pt[0] + width / 2 + hs_left)
				locations.append(pt[1] + height / 2 + hs_top)
				break
			return locations
		return []