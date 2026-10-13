# 播客清单 Podcast Reading List（按播客配额 + 频道内播放量排序）

BigCat 人工策划（2026-10-12 重排：BigCat 在选片面板逐期勾定；砍掉大部分历史/地缘，物理/宇宙学只留 6 期，补 Acquired 的 Google 全三集，新增 The Peterman Pod）。选法：**每个播客分配名额，名额内按该频道自己的 YouTube 播放量取前 N**。
不跨频道拉通排序——各频道订阅盘子差 5–10 倍，全局排序只会让最大的频道吃掉整张清单。

已排除：AMA / Q&A / 年度回顾 / 预告（没有可追的单一论证）；同一嘉宾或同一系列超过 3 期的部分
（多样性上限，不是质量判断；Acquired 的 Google 三部曲例外，按 I→II→III 连写）。**单人深讲保留**——一个人讲透一个想法，比访谈更好精读。
Making Sense 另加主题过滤：它的意识与哲学存货大半在付费墙后，只按播放量排会选出时事政治。

> **选题 / 编号规则**
> - **严格从上往下取第一个未做的 slug**。顺序已按频道轮转排好，别跳序。
> - 文件名 `{slug}-pod{N}.html`，**N = 现有最大 N + 1**（写作顺序，与清单顺序解耦）。
> - 本清单**人工策划、routine 只读不改**（`publish.sh` 硬卡改动）。全做完 → PushNotification
>   请 BigCat 续单、本次不发布。
> - `transcript` 指向私有仓 `cissy0802/podcast-transcripts` 里的文件。**读不到就不发布**——
>   云端抓不了 YouTube 字幕，没有退路，绝不能凭记忆或二手摘要写。
> - **本清单不写内容钩子**：钩子只能从标题猜，而猜出来的钩子会变成引擎的先入之见。
>   引擎读到什么写什么。

共 128 期。播放量为抓取当日数值（原清单 2026-09-19，Peterman Pod 与 Google I/II 2026-10-12）。

The Peterman Pod 不按播放量取，按嘉宾级别人工挑：图灵奖得主、编程语言与基础系统的创造者、业界最高职级（VP / Distinguished / IC9 / CTO / 总监）；
职业发展类以高职级的人为主，另有 BigCat 逐期勾回的几期（IC7/IC8、M2 等）。

---

- **The Peterman Pod** — Amazon VP: Stack Ranking & PIPs, Working With Bezos, His Promotions | Ethan Evans
  - 2025 · 53 分钟 · 635,748 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=40-ENZmqcz0>
  - transcript: `transcripts/amazon-vp-stack-ranking-pips-working.txt`
  - slug: `amazon-vp-stack-ranking-pips-working`

- **The Peterman Pod** — Amazon VP: How Corporate Politics Work And How To Win | Ethan Evans
  - 2026 · 170 分钟 · 562,847 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=6WaeGfLnRvc>
  - transcript: `transcripts/amazon-vp-corporate-politics-work-win.txt`
  - slug: `amazon-vp-corporate-politics-work-win`

- **The Peterman Pod** — Amazon VP: Questions On Corporate Politics But They Get Increasingly Darker | Ethan Evans
  - 2026 · 187 分钟 · 141,049 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=KhjhRRz3VJw>
  - transcript: `transcripts/amazon-vp-questions-corporate-politics-but.txt`
  - slug: `amazon-vp-questions-corporate-politics-but`

- **Huberman Lab** — How to Build Immense Inner Strength | David Goggins
  - 2024 · 157 分钟 · 22,785,766 播放 · 健康 / 体能
  - source: <https://www.youtube.com/watch?v=nDLb8_wgX50>
  - transcript: `transcripts/build-immense-inner-strength-david-goggins.txt`
  - slug: `build-immense-inner-strength-david-goggins`

- **Mindscape (Sean Carroll)** — The Biggest Ideas in the Universe | 16. Gravity
  - 2020 · 109 分钟 · 875,494 播放 · 物理 / 宇宙学
  - source: <https://www.youtube.com/watch?v=353lEB63iyg>
  - transcript: `transcripts/biggest-ideas-universe-gravity.txt`
  - slug: `biggest-ideas-universe-gravity`

- **Acquired** — Porsche (with Doug DeMuro)
  - 2023 · 202 分钟 · 939,212 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=V_fYfdXpkx4>
  - transcript: `transcripts/porsche.txt`
  - slug: `porsche`

- **Lex Fridman Podcast** — Andrew Bustamante: CIA Spy | Lex Fridman Podcast #310
  - 2022 · 233 分钟 · 19,962,249 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=T3FC7qIAGZk>
  - transcript: `transcripts/andrew-bustamante-cia-spy.txt`
  - slug: `andrew-bustamante-cia-spy`

- **Dwarkesh Podcast** — Elon Musk – "In 36 months, the cheapest place to put AI will be space”
  - 2026 · 169 分钟 · 2,349,472 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=BYXbuik3dgA>
  - transcript: `transcripts/elon-musk-months-cheapest-place-put.txt`
  - slug: `elon-musk-months-cheapest-place-put`

- **The Peterman Pod** — Turing Award Winner: Disagreeing with Google, Postgres, Future Problems | Mike Stonebraker
  - 2026 · 56 分钟 · 511,993 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=YPObBOwIrHk>
  - transcript: `transcripts/turing-award-winner-disagreeing-google-postgres.txt`
  - slug: `turing-award-winner-disagreeing-google-postgres`

- **Conversations with Tyler** — @any_austin  on the Hermeneutics of Video Games
  - 2025 · 66 分钟 · 59,841 播放 · 经济 / 跨学科
  - source: <https://www.youtube.com/watch?v=rOYjgXY-Ts4>
  - transcript: `transcripts/any_austin-hermeneutics-video-games.txt`
  - slug: `any_austin-hermeneutics-video-games`

- **The Ezra Klein Show** — Kara Swisher on the Radicalization of Elon Musk | The Ezra Klein Show
  - 2025 · 67 分钟 · 1,615,303 播放 · 政治 / 社会
  - source: <https://www.youtube.com/watch?v=2xXLycFv5Gc>
  - transcript: `transcripts/kara-swisher-radicalization-elon-musk.txt`
  - slug: `kara-swisher-radicalization-elon-musk`

- **The Peterman Pod** — OpenAI & Meta Distinguished Engineer (IC9): Working With Zuck, Carmack & Career Growth | Philip Su
  - 2025 · 80 分钟 · 384,337 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=v2JxdjTi_1I>
  - transcript: `transcripts/openai-meta-distinguished-engineer-working-zuck.txt`
  - slug: `openai-meta-distinguished-engineer-working-zuck`

- **Huberman Lab** — A Process for Finding & Achieving Your Unique Purpose | Robert Greene
  - 2023 · 191 分钟 · 15,727,530 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=50BZQRT1dAg>
  - transcript: `transcripts/process-finding-achieving-unique-purpose-robert.txt`
  - slug: `process-finding-achieving-unique-purpose-robert`

- **The Peterman Pod** — Boris Cherny (Creator of Claude Code) On What Grew His Career And Building at Anthropic
  - 2025 · 84 分钟 · 273,156 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=AmdLVWMdjOk>
  - transcript: `transcripts/boris-cherny-grew-his-career-building.txt`
  - slug: `boris-cherny-grew-his-career-building`

- **Mindscape (Sean Carroll)** — The Biggest Ideas in the Universe | 7. Quantum Mechanics
  - 2020 · 65 分钟 · 463,889 播放 · 物理 / 宇宙学
  - source: <https://www.youtube.com/watch?v=BJlkkOIFjx4>
  - transcript: `transcripts/biggest-ideas-universe-quantum-mechanics.txt`
  - slug: `biggest-ideas-universe-quantum-mechanics`

- **Acquired** — Starbucks (with Howard Schultz)
  - 2024 · 195 分钟 · 612,024 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=A0fvX-wV70Y>
  - transcript: `transcripts/starbucks.txt`
  - slug: `starbucks`

- **Lex Fridman Podcast** — Tucker Carlson: Putin, Navalny, Trump, CIA, NSA, War, Politics & Freedom | Lex Fridman Podcast #414
  - 2024 · 184 分钟 · 16,977,955 播放 · 政治 / 社会
  - source: <https://www.youtube.com/watch?v=f_lRdkH_QoY>
  - transcript: `transcripts/tucker-carlson-putin-navalny-trump-cia.txt`
  - slug: `tucker-carlson-putin-navalny-trump-cia`

- **Making Sense (Sam Harris)** — Psychedelics Don't Distort Reality — They Reveal How Your Brain Constructs It
  - 2026 · 60 分钟 · 1,789,550 播放 · 神经科学 / 心理
  - source: <https://www.youtube.com/watch?v=r5KRnstXYUg>
  - transcript: `transcripts/psychedelics-don-t-distort-reality-they.txt`
  - slug: `psychedelics-don-t-distort-reality-they`

- **The Peterman Pod** — Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup
  - 2026 · 119 分钟 · 252,276 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=U46fJ2bJ-co>
  - transcript: `transcripts/creator-c-bell-labs-negative-overhead.txt`
  - slug: `creator-c-bell-labs-negative-overhead`

- **Dwarkesh Podcast** — David Reich — How one small tribe conquered the world 70,000 years ago
  - 2024 · 117 分钟 · 2,055,900 播放 · 演化 / 生物
  - source: <https://www.youtube.com/watch?v=Uj6skZIxPuI>
  - transcript: `transcripts/david-reich-one-small-tribe-conquered.txt`
  - slug: `david-reich-one-small-tribe-conquered`

- **The Peterman Pod** — Retired Netflix Eng Director: Leetcode, Regrets, Hiring Stories
  - 2026 · 79 分钟 · 235,836 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=ApG9vjbHDCk>
  - transcript: `transcripts/retired-netflix-eng-director-leetcode-regrets.txt`
  - slug: `retired-netflix-eng-director-leetcode-regrets`

- **Huberman Lab** — Dr. Paul Conti: How to Understand & Assess Your Mental Health | Huberman Lab Guest Series
  - 2023 · 222 分钟 · 15,011,220 播放 · 神经科学 / 心理
  - source: <https://www.youtube.com/watch?v=tLRCS48Ens4>
  - transcript: `transcripts/paul-conti-understand-assess-mental-health.txt`
  - slug: `paul-conti-understand-assess-mental-health`

- **The Peterman Pod** — Turing Award Winner: Thinking Clearly, Paxos vs Raft, Working With Dijkstra | Leslie Lamport
  - 2026 · 70 分钟 · 201,642 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=U719vQz-WFs>
  - transcript: `transcripts/turing-award-winner-thinking-clearly-paxos.txt`
  - slug: `turing-award-winner-thinking-clearly-paxos`

- **Mindscape (Sean Carroll)** — Episode 28: Roger Penrose on Spacetime, Consciousness, and the Universe
  - 2019 · 95 分钟 · 375,976 播放 · 物理 / 宇宙学
  - source: <https://www.youtube.com/watch?v=DJADe-_dRB0>
  - transcript: `transcripts/roger-penrose-spacetime-consciousness-universe.txt`
  - slug: `roger-penrose-spacetime-consciousness-universe`

- **Acquired** — NVIDIA CEO Jensen Huang
  - 2023 · 90 分钟 · 509,646 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=y6NfxiemvHg>
  - transcript: `transcripts/nvidia-ceo-jensen-huang.txt`
  - slug: `nvidia-ceo-jensen-huang`

- **Conversations with Tyler** — Sam Altman on Trust, Persuasion, and the Future of Intelligence - Live at the Progress Conference
  - 2025 · 54 分钟 · 45,625 播放 · 人工智能
  - source: <https://www.youtube.com/watch?v=cuSDy0Rmdks>
  - transcript: `transcripts/sam-altman-trust-persuasion-future-intelligence.txt`
  - slug: `sam-altman-trust-persuasion-future-intelligence`

- **The Peterman Pod** — Creator of TypeScript: 10x Faster Typescript, Why AI Won't Replace SWEs | Anders Hejlsberg
  - 2026 · 65 分钟 · 178,077 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=cywK3XYYJ2o>
  - transcript: `transcripts/creator-typescript-10x-faster-typescript-ai.txt`
  - slug: `creator-typescript-10x-faster-typescript-ai`

- **Lex Fridman Podcast** — Jordan Peterson: Life, Death, Power, Fame, and Meaning | Lex Fridman Podcast #313
  - 2022 · 183 分钟 · 16,799,240 播放 · 哲学 / 宗教
  - source: <https://www.youtube.com/watch?v=sY8aFSY2zv4>
  - transcript: `transcripts/jordan-peterson-life-death-power-fame.txt`
  - slug: `jordan-peterson-life-death-power-fame`

- **The Ezra Klein Show** — Tim Walz Is Kamala Harris’ V.P. Pick. Watch Our Interview With Him.
  - 2024 · 59 分钟 · 1,322,495 播放 · 政治 / 社会
  - source: <https://www.youtube.com/watch?v=3fuS9PmV9hg>
  - transcript: `transcripts/tim-walz-kamala-harris-v-p.txt`
  - slug: `tim-walz-kamala-harris-v-p`

- **Huberman Lab** — Controlling Your Dopamine For Motivation, Focus & Satisfaction
  - 2021 · 136 分钟 · 12,458,499 播放 · 神经科学 / 心理
  - source: <https://www.youtube.com/watch?v=QmOF0crdyRU>
  - transcript: `transcripts/controlling-dopamine-motivation-focus-satisfaction.txt`
  - slug: `controlling-dopamine-motivation-focus-satisfaction`

- **The Peterman Pod** — Instagram Principal Engineer (IC8): Promotions, Breaking Prod, Tech Leading | Jake Bolam
  - 2025 · 50 分钟 · 148,719 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=QUhC5BDZt-E>
  - transcript: `transcripts/instagram-principal-engineer-promotions-breaking-prod.txt`
  - slug: `instagram-principal-engineer-promotions-breaking-prod`

- **Dwarkesh Podcast** — Ilya Sutskever – We're moving from the age of scaling to the age of research
  - 2025 · 96 分钟 · 1,534,551 播放 · 人工智能
  - source: <https://www.youtube.com/watch?v=aR20FWCCjAs>
  - transcript: `transcripts/ilya-sutskever-re-moving-from-age.txt`
  - slug: `ilya-sutskever-re-moving-from-age`

- **The Peterman Pod** — Meta Senior Manager (M2): Manager Career Growth, PIPs, Amazon vs Meta | Stefan Mai
  - 2025 · 91 分钟 · 143,795 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=wUrvXN-yiyo>
  - transcript: `transcripts/meta-senior-manager-manager-career-growth.txt`
  - slug: `meta-senior-manager-manager-career-growth`

- **Mindscape (Sean Carroll)** — Episode 9: Solo -- Why Is There Something Rather than Nothing?
  - 2018 · 81 分钟 · 186,355 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=FLfvvMjuk6U>
  - transcript: `transcripts/there-something-rather-than-nothing.txt`
  - slug: `there-something-rather-than-nothing`

- **Acquired** — TSMC founder Morris Chang
  - 2025 · 174 分钟 · 251,334 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=FZItbr4ZJnc>
  - transcript: `transcripts/tsmc-founder-morris-chang.txt`
  - slug: `tsmc-founder-morris-chang`

- **The Peterman Pod** — AWS Distinguished Eng: Learning From 3000 Incidents And How Engineering Is Changing | Marc Brooker
  - 2026 · 71 分钟 · 141,221 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=u3GjIXP9N0s>
  - transcript: `transcripts/aws-distinguished-eng-learning-from-incidents.txt`
  - slug: `aws-distinguished-eng-learning-from-incidents`

- **Huberman Lab** — Dr. Andy Galpin: How to Build Strength, Muscle Size & Endurance
  - 2022 · 211 分钟 · 10,412,678 播放 · 健康 / 体能
  - source: <https://www.youtube.com/watch?v=IAnhFUUCq6c>
  - transcript: `transcripts/andy-galpin-build-strength-muscle-size.txt`
  - slug: `andy-galpin-build-strength-muscle-size`

- **Lex Fridman Podcast** — Elon Musk: War, AI, Aliens, Politics, Physics, Video Games, and Humanity | Lex Fridman Podcast #400
  - 2023 · 136 分钟 · 14,289,006 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=JN3KPFbWCy8>
  - transcript: `transcripts/elon-musk-war-ai-aliens-politics.txt`
  - slug: `elon-musk-war-ai-aliens-politics`

- **Conversations with Tyler** — Daron Acemoglu on Liberalism, Automation, and the Educated Elite
  - 2026 · 62 分钟 · 28,790 播放 · 政治 / 社会
  - source: <https://www.youtube.com/watch?v=e5O1Y-5phEU>
  - transcript: `transcripts/daron-acemoglu-liberalism-automation-educated-elite.txt`
  - slug: `daron-acemoglu-liberalism-automation-educated-elite`

- **The Peterman Pod** — Google DeepMind Distinguished Eng (L9): How To Land a Job at a Frontier Lab | Vlad Feinberg
  - 2026 · 64 分钟 · 122,103 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=cDyi91onoJ8>
  - transcript: `transcripts/google-deepmind-distinguished-eng-land-job.txt`
  - slug: `google-deepmind-distinguished-eng-land-job`

- **Dwarkesh Podcast** — Andrej Karpathy — “We’re summoning ghosts, not building animals”
  - 2025 · 146 分钟 · 1,406,203 播放 · 人工智能
  - source: <https://www.youtube.com/watch?v=lXUZvyajciY>
  - transcript: `transcripts/andrej-karpathy-re-summoning-ghosts-not.txt`
  - slug: `andrej-karpathy-re-summoning-ghosts-not`

- **Mindscape (Sean Carroll)** — Episode 45: Leonard Susskind on Quantum Information, Quantum Gravity, and Holography
  - 2019 · 73 分钟 · 176,468 播放 · 物理 / 宇宙学
  - source: <https://www.youtube.com/watch?v=XTSdPSOcdjI>
  - transcript: `transcripts/leonard-susskind-quantum-information-quantum-gravity.txt`
  - slug: `leonard-susskind-quantum-information-quantum-gravity`

- **Acquired** — The Jamie Dimon Interview: How JP Morgan Became an $800 Billion Bank
  - 2025 · 66 分钟 · 247,422 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=AR_1IPhzAtU>
  - transcript: `transcripts/jamie-dimon-interview-jp-morgan-became.txt`
  - slug: `jamie-dimon-interview-jp-morgan-became`

- **The Peterman Pod** — Shopify Distinguished Eng (L10): Principal+ Engineering, Career Story, Regrets | Ilya Grigorik
  - 2025 · 50 分钟 · 102,764 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=rY44ViY45q8>
  - transcript: `transcripts/shopify-distinguished-eng-principal-engineering-career.txt`
  - slug: `shopify-distinguished-eng-principal-engineering-career`

- **Huberman Lab** — The Science of Eating for Health, Fat Loss & Lean Muscle | Dr. Layne Norton
  - 2022 · 229 分钟 · 8,874,360 播放 · 健康 / 体能
  - source: <https://www.youtube.com/watch?v=K4Ze-Sp6aUE>
  - transcript: `transcripts/science-eating-health-fat-loss-lean.txt`
  - slug: `science-eating-health-fat-loss-lean`

- **The Ezra Klein Show** — Pete Buttigieg on 2024 and the ‘Crank Realignment’
  - 2024 · 57 分钟 · 1,211,787 播放 · 政治 / 社会
  - source: <https://www.youtube.com/watch?v=8JDMKyTpXWc>
  - transcript: `transcripts/pete-buttigieg-crank-realignment.txt`
  - slug: `pete-buttigieg-crank-realignment`

- **The Peterman Pod** — Co-Creator of Haskell: Useless vs Useful Languages, Rust vs C, Functional Programming | Simon Jones
  - 2026 · 87 分钟 · 97,476 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=xcB_LF3cdqw>
  - transcript: `transcripts/co-creator-haskell-useless-vs-useful-languages.txt`
  - slug: `co-creator-haskell-useless-vs-useful-languages`

- **Lex Fridman Podcast** — Paul Rosolie: Amazon Jungle, Uncontacted Tribes, Anacondas, and Ayahuasca | Lex Fridman Podcast #369
  - 2023 · 214 分钟 · 13,020,290 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=gPfriiHBBek>
  - transcript: `transcripts/paul-rosolie-amazon-jungle-uncontacted-tribes.txt`
  - slug: `paul-rosolie-amazon-jungle-uncontacted-tribes`

- **Making Sense (Sam Harris)** — Waking Up with Sam Harris - Looking for the Self (26 Minute Meditation)
  - 2015 · 26 分钟 · 1,098,518 播放 · 意识 / 心智
  - source: <https://www.youtube.com/watch?v=CN-_zzHpcdM>
  - transcript: `transcripts/waking-up-sam-harris-looking.txt`
  - slug: `waking-up-sam-harris-looking`

- **The Peterman Pod** — Ex-Stripe CTO: Hiring Without Leetcode, Career Growth, Coding as a Leader (Career Story)
  - 2025 · 126 分钟 · 94,488 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=hl6Ryc_NUm8>
  - transcript: `transcripts/ex-stripe-cto-hiring-without-leetcode-career.txt`
  - slug: `ex-stripe-cto-hiring-without-leetcode-career`

- **Mindscape (Sean Carroll)** — Mindscape 134 | Robert Sapolsky on Why We Behave the Way We Do
  - 2021 · 88 分钟 · 172,157 播放 · 神经科学 / 心理
  - source: <https://www.youtube.com/watch?v=pcPZ0Z0bO1o>
  - transcript: `transcripts/robert-sapolsky-behave-way-do.txt`
  - slug: `robert-sapolsky-behave-way-do`

- **Acquired** — The Mark Zuckerberg Interview
  - 2024 · 87 分钟 · 218,441 播放 · 人工智能
  - source: <https://www.youtube.com/watch?v=QciJ9ubeLQk>
  - transcript: `transcripts/mark-zuckerberg-interview.txt`
  - slug: `mark-zuckerberg-interview`

- **Huberman Lab** — What Alcohol Does to Your Body, Brain & Health
  - 2022 · 121 分钟 · 7,993,023 播放 · 神经科学 / 心理
  - source: <https://www.youtube.com/watch?v=DkS1pkKpILY>
  - transcript: `transcripts/alcohol-does-body-brain-health.txt`
  - slug: `alcohol-does-body-brain-health`

- **The Peterman Pod** — Meta Distinguished Eng (IC9): Influencing Engs, Failures, and Learnings | Adam Ernst
  - 2026 · 40 分钟 · 92,028 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=YA_OYJF3Mmw>
  - transcript: `transcripts/meta-distinguished-eng-influencing-engs-failures.txt`
  - slug: `meta-distinguished-eng-influencing-engs-failures`

- **Dwarkesh Podcast** — Ajeya Cotra – "This might be the clearest warning shot we ever get"
  - 2026 · 140 分钟 · 1,310,347 播放 · 人工智能
  - source: <https://www.youtube.com/watch?v=X50zezLFWWI>
  - transcript: `transcripts/ajeya-cotra-might-be-clearest-warning.txt`
  - slug: `ajeya-cotra-might-be-clearest-warning`

- **The Peterman Pod** — Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov
  - 2026 · 34 分钟 · 91,974 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=T9CGjbPZeaM>
  - transcript: `transcripts/turing-award-winner-data-abstraction-dijkstra.txt`
  - slug: `turing-award-winner-data-abstraction-dijkstra`

- **Conversations with Tyler** — Paul Gillingham on Why Mexico Stays Together
  - 2026 · 69 分钟 · 23,185 播放 · 经济 / 跨学科
  - source: <https://www.youtube.com/watch?v=AaeXt_ocDKY>
  - transcript: `transcripts/paul-gillingham-mexico-stays-together.txt`
  - slug: `paul-gillingham-mexico-stays-together`

- **The Peterman Pod** — Creator of Scala: Comparing Languages And How AI Will Impact Them | Martin Odersky
  - 2026 · 57 分钟 · 87,980 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=LdN4sPWM-WY>
  - transcript: `transcripts/creator-scala-comparing-languages-ai-will.txt`
  - slug: `creator-scala-comparing-languages-ai-will`

- **Lex Fridman Podcast** — David Kipping: Alien Civilizations and Habitable Worlds | Lex Fridman Podcast #355
  - 2023 · 227 分钟 · 12,476,809 播放 · 宇宙 / 地外
  - source: <https://www.youtube.com/watch?v=uZN5xjoS6TU>
  - transcript: `transcripts/david-kipping-alien-civilizations-habitable-worlds.txt`
  - slug: `david-kipping-alien-civilizations-habitable-worlds`

- **Mindscape (Sean Carroll)** — Mindscape 245 | Solo: The Crisis in Physics
  - 2023 · 262 分钟 · 169,642 播放 · 物理 / 宇宙学
  - source: <https://www.youtube.com/watch?v=MTM-8memDHs>
  - transcript: `transcripts/crisis-physics.txt`
  - slug: `crisis-physics`

- **Acquired** — Lockheed Martin (Audio)
  - 2023 · 218 分钟 · 215,681 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=atMrnp_EVcI>
  - transcript: `transcripts/lockheed-martin.txt`
  - slug: `lockheed-martin`

- **Huberman Lab** — Effects of Fasting & Time Restricted Eating on Fat Loss & Health | Huberman Lab Podcast #41
  - 2021 · 146 分钟 · 7,497,290 播放 · 健康 / 体能
  - source: <https://www.youtube.com/watch?v=9tRohh0gErM>
  - transcript: `transcripts/effects-fasting-time-restricted-eating-fat.txt`
  - slug: `effects-fasting-time-restricted-eating-fat`

- **The Peterman Pod** — Intern to Microsoft Distinguished Engineer in 11 Promotions (Career Story)
  - 2025 · 92 分钟 · 77,461 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=d8tRM8RJ52M>
  - transcript: `transcripts/intern-microsoft-distinguished-engineer-promotions.txt`
  - slug: `intern-microsoft-distinguished-engineer-promotions`

- **The Peterman Pod** — Distinguished Eng: Stack Ranking, Competing with Bezos, Regrets | Bryan Cantrill
  - 2026 · 81 分钟 · 77,259 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=qhSL-5GtmQM>
  - transcript: `transcripts/distinguished-eng-stack-ranking-competing-bezos.txt`
  - slug: `distinguished-eng-stack-ranking-competing-bezos`

- **Dwarkesh Podcast** — Dario Amodei — “We are near the end of the exponential”
  - 2026 · 142 分钟 · 1,230,846 播放 · 人工智能
  - source: <https://www.youtube.com/watch?v=n1E9IZfvGMA>
  - transcript: `transcripts/dario-amodei-near-end-exponential.txt`
  - slug: `dario-amodei-near-end-exponential`

- **The Ezra Klein Show** — The Dark Heart of Trump's Foreign Policy | The Ezra Klein Show
  - 2025 · 80 分钟 · 1,176,688 播放 · 政治 / 社会
  - source: <https://www.youtube.com/watch?v=305ZAppMlN8>
  - transcript: `transcripts/dark-heart-trump-s-foreign-policy.txt`
  - slug: `dark-heart-trump-s-foreign-policy`

- **The Peterman Pod** — OpenAI & Meta Distinguished Eng (IC9): The Psychology Behind Tech Career Peaks | Philip Su
  - 2026 · 44 分钟 · 76,927 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=RMo04pSSiao>
  - transcript: `transcripts/openai-meta-distinguished-eng-psychology-behind.txt`
  - slug: `openai-meta-distinguished-eng-psychology-behind`

- **Huberman Lab** — ADHD & How Anyone Can Improve Their Focus
  - 2021 · 138 分钟 · 7,329,554 播放 · 神经科学 / 心理
  - source: <https://www.youtube.com/watch?v=hFL6qRIJZ_Y>
  - transcript: `transcripts/adhd-anyone-can-improve-their-focus.txt`
  - slug: `adhd-anyone-can-improve-their-focus`

- **Mindscape (Sean Carroll)** — Mindscape 149 | Lee Smolin on Time, Philosophy, and the Nature of Reality
  - 2021 · 89 分钟 · 133,680 播放 · 哲学 / 宗教
  - source: <https://www.youtube.com/watch?v=3-GRc-ld8-M>
  - transcript: `transcripts/lee-smolin-time-philosophy-nature-reality.txt`
  - slug: `lee-smolin-time-philosophy-nature-reality`

- **Acquired** — Charlie Munger (Audio)
  - 2023 · 66 分钟 · 194,199 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=w6qRb171cog>
  - transcript: `transcripts/charlie-munger.txt`
  - slug: `charlie-munger`

- **Lex Fridman Podcast** — Ben Shapiro vs Destiny Debate: Politics, Jan 6, Israel, Ukraine & Wokeism | Lex Fridman Podcast #410
  - 2024 · 140 分钟 · 12,450,317 播放 · 政治 / 社会
  - source: <https://www.youtube.com/watch?v=tYrdMjVXyNg>
  - transcript: `transcripts/ben-shapiro-vs-destiny-debate-politics.txt`
  - slug: `ben-shapiro-vs-destiny-debate-politics`

- **The Peterman Pod** — Creator of Lua: What People Get Wrong About Scripting Languages | Roberto Ierusalimschy
  - 2026 · 65 分钟 · 62,400 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=jCZnFKk6M9A>
  - transcript: `transcripts/creator-lua-people-get-wrong-about.txt`
  - slug: `creator-lua-people-get-wrong-about`

- **Conversations with Tyler** — Dan Wang on What China and America Can Learn from Each Other
  - 2025 · 97 分钟 · 15,601 播放 · 经济 / 跨学科
  - source: <https://www.youtube.com/watch?v=qCGG3s4Luyw>
  - transcript: `transcripts/dan-wang-china-america-can-learn.txt`
  - slug: `dan-wang-china-america-can-learn`

- **The Peterman Pod** — Sergey Levine: Humanoid Robotics Results, Chinese Labs & Future Timelines
  - 2026 · 57 分钟 · 61,416 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=9OSbaPjv0Rc>
  - transcript: `transcripts/sergey-levine-humanoid-robotics-results-chinese.txt`
  - slug: `sergey-levine-humanoid-robotics-results-chinese`

- **Dwarkesh Podcast** — Jensen Huang – Will Nvidia’s moat persist?
  - 2026 · 103 分钟 · 967,792 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=Hrbq66XqtCo>
  - transcript: `transcripts/jensen-huang-will-nvidia-s-moat.txt`
  - slug: `jensen-huang-will-nvidia-s-moat`

- **The Peterman Pod** — Meta Senior Staff Eng (IC7): Zuck Stories, Rapid Career Growth, Code Machine Archetype
  - 2025 · 86 分钟 · 56,994 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=OzlK68kcuHc>
  - transcript: `transcripts/meta-senior-staff-eng-zuck-stories.txt`
  - slug: `meta-senior-staff-eng-zuck-stories`

- **Huberman Lab** — How Meditation Works & Science-Based Effective Meditations
  - 2022 · 146 分钟 · 7,191,349 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=wTBSGgbIvsY>
  - transcript: `transcripts/meditation-works-science-based-effective-meditations.txt`
  - slug: `meditation-works-science-based-effective-meditations`

- **Mindscape (Sean Carroll)** — Mindscape 131 | Avi Loeb on Taking Aliens Seriously
  - 2021 · 100 分钟 · 122,043 播放 · 宇宙 / 地外
  - source: <https://www.youtube.com/watch?v=_DQYiyQ7Tkk>
  - transcript: `transcripts/avi-loeb-taking-aliens-seriously.txt`
  - slug: `avi-loeb-taking-aliens-seriously`

- **Acquired** — Renaissance Technologies (Audio)
  - 2024 · 190 分钟 · 184,272 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=2KjW4BqNFy0>
  - transcript: `transcripts/renaissance-technologies.txt`
  - slug: `renaissance-technologies`

- **The Peterman Pod** — The Co-Creator of Kubernetes: Engineering-Led Direction and Convincing Management | Brendan Burns
  - 2026 · 67 分钟 · 55,721 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=FKijpCEH9D8>
  - transcript: `transcripts/co-creator-kubernetes-engineering-led-direction-convincing-management.txt`
  - slug: `co-creator-kubernetes-engineering-led-direction-convincing-management`

- **Lex Fridman Podcast** — Michael Saylor: Bitcoin, Inflation, and the Future of Money | Lex Fridman Podcast #276
  - 2022 · 236 分钟 · 11,427,643 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=mC43pZkpTec>
  - transcript: `transcripts/michael-saylor-bitcoin-inflation-future-money.txt`
  - slug: `michael-saylor-bitcoin-inflation-future-money`

- **Making Sense (Sam Harris)** — Final Thoughts on Free Will (Episode #241)
  - 2021 · 44 分钟 · 372,634 播放 · 意识 / 心智
  - source: <https://www.youtube.com/watch?v=u45SP7Xv_oU>
  - transcript: `transcripts/final-thoughts-free-will.txt`
  - slug: `final-thoughts-free-will`

- **The Peterman Pod** — Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson
  - 2026 · 135 分钟 · 47,693 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=5GUcvSAJcJw>
  - transcript: `transcripts/turing-award-winner-p-vs-np.txt`
  - slug: `turing-award-winner-p-vs-np`

- **The Ezra Klein Show** — Is Trump ‘Detoxing’ the Economy or Poisoning It? | The Ezra Klein Show
  - 2025 · 60 分钟 · 1,144,601 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=3PXVrLH4zSU>
  - transcript: `transcripts/trump-detoxing-economy-poisoning.txt`
  - slug: `trump-detoxing-economy-poisoning`

- **Huberman Lab** — Science of Muscle Growth, Increasing Strength & Muscular Recovery
  - 2021 · 124 分钟 · 6,693,987 播放 · 健康 / 体能
  - source: <https://www.youtube.com/watch?v=XLr2RKoD-oY>
  - transcript: `transcripts/science-muscle-growth-increasing-strength-muscular.txt`
  - slug: `science-muscle-growth-increasing-strength-muscular`

- **The Peterman Pod** — Dropbox’s Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling
  - 2026 · 121 分钟 · 43,089 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=3XkmNSuHFmY>
  - transcript: `transcripts/dropbox-s-former-most-senior-eng.txt`
  - slug: `dropbox-s-former-most-senior-eng`

- **Mindscape (Sean Carroll)** — Mindscape 155 | Stephen Wolfram on Computation, Hypergraphs, and Fundamental Physics
  - 2021 · 160 分钟 · 108,612 播放 · 物理 / 宇宙学
  - source: <https://www.youtube.com/watch?v=0bMYtEKjHs0>
  - transcript: `transcripts/stephen-wolfram-computation-hypergraphs-fundamental-physics.txt`
  - slug: `stephen-wolfram-computation-hypergraphs-fundamental-physics`

- **Acquired** — Costco (Audio)
  - 2023 · 181 分钟 · 181,029 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=9PxxtJVWRrg>
  - transcript: `transcripts/costco.txt`
  - slug: `costco`

- **Dwarkesh Podcast** — Mark Zuckerberg — Llama 3, $10B models, Caesar Augustus, & 1 GW datacenters
  - 2024 · 78 分钟 · 866,123 播放 · 人工智能
  - source: <https://www.youtube.com/watch?v=bc6uFV9CJGg>
  - transcript: `transcripts/mark-zuckerberg-llama-10b-models-caesar.txt`
  - slug: `mark-zuckerberg-llama-10b-models-caesar`

- **The Peterman Pod** — How Anthropic Builds And How Engineering Will Change Soon | Thariq Shihipar
  - 2026 · 70 分钟 · 42,877 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=2Kch3tWMnw8>
  - transcript: `transcripts/anthropic-builds-engineering-will-change-soon.txt`
  - slug: `anthropic-builds-engineering-will-change-soon`

- **Conversations with Tyler** — Katja Hoyer on Weimar, the GDR, and the German Character
  - 2026 · 67 分钟 · 15,391 播放 · 经济 / 跨学科
  - source: <https://www.youtube.com/watch?v=pziNQu9Ltxs>
  - transcript: `transcripts/katja-hoyer-weimar-gdr-german-character.txt`
  - slug: `katja-hoyer-weimar-gdr-german-character`

- **Lex Fridman Podcast** — Elon Musk: SpaceX, Mars, Tesla Autopilot, Self-Driving, Robotics, and AI | Lex Fridman Podcast #252
  - 2021 · 151 分钟 · 11,173,774 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=DxREm3s1scA>
  - transcript: `transcripts/elon-musk-spacex-mars-tesla-autopilot.txt`
  - slug: `elon-musk-spacex-mars-tesla-autopilot`

- **The Peterman Pod** — Turing Award Winner: TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC | David Patterson
  - 2026 · 59 分钟 · 41,475 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=Pn4ZwlEh5nw>
  - transcript: `transcripts/turing-award-winner-tpu-vs-gpu.txt`
  - slug: `turing-award-winner-tpu-vs-gpu`

- **Huberman Lab** — Dr. Andy Galpin: How to Build Physical Endurance & Lose Fat | Huberman Lab Guest Series
  - 2023 · 228 分钟 · 5,665,144 播放 · 健康 / 体能
  - source: <https://www.youtube.com/watch?v=oNkDA2F7CjM>
  - transcript: `transcripts/andy-galpin-build-physical-endurance-lose.txt`
  - slug: `andy-galpin-build-physical-endurance-lose`

- **The Peterman Pod** — Meta Superintelligence Labs (MSL) Eng Director: Promo Hacking, Industry Shifts, Regrets | John White
  - 2026 · 43 分钟 · 40,220 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=aPfnP4iAIH8>
  - transcript: `transcripts/meta-superintelligence-labs-eng-director-promo.txt`
  - slug: `meta-superintelligence-labs-eng-director-promo`

- **Mindscape (Sean Carroll)** — Episode 25: David Chalmers on Consciousness, the Hard Problem, and Living in a Simulation
  - 2018 · 82 分钟 · 107,503 播放 · 意识 / 心智
  - source: <https://www.youtube.com/watch?v=Myl_gnRxh94>
  - transcript: `transcripts/david-chalmers-consciousness-hard-problem-living.txt`
  - slug: `david-chalmers-consciousness-hard-problem-living`

- **The Peterman Pod** — Uber Distinguished Eng: Unfair Promos, Influence, Engineering Regrets | Joakim Recht
  - 2025 · 86 分钟 · 39,281 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=feNh_ubBAMI>
  - transcript: `transcripts/uber-distinguished-eng-unfair-promos-influence.txt`
  - slug: `uber-distinguished-eng-unfair-promos-influence`

- **Dwarkesh Podcast** — Why Leonardo was a saboteur, Gutenberg went broke, and Florence was weird – Ada Palmer
  - 2026 · 122 分钟 · 824,677 播放 · 神经科学 / 心理
  - source: <https://www.youtube.com/watch?v=PAIhVfGbREA>
  - transcript: `transcripts/leonardo-was-saboteur-gutenberg-went-broke.txt`
  - slug: `leonardo-was-saboteur-gutenberg-went-broke`

- **The Peterman Pod** — Creator of Lean: Handwritten Math Will Change Dramatically | Leonardo de Moura
  - 2026 · 68 分钟 · 36,880 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=KzdYKeAqWhY>
  - transcript: `transcripts/creator-lean-handwritten-math-will-change.txt`
  - slug: `creator-lean-handwritten-math-will-change`

- **Huberman Lab** — The Science of Making & Breaking Habits
  - 2022 · 110 分钟 · 5,587,806 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=Wcs2PFz5q6g>
  - transcript: `transcripts/science-making-breaking-habits.txt`
  - slug: `science-making-breaking-habits`

- **The Ezra Klein Show** — Yuval Noah Harari on Donald Trump’s Core Delusion | The Ezra Klein Show
  - 2026 · 115 分钟 · 1,086,798 播放 · 政治 / 社会
  - source: <https://www.youtube.com/watch?v=9NCxS__rtAo>
  - transcript: `transcripts/yuval-noah-harari-donald-trump-s.txt`
  - slug: `yuval-noah-harari-donald-trump-s`

- **Lex Fridman Podcast** — Joe Rogan: Comedy, Controversy, Aliens, UFOs, Putin, CIA, and Freedom | Lex Fridman Podcast #300
  - 2022 · 101 分钟 · 10,831,085 播放 · 宇宙 / 地外
  - source: <https://www.youtube.com/watch?v=gk4tEO4jDUM>
  - transcript: `transcripts/joe-rogan-comedy-controversy-aliens-ufos.txt`
  - slug: `joe-rogan-comedy-controversy-aliens-ufos`

- **The Peterman Pod** — Creator of OCaml: Functional Programming, Formal Verification, Programming Languages | Xavier Leroy
  - 2026 · 84 分钟 · 35,613 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=9Cswiqrq6So>
  - transcript: `transcripts/creator-ocaml-functional-programming-formal-verification.txt`
  - slug: `creator-ocaml-functional-programming-formal-verification`

- **Conversations with Tyler** — Bob Spitz: Why the Rolling Stones Outlasted Everyone
  - 2026 · 62 分钟 · 13,961 播放 · 经济 / 跨学科
  - source: <https://www.youtube.com/watch?v=YzcuM5Q7a50>
  - transcript: `transcripts/bob-spitz-rolling-stones-outlasted-everyone.txt`
  - slug: `bob-spitz-rolling-stones-outlasted-everyone`

- **Mindscape (Sean Carroll)** — Mindscape 78 | Daniel Dennett on Minds, Patterns, and the Scientific Image
  - 2020 · 121 分钟 · 102,446 播放 · 意识 / 心智
  - source: <https://www.youtube.com/watch?v=8yZw4wxvnVQ>
  - transcript: `transcripts/daniel-dennett-minds-patterns-scientific-image.txt`
  - slug: `daniel-dennett-minds-patterns-scientific-image`

- **Acquired** — Google Part I: Origins of Search. How the Best Business in Human History Happened (Audio)
  - 2025 · 219 分钟 · 109,662 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=v1nkN0sM2wc>
  - transcript: `transcripts/google-part-i-origins-search-best.txt`
  - slug: `google-part-i-origins-search-best`

- **The Peterman Pod** — OpenAI Codex Tech Lead: How His Career Grew And How He Uses Codex | Michael Bolin
  - 2026 · 80 分钟 · 32,181 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=hN5ZFzWFhhg>
  - transcript: `transcripts/openai-codex-tech-lead-his-career.txt`
  - slug: `openai-codex-tech-lead-his-career`

- **Huberman Lab** — How to Lose Fat with Science-Based Tools
  - 2021 · 113 分钟 · 5,585,801 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=GqPGXG5TlZw>
  - transcript: `transcripts/lose-fat-science-based-tools.txt`
  - slug: `lose-fat-science-based-tools`

- **The Peterman Pod** — New Grad to Principal Engineer (IC8) at Meta (Career Story) | Adrien Friggeri
  - 2026 · 56 分钟 · 28,180 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=2Sjzd9pt6Ts>
  - transcript: `transcripts/new-grad-principal-engineer-at-meta.txt`
  - slug: `new-grad-principal-engineer-at-meta`

- **Dwarkesh Podcast** — Richard Sutton – Father of RL thinks LLMs are a dead end
  - 2025 · 67 分钟 · 790,432 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=21EYKqUsPfg>
  - transcript: `transcripts/richard-sutton-father-rl-thinks-llms.txt`
  - slug: `richard-sutton-father-rl-thinks-llms`

- **The Peterman Pod** — Mozilla Firefox CTO: Chrome vs Firefox and Distinguished Eng Promos
  - 2025 · 95 分钟 · 27,582 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=KhJgI9u47kI>
  - transcript: `transcripts/mozilla-firefox-cto-chrome-vs-firefox.txt`
  - slug: `mozilla-firefox-cto-chrome-vs-firefox`

- **Lex Fridman Podcast** — Donald Hoffman: Reality is an Illusion - How Evolution Hid the Truth | Lex Fridman Podcast #293
  - 2022 · 196 分钟 · 10,409,362 播放 · 演化 / 生物
  - source: <https://www.youtube.com/watch?v=reYdQYZ9Rj4>
  - transcript: `transcripts/donald-hoffman-reality-illusion-evolution.txt`
  - slug: `donald-hoffman-reality-illusion-evolution`

- **Making Sense (Sam Harris)** — Is AI Already Conscious? (FULL EPISODE)
  - 2026 · 91 分钟 · 222,886 播放 · 意识 / 心智
  - source: <https://www.youtube.com/watch?v=DRbZyuY8EN8>
  - transcript: `transcripts/ai-already-conscious.txt`
  - slug: `ai-already-conscious`

- **Mindscape (Sean Carroll)** — Mindscape 158 | David Wallace on The Arrow of Time
  - 2021 · 108 分钟 · 96,049 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=ZusCQdM6ovw>
  - transcript: `transcripts/david-wallace-arrow-time.txt`
  - slug: `david-wallace-arrow-time`

- **Acquired** — Google Part II: Alphabet (Audio)
  - 2025 · 251 分钟 · 78,248 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=QhAftC_zFr8>
  - transcript: `transcripts/google-part-ii-alphabet.txt`
  - slug: `google-part-ii-alphabet`

- **The Peterman Pod** — Frontline Manager at Meta to Senior Director at Snapchat in 3 Years (Career Story)
  - 2025 · 42 分钟 · 23,366 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=BHlko_Mg-Jk>
  - transcript: `transcripts/frontline-manager-at-meta-senior-director.txt`
  - slug: `frontline-manager-at-meta-senior-director`

- **Huberman Lab** — Diet & Nutrition for Mental Health | Dr. Chris Palmer
  - 2022 · 183 分钟 · 5,335,703 播放 · 神经科学 / 心理
  - source: <https://www.youtube.com/watch?v=xjEFo3a1AnI>
  - transcript: `transcripts/diet-nutrition-mental-health-chris-palmer.txt`
  - slug: `diet-nutrition-mental-health-chris-palmer`

- **The Peterman Pod** — GoogleX Chief Scientist: Imposter Syndrome, Career Growth, Project Taste | Carey Nachenberg
  - 2025 · 71 分钟 · 22,403 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=zsoDJXTaahk>
  - transcript: `transcripts/googlex-chief-scientist-imposter-syndrome-career.txt`
  - slug: `googlex-chief-scientist-imposter-syndrome-career`

- **The Ezra Klein Show** — What Trump’s Tariffs Will Actually Do | The Ezra Klein Show
  - 2025 · 51 分钟 · 983,981 播放 · 政治 / 社会
  - source: <https://www.youtube.com/watch?v=DhabG-dyQu0>
  - transcript: `transcripts/trump-s-tariffs-will-actually-do.txt`
  - slug: `trump-s-tariffs-will-actually-do`

- **Conversations with Tyler** — David Brooks on Audacity, AI, and the American Psyche (Live at @92ndStreetY)
  - 2025 · 74 分钟 · 13,257 播放 · 人工智能
  - source: <https://www.youtube.com/watch?v=I8Z50JuysNg>
  - transcript: `transcripts/david-brooks-audacity-ai-american-psyche.txt`
  - slug: `david-brooks-audacity-ai-american-psyche`

- **The Peterman Pod** — Ex-Head of Eng at Instagram: Career Regrets and Learnings | James Everingham
  - 2026 · 58 分钟 · 20,624 播放 · 职业 / 管理
  - source: <https://www.youtube.com/watch?v=VIF5Fm8NdE8>
  - transcript: `transcripts/ex-head-eng-at-instagram-career-regrets.txt`
  - slug: `ex-head-eng-at-instagram-career-regrets`

- **Dwarkesh Podcast** — Ilya Sutskever (OpenAI Chief Scientist) — Why next-token prediction could surpass human intelligence
  - 2023 · 47 分钟 · 784,549 播放 · 人工智能
  - source: <https://www.youtube.com/watch?v=Yf1o0TQzry8>
  - transcript: `transcripts/ilya-sutskever-next-token-prediction-could-surpass.txt`
  - slug: `ilya-sutskever-next-token-prediction-could-surpass`

- **Lex Fridman Podcast** — Brett Johnson: US Most Wanted Cybercriminal | Lex Fridman Podcast #272
  - 2022 · 227 分钟 · 9,806,748 播放 · 思想 / 访谈
  - source: <https://www.youtube.com/watch?v=cC1LFC0KFSw>
  - transcript: `transcripts/brett-johnson-us-most-wanted-cybercriminal.txt`
  - slug: `brett-johnson-us-most-wanted-cybercriminal`

- **Mindscape (Sean Carroll)** — Mindscape 253 | David Deutsch on Science, Complexity, and Explanation
  - 2023 · 102 分钟 · 87,928 播放 · 复杂性 / 系统
  - source: <https://www.youtube.com/watch?v=ldgK7EhEnto>
  - transcript: `transcripts/david-deutsch-science-complexity-explanation.txt`
  - slug: `david-deutsch-science-complexity-explanation`

- **Acquired** — Google Part III: The AI Company. Google is amazingly well-positioned... will they win in AI? (Audio)
  - 2025 · 246 分钟 · 127,203 播放 · 商业 / 投资
  - source: <https://www.youtube.com/watch?v=lCEB7xHer5U>
  - transcript: `transcripts/google-part-iii-ai-company-google.txt`
  - slug: `google-part-iii-ai-company-google`

- **The Peterman Pod** — Turing Award Winner: Early AI, LLM Predictions, Causality | Judea Pearl
  - 2026 · 87 分钟 · 18,434 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=FleTXB1fAcQ>
  - transcript: `transcripts/turing-award-winner-early-ai-llm.txt`
  - slug: `turing-award-winner-early-ai-llm`

- **Huberman Lab** — Dr. Andy Galpin: Optimal Nutrition & Supplementation for Fitness | Huberman Lab Guest Series
  - 2023 · 185 分钟 · 5,314,785 播放 · 健康 / 体能
  - source: <https://www.youtube.com/watch?v=q37ARYnRDGc>
  - transcript: `transcripts/andy-galpin-optimal-nutrition-supplementation-fitness.txt`
  - slug: `andy-galpin-optimal-nutrition-supplementation-fitness`

- **The Peterman Pod** — Turing Award Winner: The Invention of Public Key Cryptography | Martin Hellman
  - 2026 · 61 分钟 · 9,614 播放 · 计算机 / 系统
  - source: <https://www.youtube.com/watch?v=AZLOETBCQM4>
  - transcript: `transcripts/turing-award-winner-invention-public-key.txt`
  - slug: `turing-award-winner-invention-public-key`

