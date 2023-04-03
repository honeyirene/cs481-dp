import pickle
import json
import numpy

### 피클 파일 불러오기 ###
with open("K-EmoCon.CS481.pkl", "rb") as fr:
    data = pickle.load(fr)

### json으로 변환할때 터지는 것을 막기위한 변환 로직 ###
class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        if isinstance(obj, numpy.int64):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

### json으로 변환
print('dump start')
json_str = json.dumps(data, cls=NumpyArrayEncoder)
print('dump end')

### 쪼개서 저장 (
##### 사실 임의로 쪼갠 시점에서 망가진 json파일이긴하나
##### 아무튼 포매터가 뭔가 해줄수있으니 json으로 저장
i = 0
while (len(json_str) > 0):
    print(i)
    f = open('./data' + str(i) + '.json', 'w+')
    cnt = min(len(json_str), 2 ** 28)
    target = json_str[0:cnt]
    json_str = json_str[cnt: -1]
    f.write(target)
    f.close()
    i += 1
