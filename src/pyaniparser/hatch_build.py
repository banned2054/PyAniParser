# hatch_build.py
import os

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomHook(BuildHookInterface) :
    def initialize(self, version, build_data) :
        # 从环境变量读取要用的 wheel tag
        tag = os.environ.get("PYANIPARSER_WHEEL_TAG")

        if tag :
            # 例如：py3-none-win_amd64 / py3-none-manylinux_2_17_x86_64 / ...
            build_data["tag"] = tag

            # 告诉元数据这是非纯 Python 包（带 native 库）
            build_data["pure_python"] = False
