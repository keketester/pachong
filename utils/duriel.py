import json

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Connection': 'close'}
false = False
true = True

def js(r):
    """
    转换json格式
    :param r: 需要转换的数据
    :return: json格式
    """
    s = json.dumps(r, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
    return s


def list_trans_dict(s):
    """
    将列表参数转换成字典
    :param s: 列表参数
    :return: 返回字典
    """
    data = {}
    for i in range(int(len(s)/2)):
        data[s[::2][i]] = s[1::2][i]
    return data


def analysis_json(indict, pre=None):
    """
    递归查询json数据key、value
    :param indict:
    :param pre:
    :return:
    """
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre+[key, '{}']
                else:
                    for d in analysis_json(value, pre):
                        yield d
            elif isinstance(value, list):
                if len(value) == 0:
                    yield pre + [key, '[]']
                else:
                    for v in value:
                        for d in analysis_json(v, pre):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre+[key, '()']
                else:
                    for v in value:
                        for d in analysis_json(v, pre):
                            yield d
            else:
                yield pre + [key, value]
    else:
        yield indict


def get_analysis_json(indict):
    """
    将analysis_json返回值整理成一个列表数据
    :param indict:
    :return:
    """
    data = analysis_json(indict)
    lis = []
    for i, j in enumerate(data):
        lis += [j[0], j[1]]
    return lis
