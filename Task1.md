# Flask 从入门到...
  - 2016-11-21
  - 来自你们即将滚蛋的老咸鱼部长以及郭dalao

**Important: Use Python3+, UTF-8**

## Stage 1
 - DEADLINE:**2016-11-30 23:59(UTC+8)**

**切换到 stage1 分支！！！**
**切换到 stage1 分支！！！**
**切换到 stage1 分支！！！**

### Target

熟悉Flask框架

- 安装Flask，能用虚拟环境(virtualenv)更佳。
- 能展示普通HTML页面。
- 正确放置静态文件(static)，css、js、jpg、png等等，在html中能够正确调用。
- 能配置简单的URL路由，@app.route(xxx)
- 能从URL地址中捕获变量，并进行处理。e.g. `/home/VarToCapture`，能捕获VarToCapture处的内容。
- 能渲染HTML模板(template)，包括普通HTML，带变量HTML{{ varname }}，带block的HTML（即该HTML在一个基础HTML模板上填入内容）
- 了解常见的模板变量、函数等等。
- 知道MVC设计模式， Model(data), View(page), Controller(functions)

### Tasks
**以下所有最终效果，除非特殊说明，均为使用Flask，启动项目内置webserver后，访问`http://127.0.0.1:5000`（具体看配置，一般默认为这个地址）所看到的**

在同一个Flask 项目中：
1. 码农第一步，`Hello World`
    - **要求：**访问`/step1`能看到`Hello World`字样。

2. Hello World PLUS
    - 带样式的`Hello World`或其他内容（字体，字号，颜色等等），样式请使用CSS，并且放在单独的css文件中作为外联样式表。
    - 按钮，点击后页面弹出提示框，内容随意（提示：提示框在javascript中是`alert('text');`），js脚本同样请放在外部的js文件中。
    - 一张或以上的图片，内容正常，**禁止任何违反法律法规的图片或是任何部门内人物的表情包**。
    - **要求：**访问`/step2`能正常展示页面内容，js脚本工作正常。

3. Hello Dalao
    - 创建一个base html，内容为两个block（空，仅作为占位），block命名自定。
    - 创建内容html，在base html的基础上扩展，两个block的内容写在这个页面中。
    - 第一个block内容为：放入`Hello, [1]! You are [2].`其中，1和2处均为从URL中捕获的字符串。URL规则：`/step3/[2]/[1]`
    - 第二个block，通过后台传入一个数组变量，内容为部门QQ群的六个等级头衔加上一个`other`，逐一展示在页面上，如果上面的2内容和某一个头衔匹配，标记出该头衔（加粗，变色，前面加标记均可），否则标记出`other`。**只能通过flask模板，不能通过前端的方式！**
    - 内容html是在base html的基础上扩展的，也是最终渲染的html。
    - 如果中文有问题，可以换成英文。
    - **要求：**访问`/step3/dalao/gg`，能看到`Hello, gg! You are dalao.`，下面的头衔列表中的`dalao`有标记，以此类推。

### How To Submit
- Fork这个repo，将你的代码放置在`stage1/<你名字的拼音>`目录下
- 同时在该目录中放置一份requirements.txt，记录你安装的python库，生成方法(在命令行，非python)：`$ pip freeze >> requirememts.txt`，在linux中可能是`$ pip3 freeze >> requirememts.txt`。
- 在DEADLINE之前向主库发起Pull request，分支为**stage1**。除了你自己的目录，其他所有目录的文件都**不要修改**
- **切换到 stage1 分支！！！**
- **切换到 stage1 分支！！！**
- **切换到 stage1 分支！！！**

### Recommended Resources
- [Official documents - Ver 0.11](http://flask.pocoo.org/docs/0.11/). Better read original english version.
- [Docs in Chinese - Ver 0.10](http://www.pythondoc.com/flask/)
- Tutorials about making a blog from scratch.
    - [Flask Web 开发入门](https://www.gitbook.com/book/funhacks/head-first-flask/details)
    - [Flaskr - OfficialDemo](http://flask.pocoo.org/docs/0.11/tutorial/introduction/)