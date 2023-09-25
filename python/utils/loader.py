import requests as req
from colorama import Fore as text_color
from colorama import Style as text_style
from sys import platform
from os import path


class Loader:
	@staticmethod
	def send_get_request():
		download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
		if platform == 'linux':
			target_csv_path = "dataset/nba.csv"
		else:
			target_csv_path = "python/dataset/nba.csv"

		if path.exists(target_csv_path):
			return

		response = req.get(download_url)
		if response.status_code == 200:
			with open(target_csv_path, "wb") as file:
				file.write(response.content)
			print(text_color.GREEN + "Download finished.")
		else:
			print(text_color.RED + "Error when downloading.")
		print(text_style.RESET_ALL)
