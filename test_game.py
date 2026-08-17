import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('File size (bytes):', len(text))
assert '<!DOCTYPE html>' in text, "Missing DOCTYPE"
assert '<canvas id="gameCanvas">' in text, "Missing canvas"
assert 'const GODS = {' in text, "Missing GODS"
assert 'class Player {' in text, "Missing Player class"
assert 'class SoundEngine {' in text, "Missing SoundEngine"
assert 'id="pom-modal"' in text, "Missing Peach modal"
assert 'id="altar-modal"' in text, "Missing 72 Transforms Altar"
assert 'id="codex-modal"' in text, "Missing Codex modal"
assert 'SUN WUKONG' in text, "Missing Sun Wukong HUD"

scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
print('Script count:', len(scripts))
if scripts:
    print('Main JS Script length (chars):', len(scripts[0]))

print("ALL TEST ASSERTIONS PASSED SUCCESSFULLY!")
