import qrcode
#Taking UPI ID as a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=Currency&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#you can modify these URLs based on the payment apps you want to support


phonepe_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_apy_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR Codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the QR code to image file 

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('phonepe_qr.png')
google_pay_qr.save('phonepe_qr.png')

#Display the QR Code 
phonepe_qr.show()
paytm_qr.show()
google_apy_url.show()