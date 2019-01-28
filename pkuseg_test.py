# 引入 pkuseg 北大开源分词工具包
# 结果 ['改革', '春风', '吹满', '地']['我', '就是', '这', '条', '街上', '最', '靓', '的', '仔']

import pkuseg as ps
seg = ps.pkuseg()
text = seg.cut("改革春风吹满地")
text2 = seg.cut("我就是这条街上最靓的仔")
print(text)
print(text2)