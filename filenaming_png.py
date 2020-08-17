import os
os.chdir('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_png/checkbox1')
Lredcheck = os.listdir()
Lredcheck.sort()


for a in range(round(len(Lredcheck)/4)):
    for i in range(1,5):
        name = Lredcheck[4*a + i - 1]
        if name[10:] == '_0.5x.png':
            src = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_png/checkbox1', name)
            dst = 'checkbox1.' + str(a+1) + '_0.5x.png'
            dst = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_png/checkbox1',dst)
            os.rename(src, dst)
        if name[10:] == '_1x.png':
            src = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_png/checkbox1', name)
            dst = 'checkbox1.' + str(a+1) + '_1x.png'
            dst = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_png/checkbox1',dst)
            os.rename(src, dst)
        if name[10:] == '_2x.png':
            src = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_png/checkbox1', name)
            dst = 'checkbox1.' + str(a+1) + '_2x.png'
            dst = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_png/checkbox1',dst)
            os.rename(src, dst)
        if name[10:] == '_4x.png':
            src = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_png/checkbox1', name)
            dst = 'checkbox1.' + str(a+1) + '_4x.png'
            dst = os.path.join('/Users/youngmin-woo/Desktop/#./#.Products/아이콘/업로드용 분류/CHECKBOX650/CHECKBOX_Lred_png/checkbox1',dst)
            os.rename(src, dst)
