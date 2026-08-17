"""
Journey to the West: Havoc in Heaven (西游记·大闹天宫)
Enhanced Game Generator with Complete Brand New Custom Visual Assets
"""

import os
import json
import base64

# Load all webp assets
assets_keys = [
    'hero', 'shade', 'witch', 'chronos',
    'consistent_tiles', 'seamless_floor', 'props', 'ui',
    'clean_fx', 'attack_fx_vfx', 'combo_special_vfx', 'elemental_spells_vfx',
    'all_10_gods', 'monsters_beasts', 'undead_cultists', 'new_projectiles',
    'minibosses', 'reward_icons',
    'infinite_bosses_a', 'infinite_bosses_b', 'infinite_bosses_c'
]

b64_data = {}
assets_dir = "assets_webp"
for k in assets_keys:
    webp_path = os.path.join(assets_dir, f"{k}.webp")
    if os.path.exists(webp_path):
        with open(webp_path, 'rb') as fp:
            enc = base64.b64encode(fp.read()).decode('utf-8')
            b64_data[k] = f"data:image/webp;base64,{enc}"

print(f"Loaded {len(b64_data)} brand new assets.")

# HTML / CSS / JS Template for Journey to the West
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>JOURNEY TO THE WEST: HAVOC IN HEAVEN (西游记·大闹天宫 - 100 Chambers Roguelite)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Ma+Shan+Zheng&family=Noto+Serif+SC:wght@600;700;900&family=Philosopher:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    :root {
      --gold-primary: #e6b450;
      --gold-light: #fff2a8;
      --gold-dark: #8c5b16;
      --bronze: #5a3818;
      --obsidian: #0c0914;
      --crimson-primary: #ef4444;
      --crimson-dark: #991b1b;
      --jade-green: #10b981;
      --jade-dark: #065f46;
      --qi-purple: #a855f7;
      --qi-glow: #d8b4fe;
      --peach-pink: #fb7185;
      --peach-glow: #fda4af;
      --sky-blue: #38bdf8;
      --font-chinese: 'Ma Shan Zheng', 'Noto Serif SC', serif;
      --font-title: 'Cinzel', 'Noto Serif SC', serif;
      --font-body: 'Philosopher', 'Noto Serif SC', sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
    }

    body, html {
      width: 100%;
      height: 100%;
      overflow: hidden;
      background-color: #06040a;
      font-family: var(--font-body);
      color: #f1e9da;
    }

    #game-container {
      position: relative;
      width: 100vw;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: radial-gradient(circle at center, #1e142e 0%, #06040a 100%);
    }

    canvas#gameCanvas {
      display: block;
      width: 100%;
      height: 100%;
      object-fit: contain;
      cursor: crosshair;
    }

    /* UI Layer Overlay */
    #ui-layer {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 20px;
    }

    /* Top HUD */
    .top-hud {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      width: 100%;
    }

    .player-bars {
      display: flex;
      flex-direction: column;
      gap: 8px;
      width: 350px;
      filter: drop-shadow(0 4px 14px rgba(0,0,0,0.9));
    }

    .hero-tag {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 2px;
    }

    .hero-avatar-circle {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      border: 2px solid var(--gold-primary);
      box-shadow: 0 0 10px rgba(230, 180, 80, 0.7);
      background-size: cover;
      background-position: center;
    }

    .hero-name {
      font-family: var(--font-title);
      font-size: 17px;
      font-weight: 900;
      color: var(--gold-light);
      letter-spacing: 1px;
      text-shadow: 0 0 8px rgba(230, 180, 80, 0.6);
    }

    .hero-title {
      font-family: var(--font-chinese);
      font-size: 15px;
      color: #f87171;
      margin-left: 6px;
    }

    .bar-wrapper {
      position: relative;
      height: 24px;
      background: #110e18;
      border: 2px solid var(--gold-dark);
      border-radius: 6px;
      overflow: hidden;
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.95);
    }

    .bar-fill {
      height: 100%;
      width: 100%;
      transition: width 0.15s cubic-bezier(0.2, 0.9, 0.4, 1.1);
    }

    .bar-fill.health {
      background: linear-gradient(90deg, #991b1b, #ef4444, #f87171);
      box-shadow: 0 0 14px rgba(239, 68, 68, 0.8);
    }

    .bar-fill.qi {
      background: linear-gradient(90deg, #6b21a8, #a855f7, #c084fc);
      box-shadow: 0 0 14px rgba(168, 85, 247, 0.8);
    }

    .bar-fill.awakening {
      background: linear-gradient(90deg, #b45309, #f59e0b, #fef08a);
      box-shadow: 0 0 14px rgba(245, 158, 11, 0.9);
    }

    .bar-text {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 10px;
      font-family: var(--font-title);
      font-size: 11px;
      font-weight: 700;
      color: #fff;
      text-shadow: 0 1px 3px #000, 0 0 6px #000;
      letter-spacing: 0.5px;
    }

    /* Top Center: Chamber / Biome Banner */
    .top-center-hud {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .chamber-title {
      font-family: var(--font-title);
      font-size: 21px;
      font-weight: 900;
      color: var(--gold-light);
      letter-spacing: 2px;
      text-shadow: 0 0 14px rgba(230, 180, 80, 0.8);
    }

    .chamber-subtitle {
      font-family: var(--font-chinese);
      font-size: 15px;
      color: #e2e8f0;
      letter-spacing: 1.5px;
      margin-top: 3px;
    }

    /* Currency & Meta Panel */
    .currency-panel {
      display: flex;
      align-items: center;
      gap: 16px;
      background: rgba(14, 13, 19, 0.88);
      border: 2px solid var(--gold-dark);
      border-radius: 8px;
      padding: 6px 14px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.8);
    }

    .currency-item {
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-title);
      font-size: 14px;
      font-weight: 700;
    }

    .currency-item.gold { color: #facc15; }
    .currency-item.ashes { color: #c084fc; }
    .currency-item.peaches { color: #fb7185; }
    .currency-item.lives { color: #4ade80; }

    /* Boss HUD */
    .boss-bar-container {
      position: absolute;
      top: 75px;
      left: 50%;
      transform: translateX(-50%);
      width: 600px;
      display: none;
      flex-direction: column;
      align-items: center;
      filter: drop-shadow(0 4px 20px rgba(0,0,0,0.95));
      pointer-events: none;
    }

    .boss-name {
      font-family: var(--font-title);
      font-size: 16px;
      font-weight: 900;
      color: #fbbf24;
      letter-spacing: 2px;
      margin-bottom: 4px;
      text-shadow: 0 0 10px rgba(251, 191, 36, 0.7);
    }

    .boss-bar-wrapper {
      position: relative;
      width: 100%;
      height: 24px;
      background: #110e18;
      border: 2px solid #d97706;
      border-radius: 6px;
      overflow: hidden;
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.95);
    }

    .boss-bar-fill {
      height: 100%;
      width: 100%;
      background: linear-gradient(90deg, #b91c1c, #f59e0b, #ef4444);
      box-shadow: 0 0 16px rgba(239, 68, 68, 0.9);
      transition: width 0.1s linear;
    }

    /* Bottom Controls HUD */
    .bottom-hud {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      width: 100%;
    }

    .action-slots {
      display: flex;
      gap: 12px;
    }

    .action-slot {
      position: relative;
      width: 64px;
      height: 64px;
      background: rgba(18, 14, 26, 0.88);
      border: 2px solid var(--gold-dark);
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 14px rgba(0,0,0,0.8);
      transition: border-color 0.2s, transform 0.1s;
    }

    .action-slot.active {
      border-color: var(--gold-primary);
      box-shadow: 0 0 12px rgba(230, 180, 80, 0.7);
    }

    .action-slot .key-badge {
      position: absolute;
      top: -8px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--gold-primary);
      color: #000;
      font-family: var(--font-title);
      font-size: 10px;
      font-weight: 900;
      padding: 1px 6px;
      border-radius: 4px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }

    .action-slot .slot-label {
      font-family: var(--font-title);
      font-size: 10px;
      font-weight: 700;
      color: #e2e8f0;
      margin-top: 4px;
    }

    .action-slot .slot-boon {
      font-family: var(--font-chinese);
      font-size: 11px;
      color: var(--gold-light);
      margin-top: 2px;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 58px;
    }

    /* Right Quick Buttons */
    .quick-buttons {
      display: flex;
      gap: 10px;
      pointer-events: auto;
    }

    .btn-hud {
      background: linear-gradient(180deg, #2a1f3d, #140d21);
      border: 2px solid var(--gold-dark);
      color: var(--gold-light);
      font-family: var(--font-title);
      font-size: 12px;
      font-weight: 700;
      padding: 8px 14px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
      box-shadow: 0 4px 12px rgba(0,0,0,0.7);
    }

    .btn-hud:hover {
      border-color: var(--gold-primary);
      transform: translateY(-2px);
      box-shadow: 0 0 14px rgba(230, 180, 80, 0.5);
    }

    /* Modals Overlay */
    .modal-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(4, 2, 8, 0.90);
      backdrop-filter: blur(8px);
      display: none;
      justify-content: center;
      align-items: center;
      z-index: 100;
      pointer-events: auto;
      animation: fadeIn 0.25s ease-out;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.97); }
      to { opacity: 1; transform: scale(1); }
    }

    .modal-box {
      position: relative;
      background: radial-gradient(circle at top, #231638 0%, #0e0a17 100%);
      border: 3px solid var(--gold-primary);
      border-radius: 14px;
      padding: 28px;
      width: 880px;
      max-width: 95vw;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 10px 40px rgba(0,0,0,0.95), 0 0 30px rgba(230, 180, 80, 0.3);
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .modal-header {
      text-align: center;
      margin-bottom: 20px;
      position: relative;
      width: 100%;
    }

    .modal-god-portrait {
      width: 120px;
      height: 120px;
      border-radius: 50%;
      border: 3px solid var(--gold-primary);
      box-shadow: 0 0 24px rgba(230, 180, 80, 0.8);
      margin-bottom: 12px;
      background-size: cover;
      background-position: center;
    }

    .modal-title {
      font-family: var(--font-title);
      font-size: 26px;
      font-weight: 900;
      color: var(--gold-light);
      letter-spacing: 2px;
      text-shadow: 0 0 12px rgba(230, 180, 80, 0.7);
    }

    .modal-subtitle {
      font-family: var(--font-chinese);
      font-size: 16px;
      color: #94a3b8;
      margin-top: 4px;
    }

    .modal-quote {
      font-style: italic;
      color: #cbd5e1;
      font-size: 13px;
      margin-top: 8px;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.4;
    }

    /* Cards Grid */
    .boon-cards-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
      width: 100%;
      margin-top: 10px;
    }

    .boon-card {
      position: relative;
      background: linear-gradient(180deg, rgba(38, 26, 58, 0.9), rgba(16, 12, 24, 0.95));
      border: 2px solid var(--gold-dark);
      border-radius: 10px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      cursor: pointer;
      transition: all 0.2s;
      min-height: 210px;
      box-shadow: 0 6px 16px rgba(0,0,0,0.8);
    }

    .boon-card:hover {
      border-color: var(--gold-primary);
      transform: translateY(-4px);
      box-shadow: 0 0 20px rgba(230, 180, 80, 0.6);
      background: linear-gradient(180deg, rgba(55, 36, 85, 0.95), rgba(22, 16, 35, 0.95));
    }

    .boon-slot-tag {
      align-self: flex-start;
      font-family: var(--font-title);
      font-size: 10px;
      font-weight: 700;
      background: rgba(230, 180, 80, 0.2);
      border: 1px solid var(--gold-primary);
      color: var(--gold-light);
      padding: 2px 8px;
      border-radius: 4px;
      margin-bottom: 8px;
    }

    .boon-name {
      font-family: var(--font-title);
      font-size: 16px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 6px;
    }

    .boon-desc {
      font-size: 12px;
      color: #cbd5e1;
      line-height: 1.45;
      flex-grow: 1;
    }

    .boon-action-btn {
      margin-top: 14px;
      background: linear-gradient(180deg, #b45309, #78350f);
      border: 1px solid var(--gold-light);
      color: #fff;
      font-family: var(--font-title);
      font-size: 11px;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: 6px;
      text-align: center;
    }

    /* Altar Grid */
    .altar-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      width: 100%;
      margin-top: 14px;
    }

    .altar-item {
      background: rgba(22, 16, 35, 0.9);
      border: 2px solid var(--gold-dark);
      border-radius: 8px;
      padding: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .altar-info {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .altar-name {
      font-family: var(--font-title);
      font-size: 14px;
      font-weight: 700;
      color: var(--gold-light);
    }

    .altar-desc {
      font-size: 11px;
      color: #94a3b8;
    }

    .altar-level {
      font-family: var(--font-title);
      font-size: 11px;
      color: #4ade80;
    }

    .altar-btn {
      background: linear-gradient(180deg, #7c3aed, #4c1d95);
      border: 1px solid #c084fc;
      color: #fff;
      font-family: var(--font-title);
      font-size: 11px;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      white-space: nowrap;
    }

    .altar-btn:hover {
      box-shadow: 0 0 10px #c084fc;
    }

    .altar-btn:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }

    /* Codex Grid */
    .codex-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      width: 100%;
      margin-top: 14px;
      max-height: 480px;
      overflow-y: auto;
      padding-right: 8px;
    }

    .codex-card {
      background: rgba(22, 16, 35, 0.9);
      border: 2px solid var(--gold-dark);
      border-radius: 8px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .codex-god-title {
      font-family: var(--font-title);
      font-size: 15px;
      font-weight: 700;
      color: var(--gold-light);
    }

    .codex-boon-list {
      font-size: 11px;
      color: #cbd5e1;
      line-height: 1.4;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    /* Close Button */
    .modal-close-btn {
      margin-top: 20px;
      background: linear-gradient(180deg, #374151, #1f2937);
      border: 1px solid #9ca3af;
      color: #f3f4f6;
      font-family: var(--font-title);
      font-size: 13px;
      font-weight: 700;
      padding: 8px 24px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .modal-close-btn:hover {
      background: #4b5563;
      border-color: #fff;
    }

    /* Game Over / Victory Modal */
    .gameover-box {
      text-align: center;
      max-width: 600px;
    }

    .gameover-title {
      font-family: var(--font-title);
      font-size: 36px;
      font-weight: 900;
      letter-spacing: 3px;
      margin-bottom: 10px;
    }

    .gameover-title.victory {
      color: #facc15;
      text-shadow: 0 0 20px rgba(250, 204, 21, 0.8);
    }

    .gameover-title.defeat {
      color: #ef4444;
      text-shadow: 0 0 20px rgba(239, 68, 68, 0.8);
    }

    .stats-summary {
      background: rgba(14, 10, 20, 0.8);
      border: 1px solid var(--gold-dark);
      border-radius: 8px;
      padding: 16px;
      width: 100%;
      margin: 16px 0;
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-family: var(--font-title);
      font-size: 13px;
    }

    .stat-row {
      display: flex;
      justify-content: space-between;
      color: #cbd5e1;
    }

    .stat-val {
      color: var(--gold-light);
      font-weight: 700;
    }
  </style>
</head>
<body>
  <div id="game-container">
    <canvas id="gameCanvas"></canvas>

    <div id="ui-layer">
      <!-- Top HUD -->
      <div class="top-hud">
        <div class="player-bars">
          <div class="hero-tag">
            <span class="hero-name">SUN WUKONG</span>
            <span class="hero-title">齐天大圣 · 如意金箍棒</span>
          </div>
          <div class="bar-wrapper">
            <div id="hp-bar" class="bar-fill health" style="width: 100%;"></div>
            <div class="bar-text"><span>HEALTH (气血)</span><span id="hp-text">100 / 100</span></div>
          </div>
          <div class="bar-wrapper">
            <div id="qi-bar" class="bar-fill qi" style="width: 100%;"></div>
            <div class="bar-text"><span>SPIRIT QI (真气)</span><span id="qi-text">50 / 50</span></div>
          </div>
          <div class="bar-wrapper" style="height: 16px;">
            <div id="awaken-bar" class="bar-fill awakening" style="width: 0%;"></div>
            <div class="bar-text" style="font-size: 9px;"><span>HAVOC GAUGE (大闹天宫)</span><span id="awaken-text">READY: [R/F]</span></div>
          </div>
        </div>

        <div class="top-center-hud">
          <div id="chamber-name" class="chamber-title">FLOWER-FRUIT MOUNTAIN - CHAMBER 1 / 100</div>
          <div id="chamber-sub" class="chamber-subtitle">花果山水帘洞 · 仙石初现</div>
        </div>

        <div class="currency-panel">
          <div class="currency-item gold">
            <span>🪙</span>
            <span id="gold-val">0</span>
          </div>
          <div class="currency-item ashes">
            <span>✨</span>
            <span id="ashes-val">0</span>
          </div>
          <div class="currency-item peaches">
            <span>🍑</span>
            <span id="peaches-val">0</span>
          </div>
          <div class="currency-item lives">
            <span>❤️</span>
            <span id="lives-val">1</span>
          </div>
        </div>
      </div>

      <!-- Boss HUD -->
      <div id="boss-hud" class="boss-bar-container">
        <div id="boss-name-text" class="boss-name">EAST SEA DRAGON KING AO GUANG (东海龙王·敖广)</div>
        <div class="boss-bar-wrapper">
          <div id="boss-bar-fill" class="boss-bar-fill" style="width: 100%;"></div>
        </div>
      </div>

      <!-- Bottom HUD -->
      <div class="bottom-hud">
        <div class="action-slots">
          <div class="action-slot active" id="slot-attack">
            <div class="key-badge">L-CLICK</div>
            <div class="slot-label">ATTACK</div>
            <div class="slot-boon" id="boon-tag-attack">Ruyi Staff</div>
          </div>
          <div class="action-slot" id="slot-special">
            <div class="key-badge">R-CLICK/Q</div>
            <div class="slot-label">SPECIAL</div>
            <div class="slot-boon" id="boon-tag-special">Pillar Smash</div>
          </div>
          <div class="action-slot" id="slot-cast">
            <div class="key-badge">E/CAST</div>
            <div class="slot-label">CAST</div>
            <div class="slot-boon" id="boon-tag-cast">Immobilize</div>
          </div>
          <div class="action-slot" id="slot-dash">
            <div class="key-badge">SPACE/SHIFT</div>
            <div class="slot-label">DASH</div>
            <div class="slot-boon" id="boon-tag-dash">Cloud Warp</div>
          </div>
          <div class="action-slot" id="slot-hex">
            <div class="key-badge">R/AWAKEN</div>
            <div class="slot-label">AWAKEN</div>
            <div class="slot-boon" id="boon-tag-hex">Great Sage</div>
          </div>
        </div>

        <div class="quick-buttons">
          <button class="btn-hud" onclick="openAltarOfTransformations()">📜 72 TRANSFORMS</button>
          <button class="btn-hud" onclick="openSkillCodex()">📖 GODS CODEX</button>
        </div>
      </div>
    </div>

    <!-- Modals -->
    <!-- 1. Chinese Gods Boon Modal -->
    <div id="boon-modal" class="modal-overlay">
      <div class="modal-box">
        <div class="modal-header">
          <div id="god-portrait" class="modal-god-portrait"></div>
          <div id="god-name" class="modal-title">ERLANG SHEN</div>
          <div id="god-title" class="modal-subtitle">God of Divine Retribution · 二郎神杨戬</div>
          <div id="god-quote" class="modal-quote">"Monkey, accept heaven's decree. Sunder the demons that obstruct the righteous path!"</div>
        </div>
        <div id="boon-choices-container" class="boon-cards-grid">
          <!-- Dynamically populated 3 boon choices -->
        </div>
      </div>
    </div>

    <!-- 2. Heavenly Peaches of Immortality Modal (replaces Pom of Power) -->
    <div id="pom-modal" class="modal-overlay">
      <div class="modal-box">
        <div class="modal-header">
          <div id="peach-modal-icon" style="width: 100px; height: 100px; border-radius: 50%; border: 3px solid var(--peach-pink); box-shadow: 0 0 20px rgba(251, 113, 133, 0.8); margin: 0 auto 12px; background-size: 200%; background-position: 0 0;"></div>
          <div class="modal-title" style="color: var(--peach-pink);">HEAVENLY PEACH OF IMMORTALITY (天庭蟠桃)</div>
          <div class="modal-subtitle">Queen Mother's Celestial Orchard · 延年益寿 神通精进</div>
          <div class="modal-quote">"One bite adds 3,000 years of Dao cultivation! Choose an equipped boon to elevate its power level."</div>
        </div>
        <div id="pom-choices-container" class="boon-cards-grid">
          <!-- Dynamically populated 3 equipped boons -->
        </div>
      </div>
    </div>

    <!-- 3. Dragon King's Treasury & Earth God Pavilion (Shop) -->
    <div id="shop-modal" class="modal-overlay">
      <div class="modal-box">
        <div class="modal-header">
          <div style="font-size: 48px; margin-bottom: 8px;">🏮</div>
          <div class="modal-title" style="color: #facc15;">DRAGON TREASURY & EARTH SHRINE (龙宫宝阁·土地福地)</div>
          <div class="modal-subtitle">Trade Jade Coins for Divine Relics and Elixirs</div>
        </div>
        <div id="shop-choices-container" class="boon-cards-grid">
          <!-- Dynamically populated 3 shop items -->
        </div>
        <button class="modal-close-btn" onclick="closeShopModal()">LEAVE PAVILION</button>
      </div>
    </div>

    <!-- 4. Altar of 72 Transformations (Meta Progression) -->
    <div id="altar-modal" class="modal-overlay">
      <div class="modal-box">
        <div class="modal-header">
          <div class="modal-title" style="color: #c084fc;">ALTAR OF THE 72 EARTHLY TRANSFORMS (七十二变·神通谱)</div>
          <div class="modal-subtitle">Attain Divine Immortality by Harnessing Karma Spirit Ashes</div>
        </div>
        <div id="altar-items-container" class="altar-grid">
          <!-- Dynamically populated 6 transform traits -->
        </div>
        <button class="modal-close-btn" onclick="closeAltarModal()">RESUME RUN</button>
      </div>
    </div>

    <!-- 5. Codex of Immortals & Demons -->
    <div id="codex-modal" class="modal-overlay">
      <div class="modal-box">
        <div class="modal-header">
          <div class="modal-title">CODEX OF IMMORTALS & DEMONS (西游万神伏魔录)</div>
          <div class="modal-subtitle">Complete Compendium of the 10 Deities and 100 Divine Boons</div>
        </div>
        <div id="codex-cards-container" class="codex-grid">
          <!-- Populated with all 10 gods -->
        </div>
        <button class="modal-close-btn" onclick="closeSkillCodex()">CLOSE CODEX</button>
      </div>
    </div>

    <!-- 6. Game Over / Victory Modal -->
    <div id="gameover-modal" class="modal-overlay">
      <div class="modal-box gameover-box">
        <div id="gameover-title" class="gameover-title defeat">DEFEATED</div>
        <div id="gameover-sub" class="modal-subtitle">Your mortal shell was dispersed in the Celestial Realm</div>
        <div class="stats-summary">
          <div class="stat-row"><span>Chambers Cleared:</span><span id="stat-chambers" class="stat-val">1</span></div>
          <div class="stat-row"><span>Enemies Vanquished:</span><span id="stat-kills" class="stat-val">0</span></div>
          <div class="stat-row"><span>Divine Boons Attained:</span><span id="stat-boons" class="stat-val">0</span></div>
          <div class="stat-row"><span>Heavenly Peaches Eaten:</span><span id="stat-peaches" class="stat-val">0</span></div>
          <div class="stat-row"><span>Karma Ashes Collected:</span><span id="stat-ashes" class="stat-val">0</span></div>
        </div>
        <button class="btn-hud" style="font-size: 16px; padding: 10px 32px;" onclick="restartRun()">ASCEND AGAIN (重新启程)</button>
      </div>
    </div>

  </div>

  <script>
    // Embedded Base64 Assets
    const ASSETS = %ASSETS_JSON%;
    const loadedImages = {};
    let loadedCount = 0;
    const totalAssets = Object.keys(ASSETS).length;

    for (let key in ASSETS) {
      const img = new Image();
      img.src = ASSETS[key];
      img.onload = () => {
        loadedCount++;
      };
      loadedImages[key] = img;
    }

    // ==========================================
    // SOUND SYNTHESIZER (Web Audio API)
    // Chinese Mythological Martial Soundscape
    // ==========================================
    class SoundEngine {
      constructor() {
        this.ctx = null;
        this.isMuted = false;
      }

      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioContext();
        }
        if (this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      }

      // Ruyi Staff Swoosh (Whistling Staff Arc)
      playStaffSwing() {
        if (!this.ctx) return;
        const t = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        const filter = this.ctx.createBiquadFilter();

        osc.type = 'sine';
        osc.frequency.setValueAtTime(340, t);
        osc.frequency.exponentialRampToValueAtTime(140, t + 0.14);

        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(900, t);

        gain.gain.setValueAtTime(0.3, t);
        gain.gain.linearRampToValueAtTime(0.01, t + 0.14);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(t);
        osc.stop(t + 0.14);
      }

      // Iron Staff Strike Hit (Heavy Clang + Thump)
      playStaffHit() {
        if (!this.ctx) return;
        const t = this.ctx.currentTime;
        const osc1 = this.ctx.createOscillator();
        const gain1 = this.ctx.createGain();
        osc1.type = 'triangle';
        osc1.frequency.setValueAtTime(620, t);
        osc1.frequency.exponentialRampToValueAtTime(220, t + 0.18);
        gain1.gain.setValueAtTime(0.45, t);
        gain1.gain.exponentialRampToValueAtTime(0.001, t + 0.18);
        osc1.connect(gain1);
        gain1.connect(this.ctx.destination);
        osc1.start(t);
        osc1.stop(t + 0.18);

        const osc2 = this.ctx.createOscillator();
        const gain2 = this.ctx.createGain();
        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(140, t);
        osc2.frequency.exponentialRampToValueAtTime(45, t + 0.22);
        gain2.gain.setValueAtTime(0.55, t);
        gain2.gain.exponentialRampToValueAtTime(0.001, t + 0.22);
        osc2.connect(gain2);
        gain2.connect(this.ctx.destination);
        osc2.start(t);
        osc2.stop(t + 0.22);
      }

      // Colossal Staff Smash & Shockwave
      playStaffSmash() {
        if (!this.ctx) return;
        const t = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(240, t);
        osc.frequency.exponentialRampToValueAtTime(30, t + 0.45);

        gain.gain.setValueAtTime(0.65, t);
        gain.gain.exponentialRampToValueAtTime(0.001, t + 0.45);

        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(t);
        osc.stop(t + 0.45);
      }

      // Resonant Bronze Temple Gong (开堂金锣 - Chamber Clear / Elite Defeat)
      playGong() {
        if (!this.ctx) return;
        const t = this.ctx.currentTime;
        const freqs = [180, 260, 390, 520];
        freqs.forEach((freq, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = idx % 2 === 0 ? 'sine' : 'triangle';
          osc.frequency.setValueAtTime(freq, t);
          osc.frequency.exponentialRampToValueAtTime(freq * 0.96, t + 1.8);

          gain.gain.setValueAtTime(0.28 / (idx + 1), t);
          gain.gain.exponentialRampToValueAtTime(0.0001, t + 1.8);

          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 1.8);
        });
      }

      // Jade Singing Bowl Chime (空灵玉磬 - Boon Select & Level Up)
      playJadeChime() {
        if (!this.ctx) return;
        const t = this.ctx.currentTime;
        const freqs = [523.25, 659.25, 783.99, 1046.5];
        freqs.forEach((f, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(f, t + i * 0.06);

          gain.gain.setValueAtTime(0.25, t + i * 0.06);
          gain.gain.exponentialRampToValueAtTime(0.001, t + i * 0.06 + 1.2);

          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t + i * 0.06);
          osc.stop(t + i * 0.06 + 1.2);
        });
      }

      // Heavenly Peach Bite Crunch & Immortality Chime (吃蟠桃)
      playPeachBite() {
        if (!this.ctx) return;
        const t = this.ctx.currentTime;
        const bufferSize = this.ctx.sampleRate * 0.12;
        const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
          data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.3));
        }
        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;
        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(0.45, t);
        gain.gain.exponentialRampToValueAtTime(0.01, t + 0.12);
        noise.connect(gain);
        gain.connect(this.ctx.destination);
        noise.start(t);

        setTimeout(() => this.playJadeChime(), 100);
      }

      // Somersault Cloud Dash (筋斗云破空)
      playDash() {
        if (!this.ctx) return;
        const t = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(650, t);
        osc.frequency.exponentialRampToValueAtTime(180, t + 0.2);
        gain.gain.setValueAtTime(0.28, t);
        gain.gain.linearRampToValueAtTime(0.001, t + 0.2);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(t);
        osc.stop(t + 0.2);
      }

      // Lightning Strike (九天神雷)
      playLightning() {
        if (!this.ctx) return;
        const t = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(480, t);
        osc.frequency.exponentialRampToValueAtTime(70, t + 0.25);
        gain.gain.setValueAtTime(0.48, t);
        gain.gain.exponentialRampToValueAtTime(0.01, t + 0.25);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(t);
        osc.stop(t + 0.25);
      }

      // Samadhi Fire Blast (三昧真火)
      playFire() {
        if (!this.ctx) return;
        const t = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(260, t);
        osc.frequency.linearRampToValueAtTime(100, t + 0.3);
        gain.gain.setValueAtTime(0.38, t);
        gain.gain.exponentialRampToValueAtTime(0.01, t + 0.3);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(t);
        osc.stop(t + 0.3);
      }

      // Great Sage Awakening (法天象地·大闹天宫)
      playAwaken() {
        if (!this.ctx) return;
        this.playGong();
        setTimeout(() => this.playJadeChime(), 150);
      }
    }

    const sound = new SoundEngine();
    window.addEventListener('click', () => sound.init(), { once: true });
    window.addEventListener('keydown', () => sound.init(), { once: true });

    // ==========================================
    // 10 CHINESE GODS & 100 DIVINE BOONS
    // Journey to the West Mythology
    // ==========================================
    const GODS = {
      erlangshen: {
        name: 'Erlang Shen',
        title: 'God of Divine Retribution · 二郎神杨戬',
        portraitIndex: 0,
        color: '#facc15',
        quotes: [
          '"Monkey, let us see if your staff is sharp enough to pierce the Three Realms!"',
          '"The Third Eye of Heaven perceives all deceit. Strike with true divine fury!"'
        ],
        boons: [
          { id: 'erlang_strike', name: 'Heavenly Judgment Strike', slot: 'Attack', desc: '[ATTACK] Staff strikes summon celestial lightning lances dealing 45 bonus True Damage and inflicting Retribution.' },
          { id: 'erlang_ring', name: 'Third-Eye Seal', slot: 'Cast', desc: '[CAST] Cast zone exposes enemy weaknesses, increasing all damage taken by 40% and firing laser pulses.' },
          { id: 'erlang_dash', name: 'Retribution Warp', slot: 'Dash', desc: '[DASH] Dashing triggers a heavenly lightning bolt at the departure point for 40 area damage.' },
          { id: 'erlang_special', name: 'Sky-Sunder Cleave', slot: 'Special', desc: '[SPECIAL] Ruyi Pillar Smash releases a golden shockwave that pierces through all obstacles for 75 damage.' },
          { id: 'erlang_hound', name: 'Celestial Hound Stalker', slot: 'Passive - Combat', desc: '[PASSIVE] Critical hits summon the Celestial Hound (哮天犬) to bite the target for 120 damage and stagger them.' },
          { id: 'erlang_truesight', name: 'Third Eye Insight', slot: 'Passive - Crit', desc: '[PASSIVE] All attacks gain +25% Critical Strike Chance and +50% Critical Damage.' },
          { id: 'erlang_execute', name: 'Divine Judgment', slot: 'Passive - Execution', desc: '[PASSIVE] Enemies below 20% Health take 3x damage from all your attacks.' },
          { id: 'erlang_lance', name: 'Spear of Heaven', slot: 'Passive - Special', desc: '[PASSIVE] Special attacks summon 3 secondary homing golden lances dealing 35 damage each.' },
          { id: 'erlang_wrath', name: 'Three Realms Wrath', slot: 'Passive - Survival', desc: '[PASSIVE] When taking damage, release a screen-wide blinding flash stunning all foes for 1.5s.' },
          { id: 'erlang_apotheosis', name: 'Celestial Sovereign', slot: 'Passive - Awakening', desc: '[PASSIVE] Awakened Great Sage form duration is increased by +50% and grants permanent +30% attack speed.' }
        ]
      },
      guanyin: {
        name: 'Guanyin Bodhisattva',
        title: 'Bodhisattva of Great Mercy · 观音菩萨',
        portraitIndex: 1,
        color: '#34d399',
        quotes: [
          '"Wukong, calm the restless mind. The vast ocean of mercy cleanses all torment."',
          '"Receive the dew from the Pure Jade Vase. May your golden body remain unyielding."'
        ],
        boons: [
          { id: 'guanyin_strike', name: 'Pure Nectar Strike', slot: 'Attack', desc: '[ATTACK] Staff strikes heal Wukong for 4 HP on hit and cleanse negative status effects.' },
          { id: 'guanyin_ring', name: 'Sacred Lotus Zone', slot: 'Cast', desc: '[CAST] Cast zone summons a sacred lotus that heals 8 HP/sec while slowing enemy movement by 50%.' },
          { id: 'guanyin_dash', name: 'Willow Breeze Dash', slot: 'Dash', desc: '[DASH] Dashing grants a protective jade shield absorbing up to 30 damage for 2.5s.' },
          { id: 'guanyin_special', name: 'Compassion Tide', slot: 'Special', desc: '[SPECIAL] Special attack emits a gentle radiant wave that deflects enemy projectiles and restores 15 Qi.' },
          { id: 'guanyin_nirvana', name: 'Nirvana Rebirth', slot: 'Passive - Survival', desc: '[PASSIVE] Gain +1 extra Death Defiance life charge per run. When reviving, restore 70% Max HP.' },
          { id: 'guanyin_aegis', name: 'Bodhi Jade Armor', slot: 'Passive - Defense', desc: '[PASSIVE] Reduce all incoming damage by 25% and become immune to trap hazards.' },
          { id: 'guanyin_dew', name: 'Pure Vase Dew', slot: 'Passive - Healing', desc: '[PASSIVE] Whenever you enter a new chamber, instantly restore 30 HP and 25 Qi.' },
          { id: 'guanyin_serenity', name: 'Unshakable Zen', slot: 'Passive - Qi', desc: '[PASSIVE] Spirit Qi regenerates +3 Qi per second automatically.' },
          { id: 'guanyin_bloom', name: 'Radiant Lotus Bloom', slot: 'Passive - Area', desc: '[PASSIVE] Defeated foes leave behind radiant lotus blossoms that explode for 80 healing / damage.' },
          { id: 'guanyin_grace', name: 'Boundless Mercy', slot: 'Passive - Stat', desc: '[PASSIVE] Increases Max Health by +60 and Max Spirit Qi by +30.' }
        ]
      },
      nezha: {
        name: 'Third Lotus Prince Nezha',
        title: 'Prince of Wind & Fire · 哪吒三太子',
        portraitIndex: 2,
        color: '#f97316',
        quotes: [
          '"Great Sage! Let us see if your cloud can outrun my Wind-Fire Wheels!"',
          '"Burn away these demons in the sacred blaze of the Universe Ring!"'
        ],
        boons: [
          { id: 'nezha_strike', name: 'Fire Spear Strike', slot: 'Attack', desc: '[ATTACK] Staff strikes ignite foes with Scorching Flame dealing 60 burn damage over 3s.' },
          { id: 'nezha_ring', name: 'Universe Ring Zone', slot: 'Cast', desc: '[CAST] Cast zone launches a spinning golden chakram that ricochets between up to 6 foes for 35 damage.' },
          { id: 'nezha_dash', name: 'Wind-Fire Wheel Dash', slot: 'Dash', desc: '[DASH] Dash leaves a blazing trail of fire that burns any enemy stepping on it for 50 damage.' },
          { id: 'nezha_special', name: 'Fire-Tipped Pillar Slam', slot: 'Special', desc: '[SPECIAL] Ruyi Pillar smash causes a fiery eruption dealing 90 area damage and knocking enemies airborne.' },
          { id: 'nezha_ribbon', name: 'Red Armillary Sash', slot: 'Passive - Crowd Control', desc: '[PASSIVE] Attacks have a 30% chance to bind enemies with silk ribbons, immobilizing them for 2s.' },
          { id: 'nezha_speed', name: 'Wheels of Speed', slot: 'Passive - Mobility', desc: '[PASSIVE] Gain +35% permanent Movement Speed and +1 additional Somersault Dash charge.' },
          { id: 'nezha_combust', name: 'Blazing Combustion', slot: 'Passive - Damage', desc: '[PASSIVE] Striking burning enemies triggers fiery explosions dealing 45 bonus area damage.' },
          { id: 'nezha_spearvortex', name: 'Spearhead Vortex', slot: 'Passive - Special', desc: '[PASSIVE] Special attacks launch 2 bouncing fire chakrams alongside the pillar slam.' },
          { id: 'nezha_lotusbody', name: 'Lotus Reincarnation', slot: 'Passive - Survival', desc: '[PASSIVE] When Health drops below 30%, trigger a fiery shockwave pushing all enemies back and gain 4s invincibility.' },
          { id: 'nezha_inferno', name: 'Raging Firestorm', slot: 'Passive - Status', desc: '[PASSIVE] Burn ticks 50% faster and spreads automatically to adjacent enemies.' }
        ]
      },
      laojun: {
        name: 'Supreme Lord Laozi',
        title: 'Grand Master of Dao & Alchemy · 太上老君',
        portraitIndex: 3,
        color: '#ec4899',
        quotes: [
          '"My Bagua Crucible refined your golden eyes. Now let the true fire refine your Dao!"',
          '"Nine-turn golden elixirs hold the secrets of eternity. Wield the primordial flames wisely."'
        ],
        boons: [
          { id: 'laojun_strike', name: 'Samadhi Flame Strike', slot: 'Attack', desc: '[ATTACK] Staff attacks emit waves of Samadhi True Fire dealing 50 magic damage and melting enemy armor.' },
          { id: 'laojun_ring', name: 'Bagua Crucible Zone', slot: 'Cast', desc: '[CAST] Creates a rotating Bagua array that incinerates trapped enemies for 40 damage every 0.3s.' },
          { id: 'laojun_dash', name: 'Alchemy Mist Dash', slot: 'Dash', desc: '[DASH] Dashing leaves behind clouds of golden elixir smoke that blind enemies and increase your damage by 30%.' },
          { id: 'laojun_special', name: 'Nine-Turn Pillar Smash', slot: 'Special', desc: '[SPECIAL] Ruyi Pillar slam triggers a massive alchemical explosion dealing 110 Daoist damage.' },
          { id: 'laojun_elixir', name: 'Nine-Turn Golden Elixir', slot: 'Passive - Buff', desc: '[PASSIVE] Heavenly Peaches give +1 additional level up and heal you for full health upon consumption.' },
          { id: 'laojun_yin_yang', name: 'Yin-Yang Seal', slot: 'Passive - Damage', desc: '[PASSIVE] Alternating between Attack and Special increases your damage by +60% for 3 seconds.' },
          { id: 'laojun_qi_surge', name: 'Daoist Qi Overflow', slot: 'Passive - Qi', desc: '[PASSIVE] Casting spells costs 50% less Spirit Qi and casting an ability restores 10 HP.' },
          { id: 'laojun_furnace', name: 'Crucible Resonance', slot: 'Passive - Aura', desc: '[PASSIVE] Standing inside any cast zone grants +40% attack speed and +30% critical strike chance.' },
          { id: 'laojun_transmute', name: 'Golden Transmutation', slot: 'Passive - Gold', desc: '[PASSIVE] Enemies drop +70% more Jade Coins and +50% more Karma Spirit Ashes.' },
          { id: 'laojun_primordial', name: 'Primordial Dao Breath', slot: 'Passive - Ultimate', desc: '[PASSIVE] Havoc in Heaven awakening gauge fills +50% faster.' }
        ]
      },
      aoguang: {
        name: 'East Sea Dragon King Ao Guang',
        title: 'Sovereign of the Four Oceans · 东海龙王敖广',
        portraitIndex: 4,
        color: '#38bdf8',
        quotes: [
          '"You took my Sea-Stabilizing Needle (定海神针)! Now master the wrath of the abyssal seas!"',
          '"The four oceans surge at my command. Drown these wretched fiends in crushing tides!"'
        ],
        boons: [
          { id: 'aoguang_strike', name: 'Tidal Wave Strike', slot: 'Attack', desc: '[ATTACK] Staff strikes launch pressurized water blades that knock enemies backward for 40 damage.' },
          { id: 'aoguang_ring', name: 'Abyssal Maelstrom', slot: 'Cast', desc: '[CAST] Cast zone summons a violent whirlpool dragging all nearby enemies to its center while crushing them.' },
          { id: 'aoguang_dash', name: 'Tsunami Surge Dash', slot: 'Dash', desc: '[DASH] Dashing unleashes a tidal wave behind you, pushing enemies away and inflicting Drenched.' },
          { id: 'aoguang_special', name: 'Dragon Torrent Smash', slot: 'Special', desc: '[SPECIAL] Ruyi Pillar slam summons an azure water dragon surging forward dealing 85 frost-water damage.' },
          { id: 'aoguang_pressure', name: 'Crushing Oceanic Depth', slot: 'Passive - Knockback', desc: '[PASSIVE] Knocking enemies into chamber walls deals 80 bonus crushing impact damage.' },
          { id: 'aoguang_drench', name: 'Drench & Freeze', slot: 'Passive - Status', desc: '[PASSIVE] Drenched enemies move 35% slower and take +30% bonus damage from all lightning and ice effects.' },
          { id: 'aoguang_pearl', name: 'Dragon Pearl Radiance', slot: 'Passive - Projectiles', desc: '[PASSIVE] Automatically fire 2 seeking water pearls every 2s at nearby enemies for 35 damage.' },
          { id: 'aoguang_riptide', name: 'Riptide Vortex', slot: 'Passive - Attack', desc: '[PASSIVE] Staff attack combo finisher creates a localized whirlpool for 2s.' },
          { id: 'aoguang_leviathan', name: 'Roar of the Leviathan', slot: 'Passive - Stun', desc: '[PASSIVE] Special attacks have a 40% chance to freeze struck enemies solid in ice for 2s.' },
          { id: 'aoguang_sovereign', name: 'Oceanic Sovereignty', slot: 'Passive - Defense', desc: '[PASSIVE] Gain +20% movement speed and gain a shield equal to 15% of damage dealt.' }
        ]
      },
      bullking: {
        name: 'Bull Demon King',
        title: 'Great Sage Pacifying Heaven · 平天大圣牛魔王',
        portraitIndex: 5,
        color: '#ea580c',
        quotes: [
          '"Sworn Brother Wukong! Let us shatter the heavenly gates with brute demonic might!"',
          '"Feel the earth tremble beneath our hooves! No heavenly armor can withstand this power!"'
        ],
        boons: [
          { id: 'bull_strike', name: 'Titan Sunder Strike', slot: 'Attack', desc: '[ATTACK] Staff strikes deal +40% heavy physical damage and stagger enemies with seismic shockwaves.' },
          { id: 'bull_ring', name: 'Earthquake Zone', slot: 'Cast', desc: '[CAST] Cast zone causes ground fissures that repeatedly rupture for 50 heavy damage and shatter armor.' },
          { id: 'bull_dash', name: 'Earth-Breaker Dash', slot: 'Dash', desc: '[DASH] Dashing slams through enemies, dealing 45 impact damage and knocking small foes aside.' },
          { id: 'bull_special', name: 'Mountain Cleaver Slam', slot: 'Special', desc: '[SPECIAL] Ruyi Pillar slam splits the ground in a straight line dealing 120 colossal physical damage.' },
          { id: 'bull_ironhide', name: 'Demonic Ironhide', slot: 'Passive - Defense', desc: '[PASSIVE] Gain +50 Armor that absorbs damage before Health. Armor regenerates after 8s of taking no damage.' },
          { id: 'bull_stagger', name: 'Brutal Concussion', slot: 'Passive - Stun', desc: '[PASSIVE] Heavy strikes have a 25% chance to stun enemies for 1.5s.' },
          { id: 'bull_trample', name: 'Stampeding Fury', slot: 'Passive - Speed', desc: '[PASSIVE] Dashing through enemies grants +30% attack damage for 4s (stacks up to 3 times).' },
          { id: 'bull_brute', name: 'Primordial Strength', slot: 'Passive - Damage', desc: '[PASSIVE] All base attack and special damage is increased by a flat +35%.' },
          { id: 'bull_rage', name: 'Pacifying Heaven Rage', slot: 'Passive - Low HP', desc: '[PASSIVE] When Health is below 40%, attack speed and damage are boosted by +60%.' },
          { id: 'bull_boulder', name: 'Seismic Shock', slot: 'Passive - Area', desc: '[PASSIVE] Defeated foes erupt in stone shrapnel dealing 60 damage to surrounding enemies.' }
        ]
      },
      ironfan: {
        name: 'Princess Iron Fan',
        title: 'Mistress of the Gale & Plantain Fan · 铁扇公主',
        portraitIndex: 6,
        color: '#4ade80',
        quotes: [
          '"One wave of my Plantain Fan extinguishes volcanoes; two waves summon hurricanes!"',
          '"Sweep away the celestial sentinels like dust before the endless tempest!"'
        ],
        boons: [
          { id: 'ironfan_strike', name: 'Gale Blade Strike', slot: 'Attack', desc: '[ATTACK] Staff strikes release razor-sharp wind crescents that fly forward dealing 35 piercing wind damage.' },
          { id: 'ironfan_ring', name: 'Hurricane Vortex', slot: 'Cast', desc: '[CAST] Cast zone summons a howling cyclone pulling enemies into its center and deflecting projectiles.' },
          { id: 'ironfan_dash', name: 'Zephyr Slipstream Dash', slot: 'Dash', desc: '[DASH] Dashing creates a tailwind granting +50% movement speed for 2s and blowing away nearby foes.' },
          { id: 'ironfan_special', name: 'Plantain Fan Tempest', slot: 'Special', desc: '[SPECIAL] Special attacks unleash a massive tornado that travels across the room dealing 90 total damage.' },
          { id: 'ironfan_deflect', name: 'Gale Deflection', slot: 'Passive - Defense', desc: '[PASSIVE] All staff attacks and specials automatically reflect enemy projectiles back at attackers.' },
          { id: 'ironfan_razor', name: 'Wind Shear', slot: 'Passive - Damage', desc: '[PASSIVE] Wind attacks inflict Vulnerability, causing enemies to take +25% bonus damage from all sources.' },
          { id: 'ironfan_agility', name: 'Mistress of the Wind', slot: 'Passive - Dodge', desc: '[PASSIVE] Gain a passive +20% chance to completely dodge any incoming attack.' },
          { id: 'ironfan_tailwind', name: 'Whirlwind Acceleration', slot: 'Passive - Speed', desc: '[PASSIVE] Attack speed is increased by +30%.' },
          { id: 'ironfan_twister', name: 'Twin Tornadoes', slot: 'Passive - Special', desc: '[PASSIVE] Special attacks spawn two diverging tornadoes instead of one.' },
          { id: 'ironfan_tempest', name: 'Eye of the Storm', slot: 'Passive - Aura', desc: '[PASSIVE] You are permanently surrounded by a wind barrier that deals 20 damage/sec to adjacent enemies.' }
        ]
      },
      whitebone: {
        name: 'Lady White Bone',
        title: 'Mistress of Spectral Shadows · 白骨精',
        portraitIndex: 7,
        color: '#c084fc',
        quotes: [
          '"All mortal forms are merely fleeting shadows. Embrace the cold kiss of the grave."',
          '"Feast upon their souls, Wukong. Why serve heaven when you can rule eternity?"'
        ],
        boons: [
          { id: 'bone_strike', name: 'Soul Siphon Strike', slot: 'Attack', desc: '[ATTACK] Staff strikes leech life essence, granting 15% lifesteal and inflicting Curse of Decay.' },
          { id: 'bone_ring', name: 'Bone Spire Zone', slot: 'Cast', desc: '[CAST] Cast zone causes sharp skeletal spires to erupt from the ground, impaling enemies for 60 damage.' },
          { id: 'bone_dash', name: 'Phantom Mist Dash', slot: 'Dash', desc: '[DASH] Dashing turns you into intangible spectral mist, leaving behind a shadow decoy that draws enemy aggro.' },
          { id: 'bone_special', name: 'Necrotic Talon Slam', slot: 'Special', desc: '[SPECIAL] Ruyi Pillar slam summons gigantic skeletal claws dealing 85 necrotic damage.' },
          { id: 'bone_decay', name: 'Curse of Decay', slot: 'Passive - Status', desc: '[PASSIVE] Cursed enemies suffer 30 damage/sec and explode into necrotic mist upon death.' },
          { id: 'bone_drain', name: 'Soul Harvest', slot: 'Passive - Sustain', desc: '[PASSIVE] Slaying an enemy permanently increases your Max HP by +2 (up to +60 per run).' },
          { id: 'bone_phantom', name: 'Skeletal Phantasm', slot: 'Passive - Minions', desc: '[PASSIVE] Defeated enemies have a 30% chance to rise as friendly skeletal minions fighting for you.' },
          { id: 'bone_shadow_rend', name: 'Shadow Rend', slot: 'Passive - Crit', desc: '[PASSIVE] Striking enemies from behind or while they attack a decoy deals guaranteed +100% Critical Damage.' },
          { id: 'bone_armor', name: 'Bone Carapace', slot: 'Passive - Survival', desc: '[PASSIVE] When taking fatal damage, survive with 1 HP and become invincible for 3s (once per chamber).' },
          { id: 'bone_torment', name: 'Eternal Torment', slot: 'Passive - Damage', desc: '[PASSIVE] Enemies afflicted with status effects take +40% bonus damage from your attacks.' }
        ]
      },
      yanluo: {
        name: 'King Yanluo',
        title: 'Sovereign of Diyu Netherworld · 阎罗王',
        portraitIndex: 8,
        color: '#ef4444',
        quotes: [
          '"Your name was struck from the Book of Life and Death! Now strike down the rest!"',
          '"The Eighteen Levels of Hell hold no chains that can bind the Great Sage!"'
        ],
        boons: [
          { id: 'yanluo_strike', name: 'Death Ledger Strike', slot: 'Attack', desc: '[ATTACK] Staff strikes mark enemies with the Death Rune; marked enemies take 70 delayed nether damage.' },
          { id: 'yanluo_ring', name: 'Karmic Chains Zone', slot: 'Cast', desc: '[CAST] Cast zone tethers enemies with nether chains, linking their damage so all linked foes take 50% shared damage.' },
          { id: 'yanluo_dash', name: 'Diyu Ghostfire Dash', slot: 'Dash', desc: '[DASH] Dashing leaves a trail of green ghostfire that inflicts Nether Doom on enemies.' },
          { id: 'yanluo_special', name: 'Soul Reaping Slam', slot: 'Special', desc: '[SPECIAL] Ruyi Pillar slam reaps the souls of foes, instantly executing non-boss enemies below 15% HP.' },
          { id: 'yanluo_doom', name: 'Nether Doom', slot: 'Passive - Status', desc: '[PASSIVE] Nether Doom triggers after 3s, dealing 120 massive nether damage to the afflicted target.' },
          { id: 'yanluo_execution', name: 'Judge\'s Decree', slot: 'Passive - Damage', desc: '[PASSIVE] All damage against Bosses and Elites is increased by +35%.' },
          { id: 'yanluo_soul_gem', name: 'Soul Jar Collector', slot: 'Passive - Currency', desc: '[PASSIVE] Vanquished enemies yield +100% more Karma Spirit Ashes for the 72 Transformations altar.' },
          { id: 'yanluo_ghost_gate', name: 'Ghost Gate Rift', slot: 'Passive - Special', desc: '[PASSIVE] Special attacks open a nether portal firing 4 seeking ghost skulls for 30 damage each.' },
          { id: 'yanluo_retribution', name: 'Karmic Retaliation', slot: 'Passive - Retaliation', desc: '[PASSIVE] When struck, reflect 200% of the damage back to the attacker as nether energy.' },
          { id: 'yanluo_sovereign', name: 'Lord of the Dead', slot: 'Passive - Stat', desc: '[PASSIVE] Gain +10% damage for each chamber cleared without taking damage (up to +50%).' }
        ]
      },
      change: {
        name: 'Chang\'e & Jade Rabbit',
        title: 'Celestial Moon Goddess · 嫦娥与玉兔',
        portraitIndex: 9,
        color: '#93c5fd',
        quotes: [
          '"The cold radiance of the Moon Palace guides your path through the starry void."',
          '"My Jade Rabbit has ground the herb of immortality. Drink of the lunar nectar!"'
        ],
        boons: [
          { id: 'change_strike', name: 'Moonlight Shard Strike', slot: 'Attack', desc: '[ATTACK] Staff strikes release crescent moonbeams that freeze foes for 1.2s and deal 35 frost damage.' },
          { id: 'change_ring', name: 'Lunar Glaze Zone', slot: 'Cast', desc: '[CAST] Cast zone creates a serene moon mirror that reflects all incoming attacks and chills enemies.' },
          { id: 'change_dash', name: 'Moonlit Phase Dash', slot: 'Dash', desc: '[DASH] Dashing phases through enemies, freezing all foes in your path for 1.5s.' },
          { id: 'change_special', name: 'Selenite Orbital Slam', slot: 'Special', desc: '[SPECIAL] Ruyi Pillar slam summons 3 glowing moon orbs that orbit Wukong, shielding and damaging nearby foes.' },
          { id: 'change_rabbit', name: 'Jade Rabbit Mortar', slot: 'Passive - Potion', desc: '[PASSIVE] Every 10s, the Jade Rabbit throws an immortal medicine flask healing you for 15 HP and 15 Qi.' },
          { id: 'change_frostbite', name: 'Deep Frostbite', slot: 'Passive - Status', desc: '[PASSIVE] Frozen enemies take +50% bonus damage from all physical and staff attacks.' },
          { id: 'change_moonbeam', name: 'Celestial Moonbeam', slot: 'Passive - Combat', desc: '[PASSIVE] Critical hits call down a vertical orbital moonbeam dealing 90 radiant area damage.' },
          { id: 'change_glaze', name: 'Lunar Mirror Armor', slot: 'Passive - Defense', desc: '[PASSIVE] Gain a lunar shield that blocks 1 instance of damage every 15 seconds.' },
          { id: 'change_radiance', name: 'Selenitic Glow', slot: 'Passive - Qi', desc: '[PASSIVE] Spending Spirit Qi releases a radiant nova freezing all nearby enemies for 1.5s.' },
          { id: 'change_eclipse', name: 'Eternal Eclipse', slot: 'Passive - Ultimate', desc: '[PASSIVE] During Havoc in Heaven, the entire screen is bathed in moonlight, chilling and slowing all foes by 60%.' }
        ]
      }
    };

    // ==========================================
    // GAME ENGINE & CANVAS RENDERING
    // ==========================================
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // Game State
    const gameState = {
      chamberIndex: 1,
      totalChambers: 100,
      biome: 1, // 1: Flower-Fruit Mountain, 2: Diyu Hell, 3: South Heaven Gate, 4: Peach Orchard, 5: Lingxiao Palace
      chamberCleared: false,
      chamberType: 'normal', // normal, elite, shop, boss, pom
      gold: 0,
      ashes: 0,
      peachesEaten: 0,
      enemiesKilled: 0,
      boonsCount: 0,
      screenShake: 0,
      keys: {},
      mouse: { x: 0, y: 0, isDown: false, rightDown: false },
      camera: { x: 0, y: 0 },
      isPaused: false,
      activeModal: null
    };

    // Meta Upgrade Save State (72 Transformations)
    const metaUpgrades = {
      stone_monkey: 0,    // +Max HP
      golden_eyes: 0,     // +Crit
      somersault: 0,      // +Dashes
      hair_clones: 0,     // +Clone chance
      qi_circulation: 0,  // +Qi & Regen
      nirvana_body: 0     // +Death Defiance
    };

    // Keyboard & Mouse Listeners
    window.addEventListener('keydown', (e) => {
      gameState.keys[e.key.toLowerCase()] = true;
      if (e.key === ' ' || e.key === 'Shift') {
        player.performDash();
      }
      if (e.key.toLowerCase() === 'e') {
        player.performCast();
      }
      if (e.key.toLowerCase() === 'q') {
        player.performSpecial();
      }
      if (e.key.toLowerCase() === 'r' || e.key.toLowerCase() === 'f') {
        player.triggerAwakening();
      }
    });

    window.addEventListener('keyup', (e) => {
      gameState.keys[e.key.toLowerCase()] = false;
    });

    window.addEventListener('mousemove', (e) => {
      gameState.mouse.x = e.clientX;
      gameState.mouse.y = e.clientY;
    });

    window.addEventListener('mousedown', (e) => {
      if (gameState.isPaused) return;
      if (e.button === 0) {
        gameState.mouse.isDown = true;
        player.performAttack();
      } else if (e.button === 2) {
        gameState.mouse.rightDown = true;
        player.performSpecial();
      }
    });

    window.addEventListener('mouseup', (e) => {
      if (e.button === 0) gameState.mouse.isDown = false;
      if (e.button === 2) gameState.mouse.rightDown = false;
    });

    window.addEventListener('contextmenu', (e) => e.preventDefault());

    // ==========================================
    // PLAYER CLASS: SUN WUKONG (MONKEY KING)
    // ==========================================
    class Player {
      constructor() {
        this.x = 0;
        this.y = 0;
        this.vx = 0;
        this.vy = 0;
        this.facing = 1; // 1 = right, -1 = left
        this.radius = 26;
        this.baseSpeed = 250;
        this.speed = 250;
        this.hp = 100;
        this.maxHp = 100;
        this.qi = 50;
        this.maxQi = 50;
        this.qiRegen = 1.5;
        this.armor = 0;

        // Combat Mechanics
        this.comboIndex = 0;
        this.comboTimer = 0;
        this.isAttacking = false;
        this.attackDuration = 0;
        this.attackMaxDuration = 0.18;
        this.attackAngle = 0;
        this.attackCooldown = 0;

        // Special Attack
        this.isSpecialActive = false;
        this.specialCooldown = 0;
        this.specialDuration = 0;

        // Somersault Cloud Dash
        this.isDashing = false;
        this.dashDuration = 0;
        this.dashCooldown = 0;
        this.dashCharges = 2;
        this.maxDashCharges = 2;
        this.dashRechargeTimer = 0;
        this.dashTrail = [];

        // Cast Circle
        this.castActive = null;
        this.castCooldown = 0;

        // Awakened Form (Havoc in Heaven / 法天象地)
        this.awakenGauge = 0;
        this.maxAwakenGauge = 100;
        this.isAwakened = false;
        this.awakenDuration = 0;

        // Death Defiance Lives
        this.lives = 1;
        this.maxLives = 1;

        // Equipped Boons: slot -> { id, name, godKey, level, desc, ... }
        this.boons = {
          attack: null,
          special: null,
          cast: null,
          dash: null,
          hex: null,
          passives: []
        };
      }

      resetForRun() {
        this.applyMetaUpgrades();
        this.hp = this.maxHp;
        this.qi = this.maxQi;
        this.lives = this.maxLives;
        this.awakenGauge = 0;
        this.isAwakened = false;
        this.boons = {
          attack: null,
          special: null,
          cast: null,
          dash: null,
          hex: null,
          passives: []
        };
        this.x = 0;
        this.y = 0;
        this.vx = 0;
        this.vy = 0;
        this.castActive = null;
        this.dashTrail = [];
        updateHUD();
      }

      applyMetaUpgrades() {
        this.maxHp = 100 + metaUpgrades.stone_monkey * 25;
        this.maxQi = 50 + metaUpgrades.qi_circulation * 15;
        this.qiRegen = 1.5 + metaUpgrades.qi_circulation * 0.8;
        this.maxDashCharges = 2 + metaUpgrades.somersault;
        this.dashCharges = this.maxDashCharges;
        this.maxLives = 1 + metaUpgrades.nirvana_body;
        this.lives = this.maxLives;
      }

      hasBoon(id) {
        if (this.boons.attack && this.boons.attack.id === id) return true;
        if (this.boons.special && this.boons.special.id === id) return true;
        if (this.boons.cast && this.boons.cast.id === id) return true;
        if (this.boons.dash && this.boons.dash.id === id) return true;
        if (this.boons.hex && this.boons.hex.id === id) return true;
        return this.boons.passives.some(b => b.id === id);
      }

      getBoonLevel(id) {
        if (this.boons.attack && this.boons.attack.id === id) return this.boons.attack.level || 1;
        if (this.boons.special && this.boons.special.id === id) return this.boons.special.level || 1;
        if (this.boons.cast && this.boons.cast.id === id) return this.boons.cast.level || 1;
        if (this.boons.dash && this.boons.dash.id === id) return this.boons.dash.level || 1;
        if (this.boons.hex && this.boons.hex.id === id) return this.boons.hex.level || 1;
        const p = this.boons.passives.find(b => b.id === id);
        return p ? (p.level || 1) : 1;
      }

      update(dt) {
        // Handle Qi Regeneration
        if (this.qi < this.maxQi) {
          this.qi = Math.min(this.maxQi, this.qi + this.qiRegen * dt);
        }

        // Handle Dash Recharge
        if (this.dashCharges < this.maxDashCharges) {
          this.dashRechargeTimer += dt;
          if (this.dashRechargeTimer >= 0.75) {
            this.dashCharges++;
            this.dashRechargeTimer = 0;
          }
        }

        // Handle Awakening Form Duration
        if (this.isAwakened) {
          this.awakenDuration -= dt;
          if (this.awakenDuration <= 0) {
            this.isAwakened = false;
            this.awakenGauge = 0;
          }
        }

        // Cooldowns
        if (this.attackCooldown > 0) this.attackCooldown -= dt;
        if (this.specialCooldown > 0) this.specialCooldown -= dt;
        if (this.castCooldown > 0) this.castCooldown -= dt;
        if (this.dashCooldown > 0) this.dashCooldown -= dt;

        // Combo Reset Window
        if (this.comboTimer > 0) {
          this.comboTimer -= dt;
          if (this.comboTimer <= 0) {
            this.comboIndex = 0;
          }
        }

        // Mouse facing direction
        const worldMouseX = gameState.mouse.x - canvas.width / 2 + this.x;
        if (worldMouseX < this.x) {
          this.facing = -1;
        } else {
          this.facing = 1;
        }

        // Movement Input
        let moveX = 0;
        let moveY = 0;
        if (gameState.keys['w'] || gameState.keys['arrowup']) moveY -= 1;
        if (gameState.keys['s'] || gameState.keys['arrowdown']) moveY += 1;
        if (gameState.keys['a'] || gameState.keys['arrowleft']) moveX -= 1;
        if (gameState.keys['d'] || gameState.keys['arrowright']) moveX += 1;

        const len = Math.hypot(moveX, moveY);
        if (len > 0) {
          moveX /= len;
          moveY /= len;
        }

        // Dashing Movement
        if (this.isDashing) {
          this.dashDuration -= dt;
          if (this.dashDuration <= 0) {
            this.isDashing = false;
          }
          // Spawn cloud particles
          this.dashTrail.push({
            x: this.x,
            y: this.y,
            alpha: 1.0,
            radius: 24
          });
        } else {
          // Normal Movement
          let curSpeed = this.baseSpeed;
          if (this.isAwakened) curSpeed *= 1.4;
          if (this.hasBoon('nezha_speed')) curSpeed *= (1 + 0.35 * this.getBoonLevel('nezha_speed'));
          if (this.hasBoon('ironfan_tailwind')) curSpeed *= 1.25;

          this.vx = moveX * curSpeed;
          this.vy = moveY * curSpeed;
          this.x += this.vx * dt;
          this.y += this.vy * dt;
        }

        // Chamber Boundary Clamping
        const bound = 650;
        this.x = Math.max(-bound, Math.min(bound, this.x));
        this.y = Math.max(-bound, Math.min(bound, this.y));

        // Update Dash Trail Alpha
        for (let i = this.dashTrail.length - 1; i >= 0; i--) {
          this.dashTrail[i].alpha -= dt * 3.5;
          if (this.dashTrail[i].alpha <= 0) {
            this.dashTrail.splice(i, 1);
          }
        }

        // Update Active Cast Zone
        if (this.castActive) {
          this.castActive.duration -= dt;
          this.castActive.tickTimer += dt;
          if (this.castActive.tickTimer >= 0.25) {
            this.castActive.tickTimer = 0;
            this.triggerCastTick();
          }
          if (this.castActive.duration <= 0) {
            this.castActive = null;
          }
        }

        // Auto Attack while mouse held down
        if (gameState.mouse.isDown && !this.isAttacking && this.attackCooldown <= 0) {
          this.performAttack();
        }

        // Update Attack Animation
        if (this.isAttacking) {
          this.attackDuration -= dt;
          if (this.attackDuration <= 0) {
            this.isAttacking = false;
          }
        }

        // Update Special Animation
        if (this.isSpecialActive) {
          this.specialDuration -= dt;
          if (this.specialDuration <= 0) {
            this.isSpecialActive = false;
          }
        }
      }

      performAttack() {
        if (this.isDashing || this.isAttacking || this.attackCooldown > 0) return;

        sound.playStaffSwing();
        this.isAttacking = true;
        this.attackDuration = this.attackMaxDuration;
        this.attackCooldown = 0.16;

        // Calculate attack angle towards mouse
        const worldMouseX = gameState.mouse.x - canvas.width / 2 + this.x;
        const worldMouseY = gameState.mouse.y - canvas.height / 2 + this.y;
        this.attackAngle = Math.atan2(worldMouseY - this.y, worldMouseX - this.x);

        // 3-Hit Combo Logic
        this.comboIndex = (this.comboIndex + 1) % 3;
        this.comboTimer = 0.6; // Combo reset window

        let baseDmg = 40;
        let reach = 115;
        let arc = Math.PI * 0.8;

        if (this.comboIndex === 2) {
          // 3rd Hit: Colossal Overhead Slam
          baseDmg = 90;
          reach = 150;
          arc = Math.PI * 0.95;
          sound.playStaffSmash();
          createScreenShake(7);
        } else {
          sound.playStaffHit();
        }

        if (this.isAwakened) {
          baseDmg *= 2.2;
          reach *= 1.6;
        }

        // Apply Boons Modifiers
        if (this.boons.attack) {
          const lvl = this.boons.attack.level || 1;
          baseDmg *= (1 + 0.3 * (lvl - 1));
          this.procAttackBoon(this.boons.attack.id, lvl);
        }

        // Spawn Visual Staff Sweep Arc
        fxList.push(new AnimatedAttackSweep(this.x, this.y, this.attackAngle, reach, this.comboIndex === 2 ? '#facc15' : '#ef4444'));

        // Hit Detection against Enemies
        let hitAny = false;
        enemies.forEach(enemy => {
          if (!enemy.alive) return;
          const dist = Math.hypot(enemy.x - this.x, enemy.y - this.y);
          if (dist <= reach + enemy.radius) {
            const angleToEnemy = Math.atan2(enemy.y - this.y, enemy.x - this.x);
            let angleDiff = Math.abs(this.attackAngle - angleToEnemy);
            while (angleDiff > Math.PI) angleDiff = Math.abs(angleDiff - Math.PI * 2);

            if (angleDiff <= arc / 2) {
              hitAny = true;
              let crit = Math.random() < (0.15 + (metaUpgrades.golden_eyes * 0.08) + (this.hasBoon('erlang_truesight') ? 0.25 : 0));
              let finalDmg = baseDmg * (crit ? 2.5 : 1.0);

              enemy.takeDamage(finalDmg, crit);

              // Knockback
              const knock = (this.comboIndex === 2 ? 240 : 130);
              enemy.vx += Math.cos(angleToEnemy) * knock;
              enemy.vy += Math.sin(angleToEnemy) * knock;

              // Fill Awakening Gauge
              this.awakenGauge = Math.min(this.maxAwakenGauge, this.awakenGauge + (crit ? 5 : 2.5));
            }
          }
        });

        if (hitAny) {
          sound.playStaffHit();
        }
      }

      procAttackBoon(id, level) {
        if (id === 'erlang_strike') {
          sound.playLightning();
          enemies.slice(0, 3).forEach(e => {
            if (e.alive) {
              fxList.push(new AnimatedLightningStrike(e.x, e.y));
              e.takeDamage(45 * level, false);
            }
          });
        } else if (id === 'nezha_strike') {
          sound.playFire();
          enemies.forEach(e => {
            if (e.alive && Math.hypot(e.x - this.x, e.y - this.y) < 160) {
              e.applyBurn(60 * level, 3);
            }
          });
        } else if (id === 'laojun_strike') {
          sound.playFire();
          fxList.push(new AnimatedFireExplosion(this.x + Math.cos(this.attackAngle)*80, this.y + Math.sin(this.attackAngle)*80, 75));
        } else if (id === 'aoguang_strike') {
          fxList.push(new AnimatedWaterWave(this.x, this.y, this.attackAngle));
        } else if (id === 'change_strike') {
          enemies.forEach(e => {
            if (e.alive && Math.hypot(e.x - this.x, e.y - this.y) < 140) {
              e.applyFreeze(1.5);
            }
          });
        }
      }

      performSpecial() {
        if (this.specialCooldown > 0 || this.isDashing) return;
        this.specialCooldown = 1.0;
        this.isSpecialActive = true;
        this.specialDuration = 0.35;

        sound.playStaffSmash();
        createScreenShake(8);

        const worldMouseX = gameState.mouse.x - canvas.width / 2 + this.x;
        const worldMouseY = gameState.mouse.y - canvas.height / 2 + this.y;
        const angle = Math.atan2(worldMouseY - this.y, worldMouseX - this.x);

        let baseDmg = 95;
        let reach = 200;
        if (this.boons.special) {
          const lvl = this.boons.special.level || 1;
          baseDmg *= (1 + 0.35 * (lvl - 1));
        }

        // Spawn Colossal Ruyi Pillar & Shockwave
        fxList.push(new Shockwave(this.x, this.y, reach, '#facc15'));

        enemies.forEach(enemy => {
          if (!enemy.alive) return;
          const dist = Math.hypot(enemy.x - this.x, enemy.y - this.y);
          if (dist <= reach + enemy.radius) {
            enemy.takeDamage(baseDmg, true);
            const knockAngle = Math.atan2(enemy.y - this.y, enemy.x - this.x);
            enemy.vx += Math.cos(knockAngle) * 340;
            enemy.vy += Math.sin(knockAngle) * 340;
          }
        });

        // Deflect incoming projectiles
        projectiles.forEach(p => {
          if (p.isEnemy && Math.hypot(p.x - this.x, p.y - this.y) < reach) {
            p.isEnemy = false;
            p.vx = -p.vx * 1.5;
            p.vy = -p.vy * 1.5;
          }
        });
      }

      performCast() {
        if (this.castCooldown > 0 || this.qi < 15) return;
        this.qi -= 15;
        this.castCooldown = 0.5;

        sound.playJadeChime();

        const worldMouseX = gameState.mouse.x - canvas.width / 2 + this.x;
        const worldMouseY = gameState.mouse.y - canvas.height / 2 + this.y;

        this.castActive = {
          x: worldMouseX,
          y: worldMouseY,
          radius: 125,
          duration: 6.0,
          tickTimer: 0,
          angle: 0
        };

        fxList.push(new Shockwave(worldMouseX, worldMouseY, 125, '#a855f7'));
      }

      triggerCastTick() {
        if (!this.castActive) return;
        enemies.forEach(enemy => {
          if (!enemy.alive) return;
          const dist = Math.hypot(enemy.x - this.castActive.x, enemy.y - this.castActive.y);
          if (dist <= this.castActive.radius + enemy.radius) {
            let dmg = 25;
            if (this.boons.cast) {
              dmg *= (1 + 0.3 * (this.boons.cast.level || 1));
            }
            enemy.takeDamage(dmg, false);
            enemy.applySlow(0.5, 0.4);
          }
        });
      }

      performDash() {
        if (this.isDashing || this.dashCharges <= 0) return;
        this.dashCharges--;
        this.isDashing = true;
        this.dashDuration = 0.22;
        sound.playDash();

        let moveX = 0;
        let moveY = 0;
        if (gameState.keys['w'] || gameState.keys['arrowup']) moveY -= 1;
        if (gameState.keys['s'] || gameState.keys['arrowdown']) moveY += 1;
        if (gameState.keys['a'] || gameState.keys['arrowleft']) moveX -= 1;
        if (gameState.keys['d'] || gameState.keys['arrowright']) moveX += 1;

        if (moveX === 0 && moveY === 0) {
          const worldMouseX = gameState.mouse.x - canvas.width / 2 + this.x;
          const worldMouseY = gameState.mouse.y - canvas.height / 2 + this.y;
          const ang = Math.atan2(worldMouseY - this.y, worldMouseX - this.x);
          moveX = Math.cos(ang);
          moveY = Math.sin(ang);
        } else {
          const l = Math.hypot(moveX, moveY);
          moveX /= l;
          moveY /= l;
        }

        const dashSpeed = 700;
        this.vx = moveX * dashSpeed;
        this.vy = moveY * dashSpeed;
        this.x += this.vx * 0.22;
        this.y += this.vy * 0.22;

        // Dash Boon Procs
        if (this.boons.dash) {
          const lvl = this.boons.dash.level || 1;
          if (this.boons.dash.id === 'nezha_dash') {
            fxList.push(new AnimatedFireExplosion(this.x, this.y, 80));
          } else if (this.boons.dash.id === 'aoguang_dash') {
            fxList.push(new AnimatedWaterWave(this.x, this.y, Math.atan2(moveY, moveX)));
          } else if (this.boons.dash.id === 'erlang_dash') {
            fxList.push(new AnimatedLightningStrike(this.x, this.y));
          }
        }
      }

      triggerAwakening() {
        if (this.awakenGauge < this.maxAwakenGauge || this.isAwakened) return;
        this.isAwakened = true;
        this.awakenDuration = 10.0;
        sound.playAwaken();
        createScreenShake(15);
        fxList.push(new Shockwave(this.x, this.y, 260, '#facc15'));
      }

      takeDamage(amount) {
        if (this.isDashing || this.isAwakened) return;

        // Armor absorption
        if (this.armor > 0) {
          const absorbed = Math.min(this.armor, amount);
          this.armor -= absorbed;
          amount -= absorbed;
          if (amount <= 0) return;
        }

        this.hp -= amount;
        createScreenShake(5);

        // Floating Damage Text
        floatingTexts.push(new FloatingText(this.x, this.y - 30, `-${Math.round(amount)}`, '#ef4444'));

        if (this.hp <= 0) {
          if (this.lives > 0) {
            this.lives--;
            this.hp = Math.round(this.maxHp * 0.6);
            sound.playJadeChime();
            createScreenShake(10);
            fxList.push(new Shockwave(this.x, this.y, 200, '#4ade80'));
            floatingTexts.push(new FloatingText(this.x, this.y - 45, 'REBIRTH (金身复活)!', '#4ade80'));
          } else {
            handleGameOver(false);
          }
        }
        updateHUD();
      }

      draw(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);

        // Draw Dash Trail (Somersault Cloud Wisps)
        this.dashTrail.forEach(t => {
          ctx.save();
          ctx.beginPath();
          ctx.arc(t.x - this.x, t.y - this.y, t.radius, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(255, 245, 200, ${t.alpha * 0.45})`;
          ctx.fill();
          ctx.restore();
        });

        // Draw Cast Circle if active
        if (this.castActive) {
          ctx.save();
          ctx.translate(this.castActive.x - this.x, this.castActive.y - this.y);
          this.castActive.angle += 0.02;
          ctx.rotate(this.castActive.angle);

          // Bagua / Runic Circle
          ctx.beginPath();
          ctx.arc(0, 0, this.castActive.radius, 0, Math.PI * 2);
          ctx.strokeStyle = 'rgba(168, 85, 247, 0.85)';
          ctx.lineWidth = 3;
          ctx.stroke();

          ctx.beginPath();
          ctx.arc(0, 0, this.castActive.radius * 0.6, 0, Math.PI * 2);
          ctx.strokeStyle = 'rgba(250, 204, 21, 0.7)';
          ctx.lineWidth = 2;
          ctx.stroke();

          ctx.beginPath();
          ctx.arc(0, 0, 20, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
          ctx.fill();

          ctx.restore();
        }

        // Draw Monkey King Body
        const heroImg = loadedImages['hero'];
        if (heroImg && heroImg.complete) {
          // Sprite sheet is 8 cols x 7 rows
          const cols = 8;
          const rows = 7;
          const cellW = 1024 / cols;
          const cellH = 1024 / rows;

          let r = 0;
          let c = 0;

          if (this.isAwakened) {
            r = 5; // Awakened row
            c = Math.floor((Date.now() / 90) % 8);
          } else if (this.isDashing) {
            r = 4; // Cloud dash row
            c = Math.floor((Date.now() / 70) % 8);
          } else if (this.isAttacking) {
            if (this.comboIndex === 2) {
              r = 3; // Smash row
            } else {
              r = 2; // Sweep swing row
            }
            c = Math.min(7, Math.floor((1 - this.attackDuration / this.attackMaxDuration) * 8));
          } else if (Math.hypot(this.vx, this.vy) > 10) {
            r = 1; // Walk row
            c = Math.floor((Date.now() / 100) % 8);
          } else {
            r = 0; // Idle row
            c = Math.floor((Date.now() / 120) % 8);
          }

          const scale = this.isAwakened ? 1.5 : 1.1;
          const drawW = 96 * scale;
          const drawH = 96 * scale;

          ctx.save();
          if (this.facing === -1) {
            ctx.scale(-1, 1);
          }

          ctx.drawImage(heroImg, c * cellW, r * cellH, cellW, cellH, -drawW/2, -drawH/2 - 8, drawW, drawH);
          ctx.restore();
        } else {
          // Fallback Procedural Draw
          ctx.beginPath();
          ctx.arc(0, 0, this.radius, 0, Math.PI * 2);
          ctx.fillStyle = '#f59e0b';
          ctx.fill();
          ctx.strokeStyle = '#fff';
          ctx.lineWidth = 2;
          ctx.stroke();
        }

        ctx.restore();
      }
    }

    const player = new Player();

    // ==========================================
    // ENEMY & BOSS ENGINE
    // ==========================================
    const ENEMY_TYPES = {
      demon_grunt: { name: 'Mountain Demon Ape (山妖猿)', maxHp: 70, speed: 115, radius: 26, color: '#d97706', spriteRow: 4, behavior: 'swarmer' },
      ape_slinger: { name: 'Heavenly Archer (天弓兵)', maxHp: 55, speed: 130, radius: 24, color: '#38bdf8', spriteRow: 1, behavior: 'shooter' },
      nether_shade: { name: 'Diyu Nether Ghost (地府幽灵)', maxHp: 80, speed: 100, radius: 26, color: '#10b981', spriteRow: 5, behavior: 'ghost' },
      heavenly_soldier: { name: 'Heavenly Spear Guard (天庭神兵)', maxHp: 150, speed: 105, radius: 28, color: '#facc15', spriteRow: 0, behavior: 'shield_soldier' },
      daoist_golem: { name: 'Bagua Daoist Automaton (八卦守卫)', maxHp: 240, speed: 70, radius: 36, color: '#d97706', spriteRow: 3, behavior: 'smasher' },

      // Bosses
      boss_aoguang: { name: 'East Sea Dragon King Ao Guang (东海龙王·敖广)', isBoss: true, maxHp: 2900, speed: 120, radius: 64, color: '#0284c7', spriteRow: 2, behavior: 'boss_aoguang' },
      boss_yanluo: { name: 'King Yanluo & Judge Cui (幽冥阎罗王)', isBoss: true, maxHp: 5400, speed: 110, radius: 64, color: '#b91c1c', spriteRow: 5, behavior: 'boss_yanluo' },
      boss_nezha: { name: 'Third Lotus Prince Nezha (三太子哪吒)', isBoss: true, maxHp: 8600, speed: 165, radius: 58, color: '#ea580c', spriteRow: 1, behavior: 'boss_nezha' },
      boss_erlang: { name: 'Erlang Shen & Celestial Hound (二郎神杨戬与哮天犬)', isBoss: true, maxHp: 12800, speed: 150, radius: 65, color: '#ca8a04', spriteRow: 2, behavior: 'boss_erlang' },
      boss_jade_emperor: { name: 'Supreme Jade Emperor & Laozi Crucible (玉皇大帝与太上老君)', isBoss: true, maxHp: 25000, speed: 125, radius: 75, color: '#f59e0b', spriteRow: 2, behavior: 'boss_final' }
    };

    class Enemy {
      constructor(typeKey, x, y) {
        this.typeKey = typeKey;
        const def = ENEMY_TYPES[typeKey] || ENEMY_TYPES['demon_grunt'];
        this.name = def.name;
        this.isBoss = def.isBoss || false;
        this.maxHp = def.maxHp * (1 + (gameState.chamberIndex * 0.04));
        this.hp = this.maxHp;
        this.speed = def.speed;
        this.radius = def.radius;
        this.color = def.color;
        this.spriteRow = def.spriteRow || 0;
        this.behavior = def.behavior;
        this.x = x;
        this.y = y;
        this.vx = 0;
        this.vy = 0;
        this.facing = 1;
        this.alive = true;
        this.attackTimer = 0;
        this.burnTimer = 0;
        this.burnDmg = 0;
        this.freezeTimer = 0;
        this.slowTimer = 0;
        this.slowAmount = 0;
      }

      applyBurn(dmg, duration) {
        this.burnDmg = dmg;
        this.burnTimer = duration;
      }

      applyFreeze(duration) {
        this.freezeTimer = duration;
      }

      applySlow(amount, duration) {
        this.slowAmount = amount;
        this.slowTimer = duration;
      }

      takeDamage(amount, isCrit = false) {
        this.hp -= amount;
        floatingTexts.push(new FloatingText(this.x, this.y - 20, Math.round(amount), isCrit ? '#facc15' : '#ffffff', isCrit ? 18 : 13));

        if (this.hp <= 0 && this.alive) {
          this.alive = false;
          gameState.enemiesKilled++;
          gameState.gold += Math.floor(Math.random() * 8) + (this.isBoss ? 80 : 5);
          gameState.ashes += Math.floor(Math.random() * 4) + (this.isBoss ? 40 : 2);

          // Gong sound for Boss/Elite
          if (this.isBoss) {
            sound.playGong();
          }

          updateHUD();
        }
      }

      update(dt) {
        if (!this.alive) return;

        // Status Effects
        if (this.burnTimer > 0) {
          this.burnTimer -= dt;
          this.hp -= (this.burnDmg * dt);
          if (this.hp <= 0) this.takeDamage(1);
        }

        if (this.freezeTimer > 0) {
          this.freezeTimer -= dt;
          return;
        }

        let speedMod = 1.0;
        if (this.slowTimer > 0) {
          this.slowTimer -= dt;
          speedMod *= (1 - this.slowAmount);
        }

        const distToPlayer = Math.hypot(player.x - this.x, player.y - this.y);
        const angleToPlayer = Math.atan2(player.y - this.y, player.x - this.x);

        if (player.x < this.x) {
          this.facing = -1;
        } else {
          this.facing = 1;
        }

        this.attackTimer += dt;

        // Behavior Logic
        if (this.behavior === 'swarmer' || this.behavior === 'charger') {
          if (distToPlayer > this.radius + player.radius) {
            this.vx = Math.cos(angleToPlayer) * this.speed * speedMod;
            this.vy = Math.sin(angleToPlayer) * this.speed * speedMod;
          } else {
            // Melee Attack
            if (this.attackTimer >= 1.2) {
              this.attackTimer = 0;
              player.takeDamage(this.isBoss ? 35 : 16);
            }
          }
        } else if (this.behavior === 'shooter') {
          if (distToPlayer < 240) {
            this.vx = -Math.cos(angleToPlayer) * this.speed * 0.8 * speedMod;
            this.vy = -Math.sin(angleToPlayer) * this.speed * 0.8 * speedMod;
          } else if (distToPlayer > 360) {
            this.vx = Math.cos(angleToPlayer) * this.speed * speedMod;
            this.vy = Math.sin(angleToPlayer) * this.speed * speedMod;
          } else {
            this.vx *= 0.8;
            this.vy *= 0.8;
          }

          if (this.attackTimer >= 2.0) {
            this.attackTimer = 0;
            projectiles.push(new Projectile(this.x, this.y, Math.cos(angleToPlayer)*270, Math.sin(angleToPlayer)*270, 16, '#38bdf8', true));
          }
        } else if (this.isBoss) {
          // Boss Multi-attack Pattern
          this.vx = Math.cos(angleToPlayer) * this.speed * 0.6 * speedMod;
          this.vy = Math.sin(angleToPlayer) * this.speed * 0.6 * speedMod;

          if (this.attackTimer >= 2.2) {
            this.attackTimer = 0;
            const count = 8;
            for (let i = 0; i < count; i++) {
              const bAngle = angleToPlayer + (i * Math.PI * 2 / count);
              projectiles.push(new Projectile(this.x, this.y, Math.cos(bAngle)*280, Math.sin(bAngle)*280, 20, this.color, true));
            }
          }
        }

        this.x += this.vx * dt;
        this.y += this.vy * dt;
      }

      draw(ctx) {
        if (!this.alive) return;
        ctx.save();
        ctx.translate(this.x, this.y);

        const enemyImg = loadedImages['monsters_beasts'];
        if (enemyImg && enemyImg.complete) {
          const cols = 6;
          const rows = 6;
          const cellW = 1024 / cols;
          const cellH = 1024 / rows;

          const r = this.spriteRow;
          const c = Math.floor((Date.now() / 140) % 5);

          const scale = this.isBoss ? 2.2 : 1.3;
          const drawW = 72 * scale;
          const drawH = 72 * scale;

          ctx.save();
          if (this.facing === -1) {
            ctx.scale(-1, 1);
          }

          ctx.drawImage(enemyImg, c * cellW, r * cellH, cellW, cellH, -drawW/2, -drawH/2 - 6, drawW, drawH);
          ctx.restore();
        } else {
          // Fallback Body Circle
          ctx.beginPath();
          ctx.arc(0, 0, this.radius, 0, Math.PI * 2);
          ctx.fillStyle = this.color;
          ctx.fill();
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 2;
          ctx.stroke();
        }

        // Status Effects Aura
        if (this.burnTimer > 0) {
          ctx.beginPath();
          ctx.arc(0, 0, this.radius + 6, 0, Math.PI * 2);
          ctx.strokeStyle = '#f97316';
          ctx.lineWidth = 3;
          ctx.stroke();
        }
        if (this.freezeTimer > 0) {
          ctx.beginPath();
          ctx.arc(0, 0, this.radius + 8, 0, Math.PI * 2);
          ctx.strokeStyle = '#38bdf8';
          ctx.lineWidth = 3;
          ctx.stroke();
        }

        // HP Bar above enemy
        if (!this.isBoss) {
          const hpPct = Math.max(0, this.hp / this.maxHp);
          const barW = this.radius * 2;
          ctx.fillStyle = '#110e18';
          ctx.fillRect(-barW/2, -this.radius - 14, barW, 6);
          ctx.fillStyle = '#ef4444';
          ctx.fillRect(-barW/2, -this.radius - 14, barW * hpPct, 6);
        }

        ctx.restore();
      }
    }

    let enemies = [];

    // ==========================================
    // PROJECTILES & VISUAL FX CLASSES
    // ==========================================
    class Projectile {
      constructor(x, y, vx, vy, dmg, color, isEnemy = true) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.dmg = dmg;
        this.color = color;
        this.isEnemy = isEnemy;
        this.radius = 9;
        this.alive = true;
        this.life = 4.0;
      }

      update(dt) {
        this.x += this.vx * dt;
        this.y += this.vy * dt;
        this.life -= dt;
        if (this.life <= 0) this.alive = false;

        // Collision
        if (this.isEnemy) {
          if (Math.hypot(player.x - this.x, player.y - this.y) <= player.radius + this.radius) {
            this.alive = false;
            player.takeDamage(this.dmg);
          }
        } else {
          enemies.forEach(e => {
            if (e.alive && Math.hypot(e.x - this.x, e.y - this.y) <= e.radius + this.radius) {
              this.alive = false;
              e.takeDamage(this.dmg);
            }
          });
        }
      }

      draw(ctx) {
        ctx.save();
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.shadowColor = this.color;
        ctx.shadowBlur = 10;
        ctx.restore();
      }
    }

    let projectiles = [];
    let fxList = [];
    let floatingTexts = [];

    class FloatingText {
      constructor(x, y, text, color = '#ffffff', size = 14) {
        this.x = x;
        this.y = y;
        this.text = text;
        this.color = color;
        this.size = size;
        this.alpha = 1.0;
        this.vy = -35;
      }

      update(dt) {
        this.y += this.vy * dt;
        this.alpha -= dt * 1.5;
      }

      draw(ctx) {
        ctx.save();
        ctx.font = `bold ${this.size}px 'Cinzel', serif`;
        ctx.fillStyle = this.color;
        ctx.globalAlpha = Math.max(0, this.alpha);
        ctx.textAlign = 'center';
        ctx.fillText(this.text, this.x, this.y);
        ctx.restore();
      }
    }

    class AnimatedAttackSweep {
      constructor(x, y, angle, radius, color = '#facc15') {
        this.x = x;
        this.y = y;
        this.angle = angle;
        this.radius = radius;
        this.color = color;
        this.alpha = 1.0;
        this.life = 0.18;
      }

      update(dt) {
        this.life -= dt;
        this.alpha = this.life / 0.18;
      }

      draw(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);
        ctx.beginPath();
        ctx.arc(0, 0, this.radius, -Math.PI * 0.45, Math.PI * 0.45);
        ctx.strokeStyle = this.color;
        ctx.lineWidth = 14;
        ctx.globalAlpha = Math.max(0, this.alpha);
        ctx.shadowColor = this.color;
        ctx.shadowBlur = 16;
        ctx.stroke();
        ctx.restore();
      }
    }

    class Shockwave {
      constructor(x, y, maxRadius, color = '#facc15') {
        this.x = x;
        this.y = y;
        this.maxRadius = maxRadius;
        this.currentRadius = 10;
        this.color = color;
        this.alpha = 1.0;
      }

      update(dt) {
        this.currentRadius += (this.maxRadius - this.currentRadius) * dt * 14;
        this.alpha -= dt * 2.2;
      }

      draw(ctx) {
        ctx.save();
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.currentRadius, 0, Math.PI * 2);
        ctx.strokeStyle = this.color;
        ctx.lineWidth = 4;
        ctx.globalAlpha = Math.max(0, this.alpha);
        ctx.shadowColor = this.color;
        ctx.shadowBlur = 14;
        ctx.stroke();
        ctx.restore();
      }
    }

    class AnimatedLightningStrike {
      constructor(x, y) {
        this.x = x;
        this.y = y;
        this.alpha = 1.0;
      }

      update(dt) {
        this.alpha -= dt * 4.0;
      }

      draw(ctx) {
        ctx.save();
        ctx.beginPath();
        ctx.moveTo(this.x + (Math.random()*20 - 10), this.y - 400);
        ctx.lineTo(this.x + (Math.random()*15 - 7), this.y - 200);
        ctx.lineTo(this.x + (Math.random()*10 - 5), this.y - 100);
        ctx.lineTo(this.x, this.y);
        ctx.strokeStyle = '#facc15';
        ctx.lineWidth = 6;
        ctx.globalAlpha = Math.max(0, this.alpha);
        ctx.shadowColor = '#fff';
        ctx.shadowBlur = 16;
        ctx.stroke();
        ctx.restore();
      }
    }

    class AnimatedFireExplosion {
      constructor(x, y, radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.alpha = 1.0;
      }

      update(dt) {
        this.alpha -= dt * 3.0;
      }

      draw(ctx) {
        ctx.save();
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius * (1.2 - this.alpha*0.2), 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(239, 68, 68, ' + Math.max(0, this.alpha*0.6) + ')';
        ctx.fill();
        ctx.strokeStyle = '#f97316';
        ctx.lineWidth = 4;
        ctx.stroke();
        ctx.restore();
      }
    }

    class AnimatedWaterWave {
      constructor(x, y, angle) {
        this.x = x;
        this.y = y;
        this.angle = angle;
        this.dist = 0;
        this.alpha = 1.0;
      }

      update(dt) {
        this.dist += 380 * dt;
        this.alpha -= dt * 2.0;
      }

      draw(ctx) {
        ctx.save();
        ctx.translate(this.x + Math.cos(this.angle)*this.dist, this.y + Math.sin(this.angle)*this.dist);
        ctx.rotate(this.angle);
        ctx.beginPath();
        ctx.arc(0, 0, 45, -Math.PI*0.4, Math.PI*0.4);
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 6;
        ctx.globalAlpha = Math.max(0, this.alpha);
        ctx.stroke();
        ctx.restore();
      }
    }

    function createScreenShake(amount) {
      gameState.screenShake = amount;
    }

    // ==========================================
    // EXIT GATES & CHAMBER PROGRESSION
    // ==========================================
    let exitGates = [];

    function setupExitGates() {
      exitGates = [];
      const godKeys = Object.keys(GODS);

      const count = 2 + (Math.random() > 0.5 ? 1 : 0);
      for (let i = 0; i < count; i++) {
        const ang = (i / count) * Math.PI * 2;
        const gateX = Math.cos(ang) * 450;
        const gateY = Math.sin(ang) * 450;

        let rewardType = 'god';
        let godKey = godKeys[Math.floor(Math.random() * godKeys.length)];
        let label = GODS[godKey].name;

        const roll = Math.random();
        if (roll < 0.25) {
          rewardType = 'peach';
          label = 'HEAVENLY PEACH (蟠桃)';
        } else if (roll < 0.40) {
          rewardType = 'shop';
          label = 'DRAGON TREASURY (龙宫宝阁)';
        } else if (roll < 0.55) {
          rewardType = 'heart';
          label = 'GINSENG FRUIT (人参果 +HP)';
        } else if (roll < 0.70) {
          rewardType = 'ashes';
          label = 'KARMA ASHES (功德灵砂)';
        }

        exitGates.push({
          x: gateX,
          y: gateY,
          radius: 52,
          rewardType: rewardType,
          godKey: godKey,
          label: label
        });
      }
    }

    function startChamber(index) {
      gameState.chamberIndex = index;
      gameState.chamberCleared = false;
      enemies = [];
      projectiles = [];
      fxList = [];
      exitGates = [];

      // Determine Biome
      if (index <= 20) {
        gameState.biome = 1;
        document.getElementById('chamber-name').innerText = `FLOWER-FRUIT MOUNTAIN - CHAMBER ${index} / 100`;
        document.getElementById('chamber-sub').innerText = '花果山水帘洞 · 仙石初现';
      } else if (index <= 40) {
        gameState.biome = 2;
        document.getElementById('chamber-name').innerText = `DIYU NETHER HELL - CHAMBER ${index} / 100`;
        document.getElementById('chamber-sub').innerText = '幽冥地府鬼门关 · 生死簿除名';
      } else if (index <= 60) {
        gameState.biome = 3;
        document.getElementById('chamber-name').innerText = `SOUTH HEAVEN GATE - CHAMBER ${index} / 100`;
        document.getElementById('chamber-sub').innerText = '南天门灵霄宝境 · 天兵守关';
      } else if (index <= 80) {
        gameState.biome = 4;
        document.getElementById('chamber-name').innerText = `PEACH ORCHARD & CRUCIBLE - CHAMBER ${index} / 100`;
        document.getElementById('chamber-sub').innerText = '蟠桃胜境 · 八卦炼丹炉';
      } else {
        gameState.biome = 5;
        document.getElementById('chamber-name').innerText = `LINGXIAO TREASURE HALL - CHAMBER ${index} / 100`;
        document.getElementById('chamber-sub').innerText = '凌霄宝殿 · 大闹天宫';
      }

      // Check for Boss Encounter
      const bossHud = document.getElementById('boss-hud');
      if (index === 20 || index === 40 || index === 60 || index === 80 || index === 100) {
        gameState.chamberType = 'boss';
        bossHud.style.display = 'flex';

        let bossKey = 'boss_aoguang';
        if (index === 40) bossKey = 'boss_yanluo';
        if (index === 60) bossKey = 'boss_nezha';
        if (index === 80) bossKey = 'boss_erlang';
        if (index === 100) bossKey = 'boss_jade_emperor';

        const boss = new Enemy(bossKey, 0, -220);
        enemies.push(boss);
        document.getElementById('boss-name-text').innerText = boss.name;
      } else {
        gameState.chamberType = 'normal';
        bossHud.style.display = 'none';

        // Spawn Wave of regular enemies
        const enemyCount = 3 + Math.floor(index * 0.15);
        const types = Object.keys(ENEMY_TYPES).filter(k => !ENEMY_TYPES[k].isBoss);

        for (let i = 0; i < enemyCount; i++) {
          const t = types[Math.floor(Math.random() * types.length)];
          const ang = Math.random() * Math.PI * 2;
          const dist = 220 + Math.random() * 320;
          enemies.push(new Enemy(t, Math.cos(ang)*dist, Math.sin(ang)*dist));
        }
      }

      player.x = 0;
      player.y = 200;
      updateHUD();
    }

    function checkChamberClear() {
      if (gameState.chamberCleared) return;
      if (enemies.length > 0 && enemies.every(e => !e.alive)) {
        gameState.chamberCleared = true;
        sound.playGong();
        setupExitGates();
      }
    }

    // ==========================================
    // MODALS & BOONS LOGIC
    // ==========================================
    function openGodBoonModal(godKey) {
      gameState.isPaused = true;
      const god = GODS[godKey] || GODS['erlangshen'];
      const modal = document.getElementById('boon-modal');
      const container = document.getElementById('boon-choices-container');

      document.getElementById('god-name').innerText = god.name;
      document.getElementById('god-title').innerText = god.title;
      document.getElementById('god-quote').innerText = god.quotes[Math.floor(Math.random() * god.quotes.length)];

      const portrait = document.getElementById('god-portrait');
      const godSheet = loadedImages['all_10_gods'];
      if (godSheet && godSheet.complete) {
        const col = god.portraitIndex % 5;
        const row = Math.floor(god.portraitIndex / 5);
        portrait.style.backgroundImage = `url(${godSheet.src})`;
        portrait.style.backgroundPosition = `-${col * 120}px -${row * 120}px`;
        portrait.style.backgroundSize = `600px 240px`;
      }

      container.innerHTML = '';
      const availableBoons = [...god.boons].sort(() => 0.5 - Math.random()).slice(0, 3);

      availableBoons.forEach(boon => {
        const card = document.createElement('div');
        card.className = 'boon-card';
        card.innerHTML = `
          <div>
            <div class="boon-slot-tag">${boon.slot}</div>
            <div class="boon-name">${boon.name}</div>
            <div class="boon-desc">${boon.desc}</div>
          </div>
          <div class="boon-action-btn">CLAIM BLESSING (领受神通)</div>
        `;
        card.onclick = () => {
          applyBoon(boon, godKey);
          modal.style.display = 'none';
          gameState.isPaused = false;
          sound.playJadeChime();
        };
        container.appendChild(card);
      });

      modal.style.display = 'flex';
    }

    function applyBoon(boon, godKey) {
      const slot = boon.slot.toLowerCase();
      const boonData = { ...boon, godKey: godKey, level: 1 };

      if (slot.includes('attack')) {
        player.boons.attack = boonData;
        document.getElementById('boon-tag-attack').innerText = boon.name;
      } else if (slot.includes('special')) {
        player.boons.special = boonData;
        document.getElementById('boon-tag-special').innerText = boon.name;
      } else if (slot.includes('cast')) {
        player.boons.cast = boonData;
        document.getElementById('boon-tag-cast').innerText = boon.name;
      } else if (slot.includes('dash')) {
        player.boons.dash = boonData;
        document.getElementById('boon-tag-dash').innerText = boon.name;
      } else if (slot.includes('hex') || slot.includes('awaken')) {
        player.boons.hex = boonData;
        document.getElementById('boon-tag-hex').innerText = boon.name;
      } else {
        player.boons.passives.push(boonData);
      }
      gameState.boonsCount++;
      updateHUD();
    }

    // Heavenly Peaches Modal (replaces Pom)
    function openPeachModal() {
      gameState.isPaused = true;
      const modal = document.getElementById('pom-modal');
      const container = document.getElementById('pom-choices-container');
      container.innerHTML = '';

      const peachIcon = document.getElementById('peach-modal-icon');
      const rewImg = loadedImages['reward_icons'];
      if (rewImg && rewImg.complete) {
        peachIcon.style.backgroundImage = `url(${rewImg.src})`;
        peachIcon.style.backgroundPosition = `0 0`;
        peachIcon.style.backgroundSize = `200% 200%`;
      }

      const equipped = [];
      if (player.boons.attack) equipped.push(player.boons.attack);
      if (player.boons.special) equipped.push(player.boons.special);
      if (player.boons.cast) equipped.push(player.boons.cast);
      if (player.boons.dash) equipped.push(player.boons.dash);
      player.boons.passives.forEach(b => equipped.push(b));

      if (equipped.length === 0) {
        player.maxHp += 25;
        player.hp = Math.min(player.maxHp, player.hp + 25);
        gameState.peachesEaten++;
        sound.playPeachBite();
        modal.style.display = 'none';
        gameState.isPaused = false;
        floatingTexts.push(new FloatingText(player.x, player.y - 40, '+25 MAX HP (蟠桃益寿)', '#fb7185'));
        return;
      }

      const choices = equipped.sort(() => 0.5 - Math.random()).slice(0, 3);
      choices.forEach(b => {
        const card = document.createElement('div');
        card.className = 'boon-card';
        card.innerHTML = `
          <div>
            <div class="boon-slot-tag" style="background: rgba(251, 113, 133, 0.2); border-color: var(--peach-pink); color: var(--peach-glow);">${b.slot} · LV ${b.level || 1} ➔ LV ${(b.level || 1) + 1}</div>
            <div class="boon-name" style="color: var(--peach-glow);">${b.name}</div>
            <div class="boon-desc">${b.desc}</div>
          </div>
          <div class="boon-action-btn" style="background: linear-gradient(180deg, #e11d48, #9f1239);">EAT CELESTIAL PEACH (服食蟠桃)</div>
        `;
        card.onclick = () => {
          b.level = (b.level || 1) + 1;
          gameState.peachesEaten++;
          sound.playPeachBite();
          modal.style.display = 'none';
          gameState.isPaused = false;
          floatingTexts.push(new FloatingText(player.x, player.y - 40, `LV ${b.level} ${b.name}!`, '#fb7185'));
          updateHUD();
        };
        container.appendChild(card);
      });

      modal.style.display = 'flex';
    }

    // Shop Modal
    function openShopModal() {
      gameState.isPaused = true;
      const modal = document.getElementById('shop-modal');
      const container = document.getElementById('shop-choices-container');
      container.innerHTML = '';

      const items = [
        { name: 'Millennial Lingzhi (万年灵芝)', desc: 'Restore 50 HP and gain +20 Max Health.', cost: 60, action: () => { player.maxHp += 20; player.hp = Math.min(player.maxHp, player.hp + 50); } },
        { name: 'Heavenly Peach (天庭蟠桃)', desc: 'Upgrade one of your equipped boons by +1 Level.', cost: 90, action: () => { openPeachModal(); } },
        { name: 'Karma Talisman (太上开光符箓)', desc: 'Instantly gain +25 Karma Spirit Ashes.', cost: 45, action: () => { gameState.ashes += 25; } }
      ];

      items.forEach(it => {
        const card = document.createElement('div');
        card.className = 'boon-card';
        card.innerHTML = `
          <div>
            <div class="boon-slot-tag">SHOP ITEM</div>
            <div class="boon-name">${it.name}</div>
            <div class="boon-desc">${it.desc}</div>
          </div>
          <div class="boon-action-btn">BUY: 🪙 ${it.cost} COINS</div>
        `;
        card.onclick = () => {
          if (gameState.gold >= it.cost) {
            gameState.gold -= it.cost;
            it.action();
            sound.playJadeChime();
            updateHUD();
            openShopModal();
          } else {
            alert('Not enough Jade Coins!');
          }
        };
        container.appendChild(card);
      });

      modal.style.display = 'flex';
    }

    function closeShopModal() {
      document.getElementById('shop-modal').style.display = 'none';
      gameState.isPaused = false;
    }

    // Altar of 72 Transformations
    function openAltarOfTransformations() {
      gameState.isPaused = true;
      const modal = document.getElementById('altar-modal');
      const container = document.getElementById('altar-items-container');
      container.innerHTML = '';

      const traits = [
        { key: 'stone_monkey', name: 'Stone Monkey Body (石猴金身)', desc: '+25 Max HP per rank.', cost: 10 },
        { key: 'golden_eyes', name: 'Fiery Golden Eyes (火眼金睛)', desc: '+8% Critical Strike Chance.', cost: 15 },
        { key: 'somersault', name: 'Somersault Mastery (筋斗云精通)', desc: '+1 Extra Dash charge.', cost: 25 },
        { key: 'hair_clones', name: 'Hair-Clone Technique (身外化身)', desc: 'Chance to summon clone on hit.', cost: 20 },
        { key: 'qi_circulation', name: 'Qi Circulation (胎息纳气)', desc: '+15 Max Qi and +0.8 Qi Regen/s.', cost: 12 },
        { key: 'nirvana_body', name: 'Nirvana Golden Body (不灭金身)', desc: '+1 Death Defiance life charge.', cost: 35 }
      ];

      traits.forEach(tr => {
        const lvl = metaUpgrades[tr.key];
        const cost = tr.cost * (lvl + 1);
        const div = document.createElement('div');
        div.className = 'altar-item';
        div.innerHTML = `
          <div class="altar-info">
            <div class="altar-name">${tr.name}</div>
            <div class="altar-desc">${tr.desc}</div>
            <div class="altar-level">Rank: ${lvl}</div>
          </div>
          <button class="altar-btn" ${gameState.ashes < cost ? 'disabled' : ''} onclick="upgradeTrait('${tr.key}', ${cost})">UPGRADE (${cost} ✨)</button>
        `;
        container.appendChild(div);
      });

      modal.style.display = 'flex';
    }

    function upgradeTrait(key, cost) {
      if (gameState.ashes >= cost) {
        gameState.ashes -= cost;
        metaUpgrades[key]++;
        player.applyMetaUpgrades();
        sound.playJadeChime();
        updateHUD();
        openAltarOfTransformations();
      }
    }

    function closeAltarModal() {
      document.getElementById('altar-modal').style.display = 'none';
      gameState.isPaused = false;
    }

    // Codex Modal
    function openSkillCodex() {
      gameState.isPaused = true;
      const modal = document.getElementById('codex-modal');
      const container = document.getElementById('codex-cards-container');
      container.innerHTML = '';

      for (let k in GODS) {
        const g = GODS[k];
        const card = document.createElement('div');
        card.className = 'codex-card';
        card.innerHTML = `
          <div class="codex-god-title" style="color: ${g.color};">${g.name} (${g.title})</div>
          <div class="codex-boon-list">
            ${g.boons.map(b => `<div>• <b>${b.name}</b> (${b.slot}): ${b.desc}</div>`).join('')}
          </div>
        `;
        container.appendChild(card);
      }

      modal.style.display = 'flex';
    }

    function closeSkillCodex() {
      document.getElementById('codex-modal').style.display = 'none';
      gameState.isPaused = false;
    }

    function handleGameOver(isVictory) {
      gameState.isPaused = true;
      const modal = document.getElementById('gameover-modal');
      const title = document.getElementById('gameover-title');
      const sub = document.getElementById('gameover-sub');

      if (isVictory) {
        title.className = 'gameover-title victory';
        title.innerText = 'HAVOC IN HEAVEN ACHIEVED (威震三界·大闹天宫)!';
        sub.innerText = 'Sun Wukong conquered the Lingxiao Hall and transcended the cosmos!';
        sound.playGong();
      } else {
        title.className = 'gameover-title defeat';
        title.innerText = 'DEFEATED (道消身殒)';
        sub.innerText = 'Your mortal shell dispersed. Return to Flower-Fruit Mountain to train your 72 Transformations.';
      }

      document.getElementById('stat-chambers').innerText = `${gameState.chamberIndex} / 100`;
      document.getElementById('stat-kills').innerText = gameState.enemiesKilled;
      document.getElementById('stat-boons').innerText = gameState.boonsCount;
      document.getElementById('stat-peaches').innerText = gameState.peachesEaten;
      document.getElementById('stat-ashes').innerText = gameState.ashes;

      modal.style.display = 'flex';
    }

    function restartRun() {
      document.getElementById('gameover-modal').style.display = 'none';
      gameState.isPaused = false;
      player.resetForRun();
      startChamber(1);
    }

    function updateHUD() {
      const hpPct = Math.max(0, player.hp / player.maxHp) * 100;
      const qiPct = Math.max(0, player.qi / player.maxQi) * 100;
      const awakenPct = Math.max(0, player.awakenGauge / player.maxAwakenGauge) * 100;

      document.getElementById('hp-bar').style.width = `${hpPct}%`;
      document.getElementById('hp-text').innerText = `${Math.round(player.hp)} / ${player.maxHp}`;

      document.getElementById('qi-bar').style.width = `${qiPct}%`;
      document.getElementById('qi-text').innerText = `${Math.round(player.qi)} / ${player.maxQi}`;

      document.getElementById('awaken-bar').style.width = `${awakenPct}%`;
      document.getElementById('awaken-text').innerText = player.isAwakened ? `AWAKENED (${Math.ceil(player.awakenDuration)}s)` : (awakenPct >= 100 ? 'READY: [R/F]' : `${Math.round(awakenPct)}%`);

      document.getElementById('gold-val').innerText = gameState.gold;
      document.getElementById('ashes-val').innerText = gameState.ashes;
      document.getElementById('peaches-val').innerText = gameState.peachesEaten;
      document.getElementById('lives-val').innerText = player.lives;

      // Boss Bar
      if (gameState.chamberType === 'boss') {
        const boss = enemies.find(e => e.isBoss && e.alive);
        if (boss) {
          const bossPct = Math.max(0, boss.hp / boss.maxHp) * 100;
          document.getElementById('boss-bar-fill').style.width = `${bossPct}%`;
        }
      }
    }

    // ==========================================
    // MAIN GAME LOOP & RENDERING
    // ==========================================
    let lastTime = performance.now();

    function gameLoop(currentTime) {
      const dt = Math.min(0.1, (currentTime - lastTime) / 1000);
      lastTime = currentTime;

      if (!gameState.isPaused) {
        // Update Player & Entities
        player.update(dt);

        enemies.forEach(e => e.update(dt));
        enemies = enemies.filter(e => e.alive || e.burnTimer > 0);

        projectiles.forEach(p => p.update(dt));
        projectiles = projectiles.filter(p => p.alive);

        fxList.forEach(fx => fx.update(dt));
        fxList = fxList.filter(fx => fx.alpha > 0);

        floatingTexts.forEach(ft => ft.update(dt));
        floatingTexts = floatingTexts.filter(ft => ft.alpha > 0);

        checkChamberClear();

        // Check Exit Gate Entry
        if (gameState.chamberCleared) {
          exitGates.forEach(gate => {
            const dist = Math.hypot(player.x - gate.x, player.y - gate.y);
            if (dist <= gate.radius + player.radius) {
              // Proceed to next chamber
              if (gate.rewardType === 'god') {
                openGodBoonModal(gate.godKey);
              } else if (gate.rewardType === 'peach') {
                openPeachModal();
              } else if (gate.rewardType === 'shop') {
                openShopModal();
              } else if (gate.rewardType === 'heart') {
                player.maxHp += 25;
                player.hp = Math.min(player.maxHp, player.hp + 25);
                sound.playJadeChime();
                floatingTexts.push(new FloatingText(player.x, player.y - 40, '+25 MAX HP!', '#10b981'));
              } else if (gate.rewardType === 'ashes') {
                gameState.ashes += 20;
                sound.playJadeChime();
                floatingTexts.push(new FloatingText(player.x, player.y - 40, '+20 KARMA ASHES!', '#c084fc'));
              }

              if (gameState.chamberIndex >= 100) {
                handleGameOver(true);
              } else {
                startChamber(gameState.chamberIndex + 1);
              }
            }
          });
        }
      }

      // Render
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      ctx.save();
      // Camera Follow with Screen Shake
      let shakeX = 0;
      let shakeY = 0;
      if (gameState.screenShake > 0) {
        shakeX = (Math.random() * 2 - 1) * gameState.screenShake;
        shakeY = (Math.random() * 2 - 1) * gameState.screenShake;
        gameState.screenShake = Math.max(0, gameState.screenShake - dt * 25);
      }

      ctx.translate(canvas.width / 2 - player.x + shakeX, canvas.height / 2 - player.y + shakeY);

      // 1. Draw Floor Tiles (Heavenly Court / Tian Ting Jade Pavers)
      const floorImg = loadedImages['seamless_floor'];
      if (floorImg && floorImg.complete) {
        ctx.drawImage(floorImg, -700, -700, 1400, 1400);
      } else {
        ctx.fillStyle = '#140f20';
        ctx.fillRect(-700, -700, 1400, 1400);
      }

      // Chamber Boundary Border (Golden Chinese Gate Frame)
      ctx.strokeStyle = 'rgba(230, 180, 80, 0.75)';
      ctx.lineWidth = 10;
      ctx.strokeRect(-680, -680, 1360, 1360);

      // 2. Draw Exit Gates
      if (gameState.chamberCleared) {
        exitGates.forEach(gate => {
          ctx.save();
          ctx.translate(gate.x, gate.y);

          // Glowing Gate Ring
          ctx.beginPath();
          ctx.arc(0, 0, gate.radius, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(230, 180, 80, 0.25)';
          ctx.fill();
          ctx.strokeStyle = '#facc15';
          ctx.lineWidth = 4;
          ctx.shadowColor = '#facc15';
          ctx.shadowBlur = 16;
          ctx.stroke();

          // Gate Icon
          const rewImg = loadedImages['reward_icons'];
          if (rewImg && rewImg.complete) {
            let col = 0, row = 0;
            if (gate.rewardType === 'peach') { col = 0; row = 0; }
            else if (gate.rewardType === 'shop') { col = 1; row = 0; }
            else if (gate.rewardType === 'heart') { col = 0; row = 1; }
            else if (gate.rewardType === 'ashes') { col = 1; row = 1; }
            else if (gate.rewardType === 'god') {
              const godsImg = loadedImages['all_10_gods'];
              if (godsImg && godsImg.complete) {
                const gIndex = GODS[gate.godKey].portraitIndex;
                const gCol = gIndex % 5;
                const gRow = Math.floor(gIndex / 5);
                const gW = godsImg.width / 5;
                const gH = godsImg.height / 2;
                ctx.drawImage(godsImg, gCol * gW, gRow * gH, gW, gH, -36, -36, 72, 72);
              }
            }

            if (gate.rewardType !== 'god') {
              const rW = rewImg.width / 2;
              const rH = rewImg.height / 2;
              ctx.drawImage(rewImg, col * rW, row * rH, rW, rH, -36, -36, 72, 72);
            }
          }

          // Gate Label
          ctx.font = 'bold 13px Cinzel, serif';
          ctx.fillStyle = '#fff2a8';
          ctx.textAlign = 'center';
          ctx.shadowColor = '#000';
          ctx.shadowBlur = 6;
          ctx.fillText(gate.label, 0, -gate.radius - 12);

          ctx.restore();
        });
      }

      // 3. Draw Entities
      player.draw(ctx);
      enemies.forEach(e => e.draw(ctx));
      projectiles.forEach(p => p.draw(ctx));
      fxList.forEach(fx => fx.draw(ctx));
      floatingTexts.forEach(ft => ft.draw(ctx));

      ctx.restore();

      requestAnimationFrame(gameLoop);
    }

    // Start Game on Load
    player.resetForRun();
    startChamber(1);
    requestAnimationFrame(gameLoop);
  </script>
</body>
</html>
"""

final_html = html_template.replace('%ASSETS_JSON%', json.dumps(b64_data))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('generate_game.py', 'w', encoding='utf-8') as f:
    f.write(f'''# Journey to the West: Havoc in Heaven build generator
import json
import base64
import os

b64_data = {json.dumps(b64_data)}

html_template = """{html_template}"""
final_html = html_template.replace('%ASSETS_JSON%', json.dumps(b64_data))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully compiled index.html with all brand new custom Journey to the West assets!")
''')

print(f"Successfully compiled brand new index.html ({len(final_html)} bytes)!")
