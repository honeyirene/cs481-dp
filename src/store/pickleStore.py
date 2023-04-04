import pickle

class PickleStore:
    # TODO: 데이터에 맞게 struct 만들기
    def load(self) -> any:
        with open("../K-EmoCon.CS481.pkl", "rb") as fr:
            data = pickle.load(fr)
        return data

if __name__ == '__main__':
    store = PickleStore()
    store.load()
