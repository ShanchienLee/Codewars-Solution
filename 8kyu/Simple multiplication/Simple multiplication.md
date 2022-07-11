# 題目要求

1. 題目給定一數字，如為偶數即乘以 8 ，其餘則乘以 9 。
   
2. 回傳答案。

-----------------

# 解題思路

1. 以 if 判斷式進行。

2. 以除以 2 是否餘數為 1 判斷奇偶。
    * 採用的是 % 計算除法餘數的運算子

>       def simple_multiplication(number) :
>           if number % 2 == 0:
>               return number * 8
>           elif number % 2 == 1:
>               return number * 9
