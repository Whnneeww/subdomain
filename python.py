input_string = input("Enter a string: ")  # ユーザーから文字列を入力 
 
# 文字列を小文字に変換し、スペースをハイフンに置換してサブドメインを作成 
subdomain = input_string.lower().replace(" ", "-") 
 
print("Subdomain created: " + subdomain) 
