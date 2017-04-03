#!/usr/bin/python
# -*- coding: euc-kr -*-

import re
import os
import sys
import types
import copy
import shutil
import glob

# ���� ��� ��ȯ
# ������ ���α׷��� ������ ��θ� ��ȯ�Ͽ� ������ ���� �ʴ� ��찡 �߻���
def getCurrentPath ():
	# ���� ���α׷��� ����� ������ ��� �� MAIN ������ ��θ� ��ȯ��
	#return os.path.abspath(os.path.curdir)
	
	# ���� ������ ��θ� ��ȯ��
	return os.path.dirname(sys.argv[0])

# ���� ���� ��� ��ȯ
def mvParentFolder (curPath,upLevel = 1):
	parentFolderPath = curPath
	for i in range(upLevel):
		parentFolderPath = os.path.abspath(os.path.join(parentFolderPath,os.path.pardir))
	
	return parentFolderPath

# ��� ���ڿ� ����
def joinPath(basePath, fileName):
	return os.path.normpath(os.path.join(basePath, fileName))

# ���� ���� �Լ�
def fileCopy (src, dest):
	try	:
		shutil.copy(src, dest)
	except EnvironmentError, e:
		#print "Unable to copy file(%s)" % e
		raise EnvironmentError(e)

# ����/���� �̵� �Լ�
def fileMove (src, dest):
	shutil.move(src, dest)

# ���� ���� �Լ�
# List Type	: List�� ��� ���� ����
# Str Type : �ش� ���ϸ� ����
def fileDelete (path):
	if type(path) == types.ListType:
		for	delFileName	in path:
			os.remove(delFileName)
	else:
		os.remove(path)

# ������ ���� ��/�� Ȯ��
# List Item���� �ݺ����� �����ϸ�, pop() �Լ� ����
# ����Ʈ�� ���	�������� ��ġ��	�ʱ� ������	������ ����Ʈ ���
def getFileListInFolder (path):
	fileListInFolder = os.listdir(path)
	tmpFileList	= copy.deepcopy(fileListInFolder)
	for	fileName in	tmpFileList:
		if os.path.isfile(os.path.join(path,fileName)) == False:
			fileListInFolder.pop(fileListInFolder.index(fileName))
	
	return fileListInFolder

# ������ ���� ��/��	Ȯ��
# List Item����	�ݺ����� �����ϸ�, pop() �Լ� ����
# ����Ʈ�� ���	�������� ��ġ��	�ʱ� ������	������ ����Ʈ ���
def getSubFolderListInFolder (path):
	fileListInFolder = os.listdir(path)
	tmpFileList	= copy.deepcopy(fileListInFolder)
	for	fileName in	tmpFileList:
		if os.path.isfile(os.path.join(path,fileName)) == True:
			fileListInFolder.pop(fileListInFolder.index(fileName))
	
	return fileListInFolder

def isExistFile(path):
	return os.path.isfile(path)

# ���� ����	�Լ�
def folderDelete (path):
	# ���� shutil�� �Լ��� �����Ϸ� �Ͽ����� ���� ������
	# BATCH ������ �̿��� �����ϴ� ������ ������ ������
	os.system('fileDel.bat "%s"' % path)

# ���� Ȯ��	�Լ�
def isExistFolder (path):
	return os.path.isdir(path)

def handleExistFolder (path):
	print "Already exist same folder on your path(%s)" % path
	print "Are you want to delete it(y/n): "
	inputSelect	= raw_input().strip().lower()
	
	if (inputSelect	== "y"):
		folderDelete(path)
		print "Ok!! Delete exist folder and create new one"
		try:
			os.mkdir(path)
		except OSError, e:
			print e
			handleExistFolder(path)
	elif (inputSelect == "n"):
		print "New folder create operation has been halted"
	else:
		print "You are wrong selection\nMust select	between	[y]	or [n]"
		folderCreate(path)

# ���� ���� �Լ�
def folderCreate (path):
	if isExistFolder(path) == True:
		handleExistFolder(path)
	else :
		try:
			os.mkdir(path)
		except OSError, e:
			print e
			handleExistFolder(path)

# �� ���� ���� Ȯ��
def isEmptyFolder (path):
	fileListInFolder = getFileListInFolder(path)
	if len(fileListInFolder) ==	0:
		return True
	else:
		return False

if __name__	== "__main__" :
	print "Test Start"
	#print "Test Current Path(%s)" % os.path.curdir
	#print isEmptyFolder(os.path.curdir)
	print getCurrentPath()
	#folderCreate("a")
	#print getFileListInFolder(os.path.join(os.path.curdir,	"CurrentOFPHeader")	)