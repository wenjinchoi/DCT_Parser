# -*- coding: utf-8 -*- 
#
# Copyright (C) 2012 Wenjin Choi. All Rights Reserved.

import os, sys

from lib.parser import *

def main():	
	parser = DC_Parser()
	parser.init_collection_data_with_file(sys.argv[1])
	parser.parse_path(sys.argv[2])
	parser.format_out()


if __name__ == '__main__':
	try:
		main()
	except IndexError:
		print 'Usage: '
		print '  python %s [path:Collection Data File] [path:Source File or Directrory]'\
				% sys.argv[0]
	except Exception, e:
		print e
