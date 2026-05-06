# 电影搭子.skill

<p align="center">
  <img src="skills/movie-companion/references/logo.png" alt="电影搭子.skill logo" width="180" />
</p>

一个无剧透、包容接纳的 Codex 电影陪看 skill。

A no-spoiler, inclusive Codex movie companion skill.

你说“开始观看”，它记录当前墙钟时间和片内时间；之后你随时提问，它会先计算电影播放到哪里，再只读取安全时间点之前的字幕上下文来回答。它像一个搭子一样陪你聊电影，但不会提前说后面的剧情。

When you say "开始观看" or "start watching", it records wall-clock time and movie time. When you ask a question later, it calculates where the movie should be, retrieves only subtitle context before the safe time, and answers like a movie buddy without spoiling later events.

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

> Replace `<owner>/<repo>` with the GitHub repository where this skill is published.
>
> 把 `<owner>/<repo>` 替换成你发布这个 skill 的 GitHub 仓库名。

### Option A: Codex `$skill-installer`

Codex's official installer can install a skill from a GitHub repo path. This repository stores the skill at `skills/movie-companion`:

Codex 官方安装器可以从 GitHub 仓库路径安装 skill。这个仓库把 skill 放在 `skills/movie-companion`：

```text
$skill-installer install the movie-companion skill from <owner>/<repo> with path skills/movie-companion
```

Equivalent command if you are using the local installer script directly:

如果你直接使用本地安装脚本，对应命令是：

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path skills/movie-companion
```

Restart Codex after installation.

安装完成后重启 Codex。

### Option B: Skills CLI

The open agent skills ecosystem also supports GitHub installs:

开放 Agent Skills 生态也支持从 GitHub 安装：

```bash
npx skills add <owner>/<repo> --agent codex
```

If your installer asks for a specific skill, choose `movie-companion`.

如果安装器要求选择具体 skill，请选择 `movie-companion`。

### Option C: Manual Install

Clone the repository, then run the included installer:

克隆仓库，然后运行仓库自带安装脚本：

```bash
git clone https://github.com/<owner>/<repo>.git movie-companion
cd movie-companion
bash scripts/install.sh
```

PowerShell version:

PowerShell 版本：

```powershell
git clone https://github.com/<owner>/<repo>.git movie-companion
Set-Location movie-companion
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

Validate the install:

验证安装：

```bash
ls ~/.codex/skills/movie-companion
head -n 5 ~/.codex/skills/movie-companion/SKILL.md
```

After restarting Codex, the display name is:

重启 Codex 后，显示名是：

```text
电影搭子.skill
```

The internal invocation name is:

内部调用名是：

```text
$movie-companion
```

## 快速开始 / Quick Start

Use your own subtitle paths. The examples below use placeholder filenames.

请替换成你自己的字幕路径。下面都是通用占位示例。

Create a subtitle index:

生成字幕索引：

```bash
python skills/movie-companion/scripts/movie_sync.py index \
  --subtitle /path/to/movie-dialogue.srt \
  --description /path/to/movie-description.srt \
  --movie "Movie Title" \
  --output /path/to/movie.movie-index.json
```

If you only have dialogue subtitles, omit `--description`:

如果只有普通对白字幕，可以省略 `--description`：

```bash
python skills/movie-companion/scripts/movie_sync.py index \
  --subtitle /path/to/movie-dialogue.srt \
  --movie "Movie Title" \
  --output /path/to/movie.movie-index.json
```

Start screening mode:

开始放映：

```bash
python skills/movie-companion/scripts/movie_sync.py start \
  --index /path/to/movie.movie-index.json \
  --at 00:00:00 \
  --session /path/to/movie.watch-session.json
```

Get the spoiler-safe context bundle before answering:

提问前获取无剧透安全上下文：

```bash
python skills/movie-companion/scripts/movie_sync.py ask \
  --session /path/to/movie.watch-session.json \
  --before 900
```

PowerShell users can use the same commands on one line, or replace `\` with PowerShell backticks.

PowerShell 用户可以写成一行，或把 `\` 换成 PowerShell 的反引号。

Pause, close, or inspect a session:

暂停、关闭或查看会话状态：

```bash
python skills/movie-companion/scripts/movie_sync.py pause --session /path/to/movie.watch-session.json
python skills/movie-companion/scripts/movie_sync.py close --session /path/to/movie.watch-session.json
python skills/movie-companion/scripts/movie_sync.py status --session /path/to/movie.watch-session.json
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

If you can find SDH, closed captions, descriptive subtitles, or audio-description transcripts, this skill gets better scene context. Regular dialogue subtitles still work, but visual details will be handled more cautiously.

如果能找到 SDH、closed captions、descriptive subtitles 或 audio-description transcript，这个 skill 会更懂场面；只有普通字幕也可以，只是视觉细节会更谨慎。

## 放映模式口令 / Screening Mode Commands

You can say:

你可以这样说：

```text
开始观看
```

If you are not starting from the beginning:

如果不是从头开始：

```text
开始观看 00:17:42
```

Pause or close:

暂停或关闭：

```text
暂停
关闭放映模式
```

Resume with a visible timestamp:

继续时重新给一个可见时间点：

```text
开始观看 00:28:10
```

## 无剧透规则 / No-Spoiler Rule

Default safe time:

默认安全时间是：

```text
estimated movie time - 8 seconds
当前估算片内时间 - 8 秒
```

Answers can only use subtitles and descriptive tracks before the safe time. Even if the model knows the ending, it must not bring later information into the answer.

回答只能使用安全时间之前的字幕和描述轨。即使模型知道电影结局，也不能把后面的信息带进来。

## 搭子语气 / Companion Voice

The skill should sound inclusive, accepting, and easy to talk to. Basic questions, missed details, confused reactions, emotional responses, or unusual interpretations are all welcome.

这个 skill 的语气要包容、接纳、轻松。用户问基础问题、看漏了、没听懂歌词、对角色有不同感受，都应该被正常接住。

## 仓库结构 / Repository Structure

```text
.
├── skills/
│   └── movie-companion/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       ├── references/
│       │   ├── architecture.md
│       │   └── logo.png
│       ├── scripts/
│       │   ├── __init__.py
│       │   └── movie_sync.py
│       └── examples/
│           └── sample-dialogue.srt
├── scripts/
│   ├── install.ps1
│   └── install.sh
├── tests/
│   └── test_movie_sync.py
├── README.md
├── 搭子说明.md
├── LICENSE
└── .gitignore
```
