import os
os.chdir('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_svg/checkbox3')
Lredcheckbox3 = os.listdir()
Lredcheckbox3.sort()


for i in range(round(len(Lredcheckbox3))):
               name = Lredcheckbox3[i]
               src = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_svg/checkbox3', name)
               dst = 'checkbox3.' + str(i+1) + '.svg'
               dst = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_svg/checkbox3',dst)
               os.rename(src, dst)
