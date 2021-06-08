import re
"""
File Cleaning Class
Prepares a DHT file that has been filtered for users
to be formed into a data set. Cleans out all the artifacts
from Discord and messages that are too short to be meaningful
"""
class FileCleaner():
	# Expects to recieve the exact PATH of the file.
	def __init__(self, file):
		self.file = file
		# TODO: Add error handling if file format
		# isn't what is to be expected.
		with open(file, 'r', encoding='utf-8') as read_file:
			self.text = read_file.read()

	def build_data_file(self):
		with open('./text_files/fixed_dht.txt', 'w', encoding='utf-8') as write_file:
			write_file.write(self.fix_text())

	def fix_text(self):
		data = self.text
		data = self.run_regex(r'"},"(\d*?)":{"\w*?":\d*?,"\w*?":\d*?,"\w*?":"', data)
		return data

	def run_regex(self, regex_string, text):
		text = re.split(regex_string, text)
		text = '\n'.join(text)
		text = ' '.join(text.split())
		return text

	def get_file(self):
		print('File: {file}')
		return file

	def set_file(self, file):
		self.file = file