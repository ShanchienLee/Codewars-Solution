# 題目要求

1. 題目給定一字串，目標為回傳重複一次每個字母的字串。

2. Examples:

    > "String" -> "SSttrriinngg"
    > 
    > "Hello World" -> "HHeelllloo WWoorrlldd"
    > 
    > "1234!_" -> "11223344!!__"

-----------------

# 解題思路

1. 設立一變數 temp 存放 list 。

>       temp = []

2. 以 for 迴圈從給定字串 s 中，取字母。

>       for i in s:

3. 以 append 函數讓選取的字母重複。

>           temp.append(i+i)

* 此處會利用 join 函數，可以將序列、元組等等以指定元素連接，並轉為字串。此處以空字串 ”“ 作為連結元素。

>       return "".join(temp)
