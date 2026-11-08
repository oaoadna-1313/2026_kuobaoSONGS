import os
import shutil
import json

BASE_DIR = r"C:\2026_歌SONG國文"
TARGET_DIR = os.path.join(BASE_DIR, "B01L08朋友相交好歌")
ASSETS_SRC = os.path.join(BASE_DIR, "assets")
MATERIALS_DIR = os.path.join(BASE_DIR, r"材料\B1_SONG\[好歌]B01L08朋友相交")

# Ensure target directories exist
os.makedirs(os.path.join(TARGET_DIR, "assets"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "media"), exist_ok=True)

# 1. Copy Assets
for asset in ["baoden.png", "badge-songlogo.PNG", "SSS_Stamp02.png"]:
    src = os.path.join(ASSETS_SRC, asset)
    dst = os.path.join(TARGET_DIR, "assets", asset)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied asset: {asset}")
    else:
        print(f"Warning: Asset {src} not found!")

# 2. Copy Media & PDFs
media_map = [
    ("[國寶]B01L08朋友相交好歌-01朋友歌.mp3", "media/friends-song.mp3"),
    ("[國寶]B01L08朋友相交好歌-02當我們一起走過.mp3", "media/walk-together.mp3"),
    ("[國寶]B01L08朋友相交好歌-03超人披風.mp3", "media/superman-cape.mp3"),
    ("[國寶]B01L08朋友相交好歌-03超人披風MV.mp4", "media/superman-cape.mp4"),
    ("[國寶]B01L08朋友相交好歌-01朋友歌.pdf", "worksheet-friends-song.pdf"),
    ("[國寶]B01L08朋友相交好歌-02當我們一起走過.pdf", "worksheet-walk-together.pdf"),
    ("[國寶]B01L08朋友相交好歌-03超人披風.pdf", "worksheet-superman-cape.pdf"),
]

for src_name, dst_rel in media_map:
    src = os.path.join(MATERIALS_DIR, src_name)
    dst = os.path.join(TARGET_DIR, dst_rel)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {src_name} -> {dst_rel}")
    else:
        print(f"Warning: Material {src} not found!")

# 3. Songs Data Definition
songsData = [
    {
        "id": "friends-song",
        "title": "朋友歌",
        "artist": "陶大偉",
        "lyricist": "陶大偉",
        "composer": "陶大偉",
        "year": "1981",
        "album": "朋友歌",
        "tag": "經典民歌・豁達真情",
        "order": "第一曲",
        "sheet": "好歌學習單 第46頁",
        "audio": "media/friends-song.mp3",
        "video": None,
        "bgGradient": "from-amber-600 via-orange-600 to-stone-900",
        "lightBg": "bg-amber-50/70 border-amber-200",
        "intro": "陶大偉包辦詞曲創作與演唱的台灣流行音樂傳奇經典。歌曲以詼諧幽默的口吻、輕快明朗的節奏，道出人生最質樸深刻的友誼智慧。歌詞以「拋開煩惱和憂愁，享受人生樂悠悠」撫慰朋友心靈，更以平實生動的譬喻「幸福靠你去追求，渣泥不會冒出石油，橫財不如細水長流」勸勉朋友勤懇奮鬥、踏實前行。呼應課文《朋友相交》之真諦，朋友不只是共度歡樂時光的夥伴，更是在迷惘時相互提攜、坦誠相照的人生知己。",
        "lyrics": [
            [{"t": "嘿嘿我的朋友 讓我向你來問候  拋開"}, {"b": "煩惱", "h": "2字"}, {"t": "和憂愁 享受人生樂"}, {"b": "悠悠", "h": "2字"}],
            [{"t": "啦啦...人生好比在作秀  啦啦...海闊天空任我"}, {"b": "遨遊", "h": "2字"}, {"t": " (大家一起來)"}],
            [{"t": "唱唱你的歌來拍拍你的手 眨眨你的眼來甩甩你的頭"}],
            [{"t": "洋煙不比"}, {"b": "長壽", "h": "2字"}, {"t": " 清茶勝過酒 只要我的朋友和我常"}, {"b": "聚首", "h": "2字"}],
            [{"type": "space"}],
            [{"t": "嘿 嘿 我的朋友 "}, {"b": "幸福", "h": "2字"}, {"t": "靠你去追求 渣泥不會冒出"}, {"b": "石油", "h": "2字"}, {"t": " 橫財不如"}, {"b": "細水長流", "h": "4字"}],
            [{"t": "啦啦...大腦不用會"}, {"b": "生銹", "h": "2字"}, {"t": " 啦啦...只要努力就能"}, {"b": "出頭", "h": "2字"}, {"t": " (大家一起來)"}],
            [{"t": "唱唱你的歌來拍拍你的手 眨眨你的眼來甩甩你的頭"}],
            [{"t": "洋煙不比長壽 清茶勝過酒 只要"}, {"b": "逍遙快樂", "h": "4字"}, {"t": "常在我心頭"}]
        ],
        "keySentence": "拋開煩惱和憂愁 享受人生樂悠悠"
    },
    {
        "id": "walk-together",
        "title": "當我們一起走過",
        "artist": "蘇打綠",
        "lyricist": "史俊威",
        "composer": "史俊威",
        "year": "2011",
        "album": "你在煩惱什麼",
        "tag": "真摯抒情・風雨相伴",
        "order": "第二曲",
        "sheet": "好歌學習單 第47頁",
        "audio": "media/walk-together.mp3",
        "video": None,
        "bgGradient": "from-orange-600 via-rose-600 to-stone-900",
        "lightBg": "bg-orange-50/70 border-orange-200",
        "intro": "蘇打綠鼓手史俊威詞曲創作、吳青峰真情演唱的代表作。全曲深情回顧夥伴與知己在生命歷程中，共同走過的風雨沉重與挫折傷痛。正如同課文《朋友相交》所闡釋的患難之情，真正的知交不只是同甘，更在於共苦——「包著碎裂的心，繼續下一個夢」。在生命的曠野漂流中，因為有朋友在眼底保留的溫柔與寬容，彼此才能跨越重重困難。「有多少苦痛有你和我一起度過、一起承受；有多少快樂有你和我一起享受、一起感動」，唱出了友誼最溫厚深沉的守護力量。",
        "lyrics": [
            [{"t": "我們都曾有過 風雨過後的"}, {"b": "沉重", "h": "2字"}, {"t": " 形同"}, {"b": "陌路", "h": "2字"}, {"t": "的口 但心卻還流通"}],
            [{"t": "當我們一起走過 這些傷痛的時候 包著"}, {"b": "碎裂", "h": "2字"}, {"t": "的心 繼續下一個夢"}],
            [{"t": "也知道 我們並不會"}, {"b": "退縮", "h": "2字"}, {"t": " 狂奔的念頭 不曾停止"}, {"b": "溫柔", "h": "2字"}],
            [{"t": "一直到 將來我們都"}, {"b": "成熟", "h": "2字"}, {"t": " 就不再"}, {"b": "困惑", "h": "2字"}, {"t": " 生命有多少"}, {"b": "過錯", "h": "2字"}],
            [{"t": "我在曠野"}, {"b": "漂流", "h": "2字"}, {"t": " 漂流的盡頭就是你愛的"}, {"b": "寬容", "h": "2字"}, {"t": "  你眼底的溫柔 也為我保留心的"}, {"b": "寄託", "h": "2字"}],
            [{"type": "space"}],
            [{"t": "我們都曾有過 風雨過後的沉重 形同陌路的口 但心卻還流通"}],
            [{"t": "當我們一起走過 這些傷痛的時候 包著碎裂的心 繼續下一個夢"}],
            [{"t": "一直到 將來我們都成熟 就不再困惑 生命有多少過錯"}],
            [{"t": "我在曠野漂流 漂流的盡頭就是你愛的寬容 你眼底的溫柔 也為我保留心的寄託"}],
            [{"type": "space"}],
            [{"t": "過去種種"}, {"b": "抵擋", "h": "2字"}, {"t": "我的手 掌握 不管那有多困難"}, {"b": "重重", "h": "2字"}],
            [{"t": "你"}, {"b": "慈悲", "h": "2字"}, {"t": "的手中 有心的窗口 這就是"}, {"b": "保留", "h": "2字"}, {"t": " 這就是"}, {"b": "寬容", "h": "2字"}],
            [{"t": "我在曠野漂流 漂流的盡頭就是你愛的寬容 你眼底的溫柔 也為我保留心的寄託"}],
            [{"type": "space"}],
            [{"t": "有多少苦痛有你和我一起"}, {"b": "度過", "h": "2字"}, {"t": " 一起"}, {"b": "承受", "h": "2字"}],
            [{"t": "有多少快樂有你和我一起"}, {"b": "享受", "h": "2字"}, {"t": " 一起"}, {"b": "感動", "h": "2字"}]
        ],
        "keySentence": "有多少苦痛有你和我一起度過 一起承受\n有多少快樂有你和我一起享受 一起感動"
    },
    {
        "id": "superman-cape",
        "title": "超人披風",
        "artist": "呂思緯、蕭秉治",
        "lyricist": "呂思緯、蕭秉治",
        "composer": "蕭秉治",
        "year": "2025",
        "album": "GX 兄弟熱血單曲",
        "tag": "熱血搖滾・兄弟情深",
        "order": "第三曲",
        "sheet": "好歌學習單 第48頁",
        "audio": "media/superman-cape.mp3",
        "video": "media/superman-cape.mp4",
        "bgGradient": "from-slate-800 via-orange-950 to-stone-900",
        "lightBg": "bg-slate-50/70 border-slate-200",
        "intro": "由鼓鼓（呂思緯）與蕭秉治組成的限定雙人團體 GX 共同詞曲創作並熱血合唱。兩人自 MP 魔幻力量時期並肩奮戰十餘載，歷經各自沉潛、逆境挑戰，重聚後將真摯不渝的兄弟情誼化為最堅毅的戰歌。「在這世界上遇見同類的機會很少，原來我和你一直活在相同的頻道」，彼此如同穿上超人披風，在彼此脆弱發出求救訊號的第一秒飛奔而至。縱使歲月帶著大家回不同的星球，這份從地心直達宇宙的初衷與默契，將在心中永遠不朽。",
        "lyrics": [
            [{"t": "在這世界上遇見"}, {"b": "同類", "h": "2字"}, {"t": "的機會很少 原來我和你一直活在相同的"}, {"b": "頻道", "h": "2字"}],
            [{"t": "曾經孤獨的我們 突然間 "}, {"b": "繽紛", "h": "2字"}, {"t": "了彼此人生"}],
            [{"type": "space"}],
            [{"t": "當傷痕累累的你發出了"}, {"b": "求救", "h": "2字"}, {"t": "訊號 別害怕我會在第一個時間就收到"}],
            [{"t": "曾經煎熬的我們 突然間 "}, {"b": "拯救", "h": "2字"}, {"t": "了彼此人生"}],
            [{"type": "space"}],
            [{"t": "就算生命再多"}, {"b": "紛擾", "h": "2字"}, {"t": " 都不曾"}, {"b": "動搖", "h": "2字"}],
            [{"t": "讓我陪你微笑 讓我帶你奔跑 穿越每一片"}, {"b": "風暴", "h": "2字"}],
            [{"type": "space"}],
            [{"t": "我穿上"}, {"b": "超人披風", "h": "4字"}, {"t": " 陪你飛 陪你飛 我寫下"}, {"b": "無垠", "h": "2字"}, {"t": "的夢 陪你追 陪你追"}],
            [{"t": "直到幾"}, {"b": "光年", "h": "2字"}, {"t": "的以後 依然守護"}, {"b": "初衷", "h": "2字"}, {"t": " 這份感動從地心直達宇宙"}],
            [{"type": "space"}],
            [{"t": "我穿上超人披風 陪你飛 陪你飛 我寫下無垠的夢 陪你追 陪你追"}],
            [{"t": "直到歲月帶著我們 回不同的星球 別忘了一直活在彼此心中 永遠"}, {"b": "不朽", "h": "2字"}],
            [{"type": "space"}],
            [{"t": "無論在哪一個時空我都不會走掉 雖然你總裝沒事不需要任何擁抱"}],
            [{"t": "曾經"}, {"b": "逞強", "h": "2字"}, {"t": "的我們 突然間 "}, {"b": "柔軟", "h": "2字"}, {"t": "了彼此人生"}],
            [{"type": "space"}],
            [{"t": "就算生命再多紛擾 都不曾動搖"}],
            [{"t": "讓我陪你微笑 讓我帶你奔跑 穿越每一片風暴"}],
            [{"type": "space"}],
            [{"t": "我穿上超人披風 陪你飛 陪你飛 我寫下無垠的夢 陪你追 陪你追"}],
            [{"t": "直到幾光年的以後 依然守護初衷 這份感動從地心直達宇宙"}],
            [{"type": "space"}],
            [{"t": "我穿上超人披風 陪你飛 陪你飛 我寫下無垠的夢 陪你追 陪你追"}],
            [{"t": "直到歲月帶著我們 回不同的星球 別忘了一直活在彼此心中 永遠不朽"}],
            [{"type": "space"}],
            [{"t": "我穿上超人披風 我穿上超人披風 我穿上超人披風 我穿上超人披風"}]
        ],
        "keySentence": "我穿上超人披風 陪你飛 陪你飛 我寫下無垠的夢 陪你追 陪你追\n直到歲月帶著我們 回不同的星球 別忘了一直活在彼此心中 永遠不朽"
    }
]

unitWorksheetMeta = {
    "unitName": "七上國文・L08 朋友相交",
    "badgeClass": "bg-orange-100 text-orange-900 border border-orange-300",
    "songs": [
        {"id": 1, "title": "朋友歌", "artist": "陶大偉", "student": "worksheet-friends-song.pdf", "teacher": "worksheet-friends-song.pdf"},
        {"id": 2, "title": "當我們一起走過", "artist": "蘇打綠", "student": "worksheet-walk-together.pdf", "teacher": "worksheet-walk-together.pdf"},
        {"id": 3, "title": "超人披風", "artist": "呂思緯、蕭秉治", "student": "worksheet-superman-cape.pdf", "teacher": "worksheet-superman-cape.pdf"}
    ]
}

def generate_html(default_song_id="friends-song"):
    songs_json = json.dumps(songsData, ensure_ascii=False)
    worksheet_json = json.dumps(unitWorksheetMeta, ensure_ascii=False)
    
    return f"""<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【七上閱思龍門】歌SONG國文・L08 朋友相交 好歌互動教學平台</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <!-- Google Fonts: Noto Serif TC & Noto Sans TC -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700&family=Noto+Serif+TC:wght@400;600;700;900&display=swap" rel="stylesheet">
  
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            serif: ['"Noto Serif TC"', 'serif'],
            sans: ['"Noto Sans TC"', 'sans-serif'],
            kaiti: ['"DFKai-SB"', '"BiauKai"', '"KaiTi"', 'serif']
          }},
          keyframes: {{
            spin_slow: {{
              '0%': {{ transform: 'rotate(0deg)' }},
              '100%': {{ transform: 'rotate(360deg)' }}
            }},
            pulse_soft: {{
              '0%, 100%': {{ opacity: 1, transform: 'scale(1)' }},
              '50%': {{ opacity: 0.85, transform: 'scale(1.03)' }}
            }}
          }},
          animation: {{
            'spin-slow': 'spin_slow 18s linear infinite',
            'pulse-soft': 'pulse_soft 2s ease-in-out infinite'
          }}
        }}
      }}
    }}
  </script>
  <style>
    /* Custom handwriting font style for teacher answers */
    .font-handwriting {{
      font-family: "DFKai-SB", "BiauKai", "KaiTi", "Noto Serif TC", serif;
      letter-spacing: 0.08em;
    }}
    /* Custom scrollbars */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #f1f5f9;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #cbd5e1;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #94a3b8;
    }}
    
    /* Blank box styles */
    .blank-box {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 4rem;
      min-height: 1.85rem;
      padding: 0.05rem 0.5rem;
      margin: 0.05rem 0.2rem;
      background-color: #ffffff;
      border: 1.5px solid #94a3b8;
      border-radius: 0.375rem;
      vertical-align: middle;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      position: relative;
    }}
    .blank-box:hover {{
      border-color: #f97316;
      background-color: #fff7ed;
      transform: translateY(-1px);
      box-shadow: 0 4px 6px -1px rgba(249, 115, 22, 0.15);
    }}
    .blank-box.revealed {{
      border-color: #fca5a5;
      background-color: #fff1f2;
      box-shadow: 0 1px 3px 0 rgba(225, 29, 72, 0.1);
    }}
    .blank-box.revealed:hover {{
      border-color: #f87171;
      background-color: #ffe4e6;
    }}
    
    /* Vinyl arm pivot */
    .vinyl-arm {{
      transform-origin: 85% 15%;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .vinyl-arm.playing {{
      transform: rotate(26deg);
    }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col selection:bg-orange-100 selection:text-orange-900">

  <!-- ==================== STICKY HEADER (yuesilongmen-web-title-spec) ==================== -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <!-- Brand & Title (閱思龍門標準品牌標題) -->
      <div class="flex items-center space-x-3">
        <a href="index.html" class="flex items-center space-x-2.5 group" title="返回歌SONG國文教學首頁">
          <!-- 嚴格維持原生純方形，嚴禁 rounded-full -->
          <img src="assets/SSS_Stamp02.png" alt="閱思龍門" class="w-10 h-10 object-contain shadow-sm group-hover:rotate-6 transition-transform duration-300">
          <div>
            <div class="flex items-center space-x-2">
              <span class="font-serif font-bold text-lg sm:text-xl text-slate-900 tracking-wide">歌SONG國文</span>
              <span class="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-orange-100 text-orange-900 border border-orange-300">七上國文・L08 朋友相交</span>
            </div>
            <p class="text-[11px] text-slate-500 font-medium hidden md:block">聆聽友誼之歌・穿梭旋律與知音相伴的文學共鳴</p>
          </div>
        </a>
      </div>

      <!-- Quick Action Controls -->
      <div class="flex items-center space-x-2 sm:space-x-3">
        <!-- Reveal All Toggle -->
        <button id="toggleAllBtn" onclick="toggleAllBlanks()" class="px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-rose-50 text-rose-700 hover:bg-rose-100 border border-rose-200 shadow-xs cursor-pointer active:scale-95">
          <i class="fa-solid fa-graduation-cap"></i>
          <span id="toggleAllBtnText">一鍵揭曉教師版</span>
        </button>
        <!-- Reset Blanks -->
        <button onclick="resetAllBlanks()" class="px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-slate-100 text-slate-700 hover:bg-slate-200 border border-slate-200 shadow-xs cursor-pointer active:scale-95">
          <i class="fa-solid fa-rotate-left"></i>
          <span class="hidden sm:inline">重置空白</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ==================== MAIN CONTENT ==================== -->
  <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full space-y-6">

    <!-- Top Banner & Song Carousel Selector (Orange Theme) -->
    <div class="bg-gradient-to-r from-orange-600 via-amber-600 to-stone-900 rounded-2xl p-5 sm:p-6 text-white shadow-xl relative overflow-hidden">
      <!-- Background Decorative Lights -->
      <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-orange-400/20 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute right-1/3 -top-10 w-48 h-48 bg-amber-300/20 rounded-full blur-2xl pointer-events-none"></div>

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5 relative z-10">
        <!-- Left: Logo Banner -->
        <div class="flex items-center gap-4">
          <div class="flex items-center gap-3 shrink-0">
            <!-- 黃框: 國文寶典 baoden.png -->
            <img src="assets/baoden.png" alt="國文寶典" class="h-12 sm:h-14 w-auto object-contain rounded-xl shadow-md border border-white/20">
            <!-- 紅框: 歌SONG國文 badge-songlogo.PNG -->
            <img src="assets/badge-songlogo.PNG" alt="歌SONG國文" class="h-9 sm:h-11 w-auto object-contain filter drop-shadow-md">
          </div>
          <div class="hidden sm:block border-l border-white/20 pl-4">
            <h1 class="text-sm sm:text-base font-serif font-bold text-amber-100 tracking-wide">友誼真諦與心靈相伴的文學樂章</h1>
            <p class="text-xs text-orange-100/90 mt-0.5">結合課文《朋友相交》賞析，聆聽陶大偉《朋友歌》、蘇打綠《當我們一起走過》與GX《超人披風》的動人旋律，邊聽音樂邊完成歌詞填空與深度鑑賞</p>
          </div>
        </div>
      </div>

      <!-- Song Navigation & Worksheet Quick Action Bar -->
      <div class="mt-5 pt-4 border-t border-white/15 flex flex-col md:flex-row md:items-center justify-between gap-3">
        <!-- Left: Song Navigation Pills / Tabs -->
        <div class="flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none flex-1 min-w-0" id="songTabsContainer">
          <!-- Rendered via JS -->
        </div>

        <!-- Right: 學用學習單 與 教用學習單 按鈕 -->
        <div class="flex items-center gap-2 shrink-0 self-end md:self-center">
          <button type="button" onclick="openWorksheetModal('student')" class="px-3.5 py-1.5 rounded-lg text-xs font-bold whitespace-nowrap transition-all flex items-center gap-1.5 bg-amber-500/25 hover:bg-amber-500/40 text-amber-100 border border-amber-400/50 hover:border-amber-300 shadow-sm hover:shadow active:scale-95 cursor-pointer" title="查看或下載學用學習單PDF">
            <i class="fa-solid fa-file-pen text-amber-300 text-xs"></i>
            <span>學用學習單</span>
          </button>
          <button type="button" onclick="openWorksheetModal('teacher')" class="px-3.5 py-1.5 rounded-lg text-xs font-bold whitespace-nowrap transition-all flex items-center gap-1.5 bg-rose-500/25 hover:bg-rose-500/40 text-rose-100 border border-rose-400/50 hover:border-rose-300 shadow-sm hover:shadow active:scale-95 cursor-pointer" title="查看或下載教用學習單PDF（教師版）">
            <i class="fa-solid fa-graduation-cap text-rose-300 text-xs"></i>
            <span>教用學習單</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Active Song Hero & Core Teaching Board (Grid Layout) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">

      <!-- Left Column: Audio Player & Song Info Card (Sticky on desktop, 5 cols) -->
      <div class="lg:col-span-5 space-y-5 lg:sticky lg:top-24">

        <!-- ==================== PLAYER CARD ==================== -->
        <div class="bg-white rounded-2xl border border-slate-200 shadow-md overflow-hidden transition-all duration-300 hover:shadow-lg">
          <!-- Card Header & Mood Badge -->
          <div class="px-5 py-4 border-b border-slate-100 flex items-center justify-between bg-slate-50/60">
            <div class="flex items-center space-x-2">
              <span id="playerOrderBadge" class="px-2 py-0.5 text-xs font-bold rounded-md bg-amber-100 text-amber-900 border border-amber-200">第一曲</span>
            </div>
            <div class="flex items-center gap-2">
              <span id="playerTagBadge" class="px-2.5 py-0.5 text-xs font-medium rounded-full bg-amber-100 text-amber-800">經典民歌・豁達真情</span>
              <!-- MV Switch Button if video available -->
              <button id="videoToggleBtn" onclick="toggleVideoMode()" class="hidden px-2 py-0.5 text-xs font-bold rounded-md bg-rose-600 hover:bg-rose-700 text-white transition-colors cursor-pointer flex items-center gap-1 shadow-xs" title="切換MV視頻播放">
                <i class="fa-solid fa-video"></i>
                <span id="videoToggleText">MV</span>
              </button>
            </div>
          </div>

          <!-- Player Body: Visualizer / Vinyl Record -->
          <div class="p-6 flex flex-col items-center justify-center bg-gradient-to-b from-stone-900 to-stone-950 text-white relative overflow-hidden">
            
            <!-- Video Player Container (Hidden by default) -->
            <div id="videoContainer" class="hidden w-full aspect-video rounded-xl overflow-hidden bg-black shadow-inner mb-3 relative z-10">
              <video id="videoPlayer" class="w-full h-full object-contain" controls playsinline>
                您的瀏覽器不支援影片播放。
              </video>
            </div>

            <!-- Vinyl Record Turntable Animation (Shown in audio mode) -->
            <div class="relative w-48 h-48 sm:w-56 sm:h-56 flex items-center justify-center my-2" id="vinylContainer">
              <!-- Vinyl Shadow & Base -->
              <div class="absolute inset-0 rounded-full bg-black/60 filter blur-md transform translate-y-2"></div>
              <!-- Vinyl Disc -->
              <div id="vinylDisc" class="relative w-full h-full rounded-full bg-stone-950 border-4 border-stone-800 flex items-center justify-center shadow-2xl transition-transform duration-300">
                <!-- Grooves Effect -->
                <div class="absolute inset-2 rounded-full border border-stone-800/80"></div>
                <div class="absolute inset-5 rounded-full border border-stone-800/70"></div>
                <div class="absolute inset-8 rounded-full border border-stone-800/60"></div>
                <div class="absolute inset-12 rounded-full border border-stone-800/50"></div>
                <div class="absolute inset-16 rounded-full border border-stone-800/40"></div>
                <!-- Vinyl Center Label -->
                <div class="w-20 h-20 sm:w-24 sm:h-24 rounded-full bg-gradient-to-tr from-amber-600 via-orange-500 to-rose-600 p-1 flex flex-col items-center justify-center text-center shadow-inner relative z-10">
                  <div class="w-full h-full rounded-full border-2 border-dashed border-amber-200/50 flex flex-col items-center justify-center p-1 text-white">
                    <i class="fa-solid fa-compact-disc text-base sm:text-lg animate-pulse text-amber-200"></i>
                    <span id="vinylSongTitle" class="text-[10px] sm:text-xs font-serif font-black truncate max-w-[4.8rem] text-white mt-0.5">朋友歌</span>
                    <span class="text-[8px] text-amber-100 opacity-80 uppercase tracking-tighter">Song國文</span>
                  </div>
                </div>
                <!-- Spindle Hole -->
                <div class="absolute w-4 h-4 rounded-full bg-stone-900 border-2 border-stone-700 z-20"></div>
              </div>
              <!-- Tonearm -->
              <div id="vinylArm" class="vinyl-arm absolute -top-4 right-2 w-16 h-28 pointer-events-none z-30 transition-transform duration-500 origin-top-right">
                <svg viewBox="0 0 60 100" class="w-full h-full drop-shadow-lg">
                  <circle cx="48" cy="12" r="8" fill="#d4d4d8" stroke="#71717a" stroke-width="2"/>
                  <rect x="44" y="12" width="8" height="48" rx="2" fill="#a1a1aa" transform="rotate(-15 48 12)"/>
                  <rect x="30" y="58" width="6" height="24" rx="1.5" fill="#71717a" transform="rotate(10 30 58)"/>
                  <path d="M 32 80 L 26 95 L 36 97 Z" fill="#f59e0b" stroke="#b45309" stroke-width="1"/>
                </svg>
              </div>
            </div>

            <!-- Song Info on Player -->
            <div class="text-center mt-3 space-y-1 z-10">
              <h2 id="playerSongTitle" class="font-serif font-bold text-lg sm:text-xl text-white tracking-wide">朋友歌</h2>
              <p id="playerArtist" class="text-xs text-amber-200/80 font-medium">演唱：陶大偉・1981</p>
            </div>

            <!-- Audio Control Bar -->
            <div class="w-full mt-4 space-y-3 z-10">
              <!-- Progress Slider -->
              <div class="space-y-1">
                <div class="relative w-full h-2 bg-stone-700/80 rounded-full cursor-pointer overflow-hidden group" onclick="seekAudio(event)">
                  <div id="progressBar" class="h-full bg-gradient-to-r from-amber-500 to-orange-500 rounded-full w-0 transition-all duration-100"></div>
                  <div id="progressHandle" class="absolute top-1/2 -mt-1.5 w-3 h-3 bg-white rounded-full shadow opacity-0 group-hover:opacity-100 transition-opacity" style="left: 0%;"></div>
                </div>
                <div class="flex justify-between text-[11px] font-mono text-stone-400">
                  <span id="currentTime">00:00</span>
                  <span id="totalDuration">--:--</span>
                </div>
              </div>

              <!-- Playback Buttons -->
              <div class="flex items-center justify-between pt-1">
                <!-- Speed Selector -->
                <div class="flex items-center gap-1">
                  <button onclick="setSpeed(0.8, this)" class="speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-white/10 hover:bg-white/20 text-slate-300">0.8x</button>
                  <button onclick="setSpeed(1.0, this)" class="speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-orange-600 text-white font-bold">1.0x</button>
                  <button onclick="setSpeed(1.2, this)" class="speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-white/10 hover:bg-white/20 text-slate-300">1.2x</button>
                </div>

                <!-- Main Media Controls -->
                <div class="flex items-center space-x-3">
                  <!-- -5s -->
                  <button onclick="skipTime(-5)" class="text-stone-300 hover:text-white transition-colors p-1" title="倒退 5 秒">
                    <i class="fa-solid fa-rotate-left text-sm"></i>
                  </button>
                  <!-- Prev Song -->
                  <button onclick="prevSong()" class="text-stone-300 hover:text-white transition-colors p-1" title="上一首">
                    <i class="fa-solid fa-backward-step text-base"></i>
                  </button>
                  <!-- Play / Pause -->
                  <button id="playPauseBtn" onclick="togglePlayPause()" class="w-11 h-11 rounded-full bg-gradient-to-r from-amber-500 to-orange-600 text-white flex items-center justify-center text-lg shadow-lg hover:scale-105 active:scale-95 transition-all cursor-pointer">
                    <i id="playIcon" class="fa-solid fa-play ml-1"></i>
                  </button>
                  <!-- Next Song -->
                  <button onclick="nextSong()" class="text-stone-300 hover:text-white transition-colors p-1" title="下一首">
                    <i class="fa-solid fa-forward-step text-base"></i>
                  </button>
                  <!-- +5s -->
                  <button onclick="skipTime(5)" class="text-stone-300 hover:text-white transition-colors p-1" title="快轉 5 秒">
                    <i class="fa-solid fa-rotate-right text-sm"></i>
                  </button>
                </div>

                <!-- Volume Control -->
                <div class="flex items-center space-x-1.5 group relative">
                  <button onclick="toggleMute()" class="text-stone-300 hover:text-white transition-colors text-xs p-1">
                    <i id="volumeIcon" class="fa-solid fa-volume-high"></i>
                  </button>
                  <input type="range" id="volumeSlider" min="0" max="1" step="0.05" value="1" oninput="changeVolume(this.value)" class="w-14 sm:w-16 h-1 bg-stone-700 rounded-lg appearance-none cursor-pointer accent-orange-500">
                </div>
              </div>
            </div>
          </div>

          <!-- Song Meta & Literature Background Description -->
          <div class="p-5 space-y-3 bg-white">
            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
              <i class="fa-solid fa-circle-info text-orange-600"></i>
              <span>歌曲背景與文學導讀</span>
            </h3>
            <p id="playerSongIntro" class="text-xs sm:text-sm text-slate-600 leading-relaxed font-sans">
              <!-- Rendered via JS -->
            </p>
            <div class="pt-2 border-t border-slate-100 flex flex-wrap gap-y-1 text-[11px] text-slate-500">
              <span class="w-1/2" id="metaLyricist">作詞：陶大偉</span>
              <span class="w-1/2" id="metaComposer">作曲：陶大偉</span>
              <span class="w-1/2" id="metaArtist">演唱：陶大偉</span>
              <span class="w-1/2" id="metaYear">發行：1981</span>
            </div>
          </div>
        </div>

        <!-- Quick Switch Checklist (Songs Grid) -->
        <div class="bg-white rounded-2xl border border-slate-200 p-4 shadow-xs">
          <h4 class="text-xs font-bold text-slate-600 mb-2.5 flex items-center justify-between">
            <span class="flex items-center gap-1.5">
              <i class="fa-solid fa-list-check text-orange-600"></i>
              <span>全系列好歌學習地圖 (3首)</span>
            </span>
            <span class="text-[11px] text-orange-600 font-semibold" id="overallCompletion">進行中 (1/3)</span>
          </h4>
          <div class="space-y-1.5" id="songListMenu">
            <!-- Rendered by JS -->
          </div>
        </div>

      </div>

      <!-- Right Column: Interactive Worksheet (7 cols) -->
      <div class="lg:col-span-7 space-y-6">

        <!-- ==================== WORKSHEET CARD ==================== -->
        <div class="worksheet-card bg-white rounded-2xl border-2 border-slate-800 shadow-lg p-5 sm:p-8 relative transition-all duration-300">

          <!-- Worksheet Top Header -->
          <div class="flex items-center justify-between border-b-2 border-slate-800 pb-4 mb-6">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 rounded-full bg-orange-600 text-white flex items-center justify-center font-serif font-black text-xl shadow-xs">
                <i class="fa-solid fa-music text-base"></i>
              </div>
              <div>
                <h2 id="sheetTitle" class="text-xl sm:text-2xl font-serif font-black text-slate-900 tracking-wide">【朋友歌】</h2>
                <p id="sheetCredits" class="text-xs text-slate-600 mt-1">作詞：陶大偉  作曲：陶大偉  演唱：陶大偉  1981</p>
              </div>
            </div>
            <div class="text-right">
            </div>
          </div>

          <!-- Lyrics Display Area -->
          <div class="space-y-2 text-base sm:text-lg leading-normal font-serif text-slate-800 tracking-wide" id="lyricsContainer">
            <!-- Rendered by JS -->
          </div>

          <!-- Worksheet Key Question & Reflection Section -->
          <div id="reflectionSec" class="mt-8 pt-6 border-t-2 border-slate-300 space-y-5">

            <!-- Single Highlighter Question Section (請問這首歌要傳達的概念或最關鍵的句子是什麼？) -->
            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 sm:p-5 space-y-3">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
                <label class="font-serif font-bold text-sm sm:text-base text-slate-900 flex items-center gap-2">
                  <i class="fa-solid fa-highlighter text-amber-500"></i>
                  <span class="bg-amber-100/90 text-amber-950 px-2.5 py-0.5 rounded font-bold">請問這首歌要傳達的概念或最關鍵的句子是什麼？</span>
                </label>
                <!-- 點選切換顯示/隱藏參考解答按鈕 -->
                <button type="button" onclick="toggleKeySentenceAnswer()" id="keyAnsToggleBtn" class="self-start sm:self-auto px-3 py-1 rounded-lg text-xs font-bold bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-300 transition-all flex items-center gap-1.5 cursor-pointer shadow-2xs active:scale-95">
                  <i id="keyAnsIcon" class="fa-regular fa-lightbulb text-amber-600"></i>
                  <span id="keyAnsText">查看關鍵句解答</span>
                </button>
              </div>

              <!-- 隱藏的參考解答區（點選按鈕後展開顯示） -->
              <div id="keySentenceAnswerBox" class="hidden p-3.5 rounded-xl border-2 border-dashed border-amber-300 bg-amber-50/90 transition-all">
                <div class="flex items-center gap-2 mb-2">
                  <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500 text-white flex items-center gap-1">
                    <i class="fa-solid fa-check"></i>
                    <span>教用學習單螢光筆解答</span>
                  </span>
                </div>
                <div id="keySentenceAnswerText" class="font-handwriting text-rose-600 font-bold text-base sm:text-lg tracking-wide leading-relaxed pl-1 whitespace-pre-line">
                </div>
              </div>
            </div>

            <!-- Emotion Chips -->
            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-2.5">
              <label class="font-serif font-bold text-xs sm:text-sm text-slate-800 flex items-center gap-1.5">
                <i class="fa-regular fa-face-smile text-orange-600"></i>
                <span>這首歌讓我覺得：</span>
              </label>
              <div class="flex flex-wrap gap-2 text-xs" id="emotionContainer">
                <button onclick="toggleEmotion(this, '豁達開朗')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-amber-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>😄</span>
                  <span>豁達開朗</span>
                </button>
                <button onclick="toggleEmotion(this, '溫暖感動')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-rose-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>💖</span>
                  <span>溫暖感動</span>
                </button>
                <button onclick="toggleEmotion(this, '攜手同行')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-blue-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>🤝</span>
                  <span>攜手同行</span>
                </button>
                <button onclick="toggleEmotion(this, '熱血沸騰')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-emerald-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>🔥</span>
                  <span>熱血沸騰</span>
                </button>
                <button onclick="toggleEmotion(this, '珍惜感恩')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-indigo-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>🌟</span>
                  <span>珍惜感恩</span>
                </button>
                <button onclick="toggleEmotion(this, '堅定守護')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-amber-100 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>🛡️</span>
                  <span>堅定守護</span>
                </button>
              </div>
            </div>

          </div>

        </div>

      </div>

    </div>

  </main>

  <!-- ==================== FOOTER (yuesilongmen-web-title-spec) ==================== -->
  <footer class="bg-slate-100 text-slate-600 py-6 border-t border-slate-200 mt-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex flex-wrap items-center justify-center sm:justify-start gap-2 sm:gap-3 text-center sm:text-left">
          <div class="flex items-center space-x-2">
            <!-- 嚴格維持原生純方形，嚴禁 rounded-full -->
            <img src="assets/SSS_Stamp02.png" alt="國文寶典" class="w-8 h-8 object-contain shadow-xs">
            <span class="font-serif font-bold text-slate-800 text-base">七上國文寶典・歌SONG國文</span>
          </div>
          <span class="hidden sm:inline text-slate-300">|</span>
          <span class="text-xs text-slate-500 font-medium">聆聽友誼之歌・穿梭旋律與知音相伴的文學共鳴</span>
        </div>
        <div class="text-[11px] text-slate-500 font-medium">© 2026 學思軒 &gt;&lt;&gt; &gt;&lt;&gt; &gt;&lt;&gt; •••本網頁由黃于珊老師與AI協作生成，僅供教學使用。•••&lt;&gt;&lt; &lt;&gt;&lt; &lt;&gt;&lt;</div>
      </div>
    </div>
  </footer>

  <!-- Invisible Audio Element -->
  <audio id="audioPlayer" preload="auto"></audio>

  <!-- ==================== CLIENT LOGIC SCRIPT ==================== -->
  <script>
    // All Songs Data
    const songsData = {songs_json};
    let currentSongIndex = 0;
    let isPlaying = false;
    let isTeacherMode = false;
    let isKeySentenceRevealed = false;
    let isVideoMode = false;
    let revealedBlanks = new Set(); // Track revealed blank IDs

    // Initial song config
    const defaultSongId = "{default_song_id}";
    const hashSong = window.location.hash.replace('#', '') || (new URLSearchParams(window.location.search)).get('song');
    const targetSongId = hashSong || defaultSongId;
    const foundIdx = songsData.findIndex(s => s.id === targetSongId);
    if (foundIdx !== -1) currentSongIndex = foundIdx;

    // DOM Elements
    const audio = document.getElementById('audioPlayer');
    const video = document.getElementById('videoPlayer');
    const videoContainer = document.getElementById('videoContainer');
    const vinylContainer = document.getElementById('vinylContainer');
    const videoToggleBtn = document.getElementById('videoToggleBtn');
    const videoToggleText = document.getElementById('videoToggleText');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const playIcon = document.getElementById('playIcon');
    const vinylDisc = document.getElementById('vinylDisc');
    const vinylArm = document.getElementById('vinylArm');
    const progressBar = document.getElementById('progressBar');
    const progressHandle = document.getElementById('progressHandle');
    const currentTimeEl = document.getElementById('currentTime');
    const totalDurationEl = document.getElementById('totalDuration');
    const volumeSlider = document.getElementById('volumeSlider');
    const volumeIcon = document.getElementById('volumeIcon');

    // Initialize App
    window.addEventListener('DOMContentLoaded', () => {{
      renderTabs();
      renderSongListMenu();
      loadSong(currentSongIndex, false);
      setupAudioEvents();
      setupVideoEvents();
    }});

    // Render Song Navigation Tabs
    function renderTabs() {{
      const container = document.getElementById('songTabsContainer');
      container.innerHTML = songsData.map((song, idx) => {{
        const isActive = idx === currentSongIndex;
        return `
          <button onclick="switchSong(${{idx}}, false)" class="song-tab px-3.5 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all flex items-center gap-1.5 cursor-pointer ${{isActive ? 'bg-white text-orange-950 shadow-md font-bold ring-2 ring-orange-300' : 'bg-white/10 text-slate-200 hover:bg-white/20 hover:text-white'}}">
            <span class="w-1.5 h-1.5 rounded-full ${{isActive ? 'bg-orange-600' : 'bg-slate-300'}}"></span>
            <span>${{song.title}}</span>
          </button>
        `;
      }}).join('');
    }}

    // Render Quick Switch Menu
    function renderSongListMenu() {{
      const container = document.getElementById('songListMenu');
      container.innerHTML = songsData.map((song, idx) => {{
        const isActive = idx === currentSongIndex;
        const isThisPlaying = isActive && isPlaying;
        return `
          <div onclick="switchSong(${{idx}}, false)" class="group p-2 rounded-lg text-xs flex items-center justify-between cursor-pointer transition-all ${{isActive ? 'bg-orange-50 text-orange-950 font-bold border border-orange-200 shadow-2xs' : 'hover:bg-slate-50 text-slate-700'}}">
            <div class="flex items-center gap-2 min-w-0">
              <!-- Dedicated Play / Pause Button in List -->
              <button onclick="event.stopPropagation(); toggleListPlay(${{idx}})" 
                      class="w-6 h-6 rounded-full flex items-center justify-center transition-all shrink-0 cursor-pointer ${{isThisPlaying ? 'bg-orange-600 text-white shadow-xs' : isActive ? 'bg-orange-200 text-orange-800 hover:bg-orange-600 hover:text-white' : 'bg-slate-100 text-slate-500 hover:bg-orange-600 hover:text-white group-hover:bg-orange-100 group-hover:text-orange-700'}}" 
                      title="${{isThisPlaying ? '暫停播放' : '立即播放《' + song.title + '》'}}">
                <i class="fa-solid ${{isThisPlaying ? 'fa-pause text-[10px]' : 'fa-play text-[9px] ml-0.5'}}"></i>
              </button>
              <span class="w-4 text-center font-mono text-[11px] ${{isActive ? 'text-orange-600 font-bold' : 'text-slate-400'}}">${{idx + 1}}</span>
              <span class="truncate">${{song.title}}</span>
            </div>
            <div class="flex items-center gap-2 text-[10px] shrink-0">
              <span class="text-slate-400">${{song.artist}}</span>
            </div>
          </div>
        `;
      }}).join('');
    }}

    // Switch Song (defaults to autoPlay = false)
    function switchSong(index, autoPlay = false) {{
      if (index < 0 || index >= songsData.length) return;
      currentSongIndex = index;
      isKeySentenceRevealed = false; // Reset key sentence revelation
      
      // If was in video mode and new song doesn't have video, reset to audio
      if (isVideoMode && !songsData[currentSongIndex].video) {{
        isVideoMode = false;
        videoContainer.classList.add('hidden');
        vinylContainer.classList.remove('hidden');
        videoToggleText.textContent = "MV";
      }}

      renderTabs();
      renderSongListMenu();
      loadSong(currentSongIndex, autoPlay);
      updateKeySentenceUI();
    }}

    // Toggle Play from List Button
    function toggleListPlay(index) {{
      if (index === currentSongIndex) {{
        togglePlayPause();
      }} else {{
        switchSong(index, true);
      }}
    }}

    function prevSong() {{
      const newIdx = (currentSongIndex - 1 + songsData.length) % songsData.length;
      switchSong(newIdx, isPlaying);
    }}

    function nextSong() {{
      const newIdx = (currentSongIndex + 1) % songsData.length;
      switchSong(newIdx, isPlaying);
    }}

    // Toggle Video Mode (if video available)
    function toggleVideoMode() {{
      const song = songsData[currentSongIndex];
      if (!song.video) return;

      isVideoMode = !isVideoMode;
      if (isVideoMode) {{
        // Switch to Video
        audio.pause();
        videoContainer.classList.remove('hidden');
        vinylContainer.classList.add('hidden');
        videoToggleText.textContent = "黑膠";
        video.currentTime = audio.currentTime;
        if (isPlaying) video.play();
      }} else {{
        // Switch to Vinyl Audio
        video.pause();
        videoContainer.classList.add('hidden');
        vinylContainer.classList.remove('hidden');
        videoToggleText.textContent = "MV";
        audio.currentTime = video.currentTime;
        if (isPlaying) audio.play();
      }}
    }}

    // Load Song Data into View
    function loadSong(index, autoPlay = false) {{
      const song = songsData[index];
      
      // Reset blank trackers for this song unless in teacher mode
      if (!isTeacherMode) {{
        revealedBlanks.clear();
      }}

      // Stop current media
      audio.pause();
      audio.currentTime = 0;
      if (video) {{
        video.pause();
        video.currentTime = 0;
      }}

      // Reset progress bar display
      progressBar.style.width = '0%';
      progressHandle.style.left = '0%';
      currentTimeEl.textContent = '00:00';
      totalDurationEl.textContent = '--:--';

      // Player Info
      document.getElementById('playerOrderBadge').textContent = song.order;
      document.getElementById('playerTagBadge').textContent = song.tag;
      document.getElementById('playerSongTitle').textContent = song.title;
      document.getElementById('vinylSongTitle').textContent = song.title;
      document.getElementById('playerArtist').textContent = `演唱：${{song.artist}}・${{song.year}}`;
      document.getElementById('playerSongIntro').textContent = song.intro;
      document.getElementById('metaLyricist').textContent = `作詞：${{song.lyricist}}`;
      document.getElementById('metaComposer').textContent = `作曲：${{song.composer}}`;
      document.getElementById('metaArtist').textContent = `演唱：${{song.artist}}`;
      document.getElementById('metaYear').textContent = `發行：${{song.year}}`;

      // Video toggle button visibility
      if (song.video) {{
        videoToggleBtn.classList.remove('hidden');
        video.src = song.video;
        video.load();
      }} else {{
        videoToggleBtn.classList.add('hidden');
        if (isVideoMode) {{
          isVideoMode = false;
          videoContainer.classList.add('hidden');
          vinylContainer.classList.remove('hidden');
          videoToggleText.textContent = "MV";
        }}
      }}

      // Worksheet Info
      document.getElementById('sheetTitle').textContent = `【${{song.title}}】`;
      document.getElementById('sheetCredits').textContent = `作詞：${{song.lyricist}}  作曲：${{song.composer}}  演唱：${{song.artist}}  ${{song.year}}`;

      // Update Audio Source
      audio.src = song.audio;
      audio.load();

      // Render Lyrics
      renderLyrics(song);

      // Update Key Sentence UI
      updateKeySentenceUI();

      // Update completion label
      document.getElementById('overallCompletion').textContent = `進行中 (${{index + 1}}/${{songsData.length}})`;

      // Load saved emotion for this song
      loadSavedEmotion();

      if (autoPlay) {{
        playMedia();
      }} else {{
        pauseMedia();
      }}
    }}

    // Render Lyrics with Blank Boxes
    function renderLyrics(song) {{
      const container = document.getElementById('lyricsContainer');
      let html = '';
      let blankCounter = 0;

      song.lyrics.forEach((line) => {{
        if (line.type === 'space' || (Array.isArray(line) && line[0] && line[0].type === 'space')) {{
          html += '<div class="h-2.5 sm:h-3"></div>';
          return;
        }}

        html += '<div class="lyric-line py-0.5 flex flex-wrap items-center leading-normal">';
        line.forEach((chunk) => {{
          if (chunk.t) {{
            html += `<span class="inline-block">${{chunk.t}}</span>`;
          }} else if (chunk.b) {{
            blankCounter++;
            const blankId = `${{song.id}}-b-${{blankCounter}}`;
            const isRevealed = isTeacherMode || revealedBlanks.has(blankId);
            html += `
              <span id="${{blankId}}" onclick="toggleBlank('${{blankId}}', '${{chunk.b}}')" class="blank-box ${{isRevealed ? 'revealed' : ''}}" title="點擊翻開/隱藏答案">
                ${{isRevealed 
                  ? `<span class="revealed-text font-handwriting text-rose-600 font-bold text-lg sm:text-xl animate-in">${{chunk.b}}</span>` 
                  : `<span class="placeholder text-xs text-slate-400 font-sans tracking-normal">[ ${{chunk.h}} ]</span>`
                }}
              </span>
            `;
          }}
        }});
        html += '</div>';
      }});

      container.innerHTML = html;
    }}

    // Toggle Single Blank Box
    function toggleBlank(blankId, word) {{
      const el = document.getElementById(blankId);
      if (!el) return;

      if (revealedBlanks.has(blankId)) {{
        revealedBlanks.delete(blankId);
        el.classList.remove('revealed');
        el.innerHTML = `<span class="placeholder text-xs text-slate-400 font-sans tracking-normal">[ ${{word.length}}字 ]</span>`;
      }} else {{
        revealedBlanks.add(blankId);
        el.classList.add('revealed');
        el.innerHTML = `<span class="revealed-text font-handwriting text-rose-600 font-bold text-lg sm:text-xl animate-in">${{word}}</span>`;
      }}
    }}

    // Teacher Mode: Reveal All Blanks
    function toggleAllBlanks() {{
      isTeacherMode = !isTeacherMode;
      const btn = document.getElementById('toggleAllBtn');
      const btnText = document.getElementById('toggleAllBtnText');
      
      if (isTeacherMode) {{
        btn.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-rose-600 text-white shadow-sm cursor-pointer active:scale-95";
        btnText.textContent = "學生自修模式";
      }} else {{
        btn.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-rose-50 text-rose-700 hover:bg-rose-100 border border-rose-200 shadow-xs cursor-pointer active:scale-95";
        btnText.textContent = "一鍵揭曉教師版";
        revealedBlanks.clear();
      }}

      renderLyrics(songsData[currentSongIndex]);
      updateKeySentenceUI();
    }}

    // Reset All Blanks
    function resetAllBlanks() {{
      isTeacherMode = false;
      const btn = document.getElementById('toggleAllBtn');
      const btnText = document.getElementById('toggleAllBtnText');
      btn.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-rose-50 text-rose-700 hover:bg-rose-100 border border-rose-200 shadow-xs cursor-pointer active:scale-95";
      btnText.textContent = "一鍵揭曉教師版";
      revealedBlanks.clear();
      isKeySentenceRevealed = false;
      renderLyrics(songsData[currentSongIndex]);
      updateKeySentenceUI();
    }}

    // Key Sentence Answer Toggle
    function toggleKeySentenceAnswer() {{
      isKeySentenceRevealed = !isKeySentenceRevealed;
      updateKeySentenceUI();
    }}

    function updateKeySentenceUI() {{
      const box = document.getElementById('keySentenceAnswerBox');
      const textEl = document.getElementById('keySentenceAnswerText');
      const btnText = document.getElementById('keyAnsText');
      const btnIcon = document.getElementById('keyAnsIcon');
      const currentSong = songsData[currentSongIndex];

      if (textEl && currentSong) {{
        textEl.textContent = currentSong.keySentence || '';
      }}

      if (isTeacherMode || isKeySentenceRevealed) {{
        box.classList.remove('hidden');
        btnText.textContent = "隱藏關鍵句解答";
        btnIcon.className = "fa-solid fa-eye-slash text-amber-700";
      }} else {{
        box.classList.add('hidden');
        btnText.textContent = "查看關鍵句解答";
        btnIcon.className = "fa-regular fa-lightbulb text-amber-600";
      }}
    }}

    // Emotion Chips Selection
    function toggleEmotion(btn, emotion) {{
      const currentSong = songsData[currentSongIndex];
      const storageKey = `song_emotion_${{currentSong.id}}`;
      
      const allBtns = document.querySelectorAll('.emotion-chip');
      const wasActive = btn.classList.contains('active-emotion');

      allBtns.forEach(b => {{
        b.classList.remove('active-emotion', 'ring-2', 'ring-orange-500', 'bg-orange-100', 'font-bold');
      }});

      if (!wasActive) {{
        btn.classList.add('active-emotion', 'ring-2', 'ring-orange-500', 'bg-orange-100', 'font-bold');
        localStorage.setItem(storageKey, emotion);
      }} else {{
        localStorage.removeItem(storageKey);
      }}
    }}

    function loadSavedEmotion() {{
      const currentSong = songsData[currentSongIndex];
      const storageKey = `song_emotion_${{currentSong.id}}`;
      const savedEmotion = localStorage.getItem(storageKey);

      const allBtns = document.querySelectorAll('.emotion-chip');
      allBtns.forEach(b => {{
        b.classList.remove('active-emotion', 'ring-2', 'ring-orange-500', 'bg-orange-100', 'font-bold');
        if (savedEmotion && b.textContent.includes(savedEmotion)) {{
          b.classList.add('active-emotion', 'ring-2', 'ring-orange-500', 'bg-orange-100', 'font-bold');
        }}
      }});
    }}

    // Media Playback Controls
    function togglePlayPause() {{
      if (isPlaying) {{
        pauseMedia();
      }} else {{
        playMedia();
      }}
    }}

    function playMedia() {{
      if (isVideoMode && video) {{
        video.play();
      }} else {{
        audio.play().catch(e => console.log('Audio playback prevented:', e));
      }}
      isPlaying = true;
      playIcon.className = "fa-solid fa-pause text-white";
      vinylDisc.classList.add('animate-spin-slow');
      vinylArm.classList.add('playing');
      renderSongListMenu();
    }}

    function pauseMedia() {{
      if (isVideoMode && video) {{
        video.pause();
      }} else {{
        audio.pause();
      }}
      isPlaying = false;
      playIcon.className = "fa-solid fa-play ml-1 text-white";
      vinylDisc.classList.remove('animate-spin-slow');
      vinylArm.classList.remove('playing');
      renderSongListMenu();
    }}

    function skipTime(seconds) {{
      const targetMedia = isVideoMode ? video : audio;
      targetMedia.currentTime = Math.max(0, Math.min(targetMedia.duration || 0, targetMedia.currentTime + seconds));
    }}

    function setSpeed(rate, btn) {{
      audio.playbackRate = rate;
      if (video) video.playbackRate = rate;
      document.querySelectorAll('.speed-btn').forEach(b => {{
        b.className = "speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-white/10 hover:bg-white/20 text-slate-300";
      }});
      btn.className = "speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-orange-600 text-white font-bold";
    }}

    function changeVolume(val) {{
      audio.volume = val;
      if (video) video.volume = val;
      updateVolumeIcon(val);
    }}

    function toggleMute() {{
      const targetMedia = isVideoMode ? video : audio;
      if (targetMedia.volume > 0) {{
        targetMedia.dataset.lastVol = targetMedia.volume;
        targetMedia.volume = 0;
        volumeSlider.value = 0;
      }} else {{
        const restored = targetMedia.dataset.lastVol || 1;
        targetMedia.volume = restored;
        volumeSlider.value = restored;
      }}
      updateVolumeIcon(targetMedia.volume);
    }}

    function updateVolumeIcon(vol) {{
      if (vol == 0) {{
        volumeIcon.className = "fa-solid fa-volume-xmark";
      }} else if (vol < 0.5) {{
        volumeIcon.className = "fa-solid fa-volume-low";
      }} else {{
        volumeIcon.className = "fa-solid fa-volume-high";
      }}
    }}

    function seekAudio(e) {{
      const targetMedia = isVideoMode ? video : audio;
      if (!targetMedia.duration) return;
      const rect = e.currentTarget.getBoundingClientRect();
      const pos = (e.clientX - rect.left) / rect.width;
      targetMedia.currentTime = pos * targetMedia.duration;
    }}

    function setupAudioEvents() {{
      audio.addEventListener('timeupdate', () => {{
        if (!isVideoMode) updateProgress(audio);
      }});
      audio.addEventListener('ended', () => {{
        nextSong();
      }});
    }}

    function setupVideoEvents() {{
      if (!video) return;
      video.addEventListener('timeupdate', () => {{
        if (isVideoMode) updateProgress(video);
      }});
      video.addEventListener('ended', () => {{
        nextSong();
      }});
    }}

    function updateProgress(media) {{
      if (!media.duration) return;
      const pct = (media.currentTime / media.duration) * 100;
      progressBar.style.width = pct + '%';
      progressHandle.style.left = pct + '%';
      currentTimeEl.textContent = formatTime(media.currentTime);
      totalDurationEl.textContent = formatTime(media.duration);
    }}

    function formatTime(sec) {{
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return `${{m < 10 ? '0' : ''}}${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
    }}
  </script>

  <!-- ==================== WORKSHEET MODAL SYSTEM ==================== -->
  <div id="worksheetModal" class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs hidden items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl border border-slate-200 space-y-5 relative max-h-[90vh] overflow-y-auto">
      
      <!-- Close Button -->
      <button onclick="closeWorksheetModal()" class="absolute top-5 right-5 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500 hover:text-slate-800 flex items-center justify-center transition-colors cursor-pointer" title="關閉">
        <i class="fa-solid fa-xmark text-sm"></i>
      </button>

      <!-- Modal Header -->
      <div class="flex items-center gap-3 pr-8">
        <div id="wsModalIconBox" class="w-12 h-12 rounded-2xl flex items-center justify-center text-xl shrink-0 shadow-xs">
          <i id="wsModalIcon" class="fa-solid fa-file-pen"></i>
        </div>
        <div class="min-w-0">
          <div class="flex items-center gap-2">
            <span id="wsModalBadge" class="px-2.5 py-0.5 rounded-full text-[11px] font-bold">單元</span>
            <span id="wsModalTypeTag" class="px-2 py-0.5 rounded-full text-[10px] font-bold">學用學習單</span>
          </div>
          <h3 id="wsModalTitle" class="text-lg sm:text-xl font-serif font-bold text-slate-900 mt-1 truncate">學習單線上預覽與下載</h3>
        </div>
      </div>

      <!-- Hint banner -->
      <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-600 flex items-center justify-between gap-2">
        <span class="flex items-center gap-1.5">
          <i class="fa-regular fa-lightbulb text-amber-500"></i>
          點擊「線上預覽」另開分頁檢視，點擊「下載」儲存 PDF。
        </span>
        <span class="text-[10px] text-slate-400 font-mono shrink-0">PDF 格式</span>
      </div>

      <!-- Worksheets Container -->
      <div id="wsModalList" class="space-y-2.5">
        <!-- Dynamically rendered -->
      </div>

      <!-- Modal Footer -->
      <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
        <span class="text-[11px] text-slate-400">學思軒・閱思龍門專用教材</span>
        <button onclick="closeWorksheetModal()" class="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition-colors cursor-pointer">
          關閉視窗
        </button>
      </div>
    </div>
  </div>

  <script>
    // Worksheet Modal System
    const unitWorksheetMeta = {worksheet_json};

    function openWorksheetModal(type) {{
      const isStudent = (type === 'student');
      const typeText = isStudent ? '學用學習單' : '教用學習單';
      const iconClass = isStudent ? 'fa-solid fa-file-pen' : 'fa-solid fa-graduation-cap';
      const iconBoxBg = isStudent ? 'bg-amber-100 text-amber-800' : 'bg-rose-100 text-rose-800';
      const typeTagBg = isStudent ? 'bg-amber-500 text-white' : 'bg-slate-800 text-white';

      document.getElementById('wsModalBadge').textContent = unitWorksheetMeta.unitName;
      document.getElementById('wsModalBadge').className = 'px-2.5 py-0.5 rounded-full text-[11px] font-bold ' + unitWorksheetMeta.badgeClass;

      document.getElementById('wsModalTypeTag').textContent = typeText;
      document.getElementById('wsModalTypeTag').className = 'px-2 py-0.5 rounded-full text-[10px] font-bold ' + typeTagBg;

      document.getElementById('wsModalTitle').textContent = unitWorksheetMeta.unitName + '・' + typeText;

      const iconBox = document.getElementById('wsModalIconBox');
      iconBox.className = 'w-12 h-12 rounded-2xl flex items-center justify-center text-xl shrink-0 shadow-xs ' + iconBoxBg;
      document.getElementById('wsModalIcon').className = iconClass;

      let listHtml = '<div class="pt-1">' +
        '<div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2 flex items-center justify-between">' +
          '<span>單曲個別學習單 (' + unitWorksheetMeta.songs.length + ' 首)</span>' +
          '<span class="text-slate-400 font-normal text-[10px]">可獨立預覽或下載</span>' +
        '</div>' +
        '<div class="space-y-2">';

      unitWorksheetMeta.songs.forEach(function(song, idx) {{
        const fileUrl = song[type];
        const isCurrent = (typeof currentSongIndex !== 'undefined' && idx === currentSongIndex);
        const cardBg = isCurrent ? 'bg-amber-50/70 border-amber-300 ring-1 ring-amber-300' : 'bg-slate-50 hover:bg-slate-100/80 border-slate-200';
        const numBg = isCurrent ? 'bg-amber-500 text-white' : 'bg-white text-slate-700 border border-slate-200';
        const currentBadge = isCurrent ? '<span class="px-1.5 py-0.2 text-[9px] font-bold bg-amber-200 text-amber-900 rounded">目前播放</span>' : '';

        listHtml += '<div class="p-3 rounded-xl ' + cardBg + ' border transition-all flex items-center justify-between gap-2">' +
          '<div class="flex items-center gap-2.5 min-w-0">' +
            '<span class="w-5 h-5 rounded-full ' + numBg + ' text-[10px] font-bold flex items-center justify-center shrink-0">' + song.id + '</span>' +
            '<div class="min-w-0">' +
              '<div class="flex items-center gap-1.5">' +
                '<span class="font-bold text-slate-800 text-xs sm:text-sm truncate">' + song.title + '</span>' +
                currentBadge +
              '</div>' +
              '<div class="text-[10px] text-slate-400 truncate">' + song.artist + '</div>' +
            '</div>' +
          '</div>' +
          '<div class="flex items-center gap-1.5 shrink-0">' +
            '<a href="' + fileUrl + '" target="_blank" rel="noopener noreferrer" class="py-1 px-2.5 rounded-lg bg-white hover:bg-slate-200/70 border border-slate-200 text-slate-700 font-medium text-xs flex items-center gap-1 transition-all" title="線上預覽">' +
              '<i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>' +
              '<span>預覽</span>' +
            '</a>' +
            '<a href="' + fileUrl + '" download class="py-1 px-2.5 rounded-lg bg-slate-800 hover:bg-slate-900 text-white font-medium text-xs flex items-center gap-1 transition-all" title="下載 PDF">' +
              '<i class="fa-solid fa-download text-[10px]"></i>' +
              '<span>下載</span>' +
            '</a>' +
          '</div>' +
        '</div>';
      }});

      listHtml += '</div></div>';

      document.getElementById('wsModalList').innerHTML = listHtml;

      const modal = document.getElementById('worksheetModal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }}

    function closeWorksheetModal() {{
      const modal = document.getElementById('worksheetModal');
      if (modal) {{
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }}
    }}

    window.addEventListener('click', function(e) {{
      const wsModal = document.getElementById('worksheetModal');
      if (e.target === wsModal) {{
        closeWorksheetModal();
      }}
    }});

    window.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        closeWorksheetModal();
      }}
    }});
  </script>
</body>
</html>
"""

# Generate HTML files
files_to_generate = [
    ("index.html", "friends-song"),
    ("friends-song.html", "friends-song"),
    ("walk-together.html", "walk-together"),
    ("superman-cape.html", "superman-cape"),
]

for filename, default_id in files_to_generate:
    filepath = os.path.join(TARGET_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(generate_html(default_id))
    print(f"Generated HTML: {filename} (default: {default_id})")

print("All tasks completed successfully for B01L08朋友相交好歌!")
