#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "The darktrain"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
from scenes import Stage


################################################################
#
#   1. Story memo
#   2. Story structure
#   3. Plot
#   4. Conte
#   5. Draft
#
################################################################

# Constant
TITLE = "暗黒鉄道の朝"
OUTLINE = "毎日人が乗り込む電車を、清掃員の男性は眺めていた"
MAJOR, MINOR, MICRO = 1, 2, 0


# Episodes
def ep1(w: World):
    return w.episode('1',
            Stage.sc_1(w),
            Stage.sc_2(w),
            Stage.sc_3(w),
            )

def ep2(w: World):
    return w.episode("2",
            Stage.sc_4(w),
            Stage.sc_5(w),
            Stage.sc_6(w),
            )

def ep3(w: World):
    return w.episode("3",
            Stage.sc_7(w),
            Stage.sc_8(w),
            w.symbol("（了）"),
            )

def ch_main(w: World):
    return w.chapter('main',
            ep1(w),
            ep2(w),
            ep3(w),
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

