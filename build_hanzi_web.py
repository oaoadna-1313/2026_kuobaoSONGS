import os
import sys
import shutil
import json

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\2026_歌SONG國文"
TARGET_DIR = os.path.join(BASE_DIR, "B02L語一漢字的結構好歌")
ASSETS_SRC = os.path.join(BASE_DIR, "assets")
MATERIAL_DIR = os.path.join(BASE_DIR, "材料", "B2_SONG", "[國寶講義]B02L語一漢字的結構好歌")

# Create target directories
os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "assets"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "media"), exist_ok=True)

# 1. Copy Assets
for asset_name in ["baoden.png", "badge-songlogo.PNG", "SSS_Stamp01.png", "SSS_Stamp02.png", "logo-gesong-bird.svg"]:
    src = os.path.join(ASSETS_SRC, asset_name)
    dst = os.path.join(TARGET_DIR, "assets", asset_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied asset: {asset_name}")

# 2. Copy Media
media_mapping = {
    "漢字的結構好歌-01倉頡-五月天.mp3": "cang-jie.mp3",
    "漢字的結構好歌-02生僻字-陳柯宇.mp3": "shengpi-zi.mp3"
}

for src_name, dst_name in media_mapping.items():
    src = os.path.join(MATERIAL_DIR, src_name)
    dst = os.path.join(TARGET_DIR, "media", dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied media: {src_name} -> {dst_name}")

# 3. Copy PDFs
pdf_mapping = {
    "08[國寶講義]B02L語一漢字的結構好歌-01倉頡.pdf": "worksheet-cang-jie.pdf",
    "08[國寶講義]B02L語一漢字的結構好歌-02生僻字.pdf": "worksheet-shengpi-zi.pdf"
}

for src_name, dst_name in pdf_mapping.items():
    src = os.path.join(MATERIAL_DIR, src_name)
    dst = os.path.join(TARGET_DIR, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied PDF: {src_name} -> {dst_name}")

# Define songsData
songsData = [
    {
        "id": "cang-jie",
        "title": "倉頡",
        "artist": "五月天",
        "lyricist": "阿信",
        "composer": "石頭",
        "year": "2011",
        "album": "第二人生 (Second Round)",
        "tag": "神話傳說・文字力量與思念",
        "order": "第一曲",
        "sheet": "好歌學習單 第18頁",
        "audio": "media/cang-jie.mp3",
        "video": None,
        "bgGradient": "from-amber-600 via-orange-600 to-stone-900",
        "lightBg": "bg-amber-50/70 border-amber-200",
        "intro": "五月天收錄於2011年《第二人生》專輯的經典磅礴之作。以傳說中造字的史官「倉頡」為意象，訴說當面對摯愛離去與文明荒蕪時，千言萬語在極度想念面前皆顯得蒼白無力。歌曲巧妙融入結繩記事、烽火狼煙、倉頡造字天雨粟鬼夜哭等深厚歷史典故，扣合《漢字的結構》六書象形、指事、會意、形聲之造字源起，展現文字超越時空、永恆傳遞思念的磅礴力量。",
        "lyrics": [
            [{"t": "一顆"}, {"b": "葡萄", "h": "2字"}, {"t": "有多甜美  用盡了所有的 "}, {"b": "圖騰", "h": "2字"}, {"t": "和"}, {"b": "語言", "h": "2字"}, {"t": " 描寫"}],
            [{"t": "想一個人有多想念  那又是文字"}, {"b": "失效", "h": "2字"}, {"t": "瞬間"}],
            [{"type": "space"}],
            [{"t": "結一個紀念的繩結 記錄你離去後 萬語和千言 "}, {"b": "瓦解", "h": "2字"}],
            [{"t": "升起了慌張的"}, {"b": "狼煙", "h": "2字"}, {"t": " 我遺落在最孤獨史前的"}, {"b": "荒野", "h": "2字"}],
            [{"type": "space"}],
            [{"t": "多"}, {"b": "遙遠", "h": "2字"}, {"t": " 多"}, {"b": "糾結", "h": "2字"}, {"t": " 多"}, {"b": "想念", "h": "2字"}, {"t": " 多"}, {"b": "無法描寫", "h": "4字"}, {"t": " 疼痛 和瘋癲  你都看不見"}],
            [{"t": "想"}, {"b": "穿越", "h": "2字"}, {"t": " 想"}, {"b": "飛天", "h": "2字"}, {"t": " 想變成 造字的"}, {"b": "倉頡", "h": "2字"}, {"t": "  寫出 能讓你快回來 的"}, {"b": "詩篇", "h": "2字"}],
            [{"type": "space"}],
            [{"t": "一隻"}, {"b": "蝴蝶", "h": "2字"}, {"t": "有多鮮豔 能不能飛越過 "}, {"b": "猜忌", "h": "2字"}, {"t": "和"}, {"b": "冷漠", "h": "2字"}, {"t": " 世界"}],
            [{"t": "給你的簡訊和留言 說不清萬分之一"}, {"b": "追悔", "h": "2字"}],
            [{"type": "space"}],
            [{"t": "當"}, {"b": "星宿", "h": "2字"}, {"t": "都"}, {"b": "沉沒", "h": "2字"}, {"t": "山岳 只盼你會抬頭 看我"}, {"b": "寄託", "h": "2字"}, {"t": "的 彎月"}],
            [{"t": "當一個文明即將"}, {"b": "熄滅", "h": "2字"}, {"t": " 有什麼證明你我存在 的歲月"}],
            [{"type": "space"}],
            [{"t": "多遙遠 多糾結 多想念 多無法描寫 疼痛 和瘋癲 你都看不見"}],
            [{"t": "想穿越 想飛天 想變成 造字的倉頡  創造 能讓你想起我 的字眼"}],
            [{"type": "space"}],
            [{"t": "多遙遠 多糾結 多想念 多無法描寫  疼痛 和瘋癲 你都看不見"}],
            [{"t": "想穿越 想飛天 想變成 造字的倉頡  寫出 能讓你快回來 的詩"}],
            [{"type": "space"}],
            [{"t": "需要你 需要你 需要你 想逆轉時間  回到 最開始 有你的世界"}],
            [{"t": "想穿越 想飛天 想變成 造字的倉頡  寫出 讓宇宙能重來 的詩篇"}],
            [{"type": "space"}],
            [{"t": "天雨"}, {"b": "粟", "h": "1字"}, {"t": "  鬼夜哭  "}, {"b": "思念", "h": "2字"}, {"t": "漫太古"}]
        ],
        "keySentence": "想一個人有多想念 那又是文字失效瞬間\n想變成 造字的倉頡 寫出 能讓你快回來 的詩\n天雨粟 鬼夜哭 思念漫太古"
    },
    {
        "id": "shengpi-zi",
        "title": "生僻字",
        "artist": "陳柯宇",
        "lyricist": "陳柯宇",
        "composer": "陳柯宇",
        "year": "2018",
        "album": "生僻字 單曲",
        "tag": "漢字奇蹟・音韻與造字之美",
        "order": "第二曲",
        "sheet": "好歌學習單 第19頁",
        "audio": "media/shengpi-zi.mp3",
        "video": None,
        "bgGradient": "from-orange-600 via-amber-600 to-stone-900",
        "lightBg": "bg-orange-50/70 border-orange-200",
        "intro": "由陳柯宇作詞作曲並演唱的網路爆紅神曲。創作者將70多個常見卻常讀錯或結構精巧的生僻漢字、疊字（二疊字、三疊字、四疊字如又双叒叕、火炎焱燚、水沝淼㵘）以及古典成語串聯成朗朗上口的旋律。歌詞讚頌「我們中國的漢字，落筆成畫留下五千年的歷史，一撇一捺都是故事」，完美呼應《漢字的結構》對漢字形音義兼備、結構美學與文化底蘊的探究。",
        "lyrics": [
            [{"t": "我們中國的漢字  落筆成畫留下五千年的歷史  讓世界都認識"}],
            [{"t": "我們中國的漢字  一撇一捺都是故事"}],
            [{"type": "space"}],
            [{"t": "跪舉火把虔誠像道光  四方田地落穀成倉"}],
            [{"t": "古人象形聲意辨惡良  魃魈魁鬾魑魅魍魎"}],
            [{"t": "Wu 又双叒叕  Wu 火炎焱燚  Wu 水沝淼㵘  㙓𨰻"}],
            [{"type": "space"}],
            [{"t": "煢煢孑立沆瀣一氣 踽踽獨行 醍醐灌頂"}],
            [{"t": "綿綿瓜瓞 奉為圭臬  龍行龘龘 犄角旮旯"}],
            [{"t": "娉婷裊娜 涕泗滂沱 呶呶不休 不稂不莠"}],
            [{"t": "卬  咄嗟 蹀躞 耄耋 饕餮 囹圄 蘡薁 覬覦 齟齬"}],
            [{"t": "狖軛鼯軒 怙惡不悛 其靁虺虺 腌臢孑孓"}],
            [{"t": "陟罰臧否 針砭時弊 鱗次櫛比 一張一翕"}],
            [{"type": "space"}],
            [{"t": "我們中國的漢字  落筆成畫留下五千年的歷史 讓世界都認識"}],
            [{"t": "我們中國的漢字  一撇一捺都是故事"}],
            [{"type": "space"}],
            [{"t": "現在全世界各地  到處有中國字  黃皮膚的人驕傲地把頭抬起"}],
            [{"t": "我們中國的漢字  一平一仄譜寫成詩"}],
            [{"type": "space"}],
            [{"t": "優美旋律自宮商角徵羽  眾人皆說成之於語故成語"}]
        ],
        "keySentence": "我們中國的漢字 落筆成畫留下五千年的歷史 讓世界都認識\n我們中國的漢字 一撇一捺都是故事\n現在全世界各地 到處有中國字 黃皮膚的人驕傲地把頭抬起\n我們中國的漢字 一平一仄譜寫成詩"
    }
]

unitWorksheetMeta = {
    "unitName": "八下國文・語一 漢字的結構",
    "badgeClass": "bg-amber-100 text-amber-900 border border-amber-300",
    "songs": [
        {"id": 1, "title": "倉頡", "artist": "五月天", "student": "worksheet-cang-jie.pdf", "teacher": "worksheet-cang-jie.pdf"},
        {"id": 2, "title": "生僻字", "artist": "陳柯宇", "student": "worksheet-shengpi-zi.pdf", "teacher": "worksheet-shengpi-zi.pdf"}
    ]
}

def build_page_html(default_song_id="cang-jie"):
    songs_json = json.dumps(songsData, ensure_ascii=False)
    meta_json = json.dumps(unitWorksheetMeta, ensure_ascii=False)
    
    html = f'''<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【八下閱思龍門】歌SONG國文・語一 漢字的結構 好歌互動教學平台</title>
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
      <!-- Brand & Title (純方形印章，絕無 rounded-full) -->
      <div class="flex items-center space-x-3">
        <a href="index.html" class="flex items-center space-x-2.5 group" title="返回歌SONG國文教學首頁">
          <!-- 嚴格維持原生純方形圖案，嚴禁 rounded-full -->
          <img src="assets/SSS_Stamp02.png" alt="學思軒" class="w-10 h-10 object-contain shadow-sm group-hover:rotate-6 transition-transform duration-300">
          <div>
            <div class="flex items-center space-x-2">
              <span class="font-serif font-bold text-lg sm:text-xl text-slate-900 tracking-wide">歌SONG國文</span>
              <span class="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-amber-100 text-amber-900 border border-amber-300">八下國文・語一 漢字的結構</span>
            </div>
            <p class="text-[11px] text-slate-500 font-medium hidden md:block">漢字奧妙・六書造字與形音義的千年交響</p>
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
            <h1 class="text-sm sm:text-base font-serif font-bold text-amber-100 tracking-wide">一撇一捺與六書奧妙的千年交響</h1>
            <p class="text-xs text-orange-100/90 mt-0.5">結合語文常識一《漢字的結構》課文賞析，聆聽五月天《倉頡》與陳柯宇《生僻字》的音樂故事，邊聽音樂邊探索六書造字奇蹟與深邃思念</p>
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
              <span id="playerTagBadge" class="px-2.5 py-0.5 text-xs font-medium rounded-full bg-amber-100 text-amber-800">神話傳說・文字力量與思念</span>
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

            <!-- Vinyl Record Turntable Animation Container -->
            <div id="vinylContainer" class="relative w-56 h-56 sm:w-64 sm:h-64 my-2 flex items-center justify-center select-none">
              <!-- Turntable Base -->
              <div class="absolute inset-0 rounded-full bg-stone-800/80 shadow-2xl border border-stone-700"></div>
              
              <!-- Vinyl Disc -->
              <div id="vinylDisc" class="w-48 h-48 sm:w-56 sm:h-56 rounded-full bg-stone-950 border-4 border-stone-800 shadow-2xl flex items-center justify-center relative overflow-hidden transition-transform duration-500">
                <!-- Vinyl Grooves -->
                <div class="absolute inset-2 rounded-full border border-stone-800/60"></div>
                <div class="absolute inset-5 rounded-full border border-stone-800/80"></div>
                <div class="absolute inset-8 rounded-full border border-stone-800/60"></div>
                <div class="absolute inset-12 rounded-full border border-stone-800/80"></div>
                <div class="absolute inset-16 rounded-full border border-stone-800/60"></div>

                <!-- Center Vinyl Label (Styled dynamically by song) -->
                <div id="vinylCenterLabel" class="w-20 h-20 sm:w-24 sm:h-24 rounded-full bg-gradient-to-tr from-amber-600 via-orange-500 to-amber-700 flex flex-col items-center justify-center text-center p-2 shadow-inner border-2 border-stone-900 z-10">
                  <span id="vinylSongTitle" class="text-[11px] sm:text-xs font-serif font-black text-amber-100 truncate w-full px-1">倉頡</span>
                  <span id="vinylArtist" class="text-[9px] text-amber-200/90 truncate w-full mt-0.5">五月天</span>
                  <div class="w-3 h-3 rounded-full bg-stone-950 border border-amber-300/40 mt-1"></div>
                </div>
              </div>

              <!-- Turntable Tonearm (Stylus Needle) -->
              <div id="vinylArm" class="vinyl-arm absolute right-2 top-2 w-16 h-28 pointer-events-none z-20">
                <svg viewBox="0 0 60 110" class="w-full h-full drop-shadow-md">
                  <!-- Pivot Base -->
                  <circle cx="45" cy="15" r="10" fill="#78716c" stroke="#44403c" stroke-width="2"/>
                  <circle cx="45" cy="15" r="5" fill="#d6d3d1"/>
                  <!-- Tone arm stick -->
                  <path d="M45,15 L25,75 L20,95" fill="none" stroke="#e7e5e4" stroke-width="3" stroke-linecap="round"/>
                  <!-- Cartridge headshell & stylus -->
                  <rect x="14" y="92" width="12" height="15" rx="2" fill="#ea580c" transform="rotate(-15 20 95)"/>
                </svg>
              </div>
            </div>

            <!-- Current Song Title & Meta Under Turntable -->
            <div class="mt-4 text-center space-y-1 relative z-10">
              <h3 id="playerSongTitle" class="text-xl sm:text-2xl font-serif font-bold text-white tracking-wide">倉頡</h3>
              <p id="playerArtistMeta" class="text-xs sm:text-sm text-stone-300">五月天 ・ 2011年《第二人生》</p>
            </div>

            <!-- Audio Progress Bar & Time Stamps -->
            <div class="w-full mt-5 space-y-1 relative z-10">
              <div class="relative h-2 bg-stone-800 rounded-full cursor-pointer group" id="progressBarContainer" onclick="seekAudio(event)">
                <div id="progressBar" class="absolute top-0 left-0 h-full bg-gradient-to-r from-amber-500 to-orange-500 rounded-full w-0 transition-all duration-100"></div>
                <div id="progressHandle" class="absolute top-1/2 -mt-2 -ml-2 w-4 h-4 bg-white rounded-full shadow-md opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none"></div>
              </div>
              <div class="flex justify-between text-[11px] font-mono text-stone-400 pt-0.5">
                <span id="currentTime">00:00</span>
                <span id="totalDuration">--:--</span>
              </div>
            </div>

            <!-- Playback Controls -->
            <div class="flex items-center justify-center space-x-5 mt-4 relative z-10">
              <!-- Rewind 5s -->
              <button onclick="skipTime(-5)" class="text-stone-300 hover:text-white transition-transform active:scale-90 p-2 cursor-pointer" title="倒退 5 秒">
                <i class="fa-solid fa-rotate-left text-base"></i>
              </button>
              
              <!-- Main Play/Pause Button -->
              <button id="playPauseBtn" onclick="togglePlay()" class="w-14 h-14 rounded-full bg-gradient-to-r from-amber-500 to-orange-600 hover:from-amber-400 hover:to-orange-500 text-white flex items-center justify-center shadow-lg transition-all duration-300 hover:scale-105 active:scale-95 cursor-pointer" title="播放 / 暫停">
                <i id="playIcon" class="fa-solid fa-play text-xl ml-0.5"></i>
              </button>

              <!-- Forward 5s -->
              <button onclick="skipTime(5)" class="text-stone-300 hover:text-white transition-transform active:scale-90 p-2 cursor-pointer" title="快進 5 秒">
                <i class="fa-solid fa-rotate-right text-base"></i>
              </button>
            </div>

            <!-- Playback Rate & Volume Controls -->
            <div class="w-full flex items-center justify-between pt-4 mt-4 border-t border-stone-800/80 text-xs text-stone-400 relative z-10">
              <!-- Speed Selector -->
              <div class="flex items-center space-x-1">
                <span class="text-[11px] text-stone-500">倍速:</span>
                <button onclick="setPlaybackSpeed(0.8)" class="speed-btn px-1.5 py-0.5 rounded hover:bg-stone-800 text-stone-400 font-mono transition-colors">0.8x</button>
                <button onclick="setPlaybackSpeed(1.0)" class="speed-btn active px-1.5 py-0.5 rounded bg-stone-800 text-amber-400 font-mono font-bold transition-colors">1.0x</button>
                <button onclick="setPlaybackSpeed(1.2)" class="speed-btn px-1.5 py-0.5 rounded hover:bg-stone-800 text-stone-400 font-mono transition-colors">1.2x</button>
              </div>

              <!-- Volume Slider -->
              <div class="flex items-center space-x-2">
                <button onclick="toggleMute()" class="hover:text-white transition-colors" title="靜音切換">
                  <i id="volumeIcon" class="fa-solid fa-volume-high text-sm"></i>
                </button>
                <input type="range" id="volumeSlider" min="0" max="1" step="0.05" value="0.85" oninput="changeVolume(this.value)" class="w-16 sm:w-20 accent-orange-500 h-1 bg-stone-700 rounded-lg cursor-pointer">
              </div>
            </div>

          </div>

          <!-- Song Background & Literary Appreciation Card -->
          <div class="p-5 bg-stone-50 border-t border-slate-100 space-y-3">
            <div class="flex items-center space-x-2 text-slate-800">
              <i class="fa-solid fa-book-open text-orange-600 text-sm"></i>
              <h4 class="font-serif font-bold text-sm tracking-wide">歌曲背景與文學導讀</h4>
            </div>
            <p id="songIntroText" class="text-xs sm:text-sm text-slate-600 leading-relaxed font-sans text-justify">
              五月天收錄於2011年《第二人生》專輯的經典磅礴之作。以傳說中造字的史官「倉頡」為意象，訴說當面對摯愛離去與文明荒蕪時，千言萬語在極度想念面前皆顯得蒼白無力。歌曲巧妙融入結繩記事、烽火狼煙、倉頡造字天雨粟鬼夜哭等深厚歷史典故，扣合《漢字的結構》六書象形、指事、會意、形聲之造字源起，展現文字超越時空、永恆傳遞思念的磅礴力量。
            </p>
          </div>
        </div>

        <!-- 全系列好歌學習地圖 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-slate-100">
            <h4 class="font-serif font-bold text-xs sm:text-sm text-slate-800 flex items-center gap-2">
              <i class="fa-solid fa-layer-group text-amber-600"></i>
              <span>全單元好歌學習地圖</span>
            </h4>
            <span class="text-[11px] text-slate-500">共 2 首精選好歌</span>
          </div>
          <div class="space-y-2" id="songListMenu">
            <!-- Dynamic song menu items rendered by JS -->
          </div>
        </div>

      </div>

      <!-- Right Column: Interactive Worksheet Card (7 cols) -->
      <div class="lg:col-span-7 space-y-6">

        <!-- ==================== MAIN WORKSHEET CONTAINER ==================== -->
        <div class="worksheet-card bg-white rounded-2xl border-2 border-slate-800 shadow-lg p-5 sm:p-8 relative transition-all duration-300">

          <!-- Worksheet Top Header -->
          <div class="flex items-center justify-between border-b-2 border-slate-800 pb-4 mb-6">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 rounded-full bg-orange-600 text-white flex items-center justify-center font-serif font-black text-xl shadow-xs">
                <i class="fa-solid fa-music text-base"></i>
              </div>
              <div>
                <h2 id="sheetTitle" class="text-xl sm:text-2xl font-serif font-black text-slate-900 tracking-wide">【倉頡】</h2>
                <p id="sheetCredits" class="text-xs text-slate-600 mt-1">作詞：阿信  作曲：石頭  演唱：五月天  2011</p>
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
                <button onclick="toggleEmotion(this, '震撼感動')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-amber-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>✨</span>
                  <span>震撼感動</span>
                </button>
                <button onclick="toggleEmotion(this, '穿越思念')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-rose-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>💖</span>
                  <span>穿越思念</span>
                </button>
                <button onclick="toggleEmotion(this, '讚嘆漢字')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-blue-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>📜</span>
                  <span>讚嘆漢字</span>
                </button>
                <button onclick="toggleEmotion(this, '文化自信')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-emerald-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>🏛️</span>
                  <span>文化自信</span>
                </button>
                <button onclick="toggleEmotion(this, '增廣見聞')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-indigo-50 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>🔍</span>
                  <span>增廣見聞</span>
                </button>
                <button onclick="toggleEmotion(this, '聲韻和諧')" class="emotion-chip px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-amber-100 text-slate-700 transition-all flex items-center gap-1.5 cursor-pointer">
                  <span>🎶</span>
                  <span>聲韻和諧</span>
                </button>
              </div>
            </div>

          </div>

        </div>

      </div>

    </div>

  </main>

  <!-- ==================== WORKSHEET MODAL (PDF 彈窗) ==================== -->
  <div id="worksheetModal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm animate-fade-in">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl border border-slate-100 space-y-4 relative">
      <!-- Modal Header -->
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <div class="flex items-center space-x-3">
          <div id="wsModalIconBox" class="w-12 h-12 rounded-2xl flex items-center justify-center text-xl shrink-0 shadow-xs">
            <i id="wsModalIcon" class="fa-solid fa-file-pdf"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span id="wsModalBadge" class="px-2.5 py-0.5 rounded-full text-[11px] font-bold"></span>
              <span id="wsModalTypeTag" class="px-2 py-0.5 rounded-full text-[10px] font-bold"></span>
            </div>
            <h3 id="wsModalTitle" class="text-base font-serif font-bold text-slate-900 mt-1">學習單下載與預覽</h3>
          </div>
        </div>
        <button onclick="closeWorksheetModal()" class="w-8 h-8 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-400 hover:text-slate-600 transition-colors cursor-pointer" title="關閉視窗">
          <i class="fa-solid fa-xmark text-lg"></i>
        </button>
      </div>

      <!-- Modal Body / Song Worksheet Cards List -->
      <div id="wsModalSongList" class="space-y-2.5 max-h-[60vh] overflow-y-auto pr-1">
        <!-- Rendered by openWorksheetModal(type) -->
      </div>

      <!-- Modal Footer -->
      <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
        <span class="flex items-center gap-1">
          <i class="fa-regular fa-circle-question text-slate-400"></i>
          <span>可點選預覽直接線上閱讀，或點下載保存</span>
        </span>
        <button onclick="closeWorksheetModal()" class="px-4 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold transition-colors cursor-pointer">
          關閉
        </button>
      </div>
    </div>
  </div>

  <!-- ==================== FOOTER ==================== -->
  <footer class="mt-auto bg-white border-t border-slate-200 py-6 text-slate-600 text-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
      <!-- Left: Brand Logo & Title (方形紅印，嚴禁 rounded-full) -->
      <div class="flex items-center space-x-2.5">
        <img src="assets/SSS_Stamp02.png" alt="學思軒" class="w-8 h-8 object-contain shadow-xs">
        <span class="font-serif font-bold text-slate-800 text-sm">八下國文寶典・歌SONG國文</span>
        <span class="text-slate-300">|</span>
        <span class="text-slate-500 text-[11px]">漢字奧妙・六書造字與形音義的千年交響</span>
      </div>
      <!-- Right: Copyright Statement -->
      <div class="text-slate-500 text-center sm:text-right font-sans text-[11px] leading-relaxed">
        © 2026 學思軒 &gt;&lt;&gt; &gt;&lt;&gt; &gt;&lt;&gt; •••本網頁由黃于珊老師與AI協作生成，僅供教學使用。•••&lt;&gt;&lt; &lt;&gt;&lt; &lt;&gt;&lt;
      </div>
    </div>
  </footer>

  <!-- Invisible Audio Element -->
  <audio id="audioPlayer" preload="auto"></audio>

  <!-- ==================== CLIENT LOGIC SCRIPT ==================== -->
  <script>
    // All Songs Data
    const songsData = {songs_json};
    const unitWorksheetMeta = {meta_json};

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
        const isCurrent = idx === currentSongIndex;
        return `
          <div onclick="switchSong(${{idx}}, false)" class="p-2.5 rounded-xl border transition-all cursor-pointer flex items-center justify-between ${{isCurrent ? 'bg-amber-50/80 border-amber-300 shadow-xs' : 'bg-slate-50 hover:bg-slate-100 border-slate-200'}}">
            <div class="flex items-center space-x-2.5">
              <span class="w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold ${{isCurrent ? 'bg-orange-600 text-white' : 'bg-slate-200 text-slate-700'}}">
                ${{idx + 1}}
              </span>
              <div>
                <h5 class="text-xs font-bold font-serif ${{isCurrent ? 'text-orange-900' : 'text-slate-800'}}">${{song.title}}</h5>
                <p class="text-[10px] text-slate-500">${{song.artist}} ・ ${{song.tag}}</p>
              </div>
            </div>
            <div class="flex items-center space-x-1.5">
              <button onclick="event.stopPropagation(); switchSong(${{idx}}, true)" class="w-7 h-7 rounded-full bg-white hover:bg-orange-600 hover:text-white text-slate-600 shadow-xs flex items-center justify-center text-xs transition-colors" title="立即播放此曲">
                <i class="fa-solid fa-play ml-0.5 text-[10px]"></i>
              </button>
            </div>
          </div>
        `;
      }}).join('');
    }}

    // Load Song Data into UI
    function loadSong(index, autoPlay = false) {{
      const song = songsData[index];
      if (!song) return;

      // Update Player Metadata
      document.getElementById('playerSongTitle').textContent = song.title;
      document.getElementById('playerArtistMeta').textContent = `${{song.artist}} ・ ${{song.year}}年《${{song.album}}》`;
      document.getElementById('playerOrderBadge').textContent = song.order;
      document.getElementById('playerTagBadge').textContent = song.tag;
      document.getElementById('vinylSongTitle').textContent = song.title;
      document.getElementById('vinylArtist').textContent = song.artist;
      document.getElementById('songIntroText').textContent = song.intro;

      // Update Worksheet Metadata
      document.getElementById('sheetTitle').textContent = `【${{song.title}}】`;
      document.getElementById('sheetCredits').textContent = `作詞：${{song.lyricist}}  作曲：${{song.composer}}  演唱：${{song.artist}}  ${{song.year}}`;

      // Set Audio Source
      audio.src = song.audio;
      audio.load();

      // Reset Player State
      pauseMedia();
      currentTimeEl.textContent = "00:00";
      progressBar.style.width = "0%";
      progressHandle.style.left = "0%";

      // Render Lyrics
      renderLyrics(song);

      // Reset Key Sentence reveal state
      isKeySentenceRevealed = false;
      updateKeySentenceUI();

      if (autoPlay) {{
        playMedia();
      }}
    }}

    // Switch Song Handler
    function switchSong(index, autoPlay = false) {{
      if (index < 0 || index >= songsData.length) return;
      currentSongIndex = index;
      renderTabs();
      renderSongListMenu();
      loadSong(currentSongIndex, autoPlay);
      window.history.replaceState(null, null, `#${{songsData[index].id}}`);
    }}

    // Render Lyrics with Blanks
    function renderLyrics(song) {{
      const container = document.getElementById('lyricsContainer');
      let html = '';
      let blankCounter = 0;

      song.lyrics.forEach((line) => {{
        // Handle Empty Space
        if (line.length === 1 && line[0].type === 'space') {{
          html += '<div class="h-2.5 sm:h-3"></div>';
          return;
        }}

        // Render Normal Line
        html += '<div class="leading-normal flex flex-wrap items-center py-0.5">';
        line.forEach((item) => {{
          if (item.t) {{
            html += `<span class="whitespace-pre-wrap">${{escapeHtml(item.t)}}</span>`;
          }} else if (item.b) {{
            const blankId = `b_${{currentSongIndex}}_${{blankCounter++}}`;
            const isRevealed = isTeacherMode || revealedBlanks.has(blankId);
            html += `
              <span id="${{blankId}}" 
                    onclick="toggleBlank('${{blankId}}', '${{escapeAttr(item.b)}}', '${{escapeAttr(item.h)}}')" 
                    class="blank-box ${{isRevealed ? 'revealed' : ''}}" 
                    title="點擊揭曉答案">
                ${{isRevealed 
                  ? `<span class="font-handwriting font-bold text-rose-600 text-base sm:text-lg tracking-wider">${{item.b}}</span>` 
                  : `<span class="text-xs text-slate-400 font-sans">[ ${{item.h}} ]</span>`
                }}
              </span>
            `;
          }}
        }});
        html += '</div>';
      }});

      container.innerHTML = html;
    }}

    // Blank Interaction Logic
    function toggleBlank(blankId, answer, hint) {{
      const el = document.getElementById(blankId);
      if (!el) return;

      if (revealedBlanks.has(blankId)) {{
        revealedBlanks.delete(blankId);
        el.classList.remove('revealed');
        el.innerHTML = `<span class="text-xs text-slate-400 font-sans">[ ${{hint}} ]</span>`;
      }} else {{
        revealedBlanks.add(blankId);
        el.classList.add('revealed');
        el.innerHTML = `<span class="font-handwriting font-bold text-rose-600 text-base sm:text-lg tracking-wider">${{answer}}</span>`;
      }}
    }}

    // Reveal All Blanks (Teacher Mode)
    function toggleAllBlanks() {{
      isTeacherMode = !isTeacherMode;
      const btn = document.getElementById('toggleAllBtn');
      const text = document.getElementById('toggleAllBtnText');

      if (isTeacherMode) {{
        btn.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-rose-600 text-white shadow-sm cursor-pointer active:scale-95";
        text.textContent = "隱藏教師答案";
      }} else {{
        btn.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-rose-50 text-rose-700 hover:bg-rose-100 border border-rose-200 shadow-xs cursor-pointer active:scale-95";
        text.textContent = "一鍵揭曉教師版";
      }}

      // Re-render lyrics & update key sentence box
      renderLyrics(songsData[currentSongIndex]);
      updateKeySentenceUI();
    }}

    // Reset All Blanks to Empty
    function resetAllBlanks() {{
      revealedBlanks.clear();
      isTeacherMode = false;
      const btn = document.getElementById('toggleAllBtn');
      const text = document.getElementById('toggleAllBtnText');
      btn.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 bg-rose-50 text-rose-700 hover:bg-rose-100 border border-rose-200 shadow-xs cursor-pointer active:scale-95";
      text.textContent = "一鍵揭曉教師版";
      renderLyrics(songsData[currentSongIndex]);
    }}

    // Toggle Key Sentence Answer
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

    // Emotion Chip Toggle
    function toggleEmotion(btn, label) {{
      const isSelected = btn.classList.contains('selected');
      if (isSelected) {{
        btn.classList.remove('selected', 'bg-orange-500', 'text-white', 'border-orange-600', 'shadow-xs');
        btn.classList.add('bg-white', 'text-slate-700', 'border-slate-300');
      }} else {{
        btn.classList.add('selected', 'bg-orange-500', 'text-white', 'border-orange-600', 'shadow-xs');
        btn.classList.remove('bg-white', 'text-slate-700', 'border-slate-300');
      }}
    }}

    // Media Controls
    function togglePlay() {{
      if (isPlaying) {{
        pauseMedia();
      }} else {{
        playMedia();
      }}
    }}

    function playMedia() {{
      audio.play().then(() => {{
        isPlaying = true;
        updatePlayState();
      }}).catch(err => {{
        console.warn("Audio play prevented:", err);
      }});
    }}

    function pauseMedia() {{
      audio.pause();
      isPlaying = false;
      updatePlayState();
    }}

    function updatePlayState() {{
      if (isPlaying) {{
        playIcon.className = "fa-solid fa-pause text-xl";
        vinylDisc.classList.add('animate-spin-slow');
        vinylArm.classList.add('playing');
      }} else {{
        playIcon.className = "fa-solid fa-play text-xl ml-0.5";
        vinylDisc.classList.remove('animate-spin-slow');
        vinylArm.classList.remove('playing');
      }}
    }}

    function skipTime(seconds) {{
      audio.currentTime = Math.max(0, Math.min(audio.duration || 0, audio.currentTime + seconds));
    }}

    function seekAudio(e) {{
      const rect = e.currentTarget.getBoundingClientRect();
      const pos = (e.clientX - rect.left) / rect.width;
      if (audio.duration) {{
        audio.currentTime = pos * audio.duration;
      }}
    }}

    function setPlaybackSpeed(speed) {{
      audio.playbackRate = speed;
      document.querySelectorAll('.speed-btn').forEach(btn => {{
        if (parseFloat(btn.textContent) === speed) {{
          btn.className = "speed-btn active px-1.5 py-0.5 rounded bg-stone-800 text-amber-400 font-mono font-bold transition-colors";
        }} else {{
          btn.className = "speed-btn px-1.5 py-0.5 rounded hover:bg-stone-800 text-stone-400 font-mono transition-colors";
        }}
      }});
    }}

    function changeVolume(val) {{
      audio.volume = val;
      if (val == 0) {{
        volumeIcon.className = "fa-solid fa-volume-xmark text-sm";
      }} else if (val < 0.5) {{
        volumeIcon.className = "fa-solid fa-volume-low text-sm";
      }} else {{
        volumeIcon.className = "fa-solid fa-volume-high text-sm";
      }}
    }}

    function toggleMute() {{
      if (audio.volume > 0) {{
        audio.dataset.prevVol = audio.volume;
        audio.volume = 0;
        volumeSlider.value = 0;
        volumeIcon.className = "fa-solid fa-volume-xmark text-sm";
      }} else {{
        const prev = audio.dataset.prevVol || 0.85;
        audio.volume = prev;
        volumeSlider.value = prev;
        volumeIcon.className = "fa-solid fa-volume-high text-sm";
      }}
    }}

    function setupAudioEvents() {{
      audio.addEventListener('timeupdate', () => {{
        if (!audio.duration) return;
        const current = audio.currentTime;
        const total = audio.duration;
        const pct = (current / total) * 100;
        progressBar.style.width = pct + '%';
        progressHandle.style.left = pct + '%';
        currentTimeEl.textContent = formatTime(current);
      }});

      audio.addEventListener('loadedmetadata', () => {{
        totalDurationEl.textContent = formatTime(audio.duration);
      }});

      audio.addEventListener('ended', () => {{
        pauseMedia();
        audio.currentTime = 0;
      }});
    }}

    function setupVideoEvents() {{
      // Reserved for video events
    }}

    function formatTime(sec) {{
      if (isNaN(sec)) return "00:00";
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;
    }}

    // ==================== WORKSHEET MODAL FUNCTIONS ====================
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
            '<a href="' + fileUrl + '" download class="py-1 px-2.5 rounded-lg bg-slate-800 hover:bg-slate-900 text-white font-medium text-xs flex items-center gap-1 transition-all shadow-xs" title="下載PDF">' +
              '<i class="fa-solid fa-download text-[10px]"></i>' +
              '<span>下載</span>' +
            '</a>' +
          '</div>' +
        '</div>';
      }});

      listHtml += '</div></div>';
      document.getElementById('wsModalSongList').innerHTML = listHtml;
      document.getElementById('worksheetModal').classList.remove('hidden');
    }}

    function closeWorksheetModal() {{
      document.getElementById('worksheetModal').classList.add('hidden');
    }}

    document.getElementById('worksheetModal').addEventListener('click', function(e) {{
      if (e.target === this) closeWorksheetModal();
    }});

    // Helper utilities
    function escapeHtml(text) {{
      const map = {{ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }};
      return text.replace(/[&<>"']/g, m => map[m]);
    }}

    function escapeAttr(text) {{
      return escapeHtml(text).replace(/\\n/g, ' ');
    }}
  </script>
</body>
</html>
'''
    return html

# 4. Generate HTML files
# index.html
with open(os.path.join(TARGET_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(build_page_html("cang-jie"))
print("Generated: index.html")

# cang-jie.html
with open(os.path.join(TARGET_DIR, "cang-jie.html"), "w", encoding="utf-8") as f:
    f.write(build_page_html("cang-jie"))
print("Generated: cang-jie.html")

# shengpi-zi.html
with open(os.path.join(TARGET_DIR, "shengpi-zi.html"), "w", encoding="utf-8") as f:
    f.write(build_page_html("shengpi-zi"))
print("Generated: shengpi-zi.html")

print("\nAll files built successfully in:", TARGET_DIR)
