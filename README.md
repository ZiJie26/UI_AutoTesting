# [UI自动化框架](/)

## [概况](/)

自动化框架测试

本项目基于Python，使用Pytest作为测试框架，使用了主流的PO模式进行设计，结合Selenium进行Web UI自动化测试。框架结构清晰，易于扩展和维护。

## [项目结构](/)

### [目录结构概览](/)

以下是整个测试框架的目录结构概览：

```plaintext
project_root/
│
├─pytest.ini                       # pytest 配置文件
├─main_run.py                      # 统一执行所有测试套件的入口脚本
├─requirements.txt                 # 项目依赖文件
│
├─cases                            # 测试用例脚本目录
│  ├─data                          # 测试数据存储区
│  │   └─test_data.json            # 测试数据
│  │
│  └─testFeature                   # 功能模块的测试目录
│      ├─test_test1.py             # 测试用例脚本
│      └─test_test2.py
│
├─config                           # 测试配置文件存放区
│  ├─config.ini                    # 默认配置文件
│  ├─db_config.yaml                # 数据库配置文件
│  └─env                           # 环境配置文件
│      ├─show_config.ini           # 演示环境配置
│      └─test_config.ini           # 测试环境配置
│
├─logs                             # 测试日志存放区
│  └─log_20240815.log              # 测试运行日志
│
├─page                             # 页面对象存放区
│  ├─base_page.py                  # 基础页面类
│  └─feature                       # 功能模块页面对象目录
│
├─report                           # 测试报告生成区
│  ├─allure-results                # Allure 报告结果
│  └─latest                        # 最新的测试报告
│
├─suites                           # 测试套件脚本目录
│  ├─conftest.py                   # 日志生成配置脚本
│  └─test_suit.py                  # 测试套件脚本
│
└─tools                            # 工具存放区
   ├─webdriver_setup.py            # WebDriver 设置脚本
   └─utils                         # 通用工具目录
```

## [项目部署](/)

本项目基于Python 3.8.19,使用到的包有：

### [快速部署](/)

1. 克隆项目到本地
2. 安装项目依赖：`pip install -r requirements.txt`
3. 运行tests/main_run.py文件，执行所有测试用例

### [详细部署](/)

请查看下列文档，其中包含详细的部署步骤和说明。
[搭建文档1](./搭建文档/1_PC%20Web端%20UI自动化搭建（1）环境准备.md)

## [编码规范](/)

* 统一使用python 3.8
* 编码使用-\*- coding:utf8 -\*-,且不指定解释器
* 类/方法的注释均写在class/def下一行，并且用三个双引号形式注释
* 局部代码注释使用#号
* 所有中文都直接使用字符串，不转换成Unicode，即不是用【u'中文'】编写
* 所有的测试模块文件都以test_projectName_moduleName.py命名
* 所有的测试类都以Test开头，类中方法(用例)都以test_开头
* 每个测试项目都在cases目录里创建一个目录，且目录都包含有api、scenrarios两个目录
* case对应setup/teardown的fixture统一命名成fixture_[test_case_method_name]
* 每一个模块中测试用例如果有顺序要求【主要针对ui自动化测试】，则自上而下排序，pytest在单个模块里会自上而下按顺序执行
