# 題目要求

1. 定義函式中會有兩個引數：

   * 父親現在的年齡

   * 兒子現在的年齡

2. 計算多少年後或是年前，父親的年齡為兒子的兩倍。

-----------------

# 解題思路

1.  可以利用 for 迴圈與 if 判斷式不斷迭代比較。

2. for 迴圈的範圍可以設定人類可能達到的歲數範圍， 例如： 0 至 100 。

    >       for years in range(0, 100):

3. if 判斷式就只要把題目條件敘明既可。
   
    >        if (dad_years_old + years) == 2 * (son_years_old + years):
    >               return years
    >        elif (dad_years_old - years) == 2 * (son_years_old - years):
    >               return years
