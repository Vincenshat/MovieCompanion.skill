# 电影搭子.skill

一个无剧透的 Codex 电影陪看 skill。

它的核心玩法很简单：你说“开始观看”，它记录当前墙钟时间和片内时间；之后你随时提问，它先计算电影播放到哪里，再只读取安全时间点之前的字幕上下文来回答。它会像一个搭子一样聊电影，但不会提前说后面的剧情。

## 能做什么

- 进入放映模式并持续推算当前片内时间
- 解析 `.srt` / `.vtt` 字幕
- 支持普通对白字幕和描述字幕、SDH、音频描述字幕
- 每次回答前自动取最新安全上下文
- 严格禁止剧透
- 不要求截图

## 不能做什么

- 不能直接读取 Netflix、Disney+ 等 DRM 视频画面
- 不能凭空知道没有出现在字幕或描述轨里的视觉细节
- 不会帮你获取盗版资源

## 安装

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

## 快速开始

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

## 放映模式口令

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

## 无剧透规则

默认安全时间是：

```text
当前估算片内时间 - 8 秒
```

回答只能使用安全时间之前的字幕和描述轨。即使模型知道电影结局，也不能把后面的信息带进来。

## 仓库结构

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

