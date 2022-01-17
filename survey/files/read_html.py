import codecs
import mmap
import io
import os
import sys
import glob

def seperate_papers_from_html(page_name=None):
  head_info = """<!DOCTYPE html>
  <html><head>
  		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  		<title>Zotero Report</title>
  		<link rel="stylesheet" type="text/css" href="data:text/css;base64,Ym9keSB7CgliYWNrZ3JvdW5kOiB3aGl0ZTsKfQoKYSB7Cgl0ZXh0LWRlY29yYXRpb246IHVuZGVybGluZTsKfQoKYm9keSB7CglwYWRkaW5nOiAwOwp9Cgp1bC5yZXBvcnQgbGkuaXRlbSB7Cglib3JkZXItdG9wOiA0cHggc29saWQgIzU1NTsKCXBhZGRpbmctdG9wOiAxZW07CglwYWRkaW5nLWxlZnQ6IDFlbTsKCXBhZGRpbmctcmlnaHQ6IDFlbTsKCW1hcmdpbi1ib3R0b206IDJlbTsKfQoKaDEsIGgyLCBoMywgaDQsIGg1LCBoNiB7Cglmb250LXdlaWdodDogbm9ybWFsOwp9CgpoMiB7CgltYXJnaW46IDAgMCAuNWVtOwp9CgpoMi5wYXJlbnRJdGVtIHsKCWZvbnQtd2VpZ2h0OiBib2xkOwoJZm9udC1zaXplOiAxZW07CglwYWRkaW5nOiAwIDAgLjVlbTsKCWJvcmRlci1ib3R0b206IDFweCBzb2xpZCAjY2NjOwp9CgovKiBJZiBjb21iaW5pbmcgY2hpbGRyZW4sIGRpc3BsYXkgcGFyZW50IHNsaWdodGx5IGxhcmdlciAqLwp1bC5yZXBvcnQuY29tYmluZUNoaWxkSXRlbXMgaDIucGFyZW50SXRlbSB7Cglmb250LXNpemU6IDEuMWVtOwoJcGFkZGluZy1ib3R0b206IC43NWVtOwoJbWFyZ2luLWJvdHRvbTogLjRlbTsKfQoKaDIucGFyZW50SXRlbSAudGl0bGUgewoJZm9udC13ZWlnaHQ6IG5vcm1hbDsKfQoKaDMgewoJbWFyZ2luLWJvdHRvbTogLjZlbTsKCWZvbnQtd2VpZ2h0OiBib2xkICFpbXBvcnRhbnQ7Cglmb250LXNpemU6IDFlbTsKCWRpc3BsYXk6IGJsb2NrOwp9CgovKiBNZXRhZGF0YSB0YWJsZSAqLwp0aCB7Cgl2ZXJ0aWNhbC1hbGlnbjogdG9wOwoJdGV4dC1hbGlnbjogcmlnaHQ7Cgl3aWR0aDogMTUlOwoJd2hpdGUtc3BhY2U6IG5vd3JhcDsKfQoKdGQgewoJcGFkZGluZy1sZWZ0OiAuNWVtOwp9CgoKdWwucmVwb3J0LCB1bC5ub3RlcywgdWwudGFncyB7CglsaXN0LXN0eWxlOiBub25lOwoJbWFyZ2luLWxlZnQ6IDA7CglwYWRkaW5nLWxlZnQ6IDA7Cn0KCi8qIFRhZ3MgKi8KaDMudGFncyB7Cglmb250LXNpemU6IDEuMWVtOwp9Cgp1bC50YWdzIHsKCWxpbmUtaGVpZ2h0OiAxLjc1ZW07CglsaXN0LXN0eWxlOiBub25lOwp9Cgp1bC50YWdzIGxpIHsKCWRpc3BsYXk6IGlubGluZTsKfQoKdWwudGFncyBsaTpub3QoOmxhc3QtY2hpbGQpOmFmdGVyIHsKCWNvbnRlbnQ6ICcsICc7Cn0KCgovKiBDaGlsZCBub3RlcyAqLwpoMy5ub3RlcyB7Cglmb250LXNpemU6IDEuMWVtOwp9Cgp1bC5ub3RlcyB7CgltYXJnaW4tYm90dG9tOiAxLjJlbTsKfQoKdWwubm90ZXMgPiBsaTpmaXJzdC1jaGlsZCBwIHsKCW1hcmdpbi10b3A6IDA7Cn0KCnVsLm5vdGVzID4gbGkgewoJcGFkZGluZzogLjdlbSAwOwp9Cgp1bC5ub3RlcyA+IGxpOm5vdCg6bGFzdC1jaGlsZCkgewoJYm9yZGVyLWJvdHRvbTogMXB4ICNjY2Mgc29saWQ7Cn0KCgp1bC5ub3RlcyA+IGxpIHA6Zmlyc3QtY2hpbGQgewoJbWFyZ2luLXRvcDogMDsKfQoKdWwubm90ZXMgPiBsaSBwOmxhc3QtY2hpbGQgewoJbWFyZ2luLWJvdHRvbTogMDsKfQoKLyogQWRkIHF1b3RhdGlvbiBtYXJrcyBhcm91bmQgYmxvY2txdW90ZSAqLwp1bC5ub3RlcyA+IGxpIGJsb2NrcXVvdGUgcDpub3QoOmVtcHR5KTpiZWZvcmUsCmxpLm5vdGUgYmxvY2txdW90ZSBwOm5vdCg6ZW1wdHkpOmJlZm9yZSB7Cgljb250ZW50OiAn4oCcJzsKfQoKdWwubm90ZXMgPiBsaSBibG9ja3F1b3RlIHA6bm90KDplbXB0eSk6bGFzdC1jaGlsZDphZnRlciwKbGkubm90ZSBibG9ja3F1b3RlIHA6bm90KDplbXB0eSk6bGFzdC1jaGlsZDphZnRlciB7Cgljb250ZW50OiAn4oCdJzsKfQoKLyogUHJlc2VydmUgd2hpdGVzcGFjZSBvbiBwbGFpbnRleHQgbm90ZXMgKi8KdWwubm90ZXMgbGkgcC5wbGFpbnRleHQsIGxpLm5vdGUgcC5wbGFpbnRleHQsIGRpdi5ub3RlIHAucGxhaW50ZXh0IHsKCXdoaXRlLXNwYWNlOiBwcmUtd3JhcDsKfQoKLyogRGlzcGxheSB0YWdzIHdpdGhpbiBjaGlsZCBub3RlcyBpbmxpbmUgKi8KdWwubm90ZXMgaDMudGFncyB7CglkaXNwbGF5OiBpbmxpbmU7Cglmb250LXNpemU6IDFlbTsKfQoKdWwubm90ZXMgaDMudGFnczphZnRlciB7Cgljb250ZW50OiAnICc7Cn0KCnVsLm5vdGVzIHVsLnRhZ3MgewoJZGlzcGxheTogaW5saW5lOwp9Cgp1bC5ub3RlcyB1bC50YWdzIGxpOm5vdCg6bGFzdC1jaGlsZCk6YWZ0ZXIgewoJY29udGVudDogJywgJzsKfQoKCi8qIENoaWxkIGF0dGFjaG1lbnRzICovCmgzLmF0dGFjaG1lbnRzIHsKCWZvbnQtc2l6ZTogMS4xZW07Cn0KCnVsLmF0dGFjaG1lbnRzIGxpIHsKCXBhZGRpbmctdG9wOiAuNWVtOwp9Cgp1bC5hdHRhY2htZW50cyBkaXYubm90ZSB7CgltYXJnaW4tbGVmdDogMmVtOwp9Cgp1bC5hdHRhY2htZW50cyBkaXYubm90ZSBwOmZpcnN0LWNoaWxkIHsKCW1hcmdpbi10b3A6IC43NWVtOwp9Cg==">
  		<link rel="stylesheet" type="text/css" media="screen,projection" href="data:text/css;base64,LyogR2VuZXJpYyBzdHlsZXMgKi8KYm9keSB7Cglmb250OiA2Mi41JSBHZW9yZ2lhLCBUaW1lcywgc2VyaWY7Cgl3aWR0aDogNzgwcHg7CgltYXJnaW46IDAgYXV0bzsKfQoKaDIgewoJZm9udC1zaXplOiAxLjVlbTsKCWxpbmUtaGVpZ2h0OiAxLjVlbTsKCWZvbnQtZmFtaWx5OiBHZW9yZ2lhLCBUaW1lcywgc2VyaWY7Cn0KCnAgewoJbGluZS1oZWlnaHQ6IDEuNWVtOwp9CgphOmxpbmssIGE6dmlzaXRlZCB7Cgljb2xvcjogIzkwMDsKfQoKYTpob3ZlciwgYTphY3RpdmUgewoJY29sb3I6ICM3Nzc7Cn0KCgp1bC5yZXBvcnQgewoJZm9udC1zaXplOiAxLjRlbTsKCXdpZHRoOiA2ODBweDsKCW1hcmdpbjogMCBhdXRvOwoJcGFkZGluZzogMjBweCAyMHB4Owp9CgovKiBNZXRhZGF0YSB0YWJsZSAqLwp0YWJsZSB7Cglib3JkZXI6IDFweCAjY2NjIHNvbGlkOwoJb3ZlcmZsb3c6IGF1dG87Cgl3aWR0aDogMTAwJTsKCW1hcmdpbjogLjFlbSBhdXRvIC43NWVtOwoJcGFkZGluZzogMC41ZW07Cn0K">
  		<link rel="stylesheet" type="text/css" media="print" href="data:text/css;base64,Ym9keSB7Cglmb250OiAxMnB0ICJUaW1lcyBOZXcgUm9tYW4iLCBUaW1lcywgR2VvcmdpYSwgc2VyaWY7CgltYXJnaW46IDA7Cgl3aWR0aDogYXV0bzsKCWNvbG9yOiBibGFjazsKfQoKLyogUGFnZSBCcmVha3MgKHBhZ2UtYnJlYWstaW5zaWRlIG9ubHkgcmVjb2duaXplZCBieSBPcGVyYSkgKi8KaDEsIGgyLCBoMywgaDQsIGg1LCBoNiB7CglwYWdlLWJyZWFrLWFmdGVyOiBhdm9pZDsKCXBhZ2UtYnJlYWstaW5zaWRlOiBhdm9pZDsKfQoKdWwsIG9sLCBkbCB7CglwYWdlLWJyZWFrLWluc2lkZTogYXZvaWQ7Cgljb2xvci1hZGp1c3Q6IGV4YWN0Owp9CgpoMiB7Cglmb250LXNpemU6IDEuM2VtOwoJbGluZS1oZWlnaHQ6IDEuM2VtOwp9CgphIHsKCWNvbG9yOiAjMDAwOwoJdGV4dC1kZWNvcmF0aW9uOiBub25lOwp9Cg==">
  	</head>
  	<body>
  		<ul class="report combineChildItems">
  """

  end_info = """</ul>

  </body></html>"""


  count = 0
  change = False
  new_file = False
  directory = page_name
  try:
      os.stat(directory)
  except:
      os.mkdir(directory)
  prev_line = ''
  with open(directory+".html", "r", encoding='utf-8') as f:
      text= f.readlines()
      Html_file = ''
      for lines in text:
          if 'h2' in lines:
              Html_file= open(directory+"/"+directory+str(count)+".html","w",encoding="utf-8")
              new_file = True
              change = False
              Html_file.write(head_info)
              Html_file.write(prev_line)
              count+=1
          if '</li>' in lines:
              if '</ul>' in prev_line:
                  change = True
          if count > 0 and change == False:
              Html_file.write(lines)
          elif change == True and new_file == True:
              Html_file.write(lines)
              Html_file.write(end_info)
              new_file = False
              Html_file.close()
          prev_line = lines
  print('Extracted '+str(count)+' papers')

def generate_index_from_html(page_name=None):
  directory = page_name
  try:
      os.stat(directory)
  except:
      os.mkdir(directory)

  with open(directory+".html", "r", encoding='utf-8') as f:
      text= f.readlines()
      Html_file = ''
      Html_file= open(directory+"/"+directory+"_index.html","w",encoding="utf-8")
      for lines in text:
          if 'h2' in lines:
              Html_file.write(lines)


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print('Please select the html file to extract')
    files = glob.glob('*.html')
    for i in range(0,len(files)):
      print(str(i)+" : "+files[i])
    f_num = int(input())
    seperate_papers_from_html(page_name=files[f_num][:-5])
    generate_index_from_html(page_name=files[f_num][:-5])
  elif len(sys.argv) == 2:
    seperate_papers_from_html(page_name=sys.argv[1][:-5])
    generate_index_from_html(page_name=sys.argv[1][:-5])
  else:
    print('wrong way to run the script !')
