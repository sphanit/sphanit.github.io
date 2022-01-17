import codecs
import mmap
import io
import os

count = 0
directory = 'survey'
try:
    os.stat(directory)
except:
    os.mkdir(directory)
with open(directory+".html", "r", encoding='utf-8') as f:
    text= f.readlines()
    Html_file = ''
    for lines in text:
        if 'h2' in lines:
            Html_file= open(directory+"/"+directory+str(count)+".html","w",encoding="utf-8")
            # with io.open(fname, "w", encoding="utf-8") as f
            count+=1
            Html_file.write(lines)
            print(lines)
        if count > 0:
            Html_file.write(lines)
Html_file.close()
