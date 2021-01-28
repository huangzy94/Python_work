# Python_ui_automation

*author：黄振宇*

*create_date：2020/03/12*

#### Python_work
Ui_Automation 是基于python+selenium编写的UI自动化脚本，涉及以下常见场景及对应的处理方法：

> select形式的下拉框及DOM结构形式的下拉框定位方法（OPS\TestCase\test_1_food.py	line38）；

> 控制滚动条滚动到页面指定位置（OPS\TestCase\test_1_food.py	line119）；

> 使用第三方工具实现调用本地文件并上传文件（OPS\TestCase\test_1_food.py	line128）；

> 无法定位元素唯一属性（或动态变化元素）时的处理方法（使用for循环在变化区间内遍历出现的元素）（OPS\TestCase\test_1_food.py	line228）；

> 配置日志文件，打印日志信息（OPS\Log\Log.py）；

> 套用测试框架，规范测试流程及用例（unittest.TestCase）；

> 引用第三方邮件插件，实现自动发送测试报告邮件（OPS\Suite\Email\AutoSendEmail.py）；

> 自定义测试报告文件，自动生成测试报告（OPS\Suite\run_test_suite.py）；

> 操作弹窗处理方法（OPS\TestCase\test_1_food.py	line146）。



#### Python  test_run_suite.py

cmd命令执行如上python脚本报： No module named xxx

> 需要在系统变量中添加python项目目录（拉取的项目根目录）。原因是python执行时会向下搜索文件，而PyCharm执行时会默认带上项目路径
>
> ![image-20210128095326793](C:\Users\hzy\AppData\Roaming\Typora\typora-user-images\image-20210128095326793.png)



#### Python+jenkin集成

- 本地jenkin集成python项目前，需安装 Python Plugin、Python Wrapper Plugin插件；

- 节点-节点属性中添加键值对（python安装路径）

  ![image-20210128100419440](C:\Users\hzy\AppData\Roaming\Typora\typora-user-images\image-20210128100419440.png)

- 执行windows命令

  ![image-20210128100543387](C:\Users\hzy\AppData\Roaming\Typora\typora-user-images\image-20210128100543387.png)