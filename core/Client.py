'''
  SSH-BOT
  
 * Author Krhertz 2017
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
	
  CLIENT CLASS
  
'''

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
			return s
		except Exception as e:

			dt = time.ctime()
			self.log_con.log_append ('\n[!] CONNECTION ALERT: Date and time -> ' + dt)
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
