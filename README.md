<h1 align="center">
  昆明医科大学易班疫情防控签到
  <br>
  Author: chiupam
</h1>

# 简介
适用于 `昆医大` 的易班疫情防控签到脚本, 请勿使用此仓库资源进行牟利.
# 目录
- [简介](#简介)
- [目录](#目录)
- [功能](#功能)
- [配置文件](#配置文件)
- [使用方式](#使用方式)
  - [腾讯云函数（推荐）](#腾讯云函数推荐)
    - [1.Fork本项目](#1fork本项目)
    - [2.准备腾讯云函数serverless的必备参数](#2准备腾讯云函数serverless的必备参数)
    - [3.将参数填到Secrets](#3将参数填到Secrets)
    - [4.同意Actions条款](#4同意Actions条款)
    - [5.部署到腾讯云函数serverless](#5部署到腾讯云函数serverless)
- [申明](#申明)
# 功能
- [x] 每天7点半、15点半自动签到
- [x] 签到失败推送消息
# 配置文件
[config.json](https://github.com/chiupam/Epidemic/blob/master/config.json) 的格式要求：

|键|值|必须|备注、举例|
|:---:|:---:|:---:|:---:|
|_name|您的姓名|否|法外狂徒张三|
|_username|您登陆的用户名,默认为您的学号|是|2018101001|
|_password|您登陆的密码,默认为您身份证后6位|是|291001|
|_notify|脚本运行结果是否需要通知|是|`true`为推送, `false`为不推送|
|_token|pushplus的token,[申请地址](http://www.pushplus.plus/push1.html)|否|当`_notify`是`true`时需要填写|
# 使用方式
## 腾讯云函数serverless（推荐）
### 1.Fork本项目
- 点击 [chiupam/Epidemic](https://github.com/chiupam/Epidemic)
- 然后点击右上角的 `Fork` 按钮即可.
### 2.准备腾讯云函数serverless的必备参数
- 腾讯云账户需要 [实名认证](https://console.cloud.tencent.com/developer/auth)
- 为了确保权限足够, 获取以下这两个参数时**不要使用子账户**
- 开通云函数 `SCF` 的腾讯云账号，在 [访问秘钥页面](https://console.cloud.tencent.com/cam/capi) 获取账号的 `SecretID`，`SecretKey`
- 依次登录 [SCF 云函数控制台](https://console.cloud.tencent.com/scf) 和 [SLS 控制台](https://console.cloud.tencent.com/sls) 开通相关服务，确保您已开通服务并创建相应 [服务角色](https://console.cloud.tencent.com/cam/role) **SCF_QcsRole、SLS_QcsRole**
### 3.将参数填到Secrets
- 打开您自己的Epidemic仓库
- 点击上方的 `Settings` , 依次点击 `Secrets` 、 `New secret`
- 依次添加以下内容
- `Name`和`Value`的内容各如下：
  
| Name | Value | 必须 |
|:---:|:---:|:---:|
|TENCENT_SECRET_ID | 腾讯云用户 SecretID | 是 |
|TENCENT_SECRET_KEY | 腾讯云账户 SecretKey | 是 |
|USERS_COVER | config.json 中内容| 是 |
### 4.同意Actions条款
- `fork` 完后点击您仓库上方的 `Actions` 里面
- 点击同意使用 `Actions` 条款.
### 5.部署到腾讯云函数serverless
- 添加完上面 `3` 个 `Secrets` 
- 依次点击仓库上方的 `Actions` 、 `Serverless`
- 点击右边的 `Run workflow` 即可部署至腾讯云函数.
# 申明
1. 如果您的体温不正常, 记得正确佩戴口罩, 及时就诊并报告辅导员.
2. 此脚本仅用于学习研究, 不保证其合法性, 准确性, 有效性, 请根据情况自行判断, 本人对此不承担任何保证责任.
3. 您必须在下载后 **24** 小时内将所有内容从您的计算机或手机或任何存储设备中完全删除, 若违反规定引起任何事件本人对此均不负责.
4. 请勿将此脚本用于任何商业或非法目的, 若违反规定请自行对此负责.
5. 此脚本涉及应用与本人无关, 本人对因此引起的任何隐私泄漏或其他后果不承担任何责任.
6. 本人对任何脚本引发的问题概不负责, 包括但不限于由脚本错误引起的任何损失和损害.
7. 如果任何单位或个人认为此脚本可能涉嫌侵犯其权利, 应及时通知并提供身份证明，所有权证明, 我将在收到认证文件确认后删除此脚本.
8. 所有直接或间接使用, 查看此脚本的人均应该仔细阅读此声明.
9. 本人保留随时更改或补充此声明的权利, 一旦您使用或复制了此脚本, 即视为您已接受此免责声明.