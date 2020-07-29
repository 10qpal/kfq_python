#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import warnings
warnings.filterwarnings('ignore')

mpl.rcParams['axes.unicode_minus'] = False
#%%

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # x 위치
width = 0.35    # 막대 너비
plt.rcParams['font.family'] = 'NanumBarunGothic'
plt.rcParams['font.size'] = 14
p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=menStd)    # 위, 아래에 나타내기 위해 bottom 설정
plt.ylabel('점수')
plt.xlabel('그룹')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
# 범례
plt.legend((p1[0], p2[0]), ('남자', '여자'))

# %%
