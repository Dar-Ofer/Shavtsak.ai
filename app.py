import streamlit as st

st.set_page_config(page_title="שבצק AI", layout="wide")

# ניווט בין המסכים
menu = st.sidebar.radio("בחר מסך:", [
    "📌 הגדרת משימה",
    "👥 ניהול כוח אדם",
    "🗓️ טבלת שיבוץ",
    "📊 דוח מסכם"
])

# מסך 1 – הגדרת משימה וצוותים
if menu == "📌 הגדרת משימה":
    st.title("📌 הגדרת משימה וצוותים")
    with st.form("mission_form"):
        mission_name = st.text_input("שם המשימה")
        mission_dates = st.date_input("טווח תאריכים למשימה", [])
        num_teams = st.number_input("כמה צוותים במשימה?", min_value=1, value=1)
        st.markdown("#### הגדרת תפקידים בצוות (לדוגמה: אמבולנס = נהג, מטפל בכיר, 2 חובשים וכו')")
        team_structure = st.text_area("תיאור חופשי או פורמט מובנה")
        mission_constraints = st.text_area("הגבלות מבצעיות (מקסימום בית, מינימום ביחידה וכו')")
        submitted = st.form_submit_button("שמור משימה")
        if submitted:
            st.success("המשימה נשמרה (עדיין לא בבסיס נתונים)")

# מסך 2 – ניהול כוח אדם
elif menu == "👥 ניהול כוח אדם":
    st.title("👥 ניהול כוח אדם")
    st.markdown("הזן פרטי חיילים באופן ידני")
    with st.form("person_form"):
        name = st.text_input("שם")
        role = st.selectbox("תפקיד ראשי", ["", "חובש", "מטפל בכיר", "נהג אמבולנס", "נהג האמר", "לוחם", "מפקד לוחמים", "מפקד לבנה", "מנהל אירוע", "קשר"])
        secondary_role = st.selectbox("תפקיד נוסף", ["", "חובש", "מטפל בכיר", "נהג אמבולנס", "נהג האמר", "לוחם", "מפקד לוחמים", "מפקד לבנה", "מנהל אירוע", "קשר"])
        preferred_team = st.text_input("עובד טוב עם (שמות) – לא חובה")
        absences = st.text_area("תאריכים בהם אינו זמין (YYYY-MM-DD, מופרדים בפסיקים)")
        submitted = st.form_submit_button("➕ הוסף לחיילים")
        if submitted:
            st.success(f"{name} נוסף לרשימת כוח האדם (עדיין לא נשמר)!")

# מסך 3 – טבלת שיבוץ בפועל (placeholder)
elif menu == "🗓️ טבלת שיבוץ":
    st.title("🗓️ טבלת שיבוץ (תצוגת צופה)")
    st.info("כאן תוצג טבלת השיבוץ המלאה לפי ימים, צוותים ותפקידים. צופים לא יראו את מצב השהות או הערות פרטיות.")
    st.markdown("⚠️ שיבוץ טרם נבנה. בהמשך נציג את החלוקה לכל צוות לפי ימים.")

# מסך 4 – דוח מסכם
elif menu == "📊 דוח מסכם":
    st.title("📊 דוח מסכם")
    st.markdown("- כמה חיילים ביחידה/בבית\n- מי בבית? כמה זמן?\n- מי חרג ממגבלה?\n- גרף ימי שירות לכל חייל\n- ייצוא ל-Excel")
    st.info("תוכן הדוח ייבנה בהתאם למידע שישובץ בפועל")