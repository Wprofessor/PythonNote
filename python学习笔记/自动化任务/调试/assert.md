# 断言
### “断言”是一个心智正常的检查，确保代码没有做什么明显错误的事情。这些 心智正常的检查由 assert语句执行。如果检查失败，就会抛出异常。
* ### assert为关键字
* ### 条件
* ### 逗号
* ### 当条件为false时显示的字符串
```
>>> podBayDoorStatus = 'open' 
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".' 
>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can't do that.'' 
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".' 
Traceback (most recent call last):    
    File "<pyshell#10>", line 1, in <module>  
        assert podBayDoorStatus == 'open', 'The pod bay doors need to be"open".' 
    AssertionError: The pod bay doors need to be "open". 
```