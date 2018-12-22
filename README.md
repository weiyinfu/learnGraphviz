graphviz是贝尔实验室开发的一个开源的工具包，它使用一个特定的DSL(领域特定语言): dot作为脚本语言，然后使用布局引擎来解析此脚本，并完成自动布局。graphviz提供丰富的导出格式，如常用的图片格式，SVG，PDF格式等。

graphviz官网地址:http://www.graphviz.org/

dot input.dot -T png -o output.png 


# 理解概念
* graphviz：一套工具包，一个软件
* dot：一门语言，一种领域特定语言DSL（Domain Specified Language）
* dot：一种布局，树形布局，也是graphviz最初的布局，也是效果最好的一种布局

# dot语言中的概念
* 图Graph
* 结点Node
* 边Edge
* 子图Subgraph

# 一些枚举
## 图布局的种类
* dot
* neato
* fdp
* sfdp
* twopi
* circo

## 导出文件的类型
* images:jpg,png
* svg
* pdf
* postscript

## 中文字体的英文名称
新細明體：PMingLiU
細明體：MingLiU
標楷體：DFKai-SB
黑体：SimHei
宋体：SimSun
新宋体：NSimSun
仿宋：FangSong
楷体：KaiTi
仿宋_GB2312：FangSong_GB2312
楷体_GB2312：KaiTi_GB2312
微軟正黑體：Microsoft JhengHei
微软雅黑体：Microsoft YaHei

# Python对graphviz的封装
很多人都对graphviz进行了python化，出现了很多版本，如pygraphviz、pydot、graphviz
其中貌似pydot用得比较多，这个库非常小，它只负责字符串处理。
https://www.programcreek.com/python/example/5579/pydot.Dot

# 查看文档
学习graphviz不必远求，安装之后在安装目录中自然就有。在share目录下。  
本repo的doc/html/info目录是最重要的graphviz文档。
