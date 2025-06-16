import streamlit as st
import pandas as pd

st.set_page_config(page_title="שיבוץ כוח אדם", layout="wide")
st.title("📋 אפליקציית שיבוץ משימות לצוותים רפואיים")

# --- הגדרת משימה ---
st.header("1. הגדרת משימה")
with st.expander("✏️ פרטי המשימה"):
    mission_name = st.text_input("שם המשימה", "הר חריף")
    num_teams = st.number_input("מספר צוותים", min_value=1, value=2)

    roles_needed = ["נהג", "מט""ב", "חוג""ד", "חובש"]
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
    with st.expander("✏️ הזנה ידנית"):
        default_data = {
            'שם': ["גל א׳", "אושרי", "נועם", "ביטרן"],
            'תפקיד': ["חובש", "חוג""ד", "מט""ב", "חובש"],
            'תפקיד נוסף': ["", "חובש", "", ""],
            'הערות': ["זמין רק באמצע שבוע", "אסור שישן בשטח", "אין מגבלות", "לא מגיע בימי שישי"]
        }
        df = pd.DataFrame(default_data)
        st.dataframe(df, use_container_width=True)

# --- סיכום ראשוני ---
st.header("3. סיכום מצב")
st.markdown(f"**שם משימה:** {mission_name} | **מספר צוותים:** {num_teams}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("כמות נדרשת לכל תפקיד")
    role_totals = {role: mission_structure[role] * num_teams for role in mission_structure}
    st.write(pd.DataFrame.from_dict(role_totals, orient='index', columns=['נדרש']))

with col2:
    st.subheader("כמות זמינה לפי החיילים")
    available = df[['תפקיד']].copy()
    available = available.value_counts().reset_index(name='כמות')
    st.write(available)

# --- אזור עתידי לשיבוץ אוטומטי ---
st.header("4. (בהמשך) שיבוץ אוטומטי")
st.info("כאן נציג את השיבוץ המוצע לפי התפקידים, ההעדפות והחוקים")