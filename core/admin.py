'''
  SSH-BOT
  
 * Copyright (C) 2017 Krhertz
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
 
 ADMIN CLASS
 
'''

from core.Client import *
from core.version import *
from core.log import *
from threading import Thread
import time
import os

class Admin ():
	
	os_list = log ('os_admin/sys_list')
	os_list.log_clean ()
	log = log ('os_admin/logs')
	log.log_clean ()
	ver = version ()
	BotNet = []
	options = '''

Options:

	1) Single or multi bot interaction
	2) Disconnect bot
	3) Add single bot
	4) Win server connection
	5) Specific actions -> used for actions that need su/sudo
	6) Refresh botlist
	7) Check log file

* Type \'exit\' to leave and close all connections.

'''
	def __init__ (self):
		pass

	def add_bot (self, target, sshuser, passwd):

		client = Client (target, sshuser, passwd)
		if client.session != False:
			self.BotNet.append (client)

	def show_bot (self):

		os.system('clear')
		os.system ('cat os_admin/sys_list')
		
	def ref_list (self): # refresh botlist

		self.os_list.log_clean ()
		self.os_list.log_append ('\n-------------- HOSTS --------------\nID\t| address\t\t| System\n----------------------------------------------------')
		i = 0
		for bot in self.BotNet:
			try:
				info =  ('['+str(i)+']\t| ' + bot.target +'\t| ' + self.ver.LinVer(bot))
				self.os_list.log_append (info)
				i += 1
			except Exception as e:
				pass

	def BotNetDis (self):
		self.ref_list ()
		print ('[+] Bots list saved: os_admin/')
		for bot in self.BotNet:
			try:
				bot.session.logout()
			except Exception as e:
				pass
		self.log.log_chname () 
		self.os_list.log_chname ()
		print ('[+] All bots successfully disconnected\n[+] Logfile under: os_admin/')


	def BotDis (self):

		val = input ('[*] Type the ID: ')
		id = val.strip('\n').strip('\r')

		bot = self.BotNet[int(id)]
		try:
			bot.session.logout ()
			self.log.log_append ('[+] Host '+bot.target+' disconnected')
			del self.BotNet[int(id)]
		except Exception as e:
			self.log.log_append ('[!] Error disconnecting host: '+bot.target+'\n[!] Specs of error ->' + str(e))
			pass
		self.ref_list ()

	def BotConn (self):

		try:
			creds = input ('[*] Insert credentials separated by a comma (eg. host,ssh_user,passwd): ').strip('\n').strip ('\r').split(',')
			t = Thread (target=self.add_bot, args=(creds[0], creds[1], creds[2]))
			child = t.start()
		except Exception as e:
			error =  ('[!] Error while trying to connect \n-> Specs of error'+str(e))
			self.log.log_append (error)

	def BotNetCmd (self):

		bots = self.bot_grouper ()
		while True:
			cmd = input ('[*] Command bot list --> ')
			
			if 'exit' in cmd.lower():
				break
			elif 'back' in cmd.lower():
				break
			else:
				for bot in bots:
					try:
						response = bot.SendCmd (cmd).decode('utf-8').strip(cmd)
						print (bot.target+' -> ' + response)
					except Exception as e:
						self.log.log_append ('[!] Error cmd host: '+bot.target+'\n[!] Specs of error ->' + str(e))
						pass
				print ('[+] Command Sent.')

	def specific (self):

		bots = self.bot_grouper ()

		for bot in bots:
			host = bot.target
			sshuser = bot.sshuser
			passwd = bot.passwd
			os.system ('xterm -T '+sshuser+':'+host+' -e \'sshpass -p '+passwd+' ssh '+sshuser+'@'+host+'\' &')
			dt = time.ctime()
			self.log.log_append ('[+] Specific connection with: '+host+' on '+dt)

	def bot_grouper (self):

		val = input ('[*] Type the ID(s) (if multiple eg. 1,2,3,4 if all \'all\'): ')
		ids = val.strip('\n').strip('\r')
		bots = []
		
		if 'all' not in ids.lower():
			for id in ids.split(','):
				if not self.BotNet[int(id)]:
					print ('[!] The '+id+' ID doesn\'t exist.')
				else:
					bots.append (self.BotNet[int(id)])
		else:
			bots = self.BotNet

		return bots

	def win_conn (self):
		creds = input ('[*] Insert credentials separated by a comma (eg. host,ssh_user): ').strip('\n').strip ('\r').split(',')
		host = creds [0]
		sshuser = creds [1]
		os.system ('xterm -hold -T '+sshuser+':'+host+' -e \'ssh '+sshuser+'@'+host+'\' &')
		dt = time.ctime ()
		system = self.ver.WinVer ()
		self.log.log_append ('[+] Conection with a '+system+' at '+host+' on '+dt)

	def checklog (self):

		os.system ('xterm -T LOG -e \'cat os_admin/logs | less\' &')

	switch = {
			1:BotNetCmd,

			2:BotDis,

			3:BotConn,

			4:win_conn,

			5:specific,

			6:ref_list,

			7:checklog,
		}

	def main_menu (self):

		self.ref_list ()
		self.show_bot ()
		print (self.options)

		while True:
			opt = input ('Option: ') + '.'

			if 'exit' in opt.lower():				
				opt = opt.strip('.')
			if opt.lower() in 'exit  ':
				self.BotNetDis ()
				break
			try:	
				function = self.switch[int(opt.strip('.'))]
				function (self)
			except Exception as e:
				pass
			finally:
				self.show_bot ()
				print (self.options)	
