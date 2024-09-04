# [UI自动化框架](/)

## [概况](/)

自动化框架测试

本项目基于Python，使用Pytest作为测试框架，使用了主流的PO模式进行设计，结合Selenium进行Web UI自动化测试。框架结构清晰，易于扩展和维护。

**如果能帮到你的话，可以点一下右上角的 'star' ，谢谢！**

## [项目结构](/)

### [目录结构概览](/)

以下是整个测试框架的目录结构概览：

```cmd
.
│  conftest.py          # pytest的全局配置文件，可以在此定义测试的前置/后置操作、hook函数等
│  main_run.py          # 主入口文件，用于启动整个测试项目的执行
│  pytest.ini           # pytest配置文件，用于配置pytest的运行参数，如测试路径、插件配置等
│  README.md            # 项目说明文档，介绍项目的背景、使用方法及结构说明
│  requirements.txt     # 项目所需的依赖库列表，用于通过pip安装依赖
│
├─cases
│  │  __init__.py       # 表示该目录为Python包，可用于初始化相关配置或依赖
│  │
│  ├─data
│  │      test_data.json # 测试数据文件，存储各个测试用例所需的数据，通常以JSON格式保存
│  │
│  └─testFeature
│          test_test1.py # 第一个测试用例文件，使用pytest框架，定义UI自动化测试的具体场景
│          test_test2.py # 第二个测试用例文件，包含另一组自动化测试场景
│          __init__.py   # 初始化文件，标记此目录为Python包，便于模块导入
│
├─config
│      cookies.json      # 登录或其他需要的cookies配置文件，保存登录后使用的cookie信息
│      db_config.json    # 数据库配置文件，存储数据库连接信息和参数
│      dev_paths.json    # 开发环境路径配置文件，包含项目在开发环境下的URL或路径信息
│      test_paths.json   # 测试环境路径配置文件，包含项目在测试环境下的URL或路径信息
│
├─page
│      base_page.py      # 页面基础类，封装常用的页面操作，如点击、输入文本等，是其他页面类的父类
│      __init__.py       # 标记page目录为Python包，便于模块导入
│
├─suites
│      suit1.py          # 测试套件1，组合多个测试用例，作为一组执行
│      suit2.py          # 测试套件2，定义另一组测试用例的组合
│      __init__.py       # 标记此目录为Python包，便于模块导入
│
├─tools
│      cleanup_utils.py  # 工具文件，包含清理测试环境或其他清理任务的工具函数
│      database_utils.py # 数据库工具文件，提供操作数据库的函数，如增删查改等操作
│      sl_cookies.py     # 与cookie相关的工具函数，用于cookie的读取、写入或删除操作
│      webdriver_setup.py# WebDriver配置工具文件，用于配置和启动WebDriver
│      __init__.py       # 标记tools目录为Python包，便于模块导入
```

### 项目结构说明

- **根目录文件**
  - `conftest.py`：这是pytest的全局配置文件，用于定义测试的前置/后置操作、fixture等通用的配置信息。
  - `main_run.py`：项目的主运行文件，用来配置测试的启动逻辑，可以控制执行哪些测试套件或具体的用例。
  - `pytest.ini`：用于pytest的配置，可以在这里设置一些pytest运行时的参数，比如测试路径、插件设置等。
  - `README.md`：文档文件，用于说明项目的目的、安装步骤、如何运行等信息。
  - `requirements.txt`：Python项目的依赖文件，列出了所有运行该项目所需的库和版本信息。

- **cases目录**
  - `cases/__init__.py`：标记`cases`目录为Python包，允许从外部导入包中的模块。
  - `cases/data/test_data.json`：存放测试用例所需的数据，方便测试用例动态使用不同的数据集。
  - `cases/testFeature/`：用于存放测试用例的具体文件，如`test_test1.py`和`test_test2.py`，这些文件中通常会使用pytest框架定义具体的测试场景。

- **config目录**
  - 用于存放项目运行环境相关的配置文件，如数据库连接信息（`db_config.json`）、测试环境路径（`test_paths.json`）等。不同的环境会有不同的配置文件。

- **page目录**
  - `base_page.py`：封装了常见的页面操作和元素查找方法，其他页面类会继承自这个基础类，用于简化代码复用。
  - `__init__.py`：标记`page`目录为Python包，便于模块之间的引用。

- **suites目录**
  - 存放测试套件文件，测试套件是多个测试用例的集合，便于按照不同的功能或模块进行批量测试执行。

- **tools目录**
  - 存放一些辅助工具文件，例如清理工具（`cleanup_utils.py`）、数据库操作工具（`database_utils.py`）、WebDriver配置工具（`webdriver_setup.py`）等。

## [项目部署](/)

本项目基于Python 3.8.19,主要使用了Selenium，Pytest，Allure等包

### [快速部署](/)

1. 克隆项目到本地
2. 安装项目依赖：`pip install -r requirements.txt`
3. 在case目录下添加用例脚本，在suites下添加测试套件，在main_run.py添加要执行的套件
4. 运行tests/main_run.py文件，执行所有测试用例

### [详细使用方法](/)

**请查看下列文档，其中包含详细的部署步骤和使用说明。**
[搭建文档1](./搭建文档/1_PC-Web端-UI自动化搭建-环境准备.md)
[搭建文档2](./搭建文档/2_PC-Web端-UI自动化搭建-使用方法.md)

## [编码规范](/)

- 统一使用python 3.8
- 编码使用`coding:utf8`,且不指定解释器
- 类/方法的注释均写在class/def下一行，并且用三个双引号形式注释
- 局部代码注释使用#号
- 所有中文都直接使用字符串，不转换成Unicode，即不是用【u'中文'】编写
- 所有的测试模块文件都以test_projectName_moduleName.py命名
- 所有的测试类都以Test开头，类中方法(用例)都以test_开头
- 每个测试项目都在cases目录里创建一个目录
- 每一个模块中测试用例如果有顺序要求【主要针对ui自动化测试】，则自上而下排序，pytest在单个模块里会自上而下按顺序执行
