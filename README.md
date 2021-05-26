<h1 align="center">
  疫情防控签到(云函数版)
  <br>
  Author: chiupam
</h1>

# 简介

适用于 `昆医大` 的易班疫情防控签到脚本, 不需要再每天盯着去签到.

# 目录

- [简介](#简介)
- [目录](#目录)
- [功能](#功能)
- [使用方式](#使用方式)
  - [腾讯云函数（推荐）](#腾讯云函数推荐)
    - [1. Fork本项目](#1Fork本项目)
    - [2. 准备需要的参数](#2准备需要的参数)
    - [3. 将参数填到Secrets](#3将参数填到secrets)
    - [4. 部署](#4部署)
- [通知推送方式](#通知推送方式)
- [同步上游代码](#同步上游代码)
  - [申请 Github Personal access tokens](#申请 Github Personal access tokens)
  - [将参数填到 Secrets](#将参数填到 Secrets)
- [申明](#申明)
- [参考项目](#参考项目)

# 功能

- [x] 每天7点半、15点半自动签到
- [x] 签到失败推送消息

# 使用方式

## 腾讯云函数（推荐）

### 1. Fork本项目

项目地址：[chiupam/Epidemic](https://github.com/chiupam/Epidemic)

### 2. 准备需要的参数

- 为了确保权限足够, 获取这两个参数时不要使用子账户! 此外, 腾讯云账户需要 [实名认证](https://console.cloud.tencent.com/developer/auth) !
- 开通云函数 `SCF` 的腾讯云账号，在 [访问秘钥页面](https://console.cloud.tencent.com/cam/capi) 获取账号的 `SecretID`，`SecretKey`
- 依次登录 [SCF 云函数控制台](https://console.cloud.tencent.com/scf) 和 [SLS 控制台](https://console.cloud.tencent.com/sls) 开通相关服务，确保您已开通服务并创建相应 [服务角色](https://console.cloud.tencent.com/cam/role) **SCF_QcsRole、SLS_QcsRole**

### 3. 将参数填到 Secrets

`Name`和`Value`格式如下：
  
| Name | Value |
|:---:|:---:|
|TENCENT_SECRET_ID | 腾讯云用户 SecretID|
|TENCENT_SECRET_KEY | 腾讯云账户 SecretKey|
|USERS_COVER | config.json 中内容|

### 4. 部署

- 首次 `fork` 可能要去 `Actions` 里面同意使用 `Actions` 条款.
- 添加完上面 `3` 个 `Secrets` 后, 进入 `Actions` --> `Serverless`, 点击右边的 `Run workflow` 即可部署至腾讯云函数

# 通知推送方式

## 1. PushPlus

只需要一个`token`, 参考 [获取 PushPlus 的 token](http://www.pushplus.plus/login?redirectUrl=/message)

# 同步上游代码

## 申请 Github Personal access tokens

- 点击左侧这个链接, [生成新的token](https://github.com/settings/tokens/new)
- 为 `token` 设置名字, 把 `workflow` 勾选上，点击最下方 `Generate token` 即可生成 `token`.
  
## 将参数填到 Secrets

`Name` 和` Value` 格式如下：

| Name | Value |
|:---:|:---:|
| PAT | 刚刚申请的 `token` 的值 |

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

