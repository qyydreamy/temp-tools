import os  
import os.path  
rootdir = "I:\\P4Trunc\\exe\\resources\\media\\shaders\\ui"
old_w1 = "/newui\\"
old_w2 = "\"newui\\"
new_w1 = "\\ui\\"
new_w2 = "\"ui\\"

def walk_all_files(rootdir):  
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            if filename.endswith(".xml") or filename.endswith(".uir"):         
                is_file_contain_word(os.path.join(parent,filename))
                
        for dirname in dirnames:
            for cp,cdirs,cfiles in os.walk(os.path.join(parent,dirname)):
                for cfile in cfiles:
                    if cfile.endswith(".xml") or filename.endswith(".uir"):         
                        is_file_contain_word(os.path.join(cp,cfile))
                    
            
def is_file_contain_word(file_):
    file_data=""
    encode='utf-8'
    if file_.endswith(".uir"):
        encode='gbk'
    with open(file_, mode='r', encoding=encode, errors='ignore') as f:
        for line in f:
            if old_w1 in line:
                #print(query_word, "->", new_word)
                line = line.replace(old_w1,new_w1)
            elif old_w2 in line:
                line = line.replace(old_w2,new_w2)
            file_data += line
    with open(file_, mode='w', encoding=encode, errors='ignore') as wf:
        wf.write(file_data)
  
walk_all_files(rootdir) 
