import requests as req
from colorama import Fore as text_color
from colorama import Style as text_style

class Loader:
	def sendGetRequest(self):
		download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
		target_csv_path = "python/dataset/nba.csv"

		response = req.get(download_url)
		if response.status_code == 200:
			with open(target_csv_path, "wb") as file:
				file.write(response.content)
			print(text_color.GREEN + "Download ready.")
		else:
			print(text_color.RED + "Error when downloading.")
		print(text_style.RESET_ALL)