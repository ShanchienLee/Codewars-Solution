# 題目要求

1. 你同學請你幫忙印作業，班上有 'n' 個同學，作業有 'm' 頁。

2. 算出需要多少張白紙，而如果 n < 0 或是 m < 0 ，則回傳 0 。

>       Example:
>
>       n = 5, m = 5: 25
>
>       n = -5, m = -5: 0

-----------------

# 解題思路

1. if 判斷式直述。

>        if n>= 0 and m >= 0:
> 
>           return n*m
> 
>        else:
> 
>           return 0
