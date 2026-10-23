
import random
import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #101827, #202c45);
        color: white;
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #60a5fa;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #d1d5db;
        margin-bottom: 30px;
    }

    .result-card {
        background-color: #273449;
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        border: 1px solid #475569;
        margin-top: 20px;
    }

    .move {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }

    div.stButton > button {
        width: 100%;
        min-height: 65px;
        border-radius: 14px;
        font-size: 19px;
        font-weight: bold;
        border: 1px solid #60a5fa;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        border-color: #93c5fd;
        transform: scale(1.03);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "ties" not in st.session_state:
    st.session_state.ties = 0

if "rounds" not in st.session_state:
    st.session_state.rounds = 0

if "last_round" not in st.session_state:
    st.session_state.last_round = None

if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# GAME DATA
# -----------------------------
choices = {
    "rock": {"emoji": "🪨", "label": "Rock"},
    "paper": {"emoji": "📄", "label": "Paper"},
    "scissors": {"emoji": "✂️", "label": "Scissors"}
}

# -----------------------------
# GAME LOGIC
# -----------------------------
def play_game(player):
    computer = random.choice(list(choices.keys()))

    if player == computer:
        result = "It's a Tie!"
        outcome = "tie"
        st.session_state.ties += 1

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        result = "You Win!"
        outcome = "win"
        st.session_state.player_score += 1

    else:
        result = "Computer Wins!"
        outcome = "loss"
        st.session_state.computer_score += 1

    st.session_state.rounds += 1

    round_data = {
        "player": player,
        "computer": computer,
        "result": result,
        "outcome": outcome,
        "round": st.session_state.rounds
    }

    st.session_state.last_round = round_data
    st.session_state.history.insert(0, round_data)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    '<div class="main-title">🎮 Rock Paper Scissors</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Challenge the computer and see who wins!'
    '</div>',
    unsafe_allow_html=True
)

st.info("👋 Welcome! Choose your move below to start playing.")

# -----------------------------
# SCOREBOARD
# -----------------------------
st.subheader("🏆 Scoreboard")

col1, col2, col3 = st.columns(3)

col1.metric(
    "👤 You",
    st.session_state.player_score
)

col2.metric(
    "🤖 Computer",
    st.session_state.computer_score
)

col3.metric(
    "🤝 Ties",
    st.session_state.ties
)

st.caption(f"Rounds played: {st.session_state.rounds}")

st.divider()

# -----------------------------
# PLAYER CHOICES
# -----------------------------
st.subheader("✋ Make Your Move")
st.write("Choose one of the three options:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Rock", key="rock", use_container_width=True):
        play_game("rock")

with col2:
    if st.button("📄 Paper", key="paper", use_container_width=True):
        play_game("paper")

with col3:
    if st.button("✂️ Scissors", key="scissors", use_container_width=True):
        play_game("scissors")

# -----------------------------
# LAST ROUND RESULT
# -----------------------------
if st.session_state.last_round:
    game = st.session_state.last_round

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.subheader("🎯 Round Result")

    player_move = choices[game["player"]]
    computer_move = choices[game["computer"]]

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.markdown("**👤 Your Move**")
        st.markdown(
            f'<div class="move">{player_move["emoji"]}</div>',
            unsafe_allow_html=True
        )
        st.write(player_move["label"])

    with result_col2:
        st.markdown("**🤖 Computer's Move**")
        st.markdown(
            f'<div class="move">{computer_move["emoji"]}</div>',
            unsafe_allow_html=True
        )
        st.write(computer_move["label"])

    if game["outcome"] == "win":
        st.success("🎉 You Win! Great job!")
        st.balloons()

    elif game["outcome"] == "loss":
        st.error("😅 Computer Wins! Try again!")

    else:
        st.warning("🤝 It's a tie! Play another round.")

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# GAME HISTORY
# -----------------------------
if st.session_state.history:
    st.divider()
    st.subheader("📜 Recent Rounds")

    for game in st.session_state.history[:5]:
        player = choices[game["player"]]
        computer = choices[game["computer"]]

        st.write(
            f"**Round {game['round']}** — "
            f"You: {player['emoji']} {player['label']} | "
            f"Computer: {computer['emoji']} {computer['label']} | "
            f"**{game['result']}**"
        )

# -----------------------------
# RESET GAME
# -----------------------------
st.divider()

if st.button("🔄 Reset Game", use_container_width=True):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.rounds = 0
    st.session_state.last_round = None
    st.session_state.history = []
    st.rerun()

st.markdown(
    "<p style='text-align:center; color:#9ca3af;'>"
    "Made with ❤️ using Python and Streamlit"
    "</p>",
    unsafe_allow_html=True
)
