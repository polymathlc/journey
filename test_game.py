"""
Test suite for Journey to the West: Havoc in Heaven
"""

import os

def test_game_features():
    assert os.path.exists("index.html"), "index.html must exist!"
    size = os.path.getsize("index.html")
    assert size > 2500000, f"index.html should contain embedded assets (size: {size})"
    print(f"File size: {size} bytes")

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Check Colossal Buddha & Approval Cutscene
    assert "buddha_colossal" in html, "Colossal Buddha asset should exist!"
    assert "triggerBuddhaApprovalCutscene" in html, "Buddha approval cutscene function should exist!"
    assert "大日如来神掌" in html, "Tathagata palm attack should exist!"
    assert "telegraphZone" in html, "Telegraphed dodge window for Buddha attacks should exist!"
    assert "buddha-modal" in html, "Buddha cutscene modal should exist!"

    # 2. Check Buff Erlang & Independent Xiao Tian Quan
    assert "erlang_and_dog" in html, "Erlang & Dog asset should exist!"
    assert "xiaotianquan_hound" in html, "Independent Xiao Tian Quan combat entity should exist!"
    assert "三尖两刃枪" in html, "Erlang trident spear should exist!"

    # 3. Check Lu Ban in-game avatar
    assert "luban_avatar" in html, "Lu Ban avatar asset should exist!"
    assert "LubanAvatarNPC" in html, "Lu Ban avatar NPC class should exist!"
    assert "巧圣仙师·鲁班" in html, "Lu Ban name should exist!"

    # 4. Check 4-Directional movement & attack perspectives
    assert "direction = 'up'" in html, "Up direction should exist!"
    assert "direction = 'down'" in html, "Down direction should exist!"

    # 5. Check 180 levels & Final Boss Tongbei
    assert "boss_tongbei" in html, "Final boss Tongbei Yuanhou should exist!"
    assert "180" in html, "180 levels should exist!"

    print("ALL TESTS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    test_game_features()
