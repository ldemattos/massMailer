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
from email.header import Header

def buildMessage(parser,tof,custom_vars):

	# read body file and create new message
	with open(parser.get('message', 'sample_file'),'r') as f:
		ctexto = customizeMessage(f.read(),custom_vars)
		msg = MIMEText(ctexto,'html',_charset='UTF-8')

	# Improving header
	msg['Content-Type'] = "text/html; charset=utf-8"

	# From field
	msg['From'] = "\"%s\" <%s>" % (Header(parser.get('from', 'name'), 'utf-8'), parser.get('from', 'email'))

    # Subject field
	msg['Subject'] = Header(parser.get('message', 'subject'), 'utf-8')

	# To field
	msg['To'] = tof

	return(msg)

def buildMessage_attach(parser,tof,custom_vars):

	# read message file
	with open(parser.get('message', 'sample_file'),'r') as text_file,\
	 open(parser.get('message', 'attach'),'r') as pdf_file:
	 	ctext = customizeMessage(text_file.read(),custom_vars)
		text = MIMEText(ctext,'html',_charset='UTF-8')
		pdf = MIMEApplication(pdf_file.read(), _subtype='pdf')
		pdf.add_header('content-disposition', 'attachment',\
		 filename=os.path.basename(parser.get('message', 'attach')))

	# Building message with body and attachment
	msg = MIMEMultipart(_subparts=(text,pdf))

	# Improving header
	msg['Content-Type'] = "text/html; charset=utf-8"

	# From field
	msg['From'] = "\"%s\" <%s>" % (Header(parser.get('from', 'name'), 'utf-8'), parser.get('from', 'email'))

    # Subject field
	msg['Subject'] = Header(parser.get('message', 'subject'), 'utf-8')

	# To field
	msg['To'] = tof

	return(msg)

def customizeMessage(body,custom_vars):
	# iterate over custom_vars
	for key, value in custom_vars.iteritems():
		body = body.replace(key,value)

	return(body)
