import json

from pyaniparser import AniParser

ani_parser = AniParser()
try :
    # 单个
    ptr = ani_parser.parse("【悠哈璃羽字幕社】[p][CHT] [复制磁连]")
    print("single:", ptr)

    # 批量
    json_path = r"C:\Code\.Net\Banned.AniParser\Banned.AniParser.Test\bin\Debug\net10.0\Data\data.json"
    with open(json_path, "r", encoding = "utf-8") as f :
        data = json.load(f)
    for file in data :
        ptr = ani_parser.parse(file)
        print("single:", ptr)
finally :
    pass
