#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""动机诊断器：基于卢比孔模型与动机诊断框架，做一轮结构化诊断。

用法：
  交互式：  python diagnose.py
  非交互：  python diagnose.py a,c,b,a,b,a,b
            （答案顺序见 QUESTIONS；每题一个字母 a/b/c，逗号分隔）

输出：卡点阶段 + 主要机制 + 干预建议（引用 skill 内 references/ 模型）。
"""
import sys

QUESTIONS = [
    ("你/他现在主要卡在哪一环？", [
        ("a", "还在想要不要做 / 做什么（定不下目标）"),
        ("b", "决定了，但没真正开始投入"),
        ("c", "开始了，但坚持不下来 / 容易放弃"),
        ("d", "做了，但受挫了、在想还要不要继续"),
    ]),
    ("对这个具体任务，自己觉得『能做到』吗？", [
        ("a", "完全能 / 比较有把握"),
        ("b", "不太确定"),
        ("c", "觉得做不到"),
    ]),
    ("觉得『做了会有用、有好结果』吗？", [
        ("a", "肯定有用"),
        ("b", "不一定"),
        ("c", "觉得没用"),
    ]),
    ("这件事对你的好处，值得付出的成本吗？", [
        ("a", "很值得"),
        ("b", "一般"),
        ("c", "不值得 / 没意义"),
    ]),
    ("是不是同时有好几个目标在互相打架？", [
        ("a", "没有冲突"),
        ("b", "有一点"),
        ("c", "严重冲突，很内耗"),
    ]),
    ("你更接近哪种说法？", [
        ("a", "『我想把 X 做成』（发展 / 求收益）"),
        ("b", "『我必须别搞砸 X』（维护 / 避损失）"),
    ]),
    ("一遇困难或压力，更像是？", [
        ("a", "动不起来、想太多（状态导向）"),
        ("b", "直接冲上去干（行动导向）"),
    ]),
    ("失败后第一反应是？", [
        ("a", "『我不行』（实体论）"),
        ("b", "『再试试 / 换个法子』（递增论）"),
    ]),
]

STAGE_MAP = {
    "a": ("决策前 / 目标选择", "还在定目标，或目标间冲突"),
    "b": ("决策 / 承诺", "决定了却没真正投入"),
    "c": ("行动 / 规划", "承诺了却启动或坚持不了"),
    "d": ("行动后 / 评估", "受挫、在考虑放弃"),
}


def ask(qidx):
    q, opts = QUESTIONS[qidx]
    print(f"\n{q}")
    for code, text in opts:
        print(f"  {code}) {text}")
    while True:
        ans = input("  你的选择> ").strip().lower()
        if ans in [c for c, _ in opts]:
            return ans
        print("  请输入对应字母。")


def main():
    print("=" * 52)
    print("动机诊断器（卢比孔模型 / 期望-价值 / 调节焦点等）")
    print("=" * 52)
    if len(sys.argv) > 1:
        answers = [x.strip().lower() for x in sys.argv[1].split(",")]
        if len(answers) != len(QUESTIONS):
            print(f"答案数量应为 {len(QUESTIONS)} 个，用逗号分隔。")
            sys.exit(1)
    else:
        answers = [ask(i) for i in range(len(QUESTIONS))]

    stage_code = answers[0]
    stage, stage_desc = STAGE_MAP.get(stage_code, ("未知", ""))

    levers = [
        ("自我效能感", answers[1]),
        ("结果预期", answers[2]),
        ("价值（益处>成本）", answers[3]),
        ("目标冲突", answers[4]),
        ("调节焦点", answers[5]),
        ("行动/状态导向", answers[6]),
        ("心智模式", answers[7]),
    ]

    print("\n" + "=" * 52)
    print("诊断结果")
    print("=" * 52)
    print(f"卡点阶段：{stage} —— {stage_desc}")

    print("\n主要机制（标 c 的为负项）：")
    for name, a in levers:
        flag = "  <-- 需干预" if a == "c" else ("  (偏弱)" if a == "b" else "")
        print(f"  - {name}: {a}{flag}")

    print("\n建议干预（按优先级）：")
    suggestions = []
    if stage_code == "a":
        suggestions.append("决策前：用『审慎心态』现实权衡利弊，先帮其把目标具体化；检查是否目标冲突（勒温四类型），必要时目标屏蔽。")
    if stage_code == "b":
        suggestions.append("承诺：做『心理对照』——写愿望→结果→障碍→计划（WOOP），可提升承诺与成绩约 35%。")
    if stage_code == "c":
        suggestions.append("行动：写『执行意向』——『如果（情境暗示）…那么（具体行为）』+后备计划；把目标改成『具体+有难度但可达』；切换到『行动心态』（闭锁、乐观）。")
    if stage_code == "d":
        suggestions.append("评估：处理自我效能归因（失败≠无能）；若目标已不现实，考虑战略性『目标解除』，把资源转向。")
    if answers[1] == "c" or answers[2] == "c" or answers[3] == "c":
        suggestions.append("期望-价值：任一项为 0 行为即为 0。自我效能低→给小胜/示范/拆解；结果预期低→澄清路径；价值低→重连其真正在意的意义。")
    if answers[4] == "c":
        suggestions.append("目标冲突：显式列出冲突目标与利弊，做取舍；用目标屏蔽保护焦点目标。")
    if answers[5] == "b":
        suggestions.append("调节焦点：对方是『维护取向』，沟通用『避损失/稳妥/质量』框架而非『收益/成长』框架（调节性匹配）。")
    if answers[6] == "a":
        suggestions.append("状态导向：用执行意向降低启动门槛；用自主选择（内在动机）对冲外在压力。")
    if answers[7] == "a":
        suggestions.append("心智模式：失败后滑向实体论，用『大脑可塑/能力靠练』的说服性材料替代『你真聪明』式表扬，推向递增论。")

    for i, s in enumerate(suggestions[:4], 1):
        print(f"  {i}. {s}")

    print("\n（详细模型见 skill 的 references/ 各文件；可填 assets/diagnosis-worksheet.md 做自检。）")


if __name__ == "__main__":
    main()
