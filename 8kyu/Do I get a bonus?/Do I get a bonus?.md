# 題目要求

1. 題目給定兩個參數，salary 為整數， bonus 為布林值。

2. 如果 bonus 為真，則回傳 "$" + salary * 10 ；如果 bonus 為否，則回傳 "$" + salary 。

-----------------

# 解題思路

1. if 判斷式直述。

>       def bonus_time(salary, bonus):
>           if bonus :
>               return "$" + str(salary * 10)
>           else:
>               return "$" + str(salary)
