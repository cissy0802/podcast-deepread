# NAVAL.md — Naval 专题

这是「Naval 专题」的执行说明，由单独的 routine 手动触发，一次写一篇。**本文件之外，`CLAUDE.md` 的第 3 节（引语规则）、第 5 节（写作要求，尤其 5.1「中文要像中文」）、第 6 节（版式）同样适用**；两者冲突时听本文件的。结构照抄 `ETHAN.md`，下面只写不一样的地方。

## 这个专题要做什么

Naval Ravikant 是硅谷的天使投资人、AngelList 的联合创始人。他在 2018 年发了一串推文《How to Get Rich (without getting lucky)》，2019 年和 Babak Nivi 把它逐条录成一季播客，后来又讲了一季幸福，Eric Jorgenson 再把他十几年的推文和访谈编成《The Almanack of Naval Ravikant》（2020）。他的东西流传极广，但几乎全是**格言**：一句话、没有论证、没有出处。

BigCat 想**系统地读他**：把散在推文、播客、访谈里的格言按主题理成体系，每条格言放回它被说出的那段对话里，看它背后有没有论证、论证站不站得住。读完一篇，读者应该能说清：他在这个主题上的核心主张是什么、这些主张彼此怎么咬合、哪些是可检验的规律、哪些只是一个成功投资人的人生哲学。

**这不是格言合集，不是「纳瓦尔宝典」的读书笔记，也不是替他做推广。** 格言的力量来自压缩，代价是丢掉了条件；本专题的功夫就在把条件找回来。

## 0. 开工

1. 跑 `bash setup.sh`，读 `.preflight`。`transcripts: BLOCKED` 或 `egress: BLOCKED` → 不发布，PushNotification 报告，结束。
2. 素材在私有仓里（与播客转写同仓）：
   - **文字**：`../podcast-transcripts/naval/*.md`，每篇一个文件，头部有 title / date / url / source。来源是 nav.al 上的播客逐字稿和文章、《How to Get Rich》推文串原文，以及《The Almanack of Naval Ravikant》（作者免费发布的版本）。
   - **访谈转写**：`../podcast-transcripts/transcripts/` 下文件名以 `naval-` 开头的那些。
   - **目录不存在或少于 10 个文件 → 不发布**，PushNotification 请 BigCat 先在笔记本上抓素材（见文末「素材清单」），结束。**绝不能凭记忆写**：他的格言网上流传的版本和原话常常不一样，很多「纳瓦尔语录」根本不是他说的。
3. 已经写好的专题页：`ls naval-*-topic*.html`。index 里「Naval 专题」分区的灰行就是待写主题。

## 1. 选题 / 编号

- 从下面「主题清单」**从上往下取第一个还没有页面的主题**，别跳序。
- 文件名 `{slug}-topic{N}.html` + `.en.html`，**N = 仓库里现有最大 topic N + 1**（和 Ethan 专题共用一个编号序列，`publish.sh` 按 `topic` 查重）。
- 全部写完 → PushNotification 告诉 BigCat 专题写完了，本次不发布。

## 2. 动手前：先真读

- **用 `grep -il` 在素材目录里按关键词找这个主题的材料**，主题清单里列的只是起点。**至少完整读 6 份**，其中至少 1 份是访谈转写（不是格言汇编），因为格言的条件往往只在对话里才说出来。
- **先分清是谁的话。** 《Almanack》是 Jorgenson 编的，有编者的串场和归类；nav.al 的播客里一半是 Nivi 在说。只把 Naval 本人的话算在他头上。网上流传的「Naval 语录」只有在素材里找得到原文时才能用。
- **把格言放回原处**：同一句话第一次是在哪说的、前后在聊什么、主持人有没有追问、他后来有没有修正。他 2018 年和 2024 年以后对同一件事的说法是否一致？**观点的演变本身是很好的素材**（比如他对加密货币、对 AI 的态度）。
- 把打算引用的句子连同出处存到 `/tmp/quotes.txt`，写作时从这里复制。
- 「边界」一节照 `CLAUDE.md` 2b 的标准找外部证据，至少读 1 份一手材料。他的说法多半是人生哲学，判「这是观点，不是事实」完全正常；但凡是能被数据检验的（谁靠什么变富、冥想对焦虑有多大效果），就去拿数据对。

## 3. 页面结构

从 `TEMPLATE.html` 复制起步，删掉所有 `TEMPLATE` 注释。**header 的 kicker 写「Naval 专题 · 第 N 篇」**（这里的 N 是本专题内的序号，不是文件名里的 topic N），meta-card 写：主题 · 用到的材料份数和年份跨度 · 用到的访谈（节目名）。

六节，同 `ETHAN.md` 第 3 节：

1. **他的主张**（主体之一）— 2–4 个核心观点，每个一个 `<h3>`。每个观点讲清：那句格言原话、它被说出时的上下文、他用什么论证或例子撑、它需要哪些前提条件才成立。**把几处材料合成一条线讲，不要一条格言一条格言地罗列。**
2. **这些主张怎么咬合** — 一两段，说清这几个观点之间的关系，以及它跟专题里其他主题（致富、判断力、幸福……）怎么连起来。Naval 自己的体系是咬得很紧的（财富是为了自由，自由是为了内心的平静），这一节要把这条链画出来，也要指出链上哪一环最弱。
3. **边界** — 1–2 个 `.claim` 框，判词沿用 `CLAUDE.md` 的五档。挑他在这个主题上**最有影响、最可能被读者照做**的说法，问：这是有证据的规律，还是一个早早押中 Twitter、Uber 的投资人的幸存者视角？换一个起点不同的人还成立吗？他自己有没有承认过例外？每框约 100 字。
4. **越界 · 跨学科的联想**（`.crossx`，3–5 条）— 照 `CLAUDE.md`。他大量借用佛学、斯多葛、进化论、博弈论，**他自己点名的只能进「他的主张」，我们联想的才进越界**（`CLAUDE.md`「展开」一节的规矩）。
5. **十条要点**（`<ol class="takeaways">`，正好 10 条）— 照 `CLAUDE.md`：每条单独抄进笔记也能看懂，**不放边界一节的判词**。
6. **出处** — 本页用到的**最重要的** 3–6 份材料，每条一句短说明。其余在正文里挂链接即可。

## 4. 写作要求

- 篇幅：中文约 3500 字，上限 4500（`.maxchars`）。
- 引语照 `CLAUDE.md` 第 3 节：每句 ≤ 两句话、全页 ≤ 8 处、一个字不改。**文字材料的引语挂它的公开 URL（nav.al 页面），访谈引语挂时间戳链接**。全页时间戳 ≤ 12。《Almanack》的引语注明书名和章节，不链接 PDF。
- **格言不算论证。** 一句漂亮的格言后面，要么接他自己给的理由，要么写明他没给理由。不要替他补论证。
- 他用的说法（specific knowledge、permissionless leverage、long-term games、「desire is a contract」……）首次出现时用大白话解释，并给英文原词。
- 引用别的页面写标题、挂链接，不写编号：专题内部互相引用写「《致富的机制》一篇」。
- 不写成鸡汤，也不写成拆台。他说对的地方照样说对。
- 中文要像中文（`CLAUDE.md` 5.1）。写完通读一遍。

## 5. index

index 最下面、「Ethan Evans 专题」之后是「Naval 专题」分区（`data-show="Naval 专题"`）。找到本主题的灰行（`data-slug` 匹配），**原地**改成链接：`.title` 写成「主题名 — 一句钩子」，`.meta` 保持「专题」/「Topic」，加 `data-updated` 和 `.date`。两个 index 都改。不要动别的分区。

## 6. 发布

`./publish.sh`。完成后 PushNotification（一行、无 markdown）：
`Naval 专题已更新：第 N 篇 <主题名> · <一句钩子> · hub.cissychen.com/podcast-deepread`

## 主题清单（按顺序写）

1. **naval-who · 读他之前：四个折扣**
   同 Ethan 专题的第一篇，不是人物小传，回答「他的话是站在什么位置上说的」。按四个折扣组织：
   - **时代**：他的财富主要来自 2000 年代末到 2010 年代硅谷早期投资的黄金期（Twitter、Uber 等）。哪些建议依赖那个窗口？
   - **位置**：天使投资人看到的是幂律分布的赢家一端。从那里看「杠杆」和「股权」是什么样，看不见什么？
   - **体裁**：推文和格言。压缩掉了哪些条件？同一句话在长访谈里是怎么说的？
   - **动机**：他是投资人、AngelList 的创始人，也是一个有大批追随者的公共人物。这会怎样影响他讲什么、不讲什么？
   「他的主张」一节在这一篇里换成「四个折扣」四个小节；其余各节照常。
2. **naval-wealth · 致富的机制：特定知识、杠杆、责任**
   起点：How to Get Rich 推文串与 2019 年播客季。关键词：specific knowledge、leverage（劳动 / 资本 / 代码与媒体）、accountability、equity、「renting out your time」、compound interest。
3. **naval-judgment · 判断力与决策**
   起点：Almanack 里讲判断、阅读、心智模型、第一性原理的部分；访谈里谈决策的段落。关键词：judgment、mental models、「if you can't decide, the answer is no」、read the originals。
4. **naval-happiness · 幸福是一种可以练的技能**
   起点：nav.al 的幸福播客季、Almanack 的 Happiness 部分。关键词：desire、peace、habits、「happiness is a choice / a skill」。
5. **naval-self · 自我、冥想与东方哲学**
   起点：他谈冥想、ego、Krishnamurti、non-duality、佛学的段落（Joe Rogan、Knowledge Project 等访谈）。这一篇最贴近读者的深度兴趣，越界可以写得深一些。
6. **naval-learning · 读书与学习**
   起点：Almanack 里讲阅读与学习的部分。关键词：read what you love、foundations（数学、科学、说服力）、learning to learn。
7. **naval-life · 长期游戏：健康、关系与人生选择**
   起点：long-term games with long-term people、健康与运动、家庭、退休的定义。

## 素材清单（在笔记本上抓，云端抓不到）

云端环境访问不到 YouTube 字幕和 nav.al，素材要在住宅网络下抓好，放进私有仓 `cissy0802/podcast-transcripts`：

- **访谈转写** → `transcripts/naval-{slug}.txt`，用 `python3 tools/fetch_transcript.py <YouTube URL> -o …`。建议至少：
  - Joe Rogan Experience #1309 — Naval Ravikant（2019）
  - The Knowledge Project（Shane Parrish）— Naval Ravikant（2017）
  - The Tim Ferriss Show 上 Naval 的几期（2015、2020）
  - nav.al 自己的播客近两年的长期节目（如有 YouTube 版）
- **文字材料** → `naval/{yyyy-mm-dd}-{slug}.md`，头部写 `title / date / url / source / words`（同 `ethan-evans/` 的格式）：
  - nav.al/rich（How to Get Rich 播客全季逐字稿）及推文串原文
  - nav.al 上幸福系列和其他带逐字稿的播客页
  - 《The Almanack of Naval Ravikant》作者免费发布的版本（navalmanack.com），按章拆成多个文件

抓好后 push 私有仓，再触发本 routine。
