# 动机诊断与干预 · Motivation Diagnosis

> 一个「诊断 → 定位卡点 → 给干预」流程的 WorkBuddy 技能（Skill）。
> 输入「一个人 + 一个卡住的目标」，它先用卢比孔（Rubicon）四阶段模型判断卡在哪一环，再用期望—价值、目标冲突、调节焦点、行动/状态导向、心智模式、成就动机等杠杆诊断「卡因」，最后输出有实证研究支撑的具体干预（心理对照、执行意向、目标具体化、调节性匹配等）。

---

## 这是什么

动机问题通常不是「懒」，而是**某个具体机制在某一个阶段断了**。本 skill 是一套可反复调用的诊断流程：先定位断点，再对症干预，而不是空喊「打起精神」。

适用范围（三视角通用，不限行业/场景）：
- **自我**：没动力写报告、总拖延、定了目标坚持不下来、一遇困难就放弃
- **管理 / 教练**：团队不出活、下属没干劲、怎么激励别人
- **目标设计**：目标总启动不了、多目标互相打架

---

## 谁该用

- 想搞懂「自己为什么动不起来」的人
- 管理者 / 教练 / 老师 / 家长（想读懂并干预他人的动机卡点）
- 任何做目标管理、习惯养成、行为改变的人

> 如果你是**销售团队管理者**，直接看派生的场景版 [`sales-motivation-coach`](https://github.com/workbuddy-motivation-skills/sales-motivation-coach)——它把这里的框架固化到销售场景，直接给可照着说的话术。

---

## 安装（WorkBuddy 用户级 Skill）

> 前提：已安装 [WorkBuddy](https://www.workbuddy.cn)。Skill 放在用户级目录 `~/.workbuddy/skills/` 后，下次对话自动生效、跨工作区可用。

### 方式一（推荐）：git clone

```bash
git clone https://github.com/workbuddy-motivation-skills/motivation-diagnosis.git \
  ~/.workbuddy/skills/motivation-diagnosis
```

### 方式二：下载 ZIP 解压

```bash
# macOS / Linux
unzip motivation-diagnosis.zip -d ~/.workbuddy/skills/motivation-diagnosis

# Windows (PowerShell)
Expand-Archive motivation-diagnosis.zip -DestinationPath "$env:USERPROFILE\.workbuddy\skills\motivation-diagnosis"
```

### 验证安装

方式 A —— 对话触发：新开对话说「我总是拖延写报告 / 团队不出活」，skill 应被自动调用。
方式 B —— 跑诊断脚本（纯 Python 标准库）：

```bash
cd ~/.workbuddy/skills/motivation-diagnosis
python3 scripts/diagnose.py c,a,a,a,b,a,a,b
```

正常会输出「卡点阶段 + 需干预机制 + 干预建议」。

---

## 目录结构

```
motivation-diagnosis/
├── SKILL.md                      # 技能入口：触发词、诊断骨架、工作流
├── references/
│   ├── rubicon-stages.md         # 卢比孔四阶段与两种心态
│   ├── expectancy-value.md        # 期望×价值公式与诊断
│   ├── goal-conflict.md           # 勒温四冲突类型与目标屏蔽
│   ├── commitment-planning.md     # 心理对照、执行意向、目标具体性
│   ├── striving-control.md        # 调节焦点、行动/状态导向、目标解除
│   └── individual-differences.md  # 成就动机、心智模式（实体论/递增论）
├── scripts/diagnose.py            # 问答式结构化诊断
├── assets/diagnosis-worksheet.md  # 可填写的自检工作表
├── LICENSE
└── README.md
```

---

## 怎么用

### 1. 对话式（最常用）

直接描述你的动机难题，命中触发词即自动启用：

> 你：我定了每天读书的目标，但总启动不了。
> Skill：先定位 → 行动/规划阶段；主因：执行意向缺失 + 目标过大；
>       干预：把「有空就读」改成「如果晚 10 点坐床边，那么先读 1 页」+ 后备计划。

### 2. 脚本式（批量 / 离线）

`scripts/diagnose.py` 接收 8 个字母（a/b/c/d），对应 8 道题答案，输出结构化诊断：

```bash
python3 scripts/diagnose.py <答案序列，逗号分隔>
# 例：c,a,a,a,b,a,a,b
```

每题含义见 `scripts/diagnose.py` 顶部注释与 `assets/diagnosis-worksheet.md`。

---

## 关联技能

- [`sales-motivation-coach`](https://github.com/workbuddy-motivation-skills/sales-motivation-coach)：本 skill 的**销售场景派生版**。通用诊断框架不变，但话术与干预按销售团队写死，管理者拿来即用。

---

## 常见问题

**Q：这个 skill 能脱离 WorkBuddy 用吗？**
A：诊断逻辑在 `scripts/diagnose.py`（纯标准库），可独立运行做结构化诊断；完整「对话触发 + 干预生成」需 WorkBuddy。

**Q：涉及真实心理困扰怎么办？**
A：本 skill 不替代心理咨询。若对方有抑郁/焦虑等情绪障碍，提示寻求专业帮助。

---

## 许可证

[MIT](LICENSE) —— 自由使用、修改、分发，包括商业用途。
