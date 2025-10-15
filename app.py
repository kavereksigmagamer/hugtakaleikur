import streamlit as st
import random

# --- Hugtök og skilgreiningar ---
hugtok_definitions = {
    "Samfélagsfræði": "landafræði og saga í sameiningu, einkum sem grunnskólafag",
    "Sjálfsþurftarbúskapur": "búskapur þar sem framleiðslan fullnægir eigin þörfum.",
    "Yfirstétt": "sá hópur í þjóðfélagi sem hefur mestan auð og völd.",
    "Félagsmótun": "félagsleg samskipti sem hafa mótandi áhrif á einstakling.",
    "Val": "það að velja",
    "Landbúnaðarbyltingin": "Tímabil þegar fólk fór að stunda landbúnað.",
    "Barnavinna": "Vinna sem börn vinna.",
    "Gildi": "það hversu mikið vægi eða verðmæti e-ð hefur.",
    "Viðmið": "Setja sér viðmið.",
    "Mansal": "Ólögleg verslun með fólk.",
    "Sveitafélag": "stjórnsýslueining undir stjórn kjörinna fulltrúa sem sinnir lögboðnum verkefnum svo sem leikskólum, grunnskólum, félagsþjónustu, menningarstarfsemi og rekstri dvalarheimila.",
    "Sjálfsmynd": "Sú mynd sem einstaklingur hefur af sjálfum sér.",
    "Hnattvæðing": "útbreiðsla e-s um heiminn allan, einkum í tengslum við alþjóðlega verslun og samskipti.",
    "Hnattrænn hugsanaháttur": "Að hugsa út frá heiminum í heild.",
    "Keyta": "Úrgangur frá dýri.",
    "Formlegt viðmið": "Skráðar reglur og lög.",
    "Óformlegt viðmið": "Óskráðar reglur og venjur.",
    "Formlegt taumhald": "Refsing eða umbun samkvæmt lögum.",
    "Óformlegt taumhald": "Refsing eða umbun sem byggir á venjum.",
    "Shobono": "Heimili Yanómama fólksins.",
    "Efnishyggja": "sú afstaða að meta efnislega hluti (eignir, stöðu) ofar öllu öðru.",
    "Samfélag": "Hópur fólks sem býr saman og hefur samskipti.",
    "Náttúra": "Allt sem er ekki skapað af manni.",
    "Menning": "þroska eða þróunarstig mannlegs samfélags, andlegt líf þess og efnisleg gæði.",
    "Kynhlutverk": "Hlutverk sem samfélagið tengir við kyn.",
    "Iðnvætt ríki": "Ríki þar sem iðnaður er mikilvægur.",
    "Óiðnvætt ríki": "Ríki þar sem iðnaður er lítil eða engin.",
    "Neyslusamfélag": "samfélag sem einkennist af mikilli neyslu og óhófi.",
    "Sjálfbær þróun": "Þróun sem tekur mið af framtíðinni og náttúru.",
    "Heimsmynd": "Hvernig einstaklingur eða hópur sér heiminn.",
    "Þjónustugreinar": "atvinnugrein þar sem þjónusta er veitt, t.d. verslun.",
    "Matarsóun": "Að henda mat sem hefði mátt nýta.",
    "Frávikshegðun": "Hegðun sem víkur frá viðmiðum samfélagsins.",
    "Afbrot": "réttarbrot sem refsing er lögð við í settum lögum, misferli.",
    "Ríkissaksóknari": "embættismaður sem fer með ákæruvald í opinberum málum.",
    "Ríkislögreglustjóri": "æðsti yfirmaður lögreglu og almannavarna í landinu.",
    "Réttarríki": "samfélag sem virðir lög og rétt við beitingu ríkisvalds, hefur óháða dómstóla og tryggir borgurunum réttaröryggi.",
    "Héraðsdómur": "Dómstóll á ákveðnu svæði.",
    "Hæstiréttur": "æðsti dómstóll ríkis, sem úrlausnum héraðsdómstóla má skjóta til.",
    "Skilorðsbundið fangelsi": "Fangelsisdómur sem er ekki afplánaður nema brotið sé aftur.",
    "Óskilorðsbundið fangelsi": "Fangelsisdómur sem er afplánaður strax.",
    "Samfélagsþjónusta": "Refsing þar sem einstaklingur vinnur fyrir samfélagið.",
    "Allsherjarþing SÞ": "Aðalþing Sameinuðu þjóðanna.",
    "Neitunarvald": "vald til að stöðva framgang einhvers, t.d. lagabreytingar, með því að samþykkja það ekki.",
    "Friðagæslusveitir SÞ": "Herlið Sameinuðu þjóðanna til að halda friði.",
    "Mannréttindi": "Grunnréttindi allra manna.",
    "Jafnrétti": "Að allir hafi sömu réttindi og tækifæri.",
    "Þjóðarréttur": "matarréttur sem er algengur og vinsæll hjá ákveðinni þjóð.",
    "Alþjóðalögregla": "alþjóðastofnun um samstarf á sviði löggæslu og rannsókna sakamála.",
    "Tjáningarfrelsi": "frelsi til að láta skoðanir sínar í ljós í ræðu eða riti, málfrelsi.",
    "Lifandi lýðræði": "Lýðræði þar sem fólk tekur virkan þátt."
}

# --- Streamlit setup ---
st.set_page_config(page_title="Hugtaka Spurningaleikur", page_icon="🎯", layout="centered")
st.markdown("<h1 style='text-align:center;'>🎯 Hugtaka Spurningaleikur</h1>", unsafe_allow_html=True)

# --- Session state setup ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "questions" not in st.session_state:
    terms = list(hugtok_definitions.keys())
    random.shuffle(terms)
    questions = []
    for term in terms:
        correct = hugtok_definitions[term]
        wrong = random.sample([hugtok_definitions[t] for t in terms if t != term], 3)
        choices = [correct] + wrong
        random.shuffle(choices)
        questions.append({"term": term, "choices": choices, "answer": correct})
    st.session_state.questions = questions
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# --- Main logic ---
def next_question(reset=False):
    if reset:
        st.session_state.score = 0
        st.session_state.question_index = 0
        random.shuffle(st.session_state.questions)
    else:
        st.session_state.question_index += 1
    st.session_state.feedback = ""

def check_answer(choice):
    q = st.session_state.questions[st.session_state.question_index]
    if choice == q["answer"]:
        st.session_state.score += 1
        st.session_state.feedback = "✅ Rétt svar!"
        next_question()
    else:
        st.session_state.feedback = "❌ Rangt svar! Byrjar aftur."
        next_question(reset=True)

# --- Display question ---
if st.session_state.question_index >= len(st.session_state.questions):
    st.success(f"🎉 Þú kláraðir leikinn! Lokastig: {st.session_state.score}")
    if st.button("Spila aftur"):
        next_question(reset=True)
else:
    q = st.session_state.questions[st.session_state.question_index]
    st.markdown(f"### Spurning {st.session_state.question_index + 1}/{len(st.session_state.questions)}")
    st.markdown(f"**Hvað þýðir hugtakið:** <span style='color:#00ff88; font-weight:bold;'>{q['term']}</span>?", unsafe_allow_html=True)
    choice = st.radio("Veldu svar:", q["choices"], index=None)
    if st.button("Svara"):
        if choice is None:
            st.warning("Veldu svar fyrst.")
        else:
            check_answer(choice)

    if st.session_state.feedback:
        st.info(st.session_state.feedback)

st.markdown(f"### Stig: {st.session_state.score}")
