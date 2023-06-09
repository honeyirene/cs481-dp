import pickle
from typing import cast
from dataStructure.researchData import ResearchData

class PickleStore:
    # TODO: 데이터에 맞게 struct 만들기

    def load(self) -> ResearchData:
        with open("../K-EmoCon.CS481.pkl", "rb") as fr:
            data: ResearchData = cast(ResearchData, pickle.load(fr))
        return data


# 코드 돌아가는지 테스트용
if __name__ == '__main__':
    store: PickleStore = PickleStore()
    data: any = store.load()
    print(data.keys())
