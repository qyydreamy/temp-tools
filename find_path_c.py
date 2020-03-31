import os  
import os.path  
rootdir = "E:\\version4.3.6\\exe\\resources\\media\\shaders\\ui_merge"

def walk_all_files(rootdir):  
    for parent,dirnames,filenames in os.walk(rootdir):
        for dirname in dirnames:
            if dirname.find("new_")==0:
                for filename in filenames:
                    if filename.endswith(".xml") or filename.endswith(".uir"):
                        #print "parent is :" + parent  
                        #print "filename is:" + filename  
                        #print "the full name of the file is :" + os.path.join(parent,filename)
                        query = dirname + "\\"
                        new_word = dirname[4:] + "\\"           
                        is_file_contain_word(os.path.join(parent,filename),query,new_word)

                for sdir in dirnames:
                    for cp,cdirs,cfiles in os.walk(os.path.join(parent,sdir)):
                        for cfile in cfiles:
                            if cfile.endswith(".xml") or cfile.endswith(".uir"):
                                oldw = dirname + "\\"
                                neww = dirname[4:] + "\\"           
                                is_file_contain_word(os.path.join(cp,cfile),oldw,neww)
                    
            
def is_file_contain_word(file_,query_word,new_word):
    file_data=""
    encode='utf-8'
    modified=0
    if file_.endswith(".uir"):
        encode='gbk'
    with open(file_, mode='r', encoding=encode, errors='ignore') as f:
        for line in f:
            if query_word in line:
                #print(query_word, "->", new_word)
                modified=1
                line = line.replace(query_word,new_word)
            file_data += line
    if modified==1:
       with open(file_, mode='w', encoding=encode, errors='ignore') as wf:
           wf.write(file_data)
  
walk_all_files(rootdir)  
