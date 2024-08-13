
# PC Web端 UI自动化搭建（1）本地环境准备

- [PC Web端 UI自动化搭建（1）本地环境准备](#pc-web端-ui自动化搭建1本地环境准备)
  - [脚本编写环境准备](#脚本编写环境准备)
    - [Anaconda](#anaconda)
    - [Pycharm](#pycharm)
    - [Chrome for Testing \& ChromeDriver](#chrome-for-testing--chromedriver)
    - [Selenium IDE](#selenium-ide)
  - [脚本运行](#脚本运行)

## 脚本编写环境准备

### Anaconda

[下载地址](https://www.anaconda.com/download/success)

![2](https://i-blog.csdnimg.cn/direct/5568383bedc448a1b3c14b450d543b31.png)

**！把自己的安装路径记下来！**

![1](https://i-blog.csdnimg.cn/direct/ebc0bc7229f942ee969c83097bf88f18.png)

这里懒得设环境变量建议全选

![1](https://i-blog.csdnimg.cn/direct/19fc94207a3744acb6cba5d98fb2da66.png)

安装完之后不用打开，可以在cmd检查一下是否添加到环境变量

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/453f5eee6b3e4306b7783fb9b25ab77a.png)

### Pycharm

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

然后我们新建一个项目安装相关包顺便测试一下

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d2968bcdbb3a421195ec08e2582ec927.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/2e2e6302926542aeb678489cc3328146.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/5639a62f65fa4255808243ea422cbaee.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/141e01dcd53d4137bea00de146ca2987.png)

创建好文件之后先看这里确认一下是不是正确的环境

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a51ee79c55434c5d88a188245869ae91.png)

打开终端![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c98335d14f5d483e837f006b377aad53.png)

在这里打开终端就很省事，会自动进入对应环境，不用在cmd输命令进入环境也不用在anaconda等他那又臭又长的加载

输入

```bash
pip install pytest
```

```bash
pip install selenium
```

这两个安装完后可以`pip list`查看

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a8dec2f45eee41c1b46c5953f64eeec3.png)

### Chrome for Testing & ChromeDriver

[下载地址](https://googlechromelabs.github.io/chrome-for-testing/#stable)
把这两个链接粘贴到地址栏下载得到两个压缩包

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c3d5e90c206148f1bbb644c989381f37.png)

把chrome解压到任意地址，比如我的就是：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e27a329144944b89bfd283449ad6ecf0.png)

**！记住这个地址！**

然后把chromedriver压缩包里的这三个文件解压到这个文件夹

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/aaedb20e56e44fb7bc20d6b4293712b1.png)

### Selenium IDE

双击这个打开测试浏览器

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/fced8391e1b04e13bbe8832bf5802888.png)

有梯子去[这里](https://chromewebstore.google.com/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd?hl=zh-CN)安装

没梯子去[这里](https://www.chajianxw.com/developer/30773.html)安装

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

## 脚本运行

导出的文件复制到刚刚创建的项目里（或者代码复制到之前创建的test.py也可以）

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e15e40ae5781489e80a59c6d158ed91f.png)

由于我们的浏览器是放在自定义目录下的，所以在启动项这里要做一些配置，简而言之，把红色方形里的代码

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c070223a64c242ae9f2475e6adbb6ad0.png)

替换成

```python
    def setup_method(self, method):
        # Chrome测试版的路径
        chrome_testing_path = r"D:\Develop\DevelopTools\chrome-win64\chrome.exe"#改成你自己的路径！
        # Chromedriver的路径
        chromedriver_path = r"D:\Develop\DevelopTools\chrome-win64\chromedriver.exe"#改成你自己的路径！
        # 设置Chrome选项
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_testing_path
        options.add_experimental_option("detach", True)
        # 设置WebDriver服务
        service = Service(chromedriver_path)
        # 创建Chrome WebDriver实例
        self.driver = webdriver.Chrome(service=service, options=options)
        self.vars = {}
```

**注意把chrome和chromedriver的路径改成自己的！**

最后在终端里输入 `pytest`+脚本文件名 执行脚本

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/15f1e2fdaefa4fa98b05c70eaea5430d.png)

执行成功，代表环境准备完毕

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/dd4ef6976b8f45dd9f49db8498748888.png)
