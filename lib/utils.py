# -*- coding: utf-8 -*- 
#
# Copyright (C) 2012 Wenjin Choi. All Rights Reserved.

import os

def walkdir(rootDir):
	list_dirs = os.walk(rootDir)
	for root, dirs, files in list_dirs:
		for d in dirs:
			walkdir(os.path.join(root, d))
		for f in files:
			yield os.path.join(root, f)

