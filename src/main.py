from store.pickleStore import PickleStore

# 이쪽도 데이터 고치기
def main() -> None:
    store: PickleStore = PickleStore()
    data: any = store.load()
    print(data.keys())
    return

if __name__ == '__main__':
    main()
