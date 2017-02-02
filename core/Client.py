from pexpect import pxssh
from core.log import *
import time
import os


class Client ():

	log_con = log ('os_admin/logs')
	
	def __init__ (self, target, sshuser, passwd):

		self.target = target
		self.sshuser = sshuser
		self.passwd = passwd
		self.session = self.CliConn()

	def CliConn (self):

		try:
			s = pxssh.pxssh()
			s.login (self.target, self.sshuser, self.passwd)
			dt = time.ctime()
			self.log_con.log_append ('[*] Successful Connection with: '+self.target+' on '+ dt)
			return s
		except Exception as e:

			dt = time.ctime()
			self.log_con.log_append ('[*] Date and time of alert: ' + dt)
			error =  ('[!] Host: '+ self.target +'\n-> Credentials: '+ self.sshuser +':'+self.passwd +'\n-> Specs of error: \n\t'+ str(e) +'\n')
			self.log_con.log_append (error)
			return False

	def SendCmd (self, cmd):

		try:
			self.session.sendline (cmd)
			self.session.prompt ()
			return self.session.before

		except Exception as e:
			log_cmd = log ('os_admin/logs')
			log_cmd.log_append ('[*] Command Error: '+cmd+ '\n-> Specs of error: \n\t'+str(e))
			pass