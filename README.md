# 说明
之前我用的node-red写的js来实现查询当日是否为休息日，同时也使用了一些第三方的接口，由于配置不方便，而且第三方的接口由于种种原因老是挂，索性就自己写一个集成来替代，先说好，这只是用来判断当日是否为休息日的插件，并不是日历，没有万年历！！！

集成已经默认配置2025年节假日日期，没有特殊需求默认添加集成即可

考虑到有时候并不会按照法定节假日休息，本集成可以自定义法定节假日，工作日，休息日（格式必须按照默认要求）。目前集成默认只有2025年法定节假日配置，2026年需根据实际休假时间修改配置。
![png](https://attachment.hasstatic.com/forum/202501/17/140543e7vz9jr47o6ua79a.png)

![png2](https://attachment.hasstatic.com/forum/202501/17/141746l8kgfky4gi3ygkq1.png)
- 插件名称：节假日助手
- 关于安装：直接下载整个项目的zip包，把下载的包解压后放到homeassistant 的 /config/custom_components/ 目录下 ，重启homeassistant , 再到集成搜索插件名称 
- 项目地址：https://github.com/XG520/HolAsst
- 作用：用于判断当日是否为工作日而实现相应的自动化