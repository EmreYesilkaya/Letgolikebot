import pyautogui 




#Dear all,I am sharing a code on GitHub for educational purposes only. This code is not intended for commercial use and should only be used for learning and experimentation purposes.It is important to note that users who choose to download and use this code are solely responsible for their actions and any consequences that may arise from using this code.Please use this code responsibly and only for the intended purposes of learning and experimentation. Do not use this code for any commercial or illegal purposes.Thank you for your understanding and responsible use of this code.Best regards,


import time
import pyperclip
print('example *name your mail*+*your domain owner*\nhappyexmp12   @   gmail.com')
Hesap=input('mail name:')
dom=input('your domain:')
pswd=input('Password:')
Hesap= None
maildom = None
psw=None
pyautogui.FAILSAFE= True

x = None
while x is None:
    x = pyautogui.locateCenterOnScreen('photos\google.PNG',grayscale=True,confidence=0.9)


pyautogui.click(x,button='left',clicks=3)


jk = None
while jk is None:
    jk=pyautogui.locateCenterOnScreen('photos\j.PNG',grayscale=True,confidence=0.9)



pyautogui.click(jk,button='left',clicks=3,interval=1)

search = None
while search is None:
    pyautogui.click(x=100,y=100,button='left',clicks=3)
    search=pyautogui.locateCenterOnScreen('photos\serch.PNG',grayscale=True,confidence=0.9)

pyautogui.click(search,button='left',clicks=3)
pyautogui.write('https://www.croxyproxy.com/',interval=0.01)
pyautogui.press('enter')
time.sleep(7)

proxy = None
while proxy is None:
    proxy=pyautogui.locateCenterOnScreen('photos\proxy.PNG',grayscale=True,confidence=0.9,)
    
pyautogui.click(proxy,button='left',clicks=3)


pyautogui.click(proxy,button='left',clicks=3)
pyautogui.write('https://www.letgo.com/',interval=0.01)
pyautogui.press('enter')
time.sleep(14)


login = None
while login is None:
    login=pyautogui.locateCenterOnScreen('photos\login.PNG',grayscale=True,confidence=0.9,)
    

pyautogui.click(login,button='left',clicks=10,interval=1)


mail = None
while mail is None:
    mail=pyautogui.locateCenterOnScreen('photos\mail.PNG',grayscale=True,confidence=0.9,)
    

pyautogui.click(mail,button='left',clicks=3,interval=0.01)



maillog = None
while maillog is None:
    maillog=pyautogui.locateCenterOnScreen('photos\maillog.PNG',grayscale=True,confidence=0.9,)
    
pyautogui.moveTo(maillog,duration=2)
pyautogui.click(button='left',clicks=1,interval=0.09)
pyautogui.write(Hesap,interval=0.09)
pyperclip.copy("@")
pyautogui.write(dom,interval=0.09)
pyautogui.hotkey("ctrl", "v")
pyautogui.write(maildom,interval=0.09)

cont = None
while cont is None:
    cont=pyautogui.locateCenterOnScreen('photos\cont.PNG',grayscale=True,confidence=0.5)

pyautogui.moveTo(cont,duration=1)
pyautogui.click(button='left',clicks=1)

pswd = None
while pswd is None:
    pswd=pyautogui.locateCenterOnScreen('E:\FallGuys\python\pswd.PNG',grayscale=True,confidence=0.9,)
    
pyautogui.moveTo(pswd)
pyautogui.click(button='left',clicks=1)
pyautogui.write(psw,interval=0.07)



clickpswd = None
while clickpswd is None:
    clickpswd=pyautogui.locateCenterOnScreen('E:\FallGuys\python\clickpswd.PNG',grayscale=True,confidence=0.7)

pyautogui.moveTo(clickpswd,)
pyautogui.click(button='left',clicks=1,interval=1)



engel = None
while engel is None:
    engel=pyautogui.locateCenterOnScreen('E:\FallGuys\python\photos\engel.PNG',grayscale=True,confidence=0.7)

pyautogui.moveTo(engel)
pyautogui.click(button='left',clicks=1)

print('location example ^Ankara Cankaya^')
ko = input('location')

konum  = None
while konum  is None:
    konum =pyautogui.locateCenterOnScreen('E:\FallGuys\python\photos\konum.PNG',grayscale=True,confidence=0.7)

pyautogui.moveTo(konum)
pyautogui.click(button='left',clicks=1)
pyautogui.press('backspace')
pyautogui.write(ko)
currentMouseX, currentMouseY = pyautogui.position()
c = pyautogui.moveTo(currentMouseX,currentMouseY + 60, duration=1)
pyautogui.click(c,button='left',clicks=1)


print('Örnek Fiat Egea')
sr = input('beğenmek istediğiniz varliği yaziniz')

serch1 = None
while serch1 is None:
    serch1=pyautogui.locateCenterOnScreen('E:\FallGuys\python\photos\serch1.PNG',grayscale=True,confidence=0.7)
pyautogui.moveTo(serch1)
pyautogui.click(button='left',clicks=1,)
pyautogui.write(sr)

serchb = None
while serchb is None:
    serchb=pyautogui.locateCenterOnScreen('E:\FallGuys\python\photos\serchb.PNG',grayscale=True,confidence=0.7)
pyautogui.moveTo(serchb)
pyautogui.click(button='left',clicks=1,)

offset = 1000
pyautogui.keyDown('shift')
pyautogui.scroll(offset)
pyautogui.keyUp('shift')



























