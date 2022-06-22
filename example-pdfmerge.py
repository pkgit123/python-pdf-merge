import os
import re
from PyPDF2 import PdfFileMerger

flag_output_name = True
pdf_merge = PdfFileMerger()
ls_files = []
re_exp_match = r"^this_string_(20\d\d)_more_string(\d+)_.*\.pdf$"

for each_file in os.listdir(os.getcwd()):
  if each_file.endswith('.pdf'):
    ls_files.append(each_file)
ls_files.sort()

for each_file in ls_files:
  pdf_merge.merge(each_file)

if flag_output_name:
  if re.search(re_exp_match, ls_files[0]):
    m_group = re.match(re_exp_match, ls_files[0])
    year = m_group.group(1)
    week = m_group.group(2)
    print(f"filename{year}_{week}.pdf")
    pdf_merge.write(f"filename{year}_{week}.pdf")
    pdf_merge.close()
else:
  pdf_merge.write(f"other_filename.pdf")
  pdf_merge.close()
