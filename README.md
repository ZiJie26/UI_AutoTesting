# [UI自动化框架](/)

## [概况](/)

UI自动化框架

## [项目结构](/)

### [目录结构概览](/)

以下是整个测试框架的目录结构概览：

```plaintext
project_root/
│
├── tests/                        # 主测试目录
│   ├── auth/                     # 认证模块的测试目录
│   │   ├── test_login.py         # 登录测试用例
│   │   ├── test_logout.py        # 登出测试用例
│   │   └── auth_suite.py         # 认证模块的测试套件脚本
│   │
│   ├── search/                   # 搜索模块的测试目录
│   │   ├── test_search.py        # 搜索功能测试用例
│   │   └── search_suite.py       # 搜索模块的测试套件脚本
│   │
│   ├──conftest.py                  # 日志工具脚本
│   └── main_run.py               # 统一执行所有测试套件的入口脚本
│   │
├── data/                    # 测试数据存储区
│   ├── auth/                     # 认证模块测试数据
│   │   ├── login_data.json       # 登录数据
│   │   └── logout_data.yaml      # 登出数据
│   │
│   ├── search/                   # 搜索模块测试数据
│   │   └── search_data.json      # 搜索数据
│
├── report/                  # 测试报告生成区
│   ├── allure-results/           # Allure 报告结果
│   └── latest/                   # 最新的测试报告
│       └── report.html           # 最新的测试报告
│
├── tools/                        # 工具存放区
│   ├── webdriver/                # WebDriver 相关工具
│   │   └── webdriver_setup.py    # WebDriver 设置脚本
│   │
│   └── utils/                    # 通用工具
│
├── config/                  # 测试配置文件存放区
│   ├── config.ini                # 默认配置文件
│   │
│   └── env/                      # 环境配置文件
│       ├── dev_config.ini        # 开发环境配置
│       └── prod_config.ini       # 生产环境配置
│
├── logs/                     # 测试日志存放区
│
├── pages/                        # 页面对象存放区
│   ├── base_page.py              # 基础页面类
│   │
│   └── auth/                     # 认证模块页面对象
│       └── login_page.py         # 登录页面对象
│
├── requirements.txt              # 项目依赖文件
└── pytest.ini                    # pytest配置文件
```

## [项目部署](/)

### [快速部署](/)

1. 克隆项目到本地
2. 安装项目依赖：`pip install -r requirements.txt`
3. 运行tests/main_run.py文件，执行所有测试用例

### [详细部署](/)

请查看下列文档，其中包含详细的部署步骤和说明。
[搭建文档1](/搭建文档/1_PC%20Web端%20UI自动化搭建（1）环境准备.md)

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
