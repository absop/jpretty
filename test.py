import cProfile
import json

from jpretty import dumps
from jpretty import gdumps


obj = {
    "test1": {
        "name": "gridea-theme-lemon",
        "version": "1.0.0",
        "description": "",
        "main": "index.js",
        "scripts": {
            "dev": "./node_modules/.bin/gulp",
            "serve": "nodemon --watch templates --watch assets -e js,ejs,less,css app.js",
            "test": "echo \"Error: no test specified\" && exit 1"
        },
        "author": "",
        "license": "ISC",
        "dependencies": {
            "ejs": "^2.6.1",
            "express": "^4.16.4"
        },
        "devDependencies": {
            "axios": "^0.18.0",
            "browser-sync": "^2.26.3",
            "gulp": "^4.0.0",
            "gulp-less": "^4.0.1",
            "gulp-nodemon": "^2.4.2",
            "nodemon": "^1.18.11"
        },
        "nodemonConfig": {
            "ignore": ["test/*", "docs/*"],
            "delay": "2500"
        }
    },
    "test2": {
        "name": "Lemon",
        "version": "1.0.0",
        "author": "虾哔哔",
        "repository": "https://github.com/Mrcxt/gridea-theme-lemon",
        "customConfig": [
            {
                "name": "github",
                "label": "Github",
                "group": "社交",
                "value": "",
                "type": "input",
                "note": "链接地址"
            },
            {
                "name": "twitter",
                "label": "Twitter",
                "group": "社交",
                "value": "",
                "type": "input",
                "note": "链接地址"
            },
            {
                "name": "weibo",
                "label": "微博",
                "group": "社交",
                "value": "",
                "type": "input",
                "note": "链接地址"
            },
            {
                "name": "facebook",
                "label": "Facebook",
                "group": "社交",
                "value": "",
                "type": "input",
                "note": "链接地址"
            },
            {
                "name": "ga",
                "label": "跟踪 ID",
                "group": "谷歌统计",
                "value": "",
                "type": "input",
                "note": "UA-xxxxxxxxx-x"
            },
            {
                "name": "notice",
                "label": "公告栏",
                "group": "侧边栏",
                "value": "",
                "type": "textarea",
                "note": "不填写则不显示"
            }
        ]
    },
    "test3": {
        "matrix": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        "enable": True,
        "free": False,
        "method": None,
        "x": 1.0,
        "y": 1.2345,
        "z": -1.3
    }
}

def p(code):
    print('=' * 80)
    print(code)
    print('=' * 80)
    cProfile.run(code)


if __name__ == '__main__':
    o = {}
    for i in range(10000):
        o[str(i)] = [obj['test1'], obj['test2'], obj['test3']]

    p('data1 = dumps(o, indent=4, sort_keys=True)')
    p('data2 = gdumps(o, indent=4, sort_keys=True)')
    p('data3 = json.dumps(o, indent=4, sort_keys=True, ensure_ascii=False)')

    assert json.loads(data1) == o
    assert json.loads(data2) == o
    assert json.loads(data3) == o

    print('=' * 80)
    print(f'Lengths: {len(data1)}, {len(data2)}, {len(data3)}')
    print(dumps(obj, indent=4, sort_keys=True))


"""
================================================================================
data1 = dumps(o, indent=4, sort_keys=True)
================================================================================
         8650020 function calls (6790020 primitive calls) in 2.094 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.094    2.094 <string>:1(<module>)
 200001/1    0.293    0.000    2.061    2.061 __init__.py:21(_iterate_list)
720000/10000    0.481    0.000    2.058    0.000 __init__.py:37(_iterate_pair)
        1    0.000    0.000    0.000    0.000 __init__.py:4(_make_pretty)
 950001/1    0.674    0.000    2.062    2.062 __init__.py:44(_iterate_obj)
   210000    0.031    0.000    0.044    0.000 __init__.py:63(<genexpr>)
        1    0.000    0.000    2.094    2.094 __init__.py:84(dumps)
  1320000    0.156    0.000    0.156    0.000 {built-in method _json.encode_basestring}
    70000    0.024    0.000    0.066    0.000 {built-in method builtins.all}
        1    0.000    0.000    2.094    2.094 {built-in method builtins.exec}
  2690006    0.168    0.000    0.168    0.000 {built-in method builtins.isinstance}
   200001    0.014    0.000    0.014    0.000 {built-in method builtins.len}
   130001    0.061    0.000    0.061    0.000 {built-in method builtins.sorted}
  2030003    0.150    0.000    0.150    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   130001    0.009    0.000    0.009    0.000 {method 'items' of 'dict' objects}
        1    0.032    0.032    0.032    0.032 {method 'join' of 'str' objects}


================================================================================
data2 = gdumps(o, indent=4, sort_keys=True)
================================================================================
         29210021 function calls (10850021 primitive calls) in 5.699 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.045    0.045    5.699    5.699 <string>:1(<module>)
8450002/2030002    1.707    0.000    4.941    0.000 __init__.py:110(_iterate_list)
5660000/2040000    1.201    0.000    4.618    0.000 __init__.py:126(_iterate_pair)
10350004/2030004    1.885    0.000    5.262    0.000 __init__.py:133(_iterate_obj)
   210000    0.032    0.000    0.045    0.000 __init__.py:152(<genexpr>)
        1    0.357    0.357    5.654    5.654 __init__.py:173(gdumps)
        1    0.000    0.000    0.000    0.000 __init__.py:93(_make_iter_pretty)
  1320000    0.156    0.000    0.156    0.000 {built-in method _json.encode_basestring}
    70000    0.024    0.000    0.066    0.000 {built-in method builtins.all}
        1    0.000    0.000    5.699    5.699 {built-in method builtins.exec}
  2690006    0.167    0.000    0.167    0.000 {built-in method builtins.isinstance}
   200001    0.015    0.000    0.015    0.000 {built-in method builtins.len}
   130001    0.064    0.000    0.064    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   130001    0.011    0.000    0.011    0.000 {method 'items' of 'dict' objects}
        1    0.036    0.036    0.036    0.036 {method 'join' of 'str' objects}


================================================================================
data3 = json.dumps(o, indent=4, sort_keys=True, ensure_ascii=False)
================================================================================
         23070028 function calls (15020028 primitive calls) in 5.686 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    5.686    5.686 <string>:1(<module>)
        1    0.046    0.046    5.686    5.686 __init__.py:183(dumps)
        1    0.000    0.000    0.000    0.000 encoder.py:104(__init__)
        1    0.510    0.510    5.640    5.640 encoder.py:182(encode)
        1    0.000    0.000    0.000    0.000 encoder.py:204(iterencode)
    30000    0.015    0.000    0.015    0.000 encoder.py:223(floatstr)
        1    0.000    0.000    0.000    0.000 encoder.py:259(_make_iterencode)
5690000/3540000    1.511    0.000    3.380    0.000 encoder.py:277(_iterencode_list)
9460004/3560004    2.226    0.000    4.178    0.000 encoder.py:333(_iterencode_dict)
  3560004    0.902    0.000    5.079    0.000 encoder.py:413(_iterencode)
  1320000    0.176    0.000    0.176    0.000 {built-in method _json.encode_basestring}
        1    0.000    0.000    5.686    5.686 {built-in method builtins.exec}
   200001    0.020    0.000    0.020    0.000 {built-in method builtins.id}
  2550008    0.152    0.000    0.152    0.000 {built-in method builtins.isinstance}
   130001    0.068    0.000    0.068    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   130001    0.010    0.000    0.010    0.000 {method 'items' of 'dict' objects}
        1    0.051    0.051    0.051    0.051 {method 'join' of 'str' objects}


================================================================================
Lengths: 30648892, 30648892, 33568892
{
    "test1": {
        "author": "",
        "dependencies": {
            "ejs": "^2.6.1",
            "express": "^4.16.4"
        },
        "description": "",
        "devDependencies": {
            "axios": "^0.18.0",
            "browser-sync": "^2.26.3",
            "gulp": "^4.0.0",
            "gulp-less": "^4.0.1",
            "gulp-nodemon": "^2.4.2",
            "nodemon": "^1.18.11"
        },
        "license": "ISC",
        "main": "index.js",
        "name": "gridea-theme-lemon",
        "nodemonConfig": {
            "delay": "2500",
            "ignore": ["test/*", "docs/*"]
        },
        "scripts": {
            "dev": "./node_modules/.bin/gulp",
            "serve": "nodemon --watch templates --watch assets -e js,ejs,less,css app.js",
            "test": "echo \"Error: no test specified\" && exit 1"
        },
        "version": "1.0.0"
    },
    "test2": {
        "author": "虾哔哔",
        "customConfig": [
            {
                "group": "社交",
                "label": "Github",
                "name": "github",
                "note": "链接地址",
                "type": "input",
                "value": ""
            },
            {
                "group": "社交",
                "label": "Twitter",
                "name": "twitter",
                "note": "链接地址",
                "type": "input",
                "value": ""
            },
            {
                "group": "社交",
                "label": "微博",
                "name": "weibo",
                "note": "链接地址",
                "type": "input",
                "value": ""
            },
            {
                "group": "社交",
                "label": "Facebook",
                "name": "facebook",
                "note": "链接地址",
                "type": "input",
                "value": ""
            },
            {
                "group": "谷歌统计",
                "label": "跟踪 ID",
                "name": "ga",
                "note": "UA-xxxxxxxxx-x",
                "type": "input",
                "value": ""
            },
            {
                "group": "侧边栏",
                "label": "公告栏",
                "name": "notice",
                "note": "不填写则不显示",
                "type": "textarea",
                "value": ""
            }
        ],
        "name": "Lemon",
        "repository": "https://github.com/Mrcxt/gridea-theme-lemon",
        "version": "1.0.0"
    },
    "test3": {
        "enable": true,
        "free": false,
        "matrix": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        "method": null,
        "x": 1.0,
        "y": 1.2345,
        "z": -1.3
    }
}
[Finished in 14.4s]
"""
