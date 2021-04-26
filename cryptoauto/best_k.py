import pyupbit
import numpy as np

def get_ror(k): # 수익률(ror) 구하는 함수
    df = pyupbit.get_ohlcv("KRW-BTC", count = 16) # 원화거래소-'원하는코인', n일전동안의 기록
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0011 # Fee 엑셀 참고
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror

"""
# k값과 수익률을 저장하기 위한 2차원 배열
a = [[0]*2 for _ in range(9)]

for k in range(1,10): # k는 소숫점 한자리로 나타내기위해 나누기 10
    ror = get_ror(k/10)
    a[k-1][0] = ror # k가 0.1때부터 0.9가 될때까지 수익률 a배열에 저장
    a[k-1][1] = k/10
    # print("%.1f %f" % (k/10, ror))

bestk = a[0] # 가장 높은 수익률을 보여주는 K값 저장
for i in a:
    if i > bestk:
        bestk = i

print("best_k =", bestk[1])
"""

def get_bestk():
    a = [[0]*2 for _ in range(9)]

    for k in range(1,10): # k는 소숫점 한자리로 나타내기위해 나누기 10
        ror = get_ror(k/10)
        a[k-1][0] = ror # k가 0.1때부터 0.9가 될때까지 수익률 a배열에 저장
        a[k-1][1] = k/10
        print("%.1f %f" % (k/10, ror))

    bestk = a[0] # 가장 높은 수익률을 보여주는 K값 저장
    for i in a:
        if i > bestk:
            bestk = i
    return bestk[1]

print(get_bestk())