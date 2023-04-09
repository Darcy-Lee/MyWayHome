> 本project用于选调生数量统计
>
> excel_each_year中是各年招生文件,旧的不要去动,是修改过表头以适应pandas的
>
> outputs是筛选过后的excel文件

运行方法:python shelter.py

说明:该脚本会进入excels_each_year,执行py脚本,遍历各个表格,按照条件筛选出符合条件的line并做简单的统计

更新维护方法:出现新一年数据的时候,将表格下载到excels文件夹,改为xlsx文件,并修改表头(表头每年做的人不太一样,但意义大致是一样的),比起改代码,还是人为统一每年excel格式比较方便

如果要改条件,则修改py脚本中的筛选条件,记得借助cursor或ChatGPT



