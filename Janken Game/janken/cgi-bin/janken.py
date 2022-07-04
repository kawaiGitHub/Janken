import random
print("番号を入力してください")
print("[1.グー　2.チョキ　3.パー]")
a = input("番号:")
b = int(a)
c = random.randint(1,3)
if b==1:
    if c==1:
        print("コンピュータ：グー　　結果：あいこ")
    elif c==2:
        print("コンピュータ：チョキ　　結果：勝ち")
    else:
        print("コンピュータ：パー　　結果：負け")
elif b==2:
    if c==1:
        print("コンピュータ：グー　　結果：負け")
    elif c==2:
        print("コンピュータ：チョキ　　結果：あいこ")
    else:
        print("コンピュータ：パー　　結果：勝ち")
elif b==3:
    if c==1:
        print("コンピュータ：グー　　結果：勝ち")
    elif c==2:
        print("コンピュータ：チョキ　　結果：負け")
    else:
        print("コンピュータ：パー　　結果：あいこ")
else:
    print("1から3の整数を入力してください")