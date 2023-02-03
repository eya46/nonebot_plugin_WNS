# why not search (这么简单为什么不搜索？)

## 默认响应

```python
{
    "百度": [{"baidu"}, "https://www.baidu.com/s?wd={}"],
    "谷歌": [{"google"}, "https://www.google.com/search?q={}"],
    "必应": [{"bing"}, "https://cn.bing.com/search?q={}"],
    "必应国际": [{"bing国际", "国际必应"}, "https://cn.bing.com/search?q={}&ensearch=1"],
    "搜狗": [{"sougou"}, "https://www.sogou.com/web?query={}"],
    "B站": [{"bilibili"}, "https://search.bilibili.com/all?keyword={}"],
    # 不包含问题
    "nonebot": [{"nb", "nonebot2", "nb2"}, "https://v2.nonebot.dev/docs"]
}
```

## 作用

返回 回复消息 的 搜索链接

## 用法

回复消息，并带上 [(默认响应)](#默认响应)

![](show.jpg)

[//]: # (## 安装)

[//]: # ()

[//]: # (pip install nonebot-plugin-WNS)

## 配置

> Dict[str, Union[
> str, Tuple[
> Set[str], str]
> ]
> ]

|      名称      |     默认值      |    描述    |
|:------------:|:------------:|:--------:|
|   wns_raw    | [默认值](#默认响应) |   默认响应   |
|  wns_search  |     None     | 配置的响应命令  |
|  wns_block   |    False     | 是否阻止向下传播 |
| wns_priority |      99      |   优先级    |

## [依赖](requirements.txt)

* nonebot2>=2.0.0-beta.1
* pydantic~=1.10.4