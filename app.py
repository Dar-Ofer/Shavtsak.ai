import streamlit as st
import pandas as pd

st.set_page_config(page_title="שיבוץ כוח אדם", layout="wide")
st.title("📋 אפליקציית שיבוץ משימות לצוותים רפואיים")

# --- הגדרת משימה ---
st.header("1. הגדרת משימה")
with st.expander("✏️ פרטי המשימה"):
    mission_name = st.text_input("שם המשימה", "הר חריף")
    num_teams = st.number_input("מספר צוותים", min_value=1, value=2)

    roles_needed = ["נהג", "מט"ב", "חוג"ד", "חובש"]
    mission_structure = {}
    for role in roles_needed:
        mission_structure[role] = st.number_input(f"כמה {role} צריך בכל צוות?", min_value=0, value=1 if role != "חובש" else 2)

# --- פרטי חיילים ---
st.header("2. הזנת כוח אדם")
st.markdown("העלה קובץ Excel או הזן ידנית")

uploaded_file = st.file_uploader("קובץ אקסל עם רשימת חיילים (עמודות: שם, תפקיד, תפקיד נוסף, הערות)", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
else:
    st.subheader("הזנה ידנית")
    if 'manual_data' not in st.session_state:
        st.session_state.manual_data = []

    with st.form(key="manual_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("שם")
            role = st.selectbox("תפקיד", ["", "חובש", "מט"ב", "נהג", "חוג"ד", "קשר", "מפקד לבנה", "מפקד אירוע"])
        with col2:
            alt_role = st.selectbox("תפקיד נוסף", ["", "חובש", "מט"ב", "נהג", "חוג"ד", "קשר", "מפקד לבנה", "מפקד אירוע"])
            notes = st.text_input("הערות")

        submitted = st.form_submit_button("➕ הוסף לרשימה")
        if submitted and name and role:
            st.session_state.manual_data.append({
                'שם': name,
                'תפקיד': role,
                'תפקיד נוסף': alt_role,
                'הערות': notes
            })

    if st.session_state.manual_data:
        df = pd.DataFrame(st.session_state.manual_data)
        st.dataframe(df, use_container_width=True)
    else:
        df = pd.DataFrame(columns=['שם', 'תפקיד', 'תפקיד נוסף', 'הערות'])
        st.info("לא הוזנו חיילים עדיין")

# --- סיכום ראשוני ---
st.header("3. סיכום מצב")
st.markdown(f"**שם משימה:** {mission_name} | **מספר צוותים:** {num_teams}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("כמות נדרשת לכל תפקיד")
    role_totals = {role: mission_structure[role] * num_teams for role in mission_structure}
    st.write(pd.DataFrame.from_dict(role_totals, orient='index', columns=['נדרש']))

with col2:
    st.subheader("כוח אדם קיים")
    if not df.empty:
        st.dataframe(df[['שם', 'תפקיד', 'תפקיד נוסף', 'הערות']], use_container_width=True)
    else:
        st.write("אין נתונים להצגה")

# --- אזור עתידי לשיבוץ אוטומטי ---
st.header("4. (בהמשך) שיבוץ אוטומטי")
st.info("כאן נציג את השיבוץ המוצע לפי התפקידים, ההעדפות והחוקים")