#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
#  massMailer.py
#
#  Copyright 2017 Leonardo M. N. de Mattos <l@mattos.eng.br>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# standard libraries
import sys
from ConfigParser import SafeConfigParser
import os.path
import ast

# local libraries
import libbuildmail
import libmailer

def main(args):

	# read config file as f:
	parser = SafeConfigParser()
	confFile = sys.argv[1]
	parser.read(confFile)

	# open mail log
	fp_log = open('mail.log','w+')

	# Variables to be customized
	custom_vars = ast.literal_eval(parser.get('message','custom'))

	# open contact list
	with open(parser.get('recipients','rec_file'),'r') as clist:

		for line in clist:

			# To field
			line = line.split(';')
			custom_vars['<<<ToName>>>'] = line[0]
			print line[0]
			print custom_vars
			tof = "%s <%s>"%(line[0],line[1][:-1])

			if parser.get('message','attach') == 'None':
				msg = libbuildmail.buildMessage(parser,tof,custom_vars)

			else:
				# check whether the attachment file is there
				if os.path.isfile(parser.get('message','attach')):
					msg = libbuildmail.buildMessage_attach(parser,tof,custom_vars)

				else:
					print "Invalid attachment path file! Quitting..."
					quit()

			# call mailer
			fp_log.write("Sending mail to %s... "%(tof))
			libmailer.mailer(parser,msg.as_string(),msg['From'],msg['Subject'],msg['To'],fp_log)

	# close mail log
	fp_log.close()

	return(0)

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
