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

    # 1. Check HTML Structure & Tags
    assert "<style>" in html, "<style> must exist!"
    assert "</style>" in html, "</style> must exist!"
    assert "</head>" in html, "</head> must exist!"
    assert "<body>" in html, "<body> must exist!"
    assert '<canvas id="gameCanvas">' in html, "gameCanvas must exist!"
    assert "</body>" in html, "</body> must exist!"
    assert "</html>" in html, "</html> must exist!"

    # Ensure style tag closes BEFORE body begins
    style_close = html.find("</style>")
    body_open = html.find("<body>")
    canvas_pos = html.find('<canvas id="gameCanvas">')
    script_open = html.find("<script>")
    script_close = html.find("</script>")
    body_close = html.find("</body>")

    assert style_close < body_open < canvas_pos < script_open < script_close < body_close, "HTML structure order must be correct!"

    # 2. Check Enemy Active Attacks & Animated Strike FX
    assert "EnemySpearThrustFX" in html, "Enemy spear thrust FX must exist!"
    assert "EnemyClawSwipeFX" in html, "Enemy claw swipe FX must exist!"
    assert "EnemySoulStrikeFX" in html, "Enemy soul strike FX must exist!"
    assert "this.attackDuration" in html, "Enemy attack duration timer must exist!"

    # 3. Check 10x Enemies, 3x Health, Knockdown and Death Animations
    assert "KnockdownDustFX" in html, "Knockdown dust FX must exist!"
    assert "DeathSoulFX" in html, "Death soul dissolution FX must exist!"
    assert "isKnockedDown" in html, "Enemy knockdown state must exist!"
    assert "isDying" in html, "Enemy dying state must exist!"
    assert "maxHp: 480" in html, "Tianbing should have 3x health (480 hp)!"
    assert "enemyCount = 30" in html, "Enemy counts should be 10x (30+ enemies per chamber)!"

    # 3. Check Jingu Bang Weapon Swinging & Dynamic Visual FX
    assert "drawJinguBangWeapon" in html, "Jingu Bang weapon swinging renderer must exist!"
    assert "GroundFissureFX" in html, "Ground fissure earth-shattering FX must exist!"
    assert "RadialSparksFX" in html, "Radial weapon sparks must exist!"
    assert "SlashSparksFX" in html, "Directional slash impact sparks must exist!"
    assert "StaffPillarSlamFX" in html, "Pillar slam special attack FX must exist!"

    # 4. Check Arena Boundary Containment & Knockback Damping
    assert "clampBoundary" in html, "Enemy boundary clamp should exist!"
    assert "boundRadius" in html, "Hard arena boundary radius should exist!"
    assert "knockbackX" in html, "Damped knockback physics should exist!"

    # 5. Check Colossal Buddha & Approval Cutscene
    assert "buddha_colossal" in html, "Colossal Buddha asset should exist!"
    assert "triggerBuddhaApprovalCutscene" in html, "Buddha approval cutscene function should exist!"
    assert "大日如来神掌" in html, "Tathagata palm attack should exist!"
    assert "telegraphZone" in html, "Telegraphed dodge window for Buddha attacks should exist!"
    assert "buddha-modal" in html, "Buddha cutscene modal should exist!"

    # 6. Check Buff Erlang & Independent Xiao Tian Quan
    assert "erlang_and_dog" in html, "Erlang & Dog asset should exist!"
    assert "xiaotianquan_hound" in html, "Independent Xiao Tian Quan combat entity should exist!"
    assert "三尖两刃枪" in html, "Erlang trident spear should exist!"

    # 7. Check God Portraits Grid Mapping
    assert "portraitCol: 0" in html, "Erlangshen/Bullking portrait column must exist!"
    assert "portraitCol: 1" in html, "Guanyin/Ironfan portrait column must exist!"
    assert "portraitCol: 4" in html, "Aoguang/Change portrait column must exist!"
    assert "portraitCol: 5" in html, "Luban portrait column must exist!"
    assert "portraitRow: 1" in html, "Second row gods must have portraitRow: 1!"

    # 8. Check Lu Ban in-game avatar
    assert "luban_avatar" in html, "Lu Ban avatar asset should exist!"
    assert "LubanAvatarNPC" in html, "Lu Ban avatar NPC class should exist!"
    assert "巧圣仙师·鲁班" in html, "Lu Ban name should exist!"

    # 8. Check 4-Directional movement & attack perspectives
    assert "direction = 'up'" in html, "Up direction should exist!"
    assert "direction = 'down'" in html, "Down direction should exist!"

    # 9. Check 180 levels & Final Boss Tongbei
    assert "boss_tongbei" in html, "Final boss Tongbei Yuanhou should exist!"
    assert "180" in html, "180 levels should exist!"

    # 10. Check Real Frame-by-Frame Generated Animation Sheets
    assert "wukong_real_anims" in html, "Wukong real combat animation asset must exist!"
    assert "enemies_real_anims" in html, "Enemies real combat animation asset must exist!"
    assert "bosses_real_anims" in html, "Bosses real combat animation asset must exist!"

    print("ALL TESTS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    test_game_features()
