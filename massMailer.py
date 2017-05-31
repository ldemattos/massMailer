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
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# local libraries
import libbuildmail
import libmailer

def main(args):

	# read config file as f:
	parser = SafeConfigParser()
	confFile = sys.argv[1]
	parser.read(confFile)

	# To field
	tof = "Leonardo <l@pot.eng.br>"

	print parser.get('message','attach')
	if parser.get('message','attach') == 'None':
		msg = libbuildmail.buildMessage(parser,tof)

	else:
		# check whether the attachment file is there
		if os.path.isfile(parser.get('message','attach')):
			filename = os.path.basename(parser.get('message','attach'))
			with open(parser.get('message','attach'),"rb") as f:
				data = f.read()
			encoded = base64.b64encode(data)
			msg = libbuildmail.buildMessage_attach(parser,tof)

		else:
			print "Invalid attachment path file! Quitting..."
			quit()

	# open mail log
	fp_log = open('mail.log','w+')
	fp_log.write("Sending mail to %s... "%(tof))

	# call mailer
	libmailer.mailer(parser,msg.as_string(),msg['From'],msg['Subject'],msg['To'],fp_log)

	fp_log.close()

	return(0)

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
