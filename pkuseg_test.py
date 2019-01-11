# 引入 pkuseg
import pkuseg as ps
seg = ps.pkuseg()
text = seg.cut("改革春风吹满地")
text1 = seg.cut("我就是这条街上最靓的仔")
print(text) 
print(text1)