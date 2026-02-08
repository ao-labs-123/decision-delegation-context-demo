import streamlit as st

# =========================
# 文脈タイプ定義（C）
# =========================

CONTEXT_TYPES = {
    "position_dependent": {
        "label": "立場依存",
        "description": (
            "意思決定を自分では行わず、"
            "相手の立場や役割に判断を委ねる文脈タイプ。"
        ),
        "deep_dive": "その辺は、〇〇さんの判断でいいと思います。",
        "examples": [
            "その辺は、〇〇さんの判断でいいと思います。",  # 深掘り
            "私はどちらでも大丈夫です。",
            "上の判断に従います。",
            "〇〇さんが決めた方で。",
            "その件は任せます。"
        ],
        "interpretation": {
            "stage1": "判断に関する発話である。",
            "stage2": "話者自身の判断は示されていない。",
            "stage3": "判断主体が他者（〇〇さん）に置かれている。",
            "stage4": "話者の責任は暗黙的に回避されている。",
            "stage5": "最終的な意思決定は相手の立場に委ねられている。"
        },
        "note": (
            "判断を他者に移すことで、"
            "対立回避や責任分散を実現する構造を持つ。"
        )
    },

    "implicit_rule": {
        "label": "暗黙ルール",
        "description": (
            "明示的な決定主体や規則を示さず、"
            "慣習や一般性を根拠として判断を固定する文脈タイプ。"
        ),
        "deep_dive": "普通は、そういうやり方ですよね。",
        "examples": [
            "普通は、そういうやり方ですよね。",  # 深掘り
            "いつもそうしてますよ。",
            "暗黙的にそうなってます。",
            "特に決まってないけど、だいたいこうです。",
            "今まではこのやり方でした。"
        ],
        "interpretation": {
            "stage1": "方法や判断基準についての発話。",
            "stage2": "明確な決定者は存在しない。",
            "stage3": "『普通』『いつも』といった規範が根拠となっている。",
            "stage4": "異議を唱えにくい構造が形成されている。",
            "stage5": "判断は慣習に固定され、個人の責任は曖昧化されている。"
        },
        "note": (
            "判断の根拠を慣習に置くことで、"
            "責任主体を消失させる文脈構造。"
        )
    },

    "responsibility_shift": {
        "label": "責任の所在",
        "description": (
            "判断を進めつつも、"
            "最終的な可否や責任を他者に委ねる文脈タイプ。"
        ),
        "deep_dive": "それで問題がなければ進めますが。",
        "examples": [
            "それで問題がなければ進めますが。",  # 深掘り
            "問題あれば言ってください。",
            "ダメなら止めます。",
            "OK出たらやります。",
            "一応確認ですけど…。"
        ],
        "interpretation": {
            "stage1": "行動や判断を前提とした発話。",
            "stage2": "条件付きでの実行が示されている。",
            "stage3": "最終判断は話者以外に委ねられている。",
            "stage4": "結果に対する責任が外部化されている。",
            "stage5": "判断と責任が分離された状態で行動が保留されている。"
        },
        "note": (
            "実行意図を示しつつ、"
            "責任の所在を相手に移動させる構造を持つ。"
        )
    }
}

# =========================
# Streamlit UI
# =========================

st.title("文脈解釈デモ：C（判断委ね系）")
st.caption("※ 統計モデル・LLMは使用していません")

context_key = st.selectbox(
    "文脈タイプを選択",
    options=list(CONTEXT_TYPES.keys()),
    format_func=lambda k: CONTEXT_TYPES[k]["label"]
)

context = CONTEXT_TYPES[context_key]

st.subheader("文脈タイプの説明")
st.write(context["description"])

st.subheader("例文一覧")
for i, ex in enumerate(context["examples"], 1):
    st.markdown(f"{i}. {ex}")

st.divider()

st.subheader("解析対象（深掘り）")
st.markdown(f"**「{context['deep_dive']}」**")

st.subheader("Stageごとの解釈")
for stage, text in context["interpretation"].items():
    st.markdown(f"- **{stage}**：{text}")

st.subheader("解釈の説明")
st.write(context["note"])

st.divider()
st.caption(
    "判断委ね系では、意思決定そのものではなく、"
    "判断主体と責任の所在の移動を解析対象とする。"
)
