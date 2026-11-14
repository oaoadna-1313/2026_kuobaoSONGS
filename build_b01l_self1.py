import os
import shutil
import json

TARGET_DIR = r"C:\2026_歌SONG國文\B01L自學1古代神話與寓言選好歌"
SOURCE_DIR = r"C:\2026_歌SONG國文\材料\B1_SONG\[好歌]B01L自學1古代神話與寓言選"
ASSETS_DIR = r"C:\2026_歌SONG國文\assets"

os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "assets"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "media"), exist_ok=True)

# Copy Assets
for asset_name in ["badge-songlogo.PNG", "baoden.png", "SSS_Stamp02.png", "SSS_Stamp01.png"]:
    src = os.path.join(ASSETS_DIR, asset_name)
    dst = os.path.join(TARGET_DIR, "assets", asset_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied asset: {asset_name}")

# Copy Media
media_map = {
    "01孫燕姿-日落mp3.mp3": "sunset.mp3",
    "02蘇打綠-未了mp3.mp3": "endless.mp3"
}
for src_name, dst_name in media_map.items():
    src = os.path.join(SOURCE_DIR, src_name)
    dst = os.path.join(TARGET_DIR, "media", dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied audio: {src_name} -> {dst_name}")

# Copy Worksheets
pdf_map = {
    "[國寶]B01L自學1古代神話與寓言選-好歌_01日落.pdf": "worksheet-sunset.pdf",
    "[國寶]B01L自學1古代神話與寓言選-好歌_02未了.pdf": "worksheet-endless.pdf"
}
for src_name, dst_name in pdf_map.items():
    src = os.path.join(SOURCE_DIR, src_name)
    dst = os.path.join(TARGET_DIR, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied pdf: {src_name} -> {dst_name}")

songsData = [
  {
    "id": "sunset",
    "title": "日落",
    "artist": "孫燕姿",
    "lyricist": "小寒",
    "composer": "張簡君偉、邵豪、寧夏",
    "year": "2025-01",
    "album": "單曲《日落》",
    "tag": "光芒與信念・心靈探索與守候",
    "order": "第一曲",
    "sheet": "好歌學習單 第57頁",
    "audio": "media/sunset.mp3",
    "video": None,
    "bgGradient": "from-orange-600 via-amber-600 to-stone-900",
    "lightBg": "bg-orange-50/70 border-orange-200",
    "intro": "孫燕姿2025年全新單曲《日落》，歌詞透過「山忽隱忽現，海市蜃樓是沙漠謊言，天銜接水面，我的地平線越縮越遠」等豐富意象，勾勒出人生旅途中迷茫與探索的深邃畫面。呼應《古代神話與寓言選》中夸父逐日的執著追尋——在日落的餘暉與廣漠的地平線前，即使被黑夜取代，內心深處的光與愛從未熄滅。「視線之外，無形同載」，不見面不代表沒想起，回憶始終牽繫著彼此，傳達出溫暖堅韌的力量。",
    "lyrics": [
      [{"t": "山忽"}, {"b": "隱", "h": "1字"}, {"t": "忽"}, {"b": "現", "h": "1字"}, {"t": " "}, {"b": "海市蜃樓", "h": "4字"}, {"t": "是沙漠謊言 天"}, {"b": "銜接", "h": "2字"}, {"t": "水面 我的地平線越縮越遠"}],
      [{"t": "我追 我推 我被  困在肢體範圍"}],
      [{"t": "生活"}, {"b": "瑣", "h": "1字"}, {"t": "碎 "}, {"b": "搗", "h": "1字"}, {"t": "碎 "}, {"b": "粉", "h": "1字"}, {"t": "碎  是有或沒不再絕對"}],
      [{"t": "我在"}, {"b": "日落", "h": "2字"}, {"t": "到來  遙望太陽"}, {"b": "潛入", "h": "2字"}, {"t": "深海 等待"}, {"b": "季節", "h": "2字"}, {"t": "更改  年復一年 行程沒改"}],
      [{"t": "儘管被"}, {"b": "夜", "h": "1字"}, {"t": "取代  不表示"}, {"b": "光", "h": "1字"}, {"t": "不存在  你的愛讓我明白  視線之外無形同載"}],
      [{"type": "space"}],
      [{"t": "星"}, {"b": "眨眼", "h": "2字"}, {"t": "瞬間  已經消失在千年以前  笑掛在嘴邊  喜悅卻只是回憶重演"}],
      [{"t": "我追 我推 我退 不讓"}, {"b": "軀體", "h": "2字"}, {"t": "包圍"}],
      [{"t": "開始"}, {"b": "理", "h": "1字"}, {"t": "會 "}, {"b": "體", "h": "1字"}, {"t": "會 "}, {"b": "領", "h": "1字"}, {"t": "會 我將是誰? 誰能答對?"}],
      [{"type": "space"}],
      [{"t": "我在日落到來 遙望太陽潛入深海  等待季節更改 年復一年 行程沒改"}],
      [{"t": "儘管被夜取代 不表示光不存在 我感覺在醒過來"}],
      [{"type": "space"}],
      [{"t": "我在日落到來 遙望戀人潛入人海  等待有天明白 我是愛情 這不會改"}],
      [{"t": "儘管不再倚賴 不表示愛不存在  我感覺在醒過來 視線之外無形同載"}]
    ],
    "keySentence": "儘管被夜取代 不表示光不存在 視線之外無形同載\n儘管不再倚賴 不表示愛不存在 視線之外無形同載",
    "emotions": [
      {"icon": "🌅", "text": "溫暖日落"},
      {"icon": "✨", "text": "光明信念"},
      {"icon": "💫", "text": "深刻情感"},
      {"icon": "🌊", "text": "探索前行"},
      {"icon": "🕊️", "text": "醒悟釋懷"},
      {"icon": "🤍", "text": "無形同載"}
    ]
  },
  {
    "id": "endless",
    "title": "未了",
    "artist": "蘇打綠",
    "lyricist": "吳青峰",
    "composer": "吳青峰",
    "year": "2015-11",
    "album": "冬 未了",
    "tag": "神話宿命・抗爭輪迴與活在當下",
    "order": "第二曲",
    "sheet": "好歌學習單 第58頁",
    "audio": "media/endless.mp3",
    "video": None,
    "bgGradient": "from-stone-800 via-amber-700 to-orange-900",
    "lightBg": "bg-amber-50/70 border-amber-200",
    "intro": "蘇打綠收錄於韋瓦第計畫第四部《冬 未了》中的重磅力作。青峰借用古希臘神話中「薛西佛斯推巨石上山」與「普羅米修斯被縛啄肝」的經典典故，對照當代人在重複日常與困境中的掙扎。呼應《古代神話與寓言選》對神話寓言的省思：即便面對看似徒勞無功、永無休止的輪迴懲罰，只要「命運被他堅持」、「支撐自己輪迴」、「每一步都是自己的」，便能超越宿命枷鎖，活出「不愛永恆但求現在，真實活著的人生」。",
    "lyrics": [
      [{"t": "推著上山"}, {"b": "巨石", "h": "2字"}, {"t": " 親愛薛西佛斯 不知道第幾次 命運被他"}, {"b": "堅持", "h": "2字"}, {"t": " balabalababa~"}],
      [{"t": "他午睡他狂歡 她教大地"}, {"b": "拾穗", "h": "2字"}, {"t": " 而你靠你"}, {"b": "蹣跚", "h": "2字"}, {"t": " 支撐自己輪迴"}],
      [{"t": "You will be the star You will be the one"}],
      [{"t": "I will be my star You'll be the one balabalababa~"}],
      [{"type": "space"}],
      [{"t": "永恆迴歸不斷 日光子夜迴圈 當他被吃了肝 其實你不孤單"}],
      [{"t": "You will be my one You will be my star"}],
      [{"t": "I will be the one You'll be my star You'll be my star balabalababa~"}],
      [{"type": "space"}],
      [{"t": "你重扛巨石輕視著眾神 你去否定了否定你的"}],
      [{"t": "雖然翻覆卻漸漸懂得 每一步都是自己的"}],
      [{"t": "不愛永恆但求現在 真實活著的人生"}],
      [{"type": "space"}],
      [{"t": "I will be the star I will be the one"}],
      [{"t": "You will be my star You'll be my one"}],
      [{"t": "I will be your one I will be your star"}],
      [{"t": "You will be my one You'll be my star We'll be the one"}]
    ],
    "keySentence": "命運被他堅持\n支撐自己輪迴",
    "emotions": [
      {"icon": "🪨", "text": "堅毅不屈"},
      {"icon": "🔥", "text": "抗爭宿命"},
      {"icon": "🌌", "text": "薛西佛斯"},
      {"icon": "✨", "text": "活在當下"},
      {"icon": "🌟", "text": "成為繁星"},
      {"icon": "🎼", "text": "磅礡交響"}
    ]
  }
]

unitWorksheetMeta = {
  "unitName": "七上國文・自學一 古代神話與寓言選",
  "badgeClass": "bg-orange-100 text-orange-900 border border-orange-300",
  "songs": [
    {
      "id": 1,
      "title": "日落",
      "artist": "孫燕姿",
      "student": "worksheet-sunset.pdf",
      "teacher": "worksheet-sunset.pdf"
    },
    {
      "id": 2,
      "title": "未了",
      "artist": "蘇打綠",
      "student": "worksheet-endless.pdf",
      "teacher": "worksheet-endless.pdf"
    }
  ]
}

def build_page_html(default_song_id='sunset'):
    songs_json = json.dumps(songsData, ensure_ascii=False)
    meta_json = json.dumps(unitWorksheetMeta, ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【歌SONG國文】自學一 古代神話與寓言選 好歌互動教學平台</title>
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
    
    /* Blank box styles - 精準緊湊行高規格，嚴格禁止撐大版面 */
    .blank-box {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 3.2rem;
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
      <!-- Brand & Title (閱思龍門標準品牌標題，方形印章絕無 rounded-full) -->
      <div class="flex items-center space-x-3">
        <a href="index.html" class="flex items-center space-x-2.5 group" title="返回歌SONG國文教學首頁">
          <!-- 嚴格維持原生純方形，嚴禁 rounded-full -->
          <img src="assets/SSS_Stamp02.png" alt="閱思龍門" class="w-10 h-10 object-contain shadow-sm group-hover:rotate-6 transition-transform duration-300">
          <div>
            <div class="flex items-center space-x-2">
              <span class="font-serif font-bold text-lg sm:text-xl text-slate-900 tracking-wide">歌SONG國文</span>
              <span class="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-orange-100 text-orange-900 border border-orange-300">七上國文・自學一 古代神話與寓言選</span>
            </div>
            <p class="text-[11px] text-slate-500 font-medium hidden md:block">穿梭神話時空・聆聽古今追尋與不屈意志的文學交響</p>
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
            <h1 class="text-sm sm:text-base font-serif font-bold text-amber-100 tracking-wide">遠古神話追尋與現代心靈探索的文學交響</h1>
            <p class="text-xs text-orange-100/90 mt-0.5">結合《古代神話與寓言選》（《夸父逐日》、《薛西佛斯神話》等）課文賞析，聆聽孫燕姿《日落》與蘇打綠《未了》，感受夸父追日的壯懷與薛西佛斯抗爭命運的不屈，邊聽音樂邊完成歌詞填空與深度鑑賞</p>
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
              <span id="playerOrderBadge" class="px-2 py-0.5 text-xs font-bold rounded-md bg-orange-100 text-orange-900 border border-orange-200">第一曲</span>
            </div>
            <div class="flex items-center gap-2">
              <span id="playerTagBadge" class="px-2.5 py-0.5 text-xs font-medium rounded-full bg-orange-100 text-orange-800">光芒與信念・心靈探索與守候</span>
            </div>
          </div>

          <!-- Player Body: Visualizer / Vinyl Record -->
          <div class="p-6 flex flex-col items-center justify-center bg-gradient-to-b from-stone-900 to-stone-950 text-white relative overflow-hidden min-h-[260px]">
            
            <!-- Vinyl Record Turntable Animation -->
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
                    <span id="vinylSongTitle" class="text-[10px] sm:text-xs font-serif font-black truncate max-w-[4.8rem] text-white mt-0.5">日落</span>
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
              <h2 id="playerSongTitle" class="font-serif font-bold text-lg sm:text-xl text-white tracking-wide">日落</h2>
              <p id="playerArtist" class="text-xs text-amber-200/80 font-medium">演唱：孫燕姿・2025</p>
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
                  <button onclick="skipTime(-5)" class="text-stone-300 hover:text-white transition-colors p-1 cursor-pointer" title="倒退 5 秒">
                    <i class="fa-solid fa-rotate-left text-sm"></i>
                  </button>
                  <!-- Prev Song -->
                  <button onclick="prevSong()" class="text-stone-300 hover:text-white transition-colors p-1 cursor-pointer" title="上一首">
                    <i class="fa-solid fa-backward-step text-base"></i>
                  </button>
                  <!-- Play / Pause -->
                  <button id="playPauseBtn" onclick="togglePlayPause()" class="w-11 h-11 rounded-full bg-gradient-to-r from-amber-500 to-orange-600 text-white flex items-center justify-center text-lg shadow-lg hover:scale-105 active:scale-95 transition-all cursor-pointer">
                    <i id="playIcon" class="fa-solid fa-play ml-1"></i>
                  </button>
                  <!-- Next Song -->
                  <button onclick="nextSong()" class="text-stone-300 hover:text-white transition-colors p-1 cursor-pointer" title="下一首">
                    <i class="fa-solid fa-forward-step text-base"></i>
                  </button>
                  <!-- +5s -->
                  <button onclick="skipTime(5)" class="text-stone-300 hover:text-white transition-colors p-1 cursor-pointer" title="快轉 5 秒">
                    <i class="fa-solid fa-rotate-right text-sm"></i>
                  </button>
                </div>

                <!-- Volume Control -->
                <div class="flex items-center space-x-1.5 group relative">
                  <button onclick="toggleMute()" class="text-stone-300 hover:text-white transition-colors text-xs p-1 cursor-pointer">
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
              <span class="w-1/2" id="metaLyricist">作詞：小寒</span>
              <span class="w-1/2" id="metaComposer">作曲：張簡君偉、邵豪、寧夏</span>
              <span class="w-1/2" id="metaArtist">演唱：孫燕姿</span>
              <span class="w-1/2" id="metaYear">發行：2025-01</span>
            </div>
          </div>
        </div>

        <!-- Quick Switch Checklist (2 Songs Grid) -->
        <div class="bg-white rounded-2xl border border-slate-200 p-4 shadow-xs">
          <h4 class="text-xs font-bold text-slate-600 mb-2.5 flex items-center justify-between">
            <span class="flex items-center gap-1.5">
              <i class="fa-solid fa-list-check text-orange-600"></i>
              <span>全系列好歌學習地圖 (2首)</span>
            </span>
            <span class="text-[11px] text-orange-600 font-semibold" id="overallCompletion">進行中 (1/2)</span>
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

          <!-- Worksheet Top Header (圓形橘色資料夾圖標＋歌名＋詞曲演唱年份，下方俐落橫線分隔) -->
          <div class="flex items-center justify-between border-b-2 border-slate-800 pb-4 mb-6">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 rounded-full bg-orange-600 text-white flex items-center justify-center font-serif font-black text-xl shadow-xs">
                <i class="fa-solid fa-music text-base"></i>
              </div>
              <div>
                <h2 id="sheetTitle" class="text-xl sm:text-2xl font-serif font-black text-slate-900 tracking-wide">【日落】</h2>
                <p id="sheetCredits" class="text-xs text-slate-600 mt-1">作詞：小寒  作曲：張簡君偉、邵豪、寧夏  演唱：孫燕姿  2025-01</p>
              </div>
            </div>
            <div class="text-right">
            </div>
          </div>

          <!-- Lyrics Display Area - 精緻適度行高排版規範，space-y-2 leading-normal，絕不空散 -->
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
                <!-- Dynamically rendered per song -->
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
          <span class="text-xs text-slate-500 font-medium">穿梭神話時空・聆聽古今追尋與不屈意志的文學交響</span>
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
    let revealedBlanks = new Set(); // Track revealed blank IDs

    // Initial song config
    const defaultSongId = "{default_song_id}";
    const hashSong = window.location.hash.replace('#', '') || (new URLSearchParams(window.location.search)).get('song');
    const targetSongId = hashSong || defaultSongId;
    const foundIdx = songsData.findIndex(s => s.id === targetSongId);
    if (foundIdx !== -1) currentSongIndex = foundIdx;

    // DOM Elements
    const audio = document.getElementById('audioPlayer');
    const vinylContainer = document.getElementById('vinylContainer');
    const vinylDisc = document.getElementById('vinylDisc');
    const vinylArm = document.getElementById('vinylArm');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const playIcon = document.getElementById('playIcon');
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
          <div onclick="switchSong(${{idx}}, false)" class="group p-2.5 rounded-xl text-xs flex items-center justify-between cursor-pointer transition-all ${{isActive ? 'bg-orange-50 text-orange-950 font-bold border border-orange-200 shadow-2xs' : 'hover:bg-slate-50 text-slate-700'}}">
            <div class="flex items-center gap-2.5 min-w-0">
              <!-- Dedicated Play / Pause Button in List -->
              <button onclick="event.stopPropagation(); toggleListPlay(${{idx}})" 
                      class="w-7 h-7 rounded-full flex items-center justify-center transition-all shrink-0 cursor-pointer ${{isThisPlaying ? 'bg-orange-600 text-white shadow-xs' : isActive ? 'bg-orange-200 text-orange-800 hover:bg-orange-600 hover:text-white' : 'bg-slate-100 text-slate-500 hover:bg-orange-600 hover:text-white group-hover:bg-orange-100 group-hover:text-orange-700'}}" 
                      title="${{isThisPlaying ? '暫停播放' : '立即播放《' + song.title + '》'}}">
                <i class="fa-solid ${{isThisPlaying ? 'fa-pause text-[10px]' : 'fa-play text-[9px] ml-0.5'}}"></i>
              </button>
              <span class="w-4 text-center font-mono text-[11px] ${{isActive ? 'text-orange-600 font-bold' : 'text-slate-400'}}">${{idx + 1}}</span>
              <span class="truncate text-sm">${{song.title}}</span>
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

    // Load Song Data into View
    function loadSong(index, autoPlay = false) {{
      const song = songsData[index];
      
      // Reset blank trackers for this song unless in teacher mode
      if (!isTeacherMode) {{
        revealedBlanks.clear();
      }}

      // Stop current playing media
      audio.pause();
      audio.currentTime = 0;

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
      document.getElementById('playerArtist').textContent = `演唱：${{song.artist}}・${{song.year.split('-')[0]}}`;
      document.getElementById('playerSongIntro').textContent = song.intro;
      document.getElementById('metaLyricist').textContent = `作詞：${{song.lyricist}}`;
      document.getElementById('metaComposer').textContent = `作曲：${{song.composer}}`;
      document.getElementById('metaArtist').textContent = `演唱：${{song.artist}}`;
      document.getElementById('metaYear').textContent = `發行：${{song.year}}`;

      // Worksheet Info
      document.getElementById('sheetTitle').textContent = `【${{song.title}}】`;
      document.getElementById('sheetCredits').textContent = `作詞：${{song.lyricist}}  作曲：${{song.composer}}  演唱：${{song.artist}}  ${{song.year}}`;

      // Update Audio Source
      audio.src = song.audio;
      audio.load();

      // Render Lyrics
      renderLyrics(song);

      // Render Emotions
      renderEmotionChips(song);

      // Update Key Sentence UI
      updateKeySentenceUI();

      // Update completion label
      document.getElementById('overallCompletion').textContent = `進行中 (${{index + 1}}/${{songsData.length}})`;

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

    // Reveal All Blanks for Current Song
    function revealCurrentSongAnswers() {{
      const song = songsData[currentSongIndex];
      let blankCounter = 0;
      song.lyrics.forEach(line => {{
        if (line.type !== 'space' && Array.isArray(line)) {{
          line.forEach(chunk => {{
            if (chunk.b) {{
              blankCounter++;
              revealedBlanks.add(`${{song.id}}-b-${{blankCounter}}`);
            }}
          }});
        }}
      }});
      renderLyrics(song);
    }}

    // Toggle Global Teacher Mode (All blanks everywhere revealed)
    function toggleAllBlanks() {{
      isTeacherMode = !isTeacherMode;
      const btnText = document.getElementById('toggleAllBtnText');

      if (isTeacherMode) {{
        btnText.textContent = "切換回學生空白版";
        revealCurrentSongAnswers();
        updateKeySentenceUI();
      }} else {{
        btnText.textContent = "一鍵揭曉教師版";
        resetAllBlanks();
        updateKeySentenceUI();
      }}
    }}

    // Reset All Blanks
    function resetAllBlanks() {{
      revealedBlanks.clear();
      isKeySentenceRevealed = false;
      renderLyrics(songsData[currentSongIndex]);
      updateKeySentenceUI();
    }}

    // Key sentence answer toggle
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

    // ==================== AUDIO PLAYBACK ====================
    function togglePlayPause() {{
      if (isPlaying) {{
        pauseMedia();
      }} else {{
        playMedia();
      }}
    }}

    function playMedia() {{
      const playPromise = audio.play();
      if (playPromise !== undefined) {{
        playPromise.catch(err => {{
          console.warn('Playback deferred or error:', err);
          isPlaying = false;
          playIcon.className = 'fa-solid fa-play ml-1';
          vinylDisc.classList.remove('animate-spin-slow');
          vinylArm.classList.remove('playing');
          renderSongListMenu();
        }});
      }}
    }}

    function pauseMedia() {{
      audio.pause();
      isPlaying = false;
      playIcon.className = 'fa-solid fa-play ml-1';
      vinylDisc.classList.remove('animate-spin-slow');
      vinylArm.classList.remove('playing');
      renderSongListMenu();
    }}

    function skipTime(seconds) {{
      audio.currentTime = Math.max(0, Math.min(audio.duration || 0, audio.currentTime + seconds));
    }}

    function seekAudio(e) {{
      if (!audio.duration) return;
      const rect = e.currentTarget.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const ratio = clickX / rect.width;
      audio.currentTime = ratio * audio.duration;
    }}

    function changeVolume(val) {{
      audio.volume = val;
      if (val == 0) {{
        volumeIcon.className = 'fa-solid fa-volume-xmark';
      }} else if (val < 0.5) {{
        volumeIcon.className = 'fa-solid fa-volume-low';
      }} else {{
        volumeIcon.className = 'fa-solid fa-volume-high';
      }}
    }}

    function toggleMute() {{
      audio.muted = !audio.muted;
      if (audio.muted) {{
        volumeIcon.className = 'fa-solid fa-volume-xmark text-rose-400';
      }} else {{
        changeVolume(volumeSlider.value);
      }}
    }}

    function setSpeed(rate, btn) {{
      audio.playbackRate = rate;
      document.querySelectorAll('.speed-btn').forEach(b => {{
        b.className = 'speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-white/10 hover:bg-white/20 text-slate-300';
      }});
      btn.className = 'speed-btn px-1.5 py-0.5 rounded text-[10px] font-mono bg-orange-600 text-white font-bold';
    }}

    function setupAudioEvents() {{
      audio.addEventListener('play', () => {{
        isPlaying = true;
        playIcon.className = 'fa-solid fa-pause';
        vinylDisc.classList.add('animate-spin-slow');
        vinylArm.classList.add('playing');
        renderSongListMenu();
      }});
      audio.addEventListener('pause', () => {{
        isPlaying = false;
        playIcon.className = 'fa-solid fa-play ml-1';
        vinylDisc.classList.remove('animate-spin-slow');
        vinylArm.classList.remove('playing');
        renderSongListMenu();
      }});
      audio.addEventListener('timeupdate', () => {{
        updateProgress(audio.currentTime, audio.duration);
      }});
      audio.addEventListener('loadedmetadata', () => {{
        totalDurationEl.textContent = formatTime(audio.duration);
      }});
      audio.addEventListener('ended', () => {{
        pauseMedia();
        audio.currentTime = 0;
      }});
    }}

    function updateProgress(current, duration) {{
      if (!duration || isNaN(duration)) return;
      const pct = (current / duration) * 100;
      progressBar.style.width = `${{pct}}%`;
      progressHandle.style.left = `${{pct}}%`;
      currentTimeEl.textContent = formatTime(current);
      totalDurationEl.textContent = formatTime(duration);
    }}

    function formatTime(sec) {{
      if (isNaN(sec)) return '00:00';
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;
    }}

    // ==================== EMOTION CHIPS ====================
    function renderEmotionChips(song) {{
      const container = document.getElementById('emotionContainer');
      const songId = song.id;
      const emotionKey = `gesong_b1l_self1_${{songId}}_emotion`;
      const savedEmotion = localStorage.getItem(emotionKey);

      container.innerHTML = song.emotions.map(em => {{
        const isSelected = savedEmotion === em.text;
        const activeClass = isSelected 
          ? 'bg-orange-100 border-orange-400 text-orange-950 font-bold shadow-xs' 
          : 'bg-white text-slate-700 border-slate-300 hover:bg-orange-50';
        return `
          <button onclick="toggleEmotion(this, '${{em.text}}')" class="emotion-chip px-3 py-1.5 rounded-lg border transition-all flex items-center gap-1.5 cursor-pointer ${{activeClass}}">
            <span>${{em.icon}}</span>
            <span>${{em.text}}</span>
          </button>
        `;
      }}).join('');
    }}

    function toggleEmotion(btn, emotionName) {{
      const songId = songsData[currentSongIndex].id;
      const emotionKey = `gesong_b1l_self1_${{songId}}_emotion`;
      const current = localStorage.getItem(emotionKey);

      document.querySelectorAll('.emotion-chip').forEach(b => setChipActive(b, false));

      if (current === emotionName) {{
        localStorage.removeItem(emotionKey);
      }} else {{
        localStorage.setItem(emotionKey, emotionName);
        setChipActive(btn, true);
      }}
    }}

    function setChipActive(btn, active) {{
      if (active) {{
        btn.classList.add('bg-orange-100', 'border-orange-400', 'text-orange-950', 'font-bold', 'shadow-xs');
        btn.classList.remove('bg-white', 'text-slate-700', 'border-slate-300');
      }} else {{
        btn.classList.remove('bg-orange-100', 'border-orange-400', 'text-orange-950', 'font-bold', 'shadow-xs');
        btn.classList.add('bg-white', 'text-slate-700', 'border-slate-300');
      }}
    }}

    // Keyboard Shortcuts (Space to play/pause)
    window.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT') return;
      if (e.code === 'Space') {{
        e.preventDefault();
        togglePlayPause();
      }}
    }});
  </script>

  <!-- ==================== WORKSHEET DOWNLOAD & PREVIEW MODAL ==================== -->
  <div id="worksheetModal" class="fixed inset-0 z-50 bg-slate-950/70 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-xl w-full p-6 sm:p-7 space-y-4 max-h-[90vh] overflow-y-auto border border-slate-200 shadow-2xl relative animate-in fade-in duration-200 text-left">
      <!-- Close Button -->
      <button onclick="closeWorksheetModal()" class="absolute right-4 top-4 text-slate-400 hover:text-slate-700 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-sm transition-colors cursor-pointer" title="關閉視窗">
        <i class="fa-solid fa-xmark"></i>
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
    const unitWorksheetMeta = {meta_json};

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
'''

# Generate HTML files
# 1. index.html
index_content = build_page_html('sunset')
with open(os.path.join(TARGET_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)
print("Generated index.html")

# 2. sunset.html
sunset_content = build_page_html('sunset')
with open(os.path.join(TARGET_DIR, "sunset.html"), "w", encoding="utf-8") as f:
    f.write(sunset_content)
print("Generated sunset.html")

# 3. endless.html
endless_content = build_page_html('endless')
with open(os.path.join(TARGET_DIR, "endless.html"), "w", encoding="utf-8") as f:
    f.write(endless_content)
print("Generated endless.html")

print("\nAll HTML pages & assets created successfully!")
