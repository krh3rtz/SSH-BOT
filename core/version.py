# OS_VERSION VERIFIER

class version ():

	WINDOWS  = {

	# antiques versions

	'5.1.': 'Windows XP',
	'5.2.': 'Windows 2003',
	'Windows 2000': 'Windows 2000',

	# Vista

	'6.0.6000':'Microsoft Windows Vista', 
	'6.0.6001':'Microsoft Windows Vista SP1', 
	'6.0.6002':'Microsoft Windows Vista SP2', 

	# Windows 7 
	
	'6.1.7600':'Microsoft Windows 7', 
	'6.1.7601':'Microsoft Windows 7 SP1', 
	
	# Windows 8 
	
	'6.2.9200':'Microsoft Windows 8', 
	'6.3.9200':'Microsoft Windows 8.1', 
	'6.3.9600':'Microsoft Windows 8.1 Update 1', 
	
	# Windows 10 Technical Preview 
	
	'6.4.9841':'Microsoft Windows 10 Technical Preview 1', 
	'6.4.9860':'Microsoft Windows 10 Technical Preview 2', 
	'6.4.9879':'Microsoft Windows 10 Technical Preview 3', 
	'10.0.9926':'Microsoft Windows 10 Technical Preview 4', 
	'10.0.10041':'Microsoft Windows 10 Technical Preview 5', 
	'10.0.10049':'Microsoft Windows 10 Technical Preview 6', 
	
	# Windows 10 Insider Preview 
	
	'10.0.10166':'Microsoft Windows 10 Insider Preview', 
	'10.0.10525':'Microsoft Windows 10 Insider Preview', 
	'10.0.10565':'Microsoft Windows 10 Insider Preview', 
	'10.0.11082':'Microsoft Windows 10 Insider Preview', 
	'10.0.11099':'Microsoft Windows 10 Insider Preview', 
	'10.0.11102':'Microsoft Windows 10 Insider Preview', 
	'10.0.14251':'Microsoft Windows 10 Insider Preview', 
	'10.0.14257':'Microsoft Windows 10 Insider Preview', 
	'10.0.14267':'Microsoft Windows 10 Insider Preview', 
	'10.0.14271':'Microsoft Windows 10 Insider Preview', 
	'10.0.14279':'Microsoft Windows 10 Insider Preview', 
	'10.0.14283':'Microsoft Windows 10 Insider Preview', 
	'10.0.14291':'Microsoft Windows 10 Insider Preview', 
	'10.0.14295':'Microsoft Windows 10 Insider Preview', 
	'10.0.14316':'Microsoft Windows 10 Insider Preview', 
	'10.0.14332':'Microsoft Windows 10 Insider Preview', 
	
	# Windows 10 RTM 
	
	'10.0.10240':'Microsoft Windows 10',
	'10.0.10586':'Microsoft Windows 10',
	}

	Linux = ('debian','redhat','centos','ubuntu', 'arch')

	def __init__ (self):
		pass

	def WinVer (self):
		banner = input ('[*] Give me the version: ').strip('\r').strip('\n')
		for version in self.WINDOWS:
			if version in banner:
				return self.WINDOWS[version]
				break
	def LinVer (self, bot):

		for system in self.Linux:
			cmd = 'uname -rv'
			banner = bot.SendCmd(cmd).decode('utf-8').strip(cmd).strip('\n\r')
			if system in banner.lower():
				return system + ' : ' + banner
			else:
				cmd = 'ls /etc/ | grep ' + system
				ls = bot.SendCmd(cmd).decode('utf-8').strip(cmd).strip('\n').strip('\r')
				if system in ls.lower():
					return system + ' : ' + banner


