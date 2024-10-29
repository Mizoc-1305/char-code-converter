import sys

# 文字コードの対応
encodings = {
    "1": "shift_jis",
    "2": "iso2022_jp",
    "3": "euc_jp",
    "4": "utf-8"
}

# 文字コード選択メニュー
def display_menu():
    print("変換前の文字コードを選択してください:")
    print("1: Shift_JIS")
    print("2: ISO-2022-JP")
    print("3: EUC-JP")
    print("4: Unicode (UTF-8)")
    source_encoding = input("番号を入力: ")

    print("\n変換後の文字コードを選択してください:")
    print("1: Shift_JIS")
    print("2: ISO-2022-JP")
    print("3: EUC-JP")
    print("4: Unicode (UTF-8)")
    target_encoding = input("番号を入力: ")

    if source_encoding in encodings and target_encoding in encodings:
        print(f"{encodings[source_encoding]} から {encodings[target_encoding]} に変換します。")
        # 番号を文字コード名の対応から変換して返す
        return encodings[source_encoding], encodings[target_encoding]
    else:
        print("無効な選択です。プログラムを終了します。")
        sys.exit()

# 16進数のバイト列をデコード
def decode_hex_to_text(hex_string, encoding):
    try:
        # 16進数のバイト列をバイトデータに変換してデコード
        byte_data = bytes.fromhex(hex_string)
        return byte_data.decode(encoding)
    except Exception as e:
        print(f"デコードエラー: {e}")
        sys.exit()

# テキストを指定の文字コードでエンコードして16進数に変換
def encode_text_to_hex(text, encoding):
    try:
        encoded_bytes = text.encode(encoding)
        return encoded_bytes.hex().upper()
    except Exception as e:
        print(f"エンコードエラー: {e}")
        sys.exit()

# メイン処理
def main():
    source_encoding, target_encoding = display_menu()
    hex_input = input("\n変換したい16進数のバイト列を入力してください。空白は入れず、Unicodeの場合「U+」は削除してください。: ")

    try:
        # 16進数の入力をデコードしてUnicode文字列に変換
        decoded_text = decode_hex_to_text(hex_input, source_encoding)
        print(f"\nデコード結果: {decoded_text}")

        # 変換後の文字コードでエンコードし、16進数表現で表示
        hex_output = encode_text_to_hex(decoded_text, target_encoding)
        print(f"{target_encoding}形式の16進数出力: {hex_output}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
