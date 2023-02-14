from typing import Dict, Union, Optional, Set, Tuple

from pydantic import BaseModel, Field, root_validator

_wns_data: Optional[Dict[str, str]] = None


class Config(BaseModel):
    wns_raw: Dict[str, Union[str, Tuple[Set[str], str]]] = Field(default={
        "百度": [{"baidu"}, "https://www.baidu.com/s?wd={}"],
        "谷歌": [{"google"}, "https://www.google.com/search?q={}"],
        "必应": [{"bing"}, "https://cn.bing.com/search?q={}"],
        "必应国际": [{"bing国际", "国际必应"}, "https://cn.bing.com/search?q={}&ensearch=1"],
        "搜狗": [{"sougou"}, "https://www.sogou.com/web?query={}"],
        "B站": [{"bilibili"}, "https://search.bilibili.com/all?keyword={}"],
        "python":[{"python3","py文档"},"https://docs.python.org/zh-cn/3.11/search.html?q={}"],
        # 不包含问题
        "nonebot": [{"nb", "nonebot2", "nb2"}, "https://v2.nonebot.dev/docs"]
    })

    wns_search: Dict[str, Union[str, Tuple[Set[str], str]]] = {}

    wns_priority: int = 99
    wns_block: bool = False

    @property
    def wns_data(self) -> Dict[str, str]:
        global _wns_data
        if _wns_data is not None:
            return _wns_data
        _wns_data = {}
        for i in self.wns_raw:
            _wns_data[i] = self.wns_raw[i][1]
            for j in self.wns_raw[i][0]:
                _wns_data[j] = self.wns_raw[i][1]
        for i in self.wns_search:
            _wns_data[i] = self.wns_search[i][1]
            for j in self.wns_search[i][0]:
                _wns_data[j] = self.wns_search[i][1]
        return _wns_data

    def get_commands(self) -> Set[str]:
        return set(self.wns_data.keys())

    def get_url(self, key) -> Optional[str]:
        return self.wns_data.get(key, None)

    @root_validator(pre=True, allow_reuse=True)
    def _parse_data(cls, values: dict):
        def _parse(data: Optional[dict]):
            if data is None:
                return
            for i in data:
                if isinstance(data[i], str):
                    data[i] = [{i}, data[i]]

        _parse(values.get("wns_raw"))
        _parse(values.get("wns_search"))

        return values
