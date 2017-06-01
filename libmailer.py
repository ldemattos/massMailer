#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  libmailer.py
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

import smtplib
import sys

def mailer(parser,msg,fromf,subf,tof,fp_log):
	try:
		smtpObj = smtplib.SMTP_SSL(parser.get('smtp','server')+':'+parser.get('smtp','port'),timeout=float(parser.get('smtp','timeout')))
		smtpObj.login(parser.get('smtp','login'),parser.get('smtp','password'))
		smtpObj.sendmail(fromf, tof, msg)
		fp_log.write("OK!\n")
	except Exception:
		fp_log.write("FAIL: %s\n"%(sys.exc_info()[0]))
