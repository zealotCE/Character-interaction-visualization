## 说明

这个东西本来只是自用的，所以比较复杂使用了多种编程环境和繁杂的步骤。

在尽量简化的状态下，已经可以正常使用了。步骤我已经走过了，所以没有问题。

如果实在是有问题就问。

## 安装

安装环境：Anaconda，java，gephi

Anaconda安装注意：

1． 打开程序：Anaconda3-4.4.0-Windows-x86_64.exe 

2． 在选择了安装路径后注意勾选 Add Anaconda to my_path…![](http://om80aljc8.bkt.clouddn.com/17-9-26/7067669.jpg)

3． 打开程序： C:\WINDOWS\system32\cmd.exe 右键管理员运行，出现一个黑框

4． 输入：pip install jieba  回车，等待出现success![](http://om80aljc8.bkt.clouddn.com/17-9-26/7774652.jpg)![](http://om80aljc8.bkt.clouddn.com/17-9-26/55291133.jpg)  

Java 安装：

1.    打开程序 JavaSetup8u144.exe

2.    一路下一步就行（用默认文件夹）

Gephi 安装：

1.    打开程序： gephi-0.9.2-20170923.130053-377-windows.exe

2.    一路下一步（用默认文件夹）

3.    打开我的电脑进入文件夹：C:\ProgramFiles\Gephi-0.9.2-SNAPSHOT\etc

4.    将文件gephi.conf替换掉（给你的压缩包里有）

 

## 使用

1.    准备小说和小说里面人物的文件（txt格式）

注意小说人物的文件请按照每个名字一行的方式存储，例如：

![](http://om80aljc8.bkt.clouddn.com/17-9-26/53715109.jpg)

2.    将文件 relationship.py 、[小说].txt、[小说人物文件].txt 放到一个文件夹。

3.    在文件夹空白处 shift + 鼠标右键，点击 在此处打开 Powershell 窗口 或者 在此处打开命令窗口（二者只会出现一种情况）。

![](http://om80aljc8.bkt.clouddn.com/17-9-26/24079899.jpg)

4.    输入 python relationship.py 

5.    出去喝杯茶聊个天再回来看。

6.    如果最后一行没有显示 

a)     **任务完成，别喝茶了！**

7.    那就再去喝杯茶咯。

8. 成功后会得到两个文件：gephi_notexx-xx.csv 和gephi_edge xx-xx.csv

9.    好了，已经只剩下把数据显示出来，做个漂亮的图表了

10.  打开程序 gephi 

11.  选择新建工程

![](http://om80aljc8.bkt.clouddn.com/17-9-26/72069226.jpg)

12.  点击数据资料 → 输入电子表格

![](http://om80aljc8.bkt.clouddn.com/17-9-26/14939218.jpg)

13.  选择文件  xx_xxgephi_note.csv

 ![](http://om80aljc8.bkt.clouddn.com/17-9-26/58856108.jpg)

14.  一定要选择Append to existing workspace 然后点击确定（节点文件算是添加了）

15.  同理：选择文件xx_xxgephi_edge.csv 

注：一定要选择 Append to existing workspace 

16.  点击概览 

17.  节点调整参数，设置好了点击右下角的应用就可以看到改变了

![](http://om80aljc8.bkt.clouddn.com/17-9-26/16364079.jpg)

18.  特别说一下调整节点的大小，这样显示圆就会有大有小。

![](http://om80aljc8.bkt.clouddn.com/17-9-26/11753371.jpg)

19.  自动化布局方式选择

![](http://om80aljc8.bkt.clouddn.com/17-9-26/88175486.jpg)

20.  自动化布局参数调整，这个自己调整就好了，鼠标放上去会有提示的

![](http://om80aljc8.bkt.clouddn.com/17-9-26/96638883.jpg)

21.  显示标签云，底部条功能

![](http://om80aljc8.bkt.clouddn.com/17-9-26/29831531.jpg)

22.  调整完了之后预览并输出层png等形式

23.  预览设置

![](http://om80aljc8.bkt.clouddn.com/17-9-26/43655532.jpg)

24.  到处调整好的图片

![](http://om80aljc8.bkt.clouddn.com/17-9-26/19090660.jpg)

25.  结束

 