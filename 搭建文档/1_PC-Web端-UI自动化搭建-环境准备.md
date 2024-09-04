
# PC Web端 UI自动化搭建（1）本地环境准备

- [PC Web端 UI自动化搭建（1）本地环境准备](#pc-web端-ui自动化搭建1本地环境准备)
  - [脚本编写环境准备](#脚本编写环境准备)
    - [Anaconda](#anaconda)
    - [Pycharm](#pycharm)
  - [其余工具](#其余工具)
    - [Chrome for Testing \& ChromeDriver](#chrome-for-testing--chromedriver)
    - [Selenium IDE](#selenium-ide)
    - [allure](#allure)
    - [Jenkins](#jenkins)
      - [Jenkins Allure插件](#jenkins-allure插件)

## 脚本编写环境准备

### Anaconda

> python 环境管理软件

[下载地址](https://www.anaconda.com/download/success)

![2](https://i-blog.csdnimg.cn/direct/5568383bedc448a1b3c14b450d543b31.png)

**把自己的安装路径记下来！下面要用。**

![1](https://i-blog.csdnimg.cn/direct/ebc0bc7229f942ee969c83097bf88f18.png)

这里懒得设环境变量建议全选

![1](https://i-blog.csdnimg.cn/direct/19fc94207a3744acb6cba5d98fb2da66.png)

安装完之后不用打开，可以在cmd检查一下是否添加到环境变量

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/453f5eee6b3e4306b7783fb9b25ab77a.png)

### Pycharm

> python 脚本编写调试工具

[点击这里](https://www.jetbrains.com/pycharm/download/?section=windows)下载
Pycharm社区版

![社区版](https://i-blog.csdnimg.cn/direct/b78612139adc4ecebcd6846ba0f04c85.png)

安装过程不再赘述

按照下图点击

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ee2b0a693d904efc96b0e45c25f95957.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/3206214a96b84a7094f767033a702261.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/6242a257e46c4f7982e24b8f67ef08aa.png)

我们创建一个新的环境

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/aeb6476fe3fa43a2aaa51a081e87e523.png)

点击确定

## 其余工具

### Chrome for Testing & ChromeDriver

> 谷歌推出的专用于测试的浏览器和驱动

[下载地址](https://googlechromelabs.github.io/chrome-for-testing/#stable)
把这两个链接粘贴到地址栏下载得到两个压缩包

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c3d5e90c206148f1bbb644c989381f37.png)

把chrome解压到任意地址（但是最好是C盘下面，因为这个项目配置的是C盘下面的地址）：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e27a329144944b89bfd283449ad6ecf0.png)

**！记住这个地址！**

然后把chromedriver压缩包里的这三个文件解压到这个文件夹

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/aaedb20e56e44fb7bc20d6b4293712b1.png)

### Selenium IDE

>用于录制操作，快速生成脚本，减少工作量

双击这个打开测试浏览器,下面的操作都在测试浏览器里进行

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/fced8391e1b04e13bbe8832bf5802888.png)

有梯子去这里<https://chromewebstore.google.com/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd?hl=zh-CN>安装

没梯子去这里<https://www.chajianxw.com/developer/30773.html>安装

安装完之后可以把它固定显示

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b5fe196bc27c4d429e80ab9c2c9f2715.png)

点击上图3号箭头打开下图页面，点第三个选项新建一个Project

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/608c9bcc1ca04b7cbe3ce04e735d8c53.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a980584d96ae4829925d7b1c7f2c524f.png)

点击录制之后会弹出被测网站的新窗口，在那个窗口进行你的测试操作（**建议不要有多余操作**）

下图就是在百度首页输入“hi”然后回车后录制下来的内容：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ecdba1e1479541cd8a78a1c578a17dcf.png)
**注意！有些情况下这个插件并不能成功复现你的操作，是插件的问题，这时候就需要导出成脚本在本地运行了**

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e46a90e1db0143fc812bbe73f980647e.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/887db633edd74bf485cf83d50f2ae4b4.png)

点击export导出py脚本

### allure

>本地部署的allure，用于本地查看生成的allure报告
>>allure可以生成比较明了的执行报告，后面部署到Jenkins上时会用到allure插件，这个可以使本地调试的时候查看allure报告

这里（<https://github.com/allure-framework/allure2/releases/tag/2.30.0>）下载：

![20240828165932](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828165932.png)

解压放到你能记住的路径

![20240828173432](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828173432.png)

双击打开`allure.bat`

![20240828173538](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828173538.png)

然后去系统变量添加这个bin文件夹：

![20240828173728](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828173728.png)

确定完可以去cmd确认一下是否添加成功：

![20240828175224](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828175224.png)

### Jenkins

>CI/CD持续集成发布工具

到这里（<https://www.jenkins.io/download/>）下载

![20240828180558](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828180558.png)

下载完之后安装，这个地方选第一个：

![20240828182658](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828182658.png)

这里要选择你的Java目录，要JDK11、17或者21（所以要先安装JDK再安装Jenkins）：

![20240828184044](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828184044.png)

然后一路next就行

安装完会自动启动，也可以在计算机管理的服务这里启动与关闭：

![20240828184729](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240828184729.png)

安装完后打开：<localhost:8080> 然后按照页面中给出的地址找到文件，复制里面的密码。

![20240904085832](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240904085832.png)

![20240904085925](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240904085925.png)

粘贴过去，点击继续。

![20240904090119](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240904090119.png)

点击左边这个：**安装推荐的插件**

然后这个填自己记得住的就行：

![20240904091410](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240904091410.png)

后面的**实例配置**点击保存并完成就行。

然后点击开始使用进入主界面。

#### Jenkins Allure插件

按照下图依次点击：

![20240904091810](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240904091810.png)

![20240904091945](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240904091945.png)

![20240904092032](https://raw.githubusercontent.com/ZiJie26/picgo-win/main/1_PC-Web端-UI自动化搭建-环境准备/20240904092032.png)
