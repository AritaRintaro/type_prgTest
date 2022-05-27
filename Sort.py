def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    
    # 探索範囲のindexを[down, up]とする
    down = 0
    up = len(sorted_array) - 1
    
    # 探索対象のサイズが2以上の場合
    while down!= up:
        mid = (up + down)//2 # 中央のindex
        if(sorted_array[mid] == target_number): # 中央の要素とターゲットを比較
            return mid
        elif(sorted_array[mid] < target_number): # ターゲットが右にある場合
            down = mid + 1 # midの次の要素から再度探索
        else:
            up = mid - 1 # midの下から再度探索
    
    # 探索対象のサイズが1の場合
    if(sorted_array[down] == target_number):
        return down
    
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
