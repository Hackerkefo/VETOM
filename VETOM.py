P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["Bangladesh","India","Indonesia"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(M))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "Nigeria" == fc:
		__import__("VETOM").lisensi()
	else:
		__import__("VETOM").lisensi()

