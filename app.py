import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Blăniță Răsfățată | Ultra Pet Spa",
    page_icon="🐾",
    layout="wide"
)

if 'form_done' not in st.session_state:
    st.session_state.form_done = False

def handle_submit():
    st.session_state.form_done = True
    st.balloons()

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
    .stApp { background: #FFFAF4; }
    
    /* Header Principal */
    .main-header {
        text-align: center;
        padding: 70px 20px;
        background: linear-gradient(135deg, #FF9A8D 0%, #FF6A88 100%);
        color: white;
        border-radius: 40px;
        margin-bottom: 40px;
        box-shadow: 0 20px 40px rgba(255, 154, 141, 0.3);
    }

    /* Carduri stil Glassmorphism */
    .premium-card {
        background: white;
        padding: 25px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        border: 1px solid rgba(255,154,141,0.1);
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .premium-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(255, 154, 141, 0.1); }

    .stButton>button {
        width: 100%;
        border-radius: 15px;
        background: #FF9A8D;
        color: white;
        padding: 12px;
        font-weight: 800;
        border: none;
    }

    .calc-box {
        background: #FFF0ED;
        padding: 30px;
        border-radius: 30px;
        text-align: center;
        border: 2px dashed #FF9A8D;
    }
    </style>
    """, unsafe_allow_html=True)

@st.dialog("📖 Articol Complet")
def read_article(articol):  
    st.image(articol["img"], use_container_width=True)
    st.title(articol["titlu"])
    st.write(articol["text"])
    
    if "extra_text" in articol:
        st.info(articol["extra_text"])
        
    st.divider()
    st.info("Sfat: Vizitează salonul nostru din Sectorul 4 pentru consultanță personalizată.")

with st.sidebar:
    st.markdown("""
        <style>
        .stSidebar [data-testid="stImage"] {
            display: flex;
            justify-content: center;
            filter: drop-shadow(0px 10px 10px rgba(255, 154, 141, 0.4));
            padding-bottom: 20px;
        }
        .stSidebar [data-testid="stImage"] img {
            border-radius: 20px; 
            width: 150px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.image("logo.jpg")
    
    st.markdown("<h2 style='text-align: center; color: #FF9A8D; font-size: 1.5rem; margin-top: -10px;'>Blăniță Răsfățată</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.8rem; margin-top: -15px;'>Premium Pet Spa</p>", unsafe_allow_html=True)
    
    st.divider()

    st.markdown("""
        <style>
        /* Elimină cercul de la radio și face meniul să arate ca butoane */
        [data-testid="stSidebarNav"] {display: none;}
        
        .stRadio [role=radiogroup] {
            gap: 10px;
        }
        
        .stRadio div[role="radiogroup"] > label {
            background-color: white;
            border: 1px solid rgba(255,154,141,0.2);
            padding: 10px 20px;
            border-radius: 12px;
            transition: 0.3s;
            width: 100%;
        }
        
        .stRadio div[role="radiogroup"] > label:hover {
            border-color: #FF9A8D;
            background-color: #FFF0ED;
        }

        [data-testid="stSidebar"] {
            background-color: white !important;
            border-right: 1px solid #eee;
        }
        </style>
    """, unsafe_allow_html=True)

    menu = st.radio("EXPLOREAZĂ", 
                    ["🏠 Acasă", "✂️ Servicii & Programări", "🛍️ Pet Boutique", "🐶 Blog Păros", "⭐ Feedback"],
                    label_visibility="collapsed") 

    st.spacer = st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background: linear-gradient(135deg, #FFF0ED 0%, #FFFAF4 100%); 
                    padding: 20px; border-radius: 20px; border: 1px solid #FFD6D0;">
            <p style="color: #FF6A88; font-weight: 800; margin-bottom: 5px; font-size: 0.9rem;">📍 LOCAȚIE</p>
            <p style="color: #555; font-size: 0.85rem; margin-bottom: 15px;">Sector 4, București</p>
            <p style="color: #FF6A88; font-weight: 800; margin-bottom: 5px; font-size: 0.9rem;">📞 CONTACT</p>
            <p style="color: #555; font-size: 0.85rem;">07xx xxx xxx</p>
        </div>
    """, unsafe_allow_html=True)

    social_html = """
        <div style="display: flex; justify-content: center; gap: 20px;">
            <a href="https://www.instagram.com/CONTUL_TAU" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); 
                            width: 40px; height: 40px; border-radius: 50%; display: flex; justify-content: center; align-items: center; 
                            box-shadow: 0 4px 8px rgba(0,0,0,0.15);">
                    <span style="color: white; font-size: 20px; font-weight: bold;">IG</span>
                </div>
            </a>
            <a href="https://www.facebook.com/PAGINA_TA" target="_blank" style="text-decoration: none;">
                <div style="background: #1877F2; width: 40px; height: 40px; border-radius: 50%; 
                            display: flex; justify-content: center; align-items: center; 
                            box-shadow: 0 4px 8px rgba(0,0,0,0.15);">
                    <span style="color: white; font-size: 20px; font-weight: bold;">FB</span>
                </div>
            </a>
        </div>
    """
    st.markdown(social_html, unsafe_allow_html=True)

if menu == "🏠 Acasă":
    st.markdown('<div class="main-header"><h1>✨ BLĂNIȚĂ RĂSFĂȚATĂ</h1><p>Standardul de Aur în Estetică Canină</p></div>', unsafe_allow_html=True)
    
    col_a1, col_a2 = st.columns([1.2, 1])
    with col_a1:
        st.subheader("Bun venit în Universul Răsfățului")
        st.write("Suntem mai mult decât un salon de grooming; suntem un centru de wellness unde prietenul tău beneficiază de aromaterapie, muzică de relaxare și cele mai fine tratamente cosmetice.")
        st.video("https://www.youtube.com/watch?v=56nQi71MPvw")
    with col_a2:
        st.markdown('<div class="premium-card"><h4>📍 Sector 4 Focus</h4><p>Suntem mândri să servim comunitatea din Sectorul 4. Locația noastră este special gândită pentru acces facil și un mediu liniștit.</p></div>', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?w=500", use_container_width=True)

elif menu == "✂️ Servicii & Programări":
    st.header("✂️ Configurează Vizita")
    
    col_calc, col_calen = st.columns([1, 1.2])
    
    with col_calc:
        st.subheader("🧮 Calculator Preț")
        talia = st.selectbox("Talia cățelului:", ["Mică (<10kg)", "Medie (10-25kg)", "Mare (>25kg)"])
        servicii = st.multiselect("Servicii extra:", ["Tuns Design", "Spălat Premium", "Igienă Dentară", "Tratament Keratină"])
        
        baza = {"Mică (<10kg)": 100, "Medie (10-25kg)": 150, "Mare (>25kg)": 220}
        total = baza[talia] + (len(servicii) * 40)
        
        st.markdown(f'<div class="calc-box"><h3>Preț Estimat</h3><h1 style="color: #FF9A8D;">{total} RON</h1></div>', unsafe_allow_html=True)

    with col_calen:
        st.subheader("📅 Programează-te")
        data = st.date_input("Alege ziua:", min_value=datetime.now())
        ora = st.select_slider("Alege ora:", options=["09:00", "11:30", "14:00", "16:30", "19:00"])
        
        st.markdown(f'<div class="premium-card"><h4>Rezumat Programare</h4><p>Data: {data}<br>Ora: {ora}<br>Talie: {talia}</p></div>', unsafe_allow_html=True)
        if st.button("Confirmă Disponibilitatea"):
            st.toast("Verificăm slotul...")
            st.success("Slotul este disponibil! Te contactăm pentru confirmare.")

elif menu == "🛍️ Pet Boutique":
    st.header("🛍️ Pet Boutique - Exclusive Collection")
    produse = [
        ("Zgardă Piele 'Royal Blue'", "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=300", "120 RON"),
        ("Parfum 'Summer Paw'", "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=300", "85 RON"),
        ("Pătuț 'Cloud Nine'", "https://images.unsplash.com/photo-1591768793355-74d7c869c177?w=300", "250 RON"),
        ("Ham Ergonomic 'Neo'", "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=300", "145 RON"),
        ("Bol Ceramic 'Marble'", "https://images.unsplash.com/photo-1615678815958-5910c6811c25?w=300", "65 RON"),
        ("Jucărie Ansamblu Pisici", "https://images.unsplash.com/photo-1545249390-6bdfa286032f?w=300", "180 RON"),
        ("Recompense Artizanale", "https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=300", "45 RON"),
        ("Sampon Organic 'Silk'", "https://images.unsplash.com/photo-1583947581924-860bda6a26df?w=300", "95 RON"),
        ("Lese Retractabilă 'Pro'", "https://images.unsplash.com/photo-1601758124510-52d02ddb7cbd?w=300", "110 RON"),
        ("Ulei Somon Wild", "https://images.unsplash.com/photo-1626107438132-72c0c7760920?w=300", "75 RON")
    ]
    
    rows = [produse[i:i+3] for i in range(0, len(produse), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, (nume, img, pret) in enumerate(row):
            with cols[i]:
                st.markdown(f"""
                <div class="premium-card">
                    <img src="{img}" style="width:100%; border-radius:15px; margin-bottom:10px;">
                    <h4>{nume}</h4>
                    <p class="product-price">{pret}</p>
                </div>
                """, unsafe_allow_html=True)
                st.button(f"Adaugă {nume.split()[0]}", key=f"p_{nume}")

elif menu == "🐶 Blog Păros":
    st.header("🐶 Blogul Codițelor")
    
    articole = [
        {
            "titlu": "🦷 Sănătatea dentară la căței",
            "teaser": "De ce este vital să curățăm dinții prietenilor noștri...",
            "img": "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400",
            "text": "Igiena orală nu este doar despre respirație proaspătă. Bacteriile pot ajunge în sânge și pot afecta inima. Recomandăm periajul săptămânal și vizite regulate la salon pentru curățarea profesională.",
            "extra_text": "Peste 80% dintre câinii de peste 3 ani suferă de boli parodontale."
        },
        {
            "titlu": "❄️ Îngrijirea blănii în sezonul rece",
            "teaser": "Cum protejăm pernuțele de sare și gheață...",
            "img": "https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?w=400",
            "text": "Iarna aduce provocări mari. Sarea de pe trotuare poate arde pernuțele. Folosiți balsam special și nu tundeți blana prea scurt, deoarece aceasta are rol de izolare termică.",
            "extra_text": "După fiecare plimbare, spală pernuțele cu apă călduță pentru a elimina chimicalele de pe stradă."
        },
        {
            "titlu": "🐱 Spa pentru pisici?",
            "teaser": "Tot ce trebuie să știi despre grooming-ul felin...",
            "img": "https://images.unsplash.com/photo-1548247416-ec66f4900b2e?w=400",
            "text": "Pisicile sunt animale curate, dar de-shedding-ul profesional ajută la eliminarea ghemotoacelor de blană și reduce căderea părului în casă.",
            "extra_text": "O pisică periată profesional va avea mult mai puține probleme cu 'hairballs'."
        },
        {
            "titlu": "🍗 Nutriția și Blana",
            "teaser": "Cum influențează dieta aspectul estetic...",
            "img": "https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400",
            "text": "O blană mată poate indica lipsa de acizi grași Omega-3. Uleiul de somon și dietele echilibrate fac minuni pentru strălucire.",
            "extra_text": "Hidratarea este la fel de importantă ca mâncarea pentru elasticitatea pielii."
        },
        {
            "titlu": "🛁 Prima băiță a puiului",
            "teaser": "Ghid pentru o experiență fără traume...",
            "img": "https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?w=400",
            "text": "Socializarea cu apa și sunetul uscătorului trebuie făcută treptat. Noi folosim metode de 'Positive Reinforcement' pentru puiuți.",
            "extra_text": "Recomandăm prima vizită la salon la vârsta de 3-4 luni, după schema completă de vaccinare."
        },
        {
            "titlu": "🌿 Aromaterapia canină",
            "teaser": "Beneficiile lavandei în timpul tunsului...",
            "img": "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=400",
            "text": "Uleiurile esențiale sigure pot calma un câine anxios. În salonul nostru folosim difuzoare cu arome special create pentru relaxare.",
            "extra_text": "Niciodată nu folosi uleiuri esențiale direct pe blană fără diluare profesională!"
        },
        {
            "titlu": "✂️ De ce să nu radem blana?",
            "teaser": "Mitul tunsului 'la piele' vara...",
            "img": "https://images.unsplash.com/photo-1514984879728-be0aff75a6e8?w=400",
            "text": "Blana are rol izolator și protejează împotriva arsurilor solare. Tunsul excesiv poate distruge textura firului de păr pe viață.",
            "extra_text": "Câinii cu blană dublă (ca Husky sau Golden) nu trebuie rași NICIODATĂ."
        }
    ]

    col1, col2 = st.columns(2)
    for i, art in enumerate(articole):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            st.markdown(f"""
            <div class="premium-card">
                <img src="{art['img']}" style="width:100%; border-radius:15px; margin-bottom:15px;">
                <h4>{art['titlu']}</h4>
                <p>{art['teaser']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Citește Articolul", key=f"blog_btn_{i}"):
                read_article(art) 


elif menu == "⭐ Feedback":
    st.header("⭐ Feedback & Localizare")
    
    if st.session_state.get('form_done', False):
        st.balloons()
        st.success("✅ Mulțumim! Mesajul tău a fost trimis.")
        st.session_state.form_done = False

    col_form, col_map = st.columns([1, 1.2], gap="large")

    with col_form:
        st.subheader("Părerea ta")
        with st.form("feedback_form", clear_on_submit=True):
            nume = st.text_input("Nume Stăpân")
            mesaj = st.text_area("Mesaj / Review")
            rating = st.select_slider("Rating", 
                                    options=["🐶", "🐶🐶", "🐶🐶🐶", "🐶🐶🐶🐶", "🐶🐶🐶🐶🐶"], 
                                    value="🐶🐶🐶🐶🐶")
            
            submit_button = st.form_submit_button("Trimite Review")
            
            if submit_button:
                if nume and mesaj:
                    st.session_state.form_done = True
                    st.rerun() 
                else:
                    st.warning("Te rugăm să completezi toate câmpurile!")

    with col_map:
        st.subheader("📍 Ne găsești aici")
        st.info("🏠 Adresă: Str. Exemplului Nr. 4, Sector 4, București")
        
        map_data = pd.DataFrame({'lat': [44.40], 'lon': [26.11]})
        st.map(map_data, use_container_width=True)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #888;'>Blăniță Răsfățată | Premium Pet Spa | București, Sector 4</div>", unsafe_allow_html=True)