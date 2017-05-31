#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  libmail.py
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

import os.path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def buildMessage(parser,tof):

	# read body file and create new message
	with open(parser.get('message', 'sample_file'),'r') as f:
		msg = MIMEText(f.read(),'html',_charset='UTF-8')

	# From field
	msg['From'] = parser.get('from', 'name') +' <'+parser.get('from', 'email')+'>'

    # Subject field
	msg['Subject'] = parser.get('message', 'subject')

	# To field
	msg['To'] = tof

	return(msg)

def buildMessage_attach(parser,tof):

	# read message file
	with open(parser.get('message', 'sample_file'),'r') as text_file,\
	 open(parser.get('message', 'attach'),'r') as pdf_file :
		text = MIMEText(text_file.read(),'html',_charset='UTF-8')
		pdf = MIMEApplication(pdf_file.read(), _subtype='pdf')
		pdf.add_header('content-disposition', 'attachment',\
		 filename=os.path.basename(parser.get('message', 'attach')))

	msg = MIMEMultipart(_subparts=(text,pdf))

	# From field
	msg['From'] = parser.get('from', 'name') +' <'+parser.get('from', 'email')+'>'

	# Subject field
	msg['Subject'] = parser.get('message', 'subject')

	# To field
	msg['To'] = tof

	return(msg)
