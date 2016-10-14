#gspread git: https://github.com/burnash/gspread
from Tkinter import *
import ttk
import tkFont
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('pi-spreadsheet-143506.json', scope)

gc = gspread.authorize(credentials)

focisheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1037uq5DzMHd1U70a0YlkyrQyR3VwLp-8550KlKvIdvs/edit#gid=0')

bent = focisheet.get_worksheet(0)
kint = focisheet.get_worksheet(1)
katlan = focisheet.get_worksheet(2)

win = Tk()

win.geometry("1024x768")

cimFont = tkFont.Font(family = 'consolas', size = 35, weight = 'bold')
meccsFont = tkFont.Font(family = 'consolas', size = 25)

bentColor = "blue"
kintColor = "red"
katlanColor = "green"


win.title("Elkovetkezendo meccsek")

cim = Label(win, text="Elkovetkezendo meccsek", font = cimFont)
cim.pack(side = TOP)

def screenupdate(benti, kinti, katlani):
	for widget in win.winfo_children():
			widget.destroy()

	print "Elkovetkezendo meccsek"

	win.title("Elkovetkezendo meccsek")

	cim = Label(win, text="Elkovetkezendo meccsek", font = cimFont)
	cim.pack(side = TOP)

	#benti palya

	bentL = Label(win, text = "Benti palya", font = meccsFont, fg=bentColor)
	bentL.place(x = 30, y = 45)

	m1text = meccsek_bent[benti][1] + " vs " + meccsek_bent[benti][2] + " Ekkor: " + meccsek_bent[benti][4]
	meccs1 = Label(win, text= m1text, font = meccsFont, fg=bentColor)
	meccs1.place(x = 50, y = 90)

	if (benti+1) <= maxWs(1):
		m2text = meccsek_bent[benti+1][1] + " vs " + meccsek_bent[benti+1][2] + " Ekkor: " + meccsek_bent[benti+1][4]
		meccs2 = Label(win, text= m2text, font = meccsFont, fg=bentColor)
		meccs2.place(x = 50, y = 135)

		if (benti + 2) <= maxWs(1):
			m3text = meccsek_bent[benti+2][1] + " vs " + meccsek_bent[benti+2][2] + " Ekkor: " + meccsek_bent[benti+2][4]
			meccs3 = Label(win, text= m3text, font = meccsFont, fg=bentColor)
			meccs3.place(x = 50, y = 180)

	#kinti palya

	bentL = Label(win, text = "Kinti palya", font = meccsFont, fg=kintColor)
	bentL.place(x = 30, y = 225+40)

	m1text = meccsek_kint[kinti][1] + " vs " + meccsek_kint[kinti][2] + " Ekkor: " + meccsek_kint[kinti][4]
	meccs1 = Label(win, text= m1text, font = meccsFont, fg=kintColor)
	meccs1.place(x = 50, y = 270+40)

	if (kinti+1) <= maxWs(2):
		m2text = meccsek_kint[kinti+1][1] + " vs " + meccsek_kint[kinti+1][2] + " Ekkor: " + meccsek_kint[kinti+1][4]
		meccs2 = Label(win, text= m2text, font = meccsFont, fg=kintColor)
		meccs2.place(x = 50, y = 315+40)

		if (kinti+2) <= maxWs(2):
			m3text = meccsek_kint[kinti+2][1] + " vs " + meccsek_kint[kinti+2][2] + " Ekkor: " + meccsek_kint[kinti+2][4]
			meccs3 = Label(win, text= m3text, font = meccsFont, fg=kintColor)
			meccs3.place(x = 50, y = 360+40)

	#katlan palya

	bentL = Label(win, text = "Katlan palya", font = meccsFont, fg=katlanColor)
	bentL.place(x = 30, y = 405+80)

	m1text = meccsek_katlan[katlani][1] + " vs " + meccsek_katlan[katlani][2] + " Ekkor: " + meccsek_katlan[katlani][4]
	meccs1 = Label(win, text= m1text, font = meccsFont, fg=katlanColor)
	meccs1.place(x = 50, y = 450+80)

	if (kinti+1) <= maxWs(3):
		m2text = meccsek_katlan[katlani+1][1] + " vs " + meccsek_katlan[katlani+1][2] + " Ekkor: " + meccsek_katlan[katlani+1][4]
		meccs2 = Label(win, text= m2text, font = meccsFont, fg=katlanColor)
		meccs2.place(x = 50, y = 495+80)

		if (kinti+2) <= maxWs(3):
			m3text = meccsek_katlan[katlani+2][1] + " vs " + meccsek_katlan[katlani+2][2] + " Ekkor: " + meccsek_katlan[katlani+2][4]
			meccs3 = Label(win, text= m3text, font = meccsFont, fg=katlanColor)
			meccs3.place(x = 50, y = 540+80)



def maxWs(wsNum):
    if wsNum == 1:
        return bent_max-1
    elif wsNum == 2:
        return kint_max-1
    else:
        return katlan_max-1

last_update = time.time() - 600
lastBenti = 0
lastKinti = 0
lastKatlani = 0

while True:
	win.update()
	if (time.time()-last_update) >= 600:
	        try:
	            print("Adatbazis\nfrissitese")
	            meccsek_bent = bent.get_all_values()
	            meccsek_kint = kint.get_all_values()
	            meccsek_katlan = katlan.get_all_values()

	            print 'meccsek bent'

	            bent_max = len(meccsek_bent)

	            print 'kint'
	            kint_max = len(meccsek_kint)
	            katlan_max = len(meccsek_katlan)

	        except:
	            print('Network error\ntry again later')

	        last_update = time.time()

	currH = int(time.strftime("%H"))
	#print str(currH)
	currM = int(time.strftime("%M"))

	benti = 2
	H, M = meccsek_bent[benti][4].split(':')[0], meccsek_bent[benti][4].split(':')[1]
	while int(H) < currH and benti < maxWs(1):
		benti += 1
		H, M = meccsek_bent[benti][4].split(':')[0], meccsek_bent[benti][4].split(':')[1]
	while int(M) < currM and benti < maxWs(1):
		benti += 1
		H, M = meccsek_bent[benti][4].split(':')[0], meccsek_bent[benti][4].split(':')[1]

	kinti = 2
	H, M = meccsek_kint[kinti][4].split(':')[0], meccsek_kint[kinti][4].split(':')[1]
	while int(H) < currH and kinti < maxWs(2):
		kinti += 1
		H, M = meccsek_kint[kinti][4].split(':')[0], meccsek_kint[kinti][4].split(':')[1]
	while int(M) < currM and kinti < maxWs(2):
		kinti += 1
		H, M = meccsek_kint[kinti][4].split(':')[0], meccsek_kint[kinti][4].split(':')[1]

	katlani = 2
	H, M = meccsek_katlan[katlani][4].split(':')[0], meccsek_katlan[katlani][4].split(':')[1]
	while int(H) < currH and katlani < maxWs(3):
		katlani += 1
		H, M = meccsek_katlan[katlani][4].split(':')[0], meccsek_katlan[katlani][4].split(':')[1]
	while int(M) < currM and katlani < maxWs(3):
		katlani += 1
		H, M = meccsek_katlan[katlani][4].split(':')[0], meccsek_katlan[katlani][4].split(':')[1]


	#print 'benti: ' + str(benti) + 'kinti: ' + str(kinti) + 'katlani: ' + str(katlani)

	if benti != lastBenti or kinti != lastKinti or katlani != lastKatlani:
		print "screenupdate"
		screenupdate(benti, kinti, katlani)

		lastBenti = benti
		lastKinti = kinti
		lastKatlani = katlani

	time.sleep(10)

