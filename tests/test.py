import json

from pyaniparser import AniParser

ani_parser = AniParser()
try :
    # 单个
    ptr = ani_parser.parse("【悠哈璃羽字幕社】[p][CHT] [复制磁连]")
    print("single:", ptr)

    # 批量
    json_path = r"D:\Source\.Net\Banned.AniParser\Banned.AniParser.Test\bin\Debug\net9.0\result\88d33433-9b81-4a17-8017-70f89239184a.json"
    with open(json_path, "r", encoding = "utf-8") as f :
        data = json.load(f)
    files = data["TitleList"]
    for file in files :
        ptr = ani_parser.parse(file)
        print("single:", ptr)
finally :
    pass
