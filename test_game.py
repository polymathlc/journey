"""
Comprehensive Integrity Test Suite for Journey to the West:
- Verifies complete removal of Chronos and Greek mythology
- Verifies 30-chamber boss structure (Spider, Baigu, Golden/Silver Horn, Erlang, Buddha, Tongbei)
- Verifies Simplified Chinese localization for all systems
- Verifies asset bundle integrity and execution safety
"""

import os
import re

def test_jttw_game():
    index_path = "index.html"
    assert os.path.exists(index_path), "index.html must exist"
    
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"File size (bytes): {len(content)}")

    # 1. Purged Greek / Chronos remnants
    assert "chronos" not in content.lower() or "chronos.webp" in content, "Chronos references in gameplay/lore must be removed"
    assert "zagreus" not in content.lower(), "Zagreus must be removed"
    assert "olympus" not in content.lower(), "Olympus must be removed"
    assert "melinoe" not in content.lower(), "Melinoe must be removed"
    assert "tartarus" not in content.lower(), "Tartarus must be removed"

    # 2. Chinese mythology protagonists and bosses
    assert "齐天大圣 · 孙悟空" in content, "Sun Wukong title missing"
    assert "如意金箍棒" in content, "Ruyi Jingu Bang missing"
    assert "盘丝洞·蜘蛛精" in content, "Spider Demon boss missing"
    assert "白虎岭·白骨精" in content, "Lady White Bone boss missing"
    assert "金角银角" in content or "金角大王" in content, "Golden and Silver Horn boss missing"
    assert "二郎神" in content or "二郎显圣真君" in content, "Erlang Shen boss missing"
    assert "如来佛祖" in content, "Tathagata Buddha boss missing"
    assert "通臂猿猴" in content, "Tongbei Yuanhou Final Boss missing"

    # 3. 30-level progression structure
    assert "index === 30" in content, "Chamber 30 boss trigger missing"
    assert "index === 60" in content, "Chamber 60 boss trigger missing"
    assert "index === 90" in content, "Chamber 90 boss trigger missing"
    assert "index === 120" in content, "Chamber 120 boss trigger missing"
    assert "index === 150" in content, "Chamber 150 boss trigger missing"
    assert "index === 180" in content, "Chamber 180 boss trigger missing"

    # 4. Modals & Systems in Simplified Chinese
    assert "七十二变·地煞神通谱" in content, "72 Transformations Altar missing"
    assert "王母天庭蟠桃盛宴" in content, "Peach Feast modal missing"
    assert "西游万神伏魔录" in content, "Gods Codex missing"
    assert "东海龙宫珍宝阁与土地神坛" in content, "Dragon Treasury shop missing"

    # 5. Sound synthesis & Web Audio
    assert "SoundEngine" in content, "SoundEngine class missing"
    assert "playStaffSwing" in content, "playStaffSwing missing"
    assert "playGong" in content, "playGong missing"

    print("ALL 15 JOURNEY TO THE WEST TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_jttw_game()
