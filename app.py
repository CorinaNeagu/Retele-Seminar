import streamlit as st
import pandas as pd
from datetime import datetime
import time

st.set_page_config(
    page_title="Blăniță Răsfățată | Ultra Pet Spa",
    page_icon="🐾",
    layout="wide"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

@st.dialog("📖 Articol Complet")
def read_article(articol):  
    st.image(articol["img"], use_container_width=True)
    
    st.markdown(f"<h2 style='color: #FF6A88; margin-top: 0;'>{articol['titlu']}</h2>", unsafe_allow_html=True)
    
    st.write(articol["text"])
    
    if "extra_text" in articol:
        st.markdown(f"""
            <div style="background-color: #FFF0ED; padding: 15px; border-left: 5px solid #FF9A8D; border-radius: 10px; margin: 15px 0;">
                <b style="color: #FF6A88;">💡 Știai că?</b><br>
                <span style="color: #555;">{articol['extra_text']}</span>
            </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    
    st.markdown("""
        <p style='text-align: center; font-style: italic; color: #888;'>
            📍 Vizitează salonul nostru din <b>Sectorul 4</b> pentru consultanță personalizată.
        </p>
    """, unsafe_allow_html=True)

if 'form_done' not in st.session_state:
    st.session_state.form_done = False

def handle_submit():
    st.session_state.form_done = True
    st.balloons()

with st.sidebar:
    st.image("assets/logo.jpg")
    st.markdown("<h2 style='text-align: center; color: #FF9A8D; margin-bottom: 0;'>Blăniță Răsfățată</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.9rem;'>Premium Pet Spa</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown("""
        <div style="display: flex; justify-content: center; gap: 15px;">
            <a href="https://www.instagram.com/blanita_rasfatata?igsh=OG54cHVhbnRvaGts&utm_source=qr" target="_blank" style="text-decoration: none;">
                <div class="social-circle" style="background: linear-gradient(45deg, #f09433, #dc2743, #bc1888);">
                    <span style="color: white; font-size: 14px;">IG</span>
                </div>
            </a>
            <a href="https://www.facebook.com/share/1LwXqXUFs6/?mibextid=wwXIfr" target="_blank" style="text-decoration: none;">
                <div class="social-circle" style="background: #1877F2;">
                    <span style="color: white; font-size: 14px;">FB</span>
                </div>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    menu = st.radio("MENIU", 
                    ["🏠 Acasă", "✂️ Servicii & Programări", "🛍️ Pet Boutique", "🐶 Blog Păros", "⭐ Feedback"],
                    label_visibility="collapsed") 

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
        <div class="sidebar-info-box">
            <small style="color: #FF6A88; font-weight: 800;">📍 LOCAȚIE</small><br>
            <span style="color: #555; font-size: 0.9rem;">Sector 4, București</span><br><br>
            <small style="color: #FF6A88; font-weight: 800;">📞 CONTACT</small><br>
            <span style="color: #555; font-size: 0.9rem;">07xx xxx xxx</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

if menu == "🏠 Acasă":
    st.markdown('<div class="main-header"><h1>✨ BLĂNIȚĂ RĂSFĂȚATĂ</h1><p>Standardul de Aur în Estetică Canină</p></div>', unsafe_allow_html=True)
    
    col_a1, col_a2 = st.columns([1.2, 1])
    with col_a1:
        st.subheader("Bun venit în Universul Răsfățului")
        st.write("Suntem mai mult decât un salon de grooming; suntem un centru de wellness unde prietenul tău beneficiază de aromaterapie, muzică de relaxare și cele mai fine tratamente cosmetice.")
        st.markdown("""
    <div style="
        background: linear-gradient(90deg, #FF9A8D 0%, #FF6A88 100%);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0 20px 0;
        box-shadow: 0 4px 15px rgba(255, 154, 141, 0.2);
    ">
        <h2 style="color: white; margin: 0; font-size: 1.5rem;">📸 MOMENTE DE RĂSFĂȚ (Galerie)</h2>
    </div>
""", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=56nQi71MPvw")
        st.image("assets/poster.jpeg")
        st.video("https://www.youtube.com/watch?v=j4bIJrYU-lI")
        st.image("assets/trim.jpg")
        st.video("https://www.youtube.com/watch?v=TzoFVi3i1Xk&list=PLpMCdON1SI6X3TfE2z9Bq8Ws9r1OVvtxk&index=2")
    with col_a2:
        st.markdown('<div class="premium-card"><h4>📍 Sector 4 Focus</h4><p>Suntem mândri să servim comunitatea din Sectorul 4. Locația noastră este special gândită pentru acces facil și un mediu liniștit.</p></div>', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?w=500", use_container_width=True)
        st.video("https://www.youtube.com/watch?v=An8ri0pFGAs")
        st.image("assets/spa.jpg")
        st.video("https://www.youtube.com/watch?v=pGXZ0tM_XeA&list=PLpMCdON1SI6X3TfE2z9Bq8Ws9r1OVvtxk")
        st.image("assets/bath.jpg")
        st.video("https://www.youtube.com/watch?v=TX957G2o5mY&list=PLpMCdON1SI6X3TfE2z9Bq8Ws9r1OVvtxk&index=5")
        st.video("https://www.youtube.com/watch?v=tkzwXX53qQ8")

elif menu == "✂️ Servicii & Programări":
    st.header("✂️ Configurează Vizita")
    
    if 'ora_h' not in st.session_state:
        st.session_state.ora_h = "09:00"

    col_calc, col_calen = st.columns([1, 1.2], gap="large")
    
    with col_calc:
        st.subheader("🧮 Calculator Preț")
        talia = st.selectbox("Talia cățelului:", ["Mică (<10kg)", "Medie (10-25kg)", "Mare (>25kg)"])
        servicii = st.multiselect("Servicii extra:", ["Tuns Design", "Spălat Premium", "Igienă Dentară", "Tratament Keratină"])
        
        baza = {"Mică (<10kg)": 100, "Medie (10-25kg)": 150, "Mare (>25kg)": 220}
        total = baza[talia] + (len(servicii) * 40)
        
        st.markdown(f'''
            <div class="calc-box">
                <span style="color: #888; font-size: 0.9rem;">Preț Estimat</span>
                <h1 style="color: #FF9A8D; margin: 0;">{total} RON</h1>
            </div>
        ''', unsafe_allow_html=True)

    with col_calen:
        st.subheader("📅 Programare Rapidă")
        
        data = st.date_input("Ziua:", min_value=datetime.now())
        
        h, m = map(int, st.session_state.ora_h.split(':'))
        hour_angle = (h % 12) * 30 + (m * 0.5)
        minute_angle = m * 6

        st.markdown(f"""
            <div class="clock-container">
                <div class="hand hour-hand" style="transform: rotate({hour_angle}deg);"></div>
                <div class="hand minute-hand" style="transform: rotate({minute_angle}deg);"></div>
            </div>
        """, unsafe_allow_html=True)

        st.write("🕒 Alege ora disponibilă:")

        ore_disponibile = [
            "08:00", "09:00", "10:00", "11:00", 
            "12:00", "13:00", "14:00", "15:00", 
            "16:00", "17:00", "18:00", "19:00"
        ]

        nr_coloane = 4 
        rows = [ore_disponibile[i:i + nr_coloane] for i in range(0, len(ore_disponibile), nr_coloane)]

        for row in rows:
            cols = st.columns(nr_coloane)
            for i, ora_opt in enumerate(row):
                label = f"{ora_opt} ✅" if st.session_state.ora_h == ora_opt else ora_opt
                
                if cols[i].button(label, key=f"btn_{ora_opt}", use_container_width=True):
                    st.session_state.ora_h = ora_opt
                    st.rerun()

        st.markdown(f"""
            <div class="ticket-container">
                <div class="ticket-grid">
                    <div><span class="ticket-item-label">Data</span><span class="ticket-item-value">{data.strftime('%d %b')}</span></div>
                    <div class="ticket-divider"></div>
                    <div><span class="ticket-item-label">Ora</span><span class="ticket-item-value highlight-value">{st.session_state.ora_h}</span></div>
                    <div class="ticket-divider"></div>
                    <div><span class="ticket-item-label">Talie</span><span class="ticket-item-value">{talia.split()[0]}</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Finalizează Rezervarea ✨", use_container_width=True, type="primary"):
            st.balloons()
            st.success(f"Te așteptăm pe {data.strftime('%d %b')} la ora {st.session_state.ora_h}!")

elif menu == "🛍️ Pet Boutique":
    if 'cart' not in st.session_state:
        st.session_state.cart = []

    st.header("🛍️ Pet Boutique - Exclusive Collection")
    
    col_prod, col_cart = st.columns([2.5, 1], gap="small")
    with col_prod:
        pass

    with col_prod:
        produse = [
            ("Zgardă Piele 'Royal Blue'", "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=300", 120),
            ("Parfum 'Summer Paw'", "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=300", 85),
            ("Pătuț 'Cloud Nine'", "assets/pat.jpg", 250),
            ("Ham Ergonomic 'Neo'", "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=300", 145),
            ("Bol Ceramic 'Marble'", "https://images.unsplash.com/photo-1615678815958-5910c6811c25?w=300", 65),
            ("Jucărie Ansamblu Pisici", "https://images.unsplash.com/photo-1545249390-6bdfa286032f?w=300", 180),
            ("Recompense Artizanale", "https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=300", 45),
            ("Sampon Organic 'Silk'", "https://images.unsplash.com/photo-1583947581924-860bda6a26df?w=300", 95),
            ("Lese Retractabilă 'Pro'", "https://images.unsplash.com/photo-1601758124510-52d02ddb7cbd?w=300", 110),
            ("Ulei Somon Wild", "assets/ulei.jpg", 75)
        ]
        
        rows = [produse[i:i+2] for i in range(0, len(produse), 2)] 
        for row in rows:
            cols = st.columns(2)
            for i, (nume, img, pret) in enumerate(row):
                with cols[i]:
                    st.image(img, use_container_width=True)
                    st.markdown(f"""
                        <div class="premium-card" style="text-align:center;">
                            <h4 style="margin-bottom:0;">{nume}</h4>
                            <p style="color: #FF6A88; font-weight: bold; font-size: 1.2rem;">{pret} RON</p>
                        </div>
                    """, unsafe_allow_html=True)
        
                    if st.button(f"Adaugă în coș 🛒", key=f"p_{nume}"):
                        st.session_state.cart.append({"nume": nume, "pret": pret})
                        st.rerun()
    with col_cart:
        st.markdown('<div id="cart-root"></div>', unsafe_allow_html=True)
        
        with st.container():
            st.subheader("🛒 Coșul tău")
            
            if not st.session_state.cart:
                st.info("Coșul este gol momentan.")
            else:
                total_cart = sum(item['pret'] for item in st.session_state.cart)
                
                for idx, item in enumerate(st.session_state.cart):
                    c_info, c_del = st.columns([4, 1])
                    c_info.write(f"**{item['nume']}** \n{item['pret']} RON")
                    if c_del.button("❌", key=f"del_{idx}"):
                        st.session_state.cart.pop(idx)
                        st.rerun()
                
                st.divider()
                st.markdown(f"### Total: {total_cart} RON")
                
                if st.button("Finalizează Comanda 💳", use_container_width=True, type="primary"):
                    st.balloons()
                    st.success("Comanda a fost trimisă!")
                    st.session_state.cart = []
                    import time
                    time.sleep(2)
                    st.rerun()
    

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
footer_html = """
<div style="text-align: center; padding: 20px 0;">
    <div style="color: #888; font-size: 0.9rem; padding: 20px;">
            Ne puteti gasi si pe retelele de socializare:
    </div>
    <div style="display: flex; justify-content: center; gap: 15px; margin-bottom: 20px;">
        <a href="https://www.instagram.com/blanita_rasfatata?igsh=OG54cHVhbnRvaGts&utm_source=qr" target="_blank" style="text-decoration: none;">
            <div class="social-circle" style="background: linear-gradient(45deg, #f09433, #dc2743, #bc1888); width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">
                <span style="color: white; font-size: 12px; font-weight: bold;">IG</span>
            </div>
        </a>
        <a href="https://www.facebook.com/share/1LwXqXUFs6/?mibextid=wwXIfr" target="_blank" style="text-decoration: none;">
            <div class="social-circle" style="background: #1877F2; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">
                <span style="color: white; font-size: 12px; font-weight: bold;">FB</span>
            </div>
        </a>
    </div>
    <div style="color: #FF6A88; font-weight: 800; font-size: 1.2rem; margin-bottom: 5px;">✨ BLĂNIȚĂ RĂSFĂȚATĂ ✨</div>
    <div style="color: #888; font-size: 0.9rem;">
        Premium Pet Spa | București, Sector 4 <br>
        <span style="opacity: 0.7; font-size: 0.8rem;">© 2026 Toate drepturile rezervate prietenilor nostri blanosi.</span>
    </div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)