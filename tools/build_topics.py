#!/usr/bin/env python3
"""Turn the cached view-count rankings into TOPICS.md.

Usage:
    python3 tools/build_topics.py <ranks_dir> -o TOPICS.md

Curation rule, decided with BigCat: quota per podcast, ranked by plays INSIDE
each podcast. Raw view counts are not comparable across channels — Lex runs
5-10x Huberman on subscriber base alone — so a single global sort would hand
the whole list to the biggest channel.

Re-runnable from the cache: rank_episodes.py parks every hydrated episode in
`<name>.raw.json`, so quotas and filters can be revised without paying the
view-count lookup again (an hour across the roster).
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from rank_episodes import select  # noqa: E402

# name -> (display, quota, topic filter or None)
# Making Sense carries a topic filter because its consciousness and philosophy
# back catalogue — the reason it is on the roster — sits mostly behind its
# paywall, so ranking what remains by plays alone returns current-affairs
# episodes that match neither the site's subject nor its shelf life.
CONSCIOUSNESS = re.compile(
    r"\b(conscious\w*|meditat\w*|mindful\w*|self|selves|free will|philosoph\w*|"
    r"buddh\w*|psychedelic\w*|moral\w*|ethic\w*|mind|minds|reality|awareness|"
    r"illusion|enlighten\w*|nirvana|dharma)\b", re.I)

ROSTER = [
    ("mindscape",   "Mindscape (Sean Carroll)",      25, None),
    ("huberman",    "Huberman Lab",                  16, None),
    ("dwarkesh",    "Dwarkesh Podcast",              15, None),
    ("acquired",    "Acquired",                      12, None),
    ("lex",         "Lex Fridman Podcast",           12, None),
    ("ezraklein",   "The Ezra Klein Show",            8, None),
    ("cowen",       "Conversations with Tyler",       8, None),
    ("makingsense", "Making Sense (Sam Harris)",      4, CONSCIOUSNESS),
]

DOMAINS = [
    (r"\b(quantum|entangle\w*|spacetime|gravit\w*|cosmolog\w*|physic\w*|multiverse|"
     r"relativity|black hole|string theory|particle)\b", "物理 / 宇宙学"),
    (r"\b(conscious\w*|mind|minds|self|selves|free will|qualia|awareness)\b", "意识 / 心智"),
    (r"\b(philosoph\w*|metaphys\w*|epistem\w*|moral\w*|ethic\w*|meaning|buddh\w*|"
     r"christian\w*|religio\w*|theolog\w*)\b", "哲学 / 宗教"),
    (r"\b(evolution\w*|genetic\w*|genome|ancient DNA|tribe|species|dna|biolog\w*)\b", "演化 / 生物"),
    (r"\b(AI|artificial intelligence|LLM|AGI|neural net\w*|machine learning|superintelligence|"
     r"scaling|alignment|model[s]?)\b", "人工智能"),
    (r"\b(dopamine|neuro\w*|brain|sleep|ADHD|focus|memory|stress|anxiety|emotion\w*|"
     r"depress\w*|mental health|psychedelic\w*)\b", "神经科学 / 心理"),
    (r"\b(muscle|strength|fitness|endurance|fat loss|nutrition|diet|fasting|supplement\w*|"
     r"exercise|training|alcohol|hormone|testosterone)\b", "健康 / 体能"),
    (r"\b(war|dictator\w*|empire|stalin|mao|history|histor\w*|geopolitic\w*|civilization)\b",
     "历史 / 地缘"),
    (r"\b(market\w*|econom\w*|compan\w*|business|founder|CEO|invest\w*|capital|semiconductor|"
     r"chips?|moat|strategy)\b", "商业 / 投资"),
    (r"\b(complex\w*|emergen\w*|network\w*|system\w*|computation\w*|information)\b", "复杂性 / 系统"),
    (r"\b(politic\w*|democra\w*|election|president\w*|trump|harris|walz|buttigieg|"
     r"liberal\w*|conservativ\w*|policy|foreign policy|ukraine|israel|hamas|"
     r"immigration|media|speech)\b", "政治 / 社会"),
    (r"\b(alien\w*|extraterrestrial|habitable|exoplanet\w*|SETI|civilizations?)\b", "宇宙 / 地外"),
]

# Titles that are just a company name, or just a person's name, carry no keyword
# to match on. Where a show's whole premise fixes the subject, the channel is a
# better signal than the title: Acquired is always a company history.
CHANNEL_DEFAULT = {
    "acquired": "商业 / 投资",
    "ezraklein": "政治 / 社会",
    "cowen": "经济 / 跨学科",
}

# Recognisable names whose episodes have no topical keyword in the title.
NAME_DOMAINS = [
    (r"\b(karpathy|sutskever|altman|amodei|hassabis|ajeya cotra|jensen huang|"
     r"zuckerberg|demis)\b", "人工智能"),
    (r"\b(sapolsky|huberman|conti|palmer|attia)\b", "神经科学 / 心理"),
    (r"\b(jamie dimon|schultz|buffett|munger)\b", "商业 / 投资"),
]

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "on", "in", "to", "for", "with", "is", "are",
    "how", "why", "what", "we", "you", "your", "our", "it", "its", "that", "this",
    "conversation", "episode", "full", "solo", "mindscape", "dr", "prof", "podcast",
}
# publish.sh keys the issue number off `-<kind><N>.html`; a slug ending in one of
# these would make a filename it parses as the wrong kind.
FORBIDDEN_SLUG_WORDS = ("day", "week", "book", "issue", "read", "paper", "blog", "talk",
                        "novel", "pod")


def domain_of(title, channel=None):
    """Topic keywords win, then a recognisable name, then the show's own premise."""
    for pat, name in DOMAINS:
        if re.search(pat, title, re.I):
            return name
    for pat, name in NAME_DOMAINS:
        if re.search(pat, title, re.I):
            return name
    if channel in CHANNEL_DEFAULT:
        return CHANNEL_DEFAULT[channel]
    return "思想 / 访谈"


def slugify(title, taken):
    t = re.sub(r"\([^)]*\)", " ", title)                 # drop "(Episode #241)" etc

    # Leading house numbering: "Mindscape 63 | Solo: ...", "Episode 28: ...".
    t = re.sub(r"^\s*(Mindscape|Episode|Ep\.?)\s*#?\d*\s*[|:]?\s*", " ", t, flags=re.I)

    # Only a TRAILING pipe segment that is the show's own branding gets dropped.
    # Blanket-stripping everything after "|" loses the real title on shows that
    # put it there: "The Biggest Ideas in the Universe | 16. Gravity" collapsed
    # to one slug for three different lectures, and two Mindscape solos came out
    # as bare "episode".
    t = re.sub(r"\|\s*[^|]*(podcast|show|lab|#\d+)[^|]*$", " ", t, flags=re.I)
    t = re.sub(r"#\d+", " ", t)
    t = t.replace("|", " ")
    t = re.sub(r"[^\w\s-]", " ", t, flags=re.UNICODE)
    words = [w.lower() for w in t.split()]
    words = [w for w in words if w and w not in STOPWORDS and not w.isdigit()]
    words = [w for w in words if w not in FORBIDDEN_SLUG_WORDS]
    slug = "-".join(words[:6]) or "episode"
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    base, n = slug, 2
    while slug in taken:
        slug, n = f"{base}-{n}", n + 1
    taken.add(slug)
    return slug


def interleave(groups):
    """Spread each podcast evenly across the whole list.

    Each channel's i-th pick is given the position it would occupy if that
    channel alone were spaced evenly over the run, then everything is sorted by
    position. A channel with 25 of 100 slots lands roughly every fourth issue,
    one with 4 lands roughly every twenty-fifth, and within a channel the plays
    order from `select` is preserved.

    Greedily taking from whichever channel has the most left does NOT work: the
    biggest quota stays the biggest until it draws level with the runner-up, so
    the list opens with ten straight issues of the same show.
    """
    total = sum(len(v) for v in groups.values())
    placed = []
    for name, eps in groups.items():
        if not eps:
            continue
        step = total / len(eps)
        for i, e in enumerate(eps):
            placed.append(((i + 0.5) * step, name, e))
    placed.sort(key=lambda p: p[0])
    return [(name, e) for _, name, e in placed]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ranks_dir")
    ap.add_argument("-o", "--out", default="TOPICS.md")
    args = ap.parse_args()

    groups, display, short = {}, {}, []
    for name, label, quota, topic in ROSTER:
        raw = Path(args.ranks_dir) / f"{name}.raw.json"
        if not raw.exists():
            sys.exit(f"ERROR: missing cache {raw} — run tools/rank_episodes.py first")
        eps = json.loads(raw.read_text(encoding="utf-8"))["episodes"]
        if topic:
            eps = [e for e in eps if topic.search(e["title"])]
        chosen, _ = select(eps, quota)
        if len(chosen) < quota:
            short.append(f"{name}: {len(chosen)}/{quota}")
        groups[name] = chosen
        display[name] = label

    if short:
        print("WARNING: quota not filled — " + "; ".join(short), file=sys.stderr)

    order = interleave(groups)
    taken = set()

    lines = [
        "# 播客清单 Podcast Reading List（按播客配额 + 频道内播放量排序）",
        "",
        "BigCat 人工策划。选法：**每个播客分配名额，名额内按该频道自己的 YouTube 播放量取前 N**。",
        "不跨频道拉通排序——各频道订阅盘子差 5–10 倍，全局排序只会让最大的频道吃掉整张清单。",
        "",
        "已排除：AMA / Q&A / 年度回顾 / 预告（没有可追的单一论证）；同一嘉宾或同一系列超过 3 期的部分",
        "（多样性上限，不是质量判断）。**单人深讲保留**——一个人讲透一个想法，比访谈更好精读。",
        "Making Sense 另加主题过滤：它的意识与哲学存货大半在付费墙后，只按播放量排会选出时事政治。",
        "",
        "> **选题 / 编号规则**",
        "> - **严格从上往下取第一个未做的 slug**。顺序已按频道轮转排好，别跳序。",
        "> - 文件名 `{slug}-pod{N}.html`，**N = 现有最大 N + 1**（写作顺序，与清单顺序解耦）。",
        "> - 本清单**人工策划、routine 只读不改**（`publish.sh` 硬卡改动）。全做完 → PushNotification",
        ">   请 BigCat 续单、本次不发布。",
        "> - `transcript` 指向私有仓 `cissy0802/podcast-transcripts` 里的文件。**读不到就不发布**——",
        ">   云端抓不了 YouTube 字幕，没有退路，绝不能凭记忆或二手摘要写。",
        "> - **本清单不写内容钩子**：钩子只能从标题猜，而猜出来的钩子会变成引擎的先入之见。",
        ">   引擎读到什么写什么。",
        "",
        f"共 {len(order)} 期。播放量为抓取当日（2026-09-19）数值。",
        "",
        "---",
        "",
    ]

    for name, e in order:
        slug = slugify(e["title"], taken)
        yr = e["upload_date"][:4]
        mins = e["duration_s"] // 60
        lines += [
            f"- **{display[name]}** — {e['title']}",
            f"  - {yr} · {mins} 分钟 · {e['views']:,} 播放 · {domain_of(e['title'], name)}",
            f"  - source: <{e['url']}>",
            f"  - transcript: `transcripts/{slug}.txt`",
            f"  - slug: `{slug}`",
            "",
        ]

    Path(args.out).write_text("\n".join(lines), encoding="utf-8")
    counts = {display[n]: len(v) for n, v in groups.items()}
    print(f"{args.out}: {len(order)} episodes")
    for k, v in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {v:>3}  {k}")


if __name__ == "__main__":
    main()
