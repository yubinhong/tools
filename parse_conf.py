#!/usr/bin/python
#To parse ini file and update config files

import sys,os,getopt,re
import ConfigParser


ini_file = ""
env = ""
conf_file = ""


opts, args = getopt.getopt(sys.argv[1:], "f:e:c:")
for op, value in opts:
    if op == "-f":
        ini_file = value
    elif op == "-e":
        env = value
    elif op == "-c":
        conf_file = value
    else:
        sys.exit()
    

def parse(config_file_path,sec,json_file):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file_path)
    keylist = cf.options(sec)
    for key in keylist:
        value = cf.get(sec, key)
        replace_conf(json_file,key,value)
        

def replace_conf(file_path, old_str, new_str):  
  try:  
    f = open(file_path,'r+')  
    all_lines = f.readlines()  
    f.seek(0)  
    f.truncate()
    for line in all_lines:  
      line = line.replace("${"+old_str+"}", new_str)  
      f.write(line)  
    f.close()  
  except Exception,e:  
    print e 

if __name__ == "__main__":
    parse(ini_file,env,conf_file)
