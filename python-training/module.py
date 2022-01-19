# 載入模組 import / import as
import sys as system
print(system.platform)
print(system.maxsize)

# 內建模組 sys模組 import sys as s

# 自訂模組 建立幾何運算模組
import modules.geometry as geometry
result= geometry.distance(1,1,5,5)
print(result)
result= geometry.slope(1,2,5,6)
print(result)

# 調整搜尋模組的路徑
import sys
sys.path.append("modules")   # 在模組的搜尋路徑列表中【新增路徑】
print (sys.path) # 印出模組的搜尋路徑

import modules.geometry as geometry
result= geometry.distance(1,1,5,5)
print(result)