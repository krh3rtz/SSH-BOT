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
 
 LOGGING Class
'''

import os
import time

class log ():
	
	def __init__ (self, filename):

		self.filename = filename
		pass

	def log_chname (self):

		os.system ('mv '+self.filename +' '+self.filename+'_$(date \'+%d-%m-%Y_%H:%M:%S\')')

	def log_append (self, data):

		log = open (self.filename,'a+')
		log.write(data + '\n')
		log.close ()

	def log_clean (self):

		log = open (self.filename,'w')
		log.close ()
