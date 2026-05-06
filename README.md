# 电影搭子.skill

一个无剧透、包容接纳的 Codex 电影陪看 skill。

A no-spoiler, inclusive Codex movie companion skill.

它的核心玩法很简单：你说“开始观看”，它记录当前墙钟时间和片内时间；之后你随时提问，它先计算电影播放到哪里，再只读取安全时间点之前的字幕上下文来回答。它会像一个搭子一样聊电影，但不会提前说后面的剧情。

The core loop is simple: when you say "开始观看" or "start watching", it records the wall-clock time and the movie timestamp. When you ask a question later, it first calculates where the movie should be, retrieves only subtitle context before the safe time, and answers like a movie buddy without spoiling later events.

## 能做什么 / Features

- 进入放映模式并持续推算当前片内时间
- 解析 `.srt` / `.vtt` 字幕
- 支持普通对白字幕和描述字幕、SDH、音频描述字幕
- 每次回答前自动取最新安全上下文
- 严格禁止剧透
- 不要求截图
- 用包容、接纳、不嘲笑问题的语气陪看

- Enter screening mode and estimate current playback time
- Parse `.srt` / `.vtt` subtitle files
- Support dialogue subtitles plus descriptive, SDH, or audio-description tracks
- Retrieve fresh safe context before every answer
- Enforce strict no-spoiler boundaries
- Never require screenshots
- Keep a welcoming, accepting, non-judgmental companion voice

## 不能做什么 / Limits

- 不能直接读取 Netflix、Disney+ 等 DRM 视频画面
- 不能凭空知道没有出现在字幕或描述轨里的视觉细节
- 不会帮你获取盗版资源

- Cannot directly read DRM-protected streaming video
- Cannot know visual details that are absent from subtitles or descriptive tracks
- Will not help obtain pirated content

## 安装 / Installation

把这个仓库作为 Codex skill 放到：

```powershell
C:\Users\Vincent\.codex\skills\movie-companion
```

或者复制仓库内容：

```powershell
Copy-Item -Recurse -Force "D:\Projects\movie companion\*" "C:\Users\Vincent\.codex\skills\movie-companion"
```

重启 Codex 后，显示名会是：

```text
电影搭子.skill
```

内部调用名仍然是：

```text
$movie-companion
```

## 快速开始 / Quick Start

生成字幕索引：

```powershell
python .\scripts\movie_sync.py index `
  --subtitle "D:\Projects\movie companion\La.La.Land.English-WWW.MY-SUBS.CO.srt" `
  --movie "La La Land" `
  --output "D:\Projects\movie companion\la-la-land.movie-index.json"
```

开始放映：

```powershell
python .\scripts\movie_sync.py start `
  --index "D:\Projects\movie companion\la-la-land.movie-index.json" `
  --at 00:00:00 `
  --session "D:\Projects\movie companion\la-la-land.watch-session.json"
```

提问前取安全上下文：

```powershell
python .\scripts\movie_sync.py ask `
  --session "D:\Projects\movie companion\la-la-land.watch-session.json" `
  --before 900
```

## GPT 推荐的 5 个字幕搜集网页 / 5 Subtitle Sites Recommended by GPT

请只为你已经合法观看或拥有访问权的影视内容寻找匹配字幕。字幕站点的可用性、域名和内容质量会变化，下载前自己判断来源和安全性。

Use these only to find matching subtitles for movies or shows you can legally watch or access. Availability, domains, and subtitle quality can change; use your own judgment before downloading files.

| 网站 / Site | 链接 / Link | 适合什么 / Best For |
| --- | --- | --- |
| OpenSubtitles | [dl.opensubtitles.com](https://dl.opensubtitles.com/en/home) | 电影/剧集/多语言最大众，英文和中文都能找。 / A large mainstream subtitle source for movies, shows, and many languages, including English and Chinese. |
| SubDL | [subdl.com](https://subdl.com/) | 很适合找电影、剧集、多语言字幕，界面比较清爽。 / Good for movies, shows, and multilingual subtitles with a clean interface. |
| Zimuku / 字幕库 | [zimuku.org](https://zimuku.org/)；备用 / mirror: [zmk.pw](https://zmk.pw/) | 中文/中英双语字幕常用。 / Commonly used for Chinese and bilingual Chinese-English subtitles. |
| SubHD | [subhd.tv](https://subhd.tv/) | 中文圈常用，适合中英双语字幕；页面也列了备用域名：`subhdtw.com`、`subhd.la`、`subhd.cc`、`subhd.me`。 / Popular in Chinese subtitle communities, especially for bilingual Chinese-English subtitles; it also lists backup domains. |
| Addic7ed | [addic7ed.com](https://www.addic7ed.com/) | 英文剧集字幕很强，尤其美剧/英剧。 / Strong for English TV subtitles, especially US and UK series. |

如果能找到 SDH、closed captions、descriptive subtitles 或 audio-description transcript，这个 skill 会更懂场面；只有普通字幕也可以，只是视觉细节会更谨慎。

If you can find SDH, closed captions, descriptive subtitles, or audio-description transcripts, this skill gets better scene context. Regular dialogue subtitles still work, but visual details will be handled more cautiously.

## 放映模式口令 / Screening Mode Commands

你可以这样跟 Codex 说：

```text
开始观看
```

如果不是从头开始：

```text
开始观看 00:17:42
```

暂停或关闭：

```text
暂停
关闭放映模式
```

继续时重新给一个可见时间点：

```text
开始观看 00:28:10
```

## 无剧透规则 / No-Spoiler Rule

默认安全时间是：

```text
当前估算片内时间 - 8 秒
```

回答只能使用安全时间之前的字幕和描述轨。即使模型知道电影结局，也不能把后面的信息带进来。

Answers can only use subtitles and descriptive tracks before the safe time. Even if the model knows the ending, it must not bring later information into the answer.

## 搭子语气 / Companion Voice

这个 skill 的语气要包容、接纳、轻松。用户问基础问题、看漏了、没听懂歌词、对角色有不同感受，都应该被正常接住。

The skill should sound inclusive, accepting, and easy to talk to. Basic questions, missed details, confused reactions, emotional responses, or unusual interpretations are all welcome.

## 仓库结构 / Repository Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── architecture.md
├── scripts/
│   └── movie_sync.py
├── examples/
│   └── sample-dialogue.srt
├── README.md
├── 搭子说明.md
├── LICENSE
└── .gitignore
```
