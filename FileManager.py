#!/usr/bin/python
# -*- coding: euc-kr -*-

import re
import os
import sys
import types
import copy
import shutil
import glob

# 현재 경로 반환
# 실제로 프로그램을 실행한 경로를 반환하여 목적에 맞지 않는 경우가 발생함
def getCurrentPath ():
	# 최초 프로그램이 실행된 파일의 경로 즉 MAIN 파일의 경로를 반환함
	#return os.path.abspath(os.path.curdir)
	
	# 실제 파일의 경로를 반환함
	return os.path.dirname(sys.argv[0])

# 상위 폴더 경로 반환
def mvParentFolder (curPath,upLevel = 1):
	parentFolderPath = curPath
	for i in range(upLevel):
		parentFolderPath = os.path.abspath(os.path.join(parentFolderPath,os.path.pardir))
	
	return parentFolderPath

# 경로 문자열 조합
def joinPath(basePath, fileName):
	return os.path.normpath(os.path.join(basePath, fileName))

# 파일 복사 함수
def fileCopy (src, dest):
	try	:
		shutil.copy(src, dest)
	except EnvironmentError, e:
		#print "Unable to copy file(%s)" % e
		raise EnvironmentError(e)

# 파일/폴더 이동 함수
def fileMove (src, dest):
	shutil.move(src, dest)

# 파일 삭제 함수
# List Type	: List의 모든 파일 삭제
# Str Type : 해당 파일만 삭제
def fileDelete (path):
	if type(path) == types.ListType:
		for	delFileName	in path:
			os.remove(delFileName)
	else:
		os.remove(path)

# 폴더내 파일 유/무 확인
# List Item으로 반복문을 수행하며, pop() 함수 사용시
# 리스트의 모든	아이템을 거치지	않기 때문에	별도의 리스트 사용
def getFileListInFolder (path):
	fileListInFolder = os.listdir(path)
	tmpFileList	= copy.deepcopy(fileListInFolder)
	for	fileName in	tmpFileList:
		if os.path.isfile(os.path.join(path,fileName)) == False:
			fileListInFolder.pop(fileListInFolder.index(fileName))
	
	return fileListInFolder

# 폴더내 파일 유/무	확인
# List Item으로	반복문을 수행하며, pop() 함수 사용시
# 리스트의 모든	아이템을 거치지	않기 때문에	별도의 리스트 사용
def getSubFolderListInFolder (path):
	fileListInFolder = os.listdir(path)
	tmpFileList	= copy.deepcopy(fileListInFolder)
	for	fileName in	tmpFileList:
		if os.path.isfile(os.path.join(path,fileName)) == True:
			fileListInFolder.pop(fileListInFolder.index(fileName))
	
	return fileListInFolder

def isExistFile(path):
	return os.path.isfile(path)

# 폴더 삭제	함수
def folderDelete (path):
	# 원래 shutil의 함수로 삭제하려 하였으나 권한 문제로
	# BATCH 파일을 이용해 삭젝하는 것으로 로직을 변경함
	os.system('fileDel.bat "%s"' % path)

# 폴더 확인	함수
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

# 폴더 생성 함수
def folderCreate (path):
	if isExistFolder(path) == True:
		handleExistFolder(path)
	else :
		try:
			os.mkdir(path)
		except OSError, e:
			print e
			handleExistFolder(path)

# 빈 폴더 유무 확인
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