import os,weasyprint,glob
from PyPDF2 import PdfFileMerger

for num in range(21):
    pdf = weasyprint.HTML('https://automatetheboringstuff.com/2e/chapter%s/' % (num)).write_pdf()
    open('automate%s.pdf' % (num), 'wb').write(pdf)
    if num !=0:
        print('Page %s of 20 complete.' % (num))

count = 1
for appendix in "abc":
    pdf = weasyprint.HTML('https://automatetheboringstuff.com/2e/appendix%s/' % (appendix)).write_pdf()
    open('automate%s.pdf' % (appendix), 'wb').write(pdf)
    print('Appendix %s of 3 complete' % (count))
    count = count + 1

print('Now merging...')

x = [a for a in sorted(os.listdir()) if a.endswith('.pdf')]
merger = PdfFileMerger()

for pdf in x:
    merger.append(open(pdf, 'rb'))

with open('sweigert.pdf;, 'wb') as fout:
    merger.write(fout)

for f in glob.glob('automate*.pdf'):
    os.remove(f)
