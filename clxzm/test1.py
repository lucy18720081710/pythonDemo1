#
# gg = [1,"nice hat"]
# print(gg)
#
# hh = {"name":"xzm", "sex":"men"}
# print(hh)
#
#
# a = [1,2,3,4,5]
# sa = set(a)
# print(sa)
#
# sb = set([4,5,6,7,8])
# print(sb)
# print(sa-sb)
#
# a = [1,2,3,3,3,4,5,6,6]
# myList = [item*4 for item in a]
# print(myList)
#
# a = [3,4,5,10]
# myList2 = []
# for item in a:
#     myList2.append(item*2)
# print(myList2)
#
#
# myList4 = [item*3 for item in a if item>4]
# print(myList4)
#
#
# myList3 = []
# for item in a:
#     if item>4:
#         myList3.append(item*3)
# print(myList3)
#
#
# from numpy import array
# mm = array((1,1,1,))
# pp = array((2,3,4))
# print(mm + pp)

# import json
# path = "ch02/usagov_bitly_data2013-03-16-1331923249.txt"

# time_zones = [rec["tz"] for rec in records if "tz" in rec]

# from pandas import DataFrame,Series
# import  pandas as pd
# import numpy as np
# frame = DataFrame(records)
# print(frame)
# print(frame["tz"][:10])
#
# import numpy as np
# from numpy.random import randn
# data = {i : randn() for i in range(7)}
# print(data)
#
# data1 = [6,7,8,2,4]
# arr1 = np.array(data1)
# print(arr1)

# print(np.empty((2,3,2)))
#
# print(np.arange(15))

# print(arr1.dtype)
# float_arr1 = arr1.astype(np.float64)
# print(float_arr1.dtype)

# from numpy.random import randn
# arr = randn(8)
# arr.sort()
# print(arr)
# arr = randn(5,3)
# arr.sort(1)
# print(arr)

# import numpy as np
# ints = np.array([3,3,3,2,1,1,4,4])
# print(np.unique(ints))

# from numpy.random import randn
# large_arr = randn(1000)
# large_arr.sort()
# a = large_arr[0.05 * len(large_arr)]
# print(a)

# import numpy as np
# arr = np.arange(15).reshape((3,5))
# print(arr.T)
# print(np.dot(arr.T,arr))

# import numpy as np
# arr = np.arange(16).reshape((2,2,4))
# print(arr.transpose((1,0,2)))
# print(arr.swapaxes(1,2))

# from numpy.random import randn
# import numpy as np
# arr = randn(4,4)
# print (np.where(arr>0,2,-2))


# import numpy as np
# arr = np.arange(10)
# np.save("some_array.npy",arr)
# print(np.load("some_array.npy"))

# import random
# position = 0
# walk = [position]
# steps = 1000
# for i in xrange(steps):
#     step = 1 if random.randint(0,1) else -1
#     position += step
# print(walk.append(position))

# import numpy as np
# nsteps = 1000
# draws = np.random.randint(0,1,size=nsteps)
# steps = np.where(draws>0,1,-1)
# walk = steps.cumsum()
# print(walk.min())
# print(walk.max())
# print((np.abs(walk) >= 10).argmax())

# import numpy as np
# nwalks = 5000
# nsteps = 1000
# draws = np.random.randint(0,2,size=(nwalks,nsteps))
# steps = np.where(draws > 0,1,-1)
# walks = steps.cumsum(1)
# print(walks)
# print(walks.max())

#
# from pandas import *
# from pandas import Series,DataFrame
# obj2 = Series([4,7,-5,3],index = ["d","b","a","c"])
# print(obj2)

# from pandas import *
# from lxml.html import parse
# from urllib2 import urlopen
# parsed = parse(urlopen("http:/finance.yahoo.com/q/op?s=AAPL+Options"))
# doc = parsed.getroot()


import pandas as pd
import numpy as np
# df1 = pd.DataFrame({"key":["b","b","a","c","a","a","b"],
#                  "data1":range(7)})
# df2 = pd.DataFrame({"key":["a","b","d"],
#                  "data2":range(3)})
# print(pd.merge(df1,df2,on="key"))
#
#
# data = pd.DataFrame(np.arange(6).reshape((2,3)),
#                     index=pd.Index(["Ohio","Colorado"],name="state"),
#                     columns=pd.Index(["one","two","three"],
#                                      name="number"))
# print(data)
# result = data.stack()
# print(result)
# print(result.unstack(0))

# s1 = pd.Series([0,1,2,3],index=["a","b","c","d"])
# s2 = pd.Series([4,5,6],index=["c","d","e"])
# data2 = pd.concat([s1,s2],keys=["one","two"])
# print(data2)
# print(data2.unstack())

