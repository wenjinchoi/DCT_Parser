# -*- coding: utf-8 -*- 
#
# Copyright (C) 2012 Wenjin Choi. All Rights Reserved.

import os
from utils import *

STR_TYPE_COUNT = 'count'
STR_TYPE_AUTO = ''
METHOD_NAME_COMMINCREASE = 'commIncreaseDataCollect'
METHOD_NAME_AUTOCREATEINCREASE = 'autoCreatedIncreaseDataCollect'

FILE_TYPE = set('c cpp cxx cc m mm'.split())

def lines(source_file):
	for line in open(source_file):
		yield line

def is_var_eq_value_in_objfile(var_name, value, file):
	for line in lines(file):
		if var_name in line:
			start = line.find(var_name) + len(var_name)
			rightpart = line[start:].lstrip()
			if rightpart.startswith('='):
				v = rightpart[rightpart.find('@"')+2:]
				v = v[:v.find('"')]
				if value == v:
					return True
	return False

def get_method_para_in_obj(string, method_name):
	start = string.find(method_name) + len(method_name)
	rightpart = string[start:]
	if rightpart.startswith(':'):
		return rightpart[1:].split(' ')[0].split(']')[0]
	else:
		return

def get_value_for_NSString(string):
	return string.lstrip('@').strip('"')


class DC_Parser(object):
	"""
	This is a c/c++/ob-c source file parser. (Only support ob-c at now)
	1. Init from a config text file, use |init_collection_data_with_file(config_file)|
	2. Use |parse_path(path)| to parse the source file or directory. (And the result will 
	   save in the list |collection_data|.)
	3. |result()| for returning raw result list, |format_out()| for printing
	"""
	def __init__(self):
		super(DC_Parser, self).__init__()
		self.collection_data = []  # 0: target id  1: key id  2:type  3:count

	def init_collection_data_with_file(self, config_file):
		for line in lines(config_file):
			if line.strip() == '': continue
			a_tatget = line.strip().split()  # split with any space
			a_tatget.append(0)  # add and init counter
			self.collection_data.append(a_tatget)

	def parse_file(self, source_file):

		inComment = False
		for line in lines(source_file):
			line.strip()
			# Ignore comment
			if line.find('//') >= 0:
				continue

			if inComment and line.strip().endswith('*/'):
				inComment = False
				continue
			if line.strip().startswith('/*'):
				inComment = True
				continue
			if inComment:
				continue

			# 0: target id  1: key id  2:type  3:count
			for keyword in self.collection_data:
				b_key_found = False
				b_target_found = False

				if keyword[2] == STR_TYPE_COUNT and METHOD_NAME_COMMINCREASE in line: # is the 1st method
					target_para = get_method_para_in_obj(line, METHOD_NAME_COMMINCREASE)
					if target_para.startswith('@'):
						if keyword[0] == get_value_for_NSString(target_para):
							b_target_found = True
					else:
						b_target_found =  is_var_eq_value_in_objfile(target_para, keyword[0], source_file)

					key_para = get_method_para_in_obj(line, 'key')
					if key_para.startswith('@'):
						if keyword[1] == get_value_for_NSString(key_para):
							b_key_found = True
					else:
						b_key_found = is_var_eq_value_in_objfile(key_para, keyword[1], source_file)

					if b_target_found and b_key_found:
						keyword[3] += 1

				if keyword[2] == STR_TYPE_AUTO:
					# TODO: need to implemention
					pass

	def parse_path(self, path):
		if os.path.isdir(path):
			for f in walkdir(path):
				if f.split('.')[-1] in FILE_TYPE:
					print 'Parsing: ' + f
					self.parse_file(f)
		elif os.path.isfile(path):
			if path.split('.')[-1] in FILE_TYPE:
				print 'Parsing: ' + path
				self.parse_file(path)
			else:
				print 'Not support this file type: ' + path.split('.')[-1] 
		else:
			print 'The path cannot access.'
		

	def result(self):
		return self.collection_data

	def format_out(self):
		print ''
		count = 0
		count_zero = 0
		count_positive = 0
		for d in self.collection_data:
			print 'Target: %20s | Key: %30s | Count: %d' % ('{0: <20}'.format(d[0]), '{0: <30}'.format(d[1]) , d[3])
			count += 1
			if d[3] == 0: count_zero += 1
			if d[3] > 0: count_positive += 1
		print '{0:-<80}'.format('')
		print 'Count all:', count
		print 'Count > 0:', count_positive
		print 'Count = 0:', count_zero
