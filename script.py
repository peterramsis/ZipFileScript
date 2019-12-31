from optparse import *
import os
import zipfile
import time

parse =OptionParser("--zipfile -z --wordlist -w");


parse.add_option("-z","--zipfile",dest="zipfile",help="Enter here your zip file")
parse.add_option("-w","--wordlist",dest="wordlist",help="Enter here your word list file")


(options,args) = parse.parse_args()


if options.zipfile == None and options.wordlist == None:
    print(parse.usage)
else:
   if os.path.isfile(options.zipfile) and os.path.isfile(options.wordlist):
      open_pl = open(options.wordlist,"r")
      for password in open_pl.readlines():
          try:
              password = password.rstrip("\n")
              try:
               zf = zipfile.ZipFile(options.zipfile,"r")
               extract = zf.extractall(pwd=password.encode("utf-8"))
               if extract:
                  exit(0)
              except zipfile.error:
                  print("error")

          except RuntimeError:
              print("password not matched {0}".format(password))
          else:
              print("password is {0}".format(password))
              exit(0)
   else:
       print("word list or zip file not found")







