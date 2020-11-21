import pyqrcode

myEmailId = " ishmeetkaur2404@gmail.com "
Twitter_Link = " ishmeetkaur2404 "
contact_no = " 8826256279 "

myQrCode = pyqrcode.create(myEmailId +"\n"  + Twitter_Link +"\n"+contact_no)
myQrCode.svg("MYQRCODE.svg")
print("Your QR is generated successfully")