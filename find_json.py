import ast

# 定義一個函式，用於在巢狀字典中尋找特定值的鍵
def find_keys_by_value(data, target_value, current_path=""):
    found_keys = []
    for key, value in data.items():
        # 建立當前層級的鍵路徑
        current_key_path = f"{current_path}['{key}']" if current_path else f"['{key}']"

        # 檢查當前值是否與目標值相符
        if value == target_value:
            found_keys.append(current_key_path)
        
        # 如果當前值是列表（陣列），則在列表中檢查目標值
        elif isinstance(value, list) and target_value in value:
            index = value.index(target_value)
            found_keys.append(f"{current_key_path}[{index}]")

        # 如果當前值是字典，則遞迴搜尋該字典
        elif isinstance(value, dict):
            found_keys.extend(find_keys_by_value(value, target_value, current_key_path))
    return found_keys

try:
    # 讀取 "find_json.txt" 檔案的內容
    with open("C:\\Users\\Blood\\Documents\\Python\\rorschach_stock_bot\\04_short\\find_json.txt", "r", encoding="utf-8") as file:
        input_str = file.read()

    # 使用 ast.literal_eval() 解析輸入字串
    input_data = ast.literal_eval(input_str)

    # 輸入目標值
    target_value = input("請輸入要尋找的值: ")

    # 尋找具有目標值的鍵
    keys_with_value = find_keys_by_value(input_data, target_value)

    # 輸出結果
    if keys_with_value:
        print(f"具有值 '{target_value}' 的鍵:")
        for key in keys_with_value:
            print(key)
    else:
        print(f"未找到值 '{target_value}' 的鍵.")

except ValueError as e:
    print(f"值錯誤: {e}")
