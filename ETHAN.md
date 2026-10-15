# ETHAN.md — Ethan Evans 专题

这是「Ethan Evans 专题」的执行说明，由单独的 routine 手动触发，一次写一篇。**本文件之外，`CLAUDE.md` 的第 3 节（引语规则）、第 5 节（写作要求，尤其 5.1「中文要像中文」）、第 6 节（版式）同样适用**；两者冲突时听本文件的。

## 这个专题要做什么

Ethan Evans 在 Amazon 做了约十五年，2020 年以 VP 身份退休，现在以教人「过晋升关」为业。他从 2023 年起写 newsletter《Level Up》，至今三百多篇，又上了几十期播客。BigCat 想**系统地学他**：不是听完一期记一期，而是按主题把他散在几百篇文章和几十小时访谈里的东西理成体系。

所以每一篇专题页是**一个主题**，素材是他关于这个主题的多篇文章 + 访谈。读完一篇，读者应该能说清：他在这个主题上的核心主张是什么、这些主张从他哪段经历里来、它们彼此怎么咬合、哪里站得住哪里只是一个人的经验。

**这不是文章摘要合集，不是「Ethan Evans 金句」，也不是替他做推广。** 他是职业教练，「我敢说别人不敢说的真话」本身就是他的品牌；写的时候要看得见这一层。

## 0. 开工

1. 跑 `bash setup.sh`，读 `.preflight`。`transcripts: BLOCKED` 或 `egress: BLOCKED` → 不发布，PushNotification 报告，结束。
2. 素材在私有仓里（与播客转写同仓）：
   - **文章**：`../podcast-transcripts/ethan-evans/*.md`，每篇一个文件，头部有 title / date / url。只有免费文章；付费文章拿不到，**不要去找、不要引用付费文章的内容**。
   - **访谈转写**：`../podcast-transcripts/transcripts/` 下文件名含 `ethan-evans` 或 `amazon-vp-` 的那些。没有的就不用。
3. 已经写好的专题页：`ls *-topic*.html`。index 里「Ethan Evans 专题」分区的灰行就是待写主题。

## 1. 选题 / 编号

- 从下面「主题清单」**从上往下取第一个还没有页面的主题**，别跳序。
- 文件名 `{slug}-topic{N}.html` + `.en.html`，**N = 现有最大 topic N + 1**。
- 全部写完 → PushNotification 告诉 BigCat 专题写完了，本次不发布。

## 2. 动手前：先真读

- **用 `grep -il` 在文章目录里按关键词找这个主题的文章**，主题清单里列的代表文章只是起点，不是全部。通常一个主题有 8–20 篇相关文章；**至少完整读 8 篇**，再加相关访谈里讲到这个主题的段落。
- 读的时候按**时间顺序**排开：他 2023 年和 2026 年对同一件事的说法是否一致？哪些观点被他反复讲（核心），哪些只出现一次（边角）？说法有没有变？**观点的演变本身是很好的素材。**
- 把打算引用的句子连同出处 URL 存到 `/tmp/quotes.txt`，写作时从这里复制。
- 「边界」一节需要的外部证据（研究、报道、公司公开文件）照 `CLAUDE.md` 2b 的标准去找，至少读 1 份一手材料。

## 3. 页面结构

从 `TEMPLATE.html` 复制起步，删掉所有 `TEMPLATE` 注释。**header 的 kicker 写「Ethan Evans 专题 · 第 N 篇」**，meta-card 写：主题 · 用到的文章篇数和年份跨度 · 用到的访谈（节目名）。

七节：

1. **那一幕** — 从他讲过的某个具体故事开场（一次会议、一次被拒、一句老板的话），带出这个主题。不要从「Ethan Evans 是前 Amazon VP」开场。
2. **他的主张**（主体之一）— 2–4 个核心观点，每个一个 `<h3>`。每个观点讲清：他怎么说、他用什么经历或例子撑、他在不同文章里怎么反复或修正这个说法。**把几篇文章合成一条线讲，不要一篇一篇地复述。** 引用文章时把链接挂在正文那个词上。
3. **这些主张怎么咬合** — 一两段，说清这个主题下的几个观点之间是什么关系，以及它跟专题里其他主题（晋升、向上管理、组织政治……）怎么连起来。这是「系统地学」的那一部分。
4. **边界** — 1–2 个 `.claim` 框，判词沿用 `CLAUDE.md` 的五档。挑他在这个主题上**最有影响、最可能被读者照做**的说法，问：这是有证据的规律，还是一个 VP 的幸存者视角？换一家公司、一个不同的人还成立吗？他自己有没有承认过例外或合理化？每框约 100 字。
5. **越界 · 跨学科的联想**（`.crossx`，3–5 条）— 照 `CLAUDE.md`。
6. **十条要点**（`<ol class="takeaways">`，正好 10 条）— 照 `CLAUDE.md`：每条单独抄进笔记也能看懂，**不放边界一节的判词**。
7. **出处** — 本页用到的**最重要的** 3–6 篇文章 / 访谈，每条一句短说明。其余文章在正文里挂链接即可。

## 4. 写作要求

- 篇幅：中文约 3500 字，上限 4500（`.maxchars`）。
- 引语照 `CLAUDE.md` 第 3 节：每句 ≤ 两句话、全页 ≤ 8 处、一个字不改。**文章引语挂文章链接，访谈引语挂时间戳链接**。全页时间戳 ≤ 12。
- 他的文章是受版权保护的付费作者的作品：**只出概括和短引，绝不整段搬运**，也不要把一篇文章的结构原样复刻成一节。
- 他用的术语（Magic Loop、L7、URA、PIP、LP……）首次出现时用大白话解释。
- 中文要像中文（`CLAUDE.md` 5.1）。写完通读一遍。

## 5. index

index 最下面是「Ethan Evans 专题」分区（`data-show="Ethan Evans 专题"`）。找到本主题的灰行（`data-slug` 匹配），**原地**改成链接：`.title` 写成「主题名 — 一句钩子」，`.meta` 保持「专题」/「Topic」，加 `data-updated` 和 `.date`。两个 index 都改。不要动别的分区。

## 6. 发布

`./publish.sh`。完成后 PushNotification（一行、无 markdown）：
`Ethan Evans 专题已更新：第 N 篇 <主题名> · <一句钩子> · hub.cissychen.com/podcast-deepread`

## 主题清单（按顺序写）

1. **ethan-evans-who · 他是谁：从工程师到 VP，再到巅峰时离开**
   职业时间线和每一段学到的东西。代表文章：My path to Amazon Vice President · Being "unreasonable" drove me to Amazon VP · From an 800-person team to IC · Why I Left Amazon at My Peak · My layoff story · Origins of a Billion Dollar Business: Amazon Prime Video · I pursued my VP role without fully understanding the job。
2. **ethan-evans-promotion · 晋升的机制**
   代表文章：The Magic Loop · Relationships Drive Promotion · "Formula" to build the relationships and trust that drive promotions · Who managers promote and why · Path to Promotion: Patience, Opportunism, A Plan · Make the case for your promotion · "Klingon Promotions" · The Amazon "secret" of controllable inputs · Speedrunning Guide: Junior to Staff Engineer in 3 years。
3. **ethan-evans-l7 · 卡在 L7：从经理到高管**
   代表文章：The "L7" Problem · Too damn many Senior Managers · Stuck at Senior Manager for 12 years · 4 reasons why people get stuck at Senior Manager · How to Break Into Senior Leadership Roles · Mindset Shift: IC to Manager · Struggles scaling as a Director at Amazon。
4. **ethan-evans-managing-up · 向上管理与影响力**
   代表文章：Surviving Bad Managers · How to decode your manager · Manage Up to Executives · Handling demanding leaders · How to win buy-in from CEOs · Saying the hard thing · "How to Say You Stink…Nicely" · Perception dictates reality · Straight Truth: My Boss Isn't Supporting Me。
5. **ethan-evans-presence · 高管气场与表达**
   代表文章：Executive Presence 系列（Ingredients · How to get "it" · Killers · Own the Room）· The New Rules of Presence · Why Public Speaking Is No Longer Optional · From Shy to Davos。
6. **ethan-evans-org-reality · 组织真实的运行方式：政治、重组、裁员、PIP**
   代表文章：Straight Truth: HR is not there to help you · Reorgs are the new promotion · Why reorgs happen · Are PIPs designed to fail? · Layoffs will continue all year · How to stay off the layoff lists · Weaponizing / Degenerate Leadership Principles · Executive advice on corporate politics。访谈：Peterman 的三期（它们已有单独的精读页，本篇链接过去，不重复其内容，侧重把文章里的观点跟访谈对照）。
7. **ethan-evans-amazon-bezos · Amazon 与 Bezos**
   代表文章：Dissecting Amazon Leadership Principles · "That's not my job" - How I wrote a part of an Amazon LP · How to "Think Big" · My Jeff Bezos Story: How to Survive a Bad Failure · A day in the life of an Amazon VP · "You're doing this all wrong" - Amazon SVP。
8. **ethan-evans-career-life · 职业选择与人生**
   代表文章：When to quit your manager? · How To Find a Great Manager · Aging in tech, the truth · It's Hard to Switch Careers without Taking a Step Back · 11 Questions You Must Answer Before Leaving Your Corporate Job · Wealth from a corporate job is a recipe · The Hidden Cost of Being a High Achiever · "In 20 years only your children will remember that you worked late" · Drop the Ball。
