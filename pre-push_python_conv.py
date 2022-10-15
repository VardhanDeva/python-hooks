#! /usr/bin/env python
from __future__ import print_function
import sys,subprocess,glob,re
class Bash2Py(object):
  __slots__ = ["val"]
  def __init__(self, value=''):
    self.val = value
  def setValue(self, value=None):
    self.val = value
    return value

def GetVariable(name, local=locals()):
  if name in local:
    return local[name]
  if name in globals():
    return globals()[name]
  return None

def Make(name, local=locals()):
  ret = GetVariable(name, local)
  if ret is None:
    ret = Bash2Py(0)
    globals()[name] = ret
  return ret

def Str(value):
  if isinstance(value, list):
    return " ".join(value)
  if isinstance(value, basestring):
    return value
  return str(value)

def Array(value):
  if isinstance(value, list):
    return value
  if isinstance(value, basestring):
    return value.strip().split(' ')
  return [ value ]

def Glob(value):
  ret = glob.glob(value)
  if (len(ret) < 1):
    ret = [ value ]
  return ret

class Expand(object):
  @staticmethod
  def hash():
    return  len(sys.argv)-1

#this script will restrict the push of specific values and files to the public github
# current_branch=$(git branch --show-current)
# echo 'the current branch is "'$current_branch'"' 
# git diff --stat --name-only origin/$current_branch > filtering_pre_push_files.txt
file=Bash2Py("./filtering_pre_push_files.txt")
result=Bash2Py("()")
restricted_file_ext=Bash2Py("(.cert .pem .crt)")
restricted_value=Bash2Py("()")
print("List of files that are created/Modified since from last push")
_rc0 = subprocess.call(["cat","filtering_pre_push_files.txt"],shell=True)
print("---------------------------------------------------------------------------------")
print("List of files that contain restricted file extensions and values")
< $filewhile (if not Make("IFS").setValue():
    str(line.val) != ''):
    for Make("item").val in Array(restricted_file_ext.val[*] ]):
        if (re.search(str(item.val),str(line.val)) ):
            Make("result").setValue("(the_"+str(line.val)+"_file_contains_a_restricted_ext_\""+str(item.val)+"\")")
    subprocess.call("cat" + " " + str(line.val),shell=True,stdout=file("file_content",'wb'))
    > file_content
    < file_contentwhile (if not Make("IFS").setValue():
        str(line_content.val) != ''):
        for Make("word").val in Array(line_content.val):
            for Make("value").val in Array(restricted_value.val[*] ]):
                if (re.search(str(value.val),str(word.val)) ):
                    Make("result").setValue("(the_"+str(line.val)+"_file_contains_restricted_value_"+str(word.val)+")")
        if (not (re.search(".md",str(line.val))) ):
            for Make("word").val in Array(line_content.val):
                subprocess.call(["shopt","-s","nocasematch"],shell=True)
                if (not (re.search("^(http|https)://",str(word.val))) ):
                    if (not (re.search("^localhost:",str(word.val))) ):
                        print(word.val)
                        if (Expand.hash()word >= 6 ):
                            subprocess.call(["shopt","-u","nocasematch"],shell=True)
                            if (re.search(Str(Glob("(^.*[A-Z].*"+"$)")),str(word.val)) and re.search(Str(Glob("(^.*[!@#$%^&*()_+].*"+"$)")),str(word.val)) and re.search(Str(Glob("(^.*[a-z].*"+"$)")),str(word.val)) and re.search(Str(Glob("(^.*[0-9].*"+"$)")),str(word.val)) ):
                                Make("result").setValue("(the_"+str(line.val)+"_file_contains_secrets_\""+str(word.val)+"\")") < file_content
    subprocess.call(["rm","-f","./file_content"],shell=True) < $file
#rm -f ./filtering_pre_push_files.txt
if (Expand.hash()result[@] > 0 ):
    for Make("i").val in Array(result.val[*] ]):
        print(i.val)
    exit(1)
else:
    exit(0)
#