import json
import logging
from dataclasses import asdict
from enum import IntEnum

from pyaniparser import AniParser

logger = logging.getLogger(__name__)
parser = AniParser()


def replace_enums(obj) :
    if isinstance(obj, IntEnum) :
        return obj.name  # 或返回 {"name": obj.name, "value": int(obj)}
    if isinstance(obj, dict) :
        return {k : replace_enums(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple, set)) :
        return [replace_enums(v) for v in obj]  # JSON 不支持 set，这里转成 list
    return obj


def test_single_parse() :
    r = parser.parse(
            "[樱桃花字幕组] 圣女因太过完美一点也不讨人喜欢而被废除婚约卖到邻国  Kanpekiseijo - 08[1080p][简日双语].mp4")
    assert r is None or r.title  # 至少能跑通


def test_batch_parse() :
    items = list(
            parser.parse_batch(
                    ["[樱桃花字幕组] 圣女因太过完美一点也不讨人喜欢而被废除婚约卖到邻国  Kanpekiseijo - 08[1080p][简日双语] .mp4",
                     "[ANi] 公爵千金的家庭教師 - 06 [1080P][Baha][WEB-DL][AAC AVC][CHT].mp4",
                     "[ANi] 和雨．和你 - 06 [1080P][Baha][WEB-DL][AAC AVC][CHT].mp4",
                     "[LoliHouse] 坂本日常 / SAKAMOTO DAYS - 14 [WebRip 1080p HEVC-10bit AACx2][简繁内封字幕]",
                     "[TOC] NYAIGHT OF THE LIVING CAT 活尸猫之夜 [03][1080P][AVC AAC][CHT][MP4]",
                     "[MingY] 明天，美食广场见。 / 明天，美食广场见。 /  Food Court de, Mata Ashita. [03][1080p][简繁日内封]（美食广场里的女高中生们在说啥）",
                     "【极影字幕·毁片党】碧蓝之海2 Grand Blue Dreaming! S2 第03集 GB_CN HEVC_opus 1080p",
                     "[Prejudice-Studio] 坂本日常 SAKAMOTO DAYS - 13 [Bilibili WEB-DL 2160P AVC 8bit AAC MP4][简日内嵌]",
                     "[Prejudice-Studio] 坂本日常 SAKAMOTO DAYS - 13 [Bilibili WEB-DL 1080P AVC 8bit AAC MP4][简日内嵌]",
                     "[黒ネズミたち] 青春猪头少年不会梦到圣诞服女郎 / Seishun Buta Yarou wa Santa Claus no Yume wo Minai - 03 (ABEMA 1280x720 AVC AAC MP4)",
                     "[黒ネズミたち] 牧神记 / Tales of Herding Gods - 40 (B-Global Donghua 1920x1080 HEVC AAC MKV)"
                     ]
            )
    )
    for r in items :
        data = replace_enums(asdict(r))
        logger.info('\n' + json.dumps(data, ensure_ascii = False, indent = 2))
    assert isinstance(items, list)


def test_get_parser_name() :
    r = parser.get_translation_parser_list()
    assert isinstance(r, list)
