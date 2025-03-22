# 说明
之前我用的node-red写的js来实现查询当日是否为休息日，同时也使用了一些第三方的接口，由于配置不方便，而且第三方的接口由于种种原因老是挂，索性就自己写一个集成来替代，先说好，这只是用来判断当日是否为休息日的插件，并不是日历，没有万年历！！！

集成已经默认配置2025年节假日日期，没有特殊需求默认添加集成即可

考虑到有时候并不会按照法定节假日休息，本集成可以自定义法定节假日，工作日，休息日（格式必须按照默认要求）。目前集成默认只有2025年法定节假日配置，2026年需根据实际休假时间修改配置。
![png](https://attachment.hasstatic.com/forum/202501/17/140543e7vz9jr47o6ua79a.png)

![png2](https://attachment.hasstatic.com/forum/202501/17/141746l8kgfky4gi3ygkq1.png)
- 插件名称：节假日助手
## 安装指引

### 方式一：HACS一键安装（推荐）
1. 确保已经安装了 [HACS](https://hacs.xyz/)
2. 在HACS中点击"自定义存储库"
3. 添加此仓库地址：`https://github.com/XG520/HolAsst`
4. 类别选择"集成"
5. 点击"添加"
6. 在HACS的集成页面中搜索"KiwiOT"
7. 点击"下载"进行安装
8. 重启Home Assistant

### 方式二：手动安装
1. 下载此仓库的最新版本
2. 将 `custom_components/kiwiot_ws` 文件夹复制到你的Home Assistant配置目录下的 `custom_components` 文件夹中
3. 重启Home Assistant

- 项目地址：https://github.com/XG520/HolAsst
- 作用：用于判断当日是否为工作日而实现相应的自动化