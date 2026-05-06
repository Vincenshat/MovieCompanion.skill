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
