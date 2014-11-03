from socket import *
import ssl
import base64

#configuration parameters
server = "smtp.live.com"
port = 587
fromEmail = "<payamrastogi@outlook.com>"
toEmail = "<payamrastogi@gmail.com>"
name = "Payam Rastogi"
subject = "Computer Networks - SMTP Assignment"
emailMessage = "I love computer networks!"
message = 'From: ' + name + '\r\n' + 'To: ' + toEmail + '\r\n' + 'Subject: ' + subject + '\r\n' + emailMessage + ' \r\n\n'
endmsg = "\r\n.\r\n"

# create socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server, port))
recv = clientSocket.recv(1024)
if recv[:3] != '220':
	print '220 reply not recieved from server'
print "From Server: "
print recv

#send HELO command
heloCommand = 'EHLO ALICE\r\n'
clientSocket.send(heloCommand)
recvHelo = clientSocket.recv(1024)
if recvHelo[:3] != '250':
	print 'HELO 250 reply not recieved from server'
print "Server replied to HELO Command: " 
print recvHelo

#send TLS command
tlsCommand = 'STARTTLS\r\n'
clientSocket.send(tlsCommand)
recvTLS = clientSocket.recv(1024)
if recvTLS[:3] != '220':
	print 'STARTTLS 220 reply not recieved from server'
print "Server replied to STARTTLS Command: " 
print recvTLS

#wrap client socket with ssl socket
sslSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

#send authentication information
authCommand = 'AUTH LOGIN\r\n'
sslSocket.send(authCommand)
recvAuth = sslSocket.recv(1024)
if recvAuth[:3] != '334':
	print 'Authentication reply not recieved from server'
print "Server replied to AUTH Command: " 
print recvAuth

#send encoded username and password
sslSocket.send(base64.b64encode('payamrastogi@outlook.com')+'\r\n')
print sslSocket.recv(1024)
sslSocket.send(base64.b64encode('<password>')+'\r\n') #password omitted
print sslSocket.recv(1024)

#send mail from command
sslSocket.send("MAIL FROM:" + fromEmail + '\r\n')
recvMailFrom = sslSocket.recv(1024)
if recvMailFrom[:3] != '250':
	print 'MAIL FROM 250 reply not recieved from server.'
print "Server replied to MailFrom Command: " 
print recvMailFrom

#send rcpt to command
sslSocket.send("RCPT TO:" + toEmail + '\r\n')
recvRcptTo = sslSocket.recv(1024)
if recvRcptTo[:3] != '250':
	print 'RCPT 250 reply not recieved from server.'
print "Server replied to RctpTo Command: " 
print recvRcptTo

#send data command
dataCommand = "DATA\r\n"
sslSocket.send(dataCommand)
recvData = sslSocket.recv(1024)
if recvData[:3] != '354':
	print 'DATA 354 reply not recieved from server.'
print "Server replied to Data Command: " 
print recvData

#send my test message
sslSocket.send(message)
sslSocket.send(endmsg)

#send quit command
quitCommand = 'QUIT\r\n'
sslSocket.send(quitCommand)
recvQuit = sslSocket.recv(1024)
if recvQuit[:3] != '250':
	print 'QUIT 250 reply not recieved from server.'
print "Server replied to Quit Command: " 
print recvQuit