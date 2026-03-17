import streamlit as st

st.set_page_config(
    page_title="AgriFood Italia 2030 — Vota le Tendenze",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&display=swap');

/* Reset padding del main block */
.block-container { padding-top: 0 !important; max-width: 1200px; }

/* Hero */
.hero {
    background: linear-gradient(135deg, #1a3a1f 0%, #2d5a35 60%, #1a4a2a 100%);
    border-radius: 16px;
    padding: 48px 40px 36px;
    margin-bottom: 28px;
    color: white;
}
.hero h1 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2.4rem;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 12px;
    color: white;
}
.hero h1 span { color: #86efac; }
.hero p { color: rgba(255,255,255,0.75); font-size: 1rem; margin-bottom: 0; }
.hero-stats { display: flex; gap: 40px; margin-top: 28px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.15); }
.stat-val { font-family: 'Playfair Display', Georgia, serif; font-size: 2rem; font-weight: 700; color: #4ade80; line-height: 1; }
.stat-lbl { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.07em; color: rgba(255,255,255,0.55); margin-top: 4px; }
.eyebrow {
    display: inline-block;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 999px;
    padding: 4px 14px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.85);
    margin-bottom: 18px;
}

/* Trend card */
.trend-card {
    background: white;
    border-radius: 14px;
    padding: 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.07), 0 0 0 1px #E8E2D9;
    height: 100%;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: box-shadow 0.2s ease;
}
.card-top { height: 4px; }
.card-body { padding: 18px 18px 10px; flex: 1; }
.card-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 6px;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.card-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1rem;
    font-weight: 600;
    line-height: 1.35;
    color: #1A1A18;
    margin-bottom: 8px;
}
.card-desc {
    font-size: 0.82rem;
    color: #6B6560;
    line-height: 1.6;
}
.card-footer { padding: 10px 18px 16px; border-top: 1px solid #E8E2D9; margin-top: 10px; }

/* Ranking row */
.rank-row {
    background: white;
    border-radius: 10px;
    padding: 14px 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06), 0 0 0 1px #E8E2D9;
    margin-bottom: 10px;
}
.rank-num { font-family: 'Playfair Display', Georgia, serif; font-size: 1.4rem; font-weight: 700; min-width: 36px; text-align: center; color: #9C968F; }
.rank-gold   { color: #F59E0B !important; }
.rank-silver { color: #9CA3AF !important; }
.rank-bronze { color: #B45309 !important; }
.rank-title { font-family: 'Playfair Display', Georgia, serif; font-size: 0.95rem; font-weight: 600; color: #1A1A18; }
.rank-badge { font-size: 0.65rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; padding: 2px 8px; border-radius: 4px; }
.rank-bar-bg { background: #E8E2D9; border-radius: 3px; height: 6px; flex: 1; overflow: hidden; }
.rank-bar-fill { height: 100%; border-radius: 3px; }
.rank-votes { font-size: 1.2rem; font-weight: 700; min-width: 44px; text-align: right; }

/* Section header */
.section-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; }
.section-title { font-family: 'Playfair Display', Georgia, serif; font-size: 1.3rem; font-weight: 600; }
.section-count { background: #E8E2D9; color: #6B6560; border-radius: 999px; padding: 3px 12px; font-size: 0.75rem; }

/* Streamlit button overrides */
div[data-testid="stButton"] > button {
    border-radius: 999px !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    padding: 6px 16px !important;
    transition: all 0.15s ease !important;
}

/* Hide streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── DATI ────────────────────────────────────────────────────────────────────
CATEGORIES = {
    'tecnologico': {'label': 'Tecnologico', 'icon': '💡', 'color': '#2563EB', 'bg': '#EFF6FF'},
    'demografico':  {'label': 'Demografico',  'icon': '👥', 'color': '#7C3AED', 'bg': '#F5F3FF'},
    'sociale':      {'label': 'Sociale',      'icon': '🤝', 'color': '#D97706', 'bg': '#FFFBEB'},
    'ambientale':   {'label': 'Ambientale',   'icon': '🌱', 'color': '#16A34A', 'bg': '#F0FDF4'},
    'normativo':    {'label': 'Normativo',    'icon': '⚖️', 'color': '#DC2626', 'bg': '#FEF2F2'},
}

TRENDS = [
    {'id':'t01','cat':'tecnologico','title':'Agricoltura di Precisione',
     'desc':'Sensori IoT, droni e analisi satellitare per ottimizzare irrigazione, concimazione e gestione dei raccolti campo per campo, riducendo sprechi e aumentando le rese.','seed':218},
    {'id':'t02','cat':'tecnologico','title':'Intelligenza Artificiale nelle Filiere',
     'desc':'Machine learning per previsione delle rese, rilevamento precoce di malattie delle piante e ottimizzazione della logistica e della supply chain agroalimentare.','seed':195},
    {'id':'t03','cat':'tecnologico','title':'Blockchain per la Tracciabilità',
     'desc':'Registri distribuiti immutabili che certificano origine, passaggi di filiera e autenticità dei prodotti DOP e IGP italiani, contrastando le frodi alimentari.','seed':167},
    {'id':'t04','cat':'tecnologico','title':'Automazione e Robotica Agricola',
     'desc':'Robot per la raccolta selettiva, sistemi autonomi per la potatura e piattaforme automatizzate per la lavorazione in magazzino, riducendo la dipendenza da manodopera stagionale.','seed':143},
    {'id':'t05','cat':'tecnologico','title':'Vertical Farming e Indoor Ag',
     'desc':'Coltivazione in ambienti controllati multi-piano con LED spettrali, consumo idrico ridotto del 95% e produzione indipendente dalle condizioni climatiche esterne.','seed':121},
    {'id':'d01','cat':'demografico','title':'Invecchiamento della Forza Lavoro Agricola',
     'desc':'L\'età media degli agricoltori italiani supera i 60 anni. Urgono politiche per il ricambio generazionale e incentivi per l\'insediamento di giovani agricoltori.','seed':189},
    {'id':'d02','cat':'demografico','title':'Ritorno alla Terra dei Giovani',
     'desc':'Crescita del fenomeno "neo-rurali": under 35 che avviano imprese agricole innovative dopo esperienze urbane, spesso con approcci digitali e orientati alla sostenibilità.','seed':156},
    {'id':'d03','cat':'demografico','title':'Dipendenza dalla Manodopera Straniera',
     'desc':'Oltre il 35% dei lavoratori stagionali è di origine straniera. I cambiamenti nei flussi migratori e nelle normative creano rischi strutturali per la raccolta e la produzione.','seed':98},
    {'id':'s01','cat':'sociale','title':'Dieta Plant-Based e Flessitarismo',
     'desc':'Crescita a doppia cifra dei consumi di proteine vegetali e sostituti della carne. Il fenomeno impatta tutta la filiera zootecnica e crea opportunità per i legumi italiani.','seed':203},
    {'id':'s02','cat':'sociale','title':'Turismo Enogastronomico',
     'desc':'L\'agriturismo e le esperienze legate al cibo diventano leva primaria di valorizzazione del territorio e del Made in Italy, con crescita del turista "food-first".','seed':178},
    {'id':'s03','cat':'sociale','title':'Consapevolezza sull\'Origine e km0',
     'desc':'Consumatori sempre più attenti a km zero, stagionalità e acquisto diretto dal produttore tramite GAS, farmers\' market e CSA (Community Supported Agriculture).','seed':145},
    {'id':'s04','cat':'sociale','title':'Riduzione dello Spreco Alimentare',
     'desc':'Pressione sociale e normativa per ridurre il 30% di cibo sprecato nella filiera. L\'economia circolare applicata al food genera nuovi modelli di business e packaging.','seed':134},
    {'id':'a01','cat':'ambientale','title':'Siccità e Stress Idrico',
     'desc':'Riduzione delle precipitazioni e periodi siccitosi sempre più lunghi mettono a rischio interi distretti produttivi (Pianura Padana, Sud Italia), richiedendo una rivoluzione nella gestione idrica.','seed':232},
    {'id':'a02','cat':'ambientale','title':'Transizione al Biologico',
     'desc':'Il Piano d\'Azione Nazionale Bio punta al 25% di superficie biologica entro il 2027. La domanda cresce ma anche i costi di certificazione e transizione per gli agricoltori.','seed':171},
    {'id':'a03','cat':'ambientale','title':'Agroecologia e Rigenerazione del Suolo',
     'desc':'Cover cropping, no-till e rotazioni complesse per ripristinare biodiversità, carbonio del suolo e resilienza degli ecosistemi agricoli italiani.','seed':142},
    {'id':'a04','cat':'ambientale','title':'Energie Rinnovabili in Agricoltura',
     'desc':'Agrivoltaico, biogas da scarti zootecnici e comunità energetiche rurali come fonti di reddito complementare e leva per l\'indipendenza energetica del settore.','seed':119},
    {'id':'n01','cat':'normativo','title':'Farm to Fork e Green Deal Europeo',
     'desc':'La strategia europea ridefinisce obiettivi ambientali e norme di produzione con impatto diretto sui margini degli agricoltori italiani e sui costi di adeguamento della filiera.','seed':198},
    {'id':'n02','cat':'normativo','title':'Concentrazione della GDO',
     'desc':'La pressione sui prezzi da parte della grande distribuzione organizzata comprime i margini degli agricoltori, spingendo verso modelli alternativi di commercializzazione.','seed':160},
    {'id':'n03','cat':'normativo','title':'Internazionalizzazione dell\'Agroalimentare',
     'desc':'Export a 64 miliardi di euro: accordi di libero scambio, Italian sounding e nuovi mercati (Asia, USA) creano opportunità e rischi per le PMI agroalimentari italiane.','seed':133},
    {'id':'n04','cat':'normativo','title':'Novel Food e Nuove Proteine',
     'desc':'La regolamentazione UE di novel food — carne coltivata, farine di insetti, alghe, fermentazione di precisione — e il suo impatto sul settore tradizionale e le abitudini alimentari.','seed':115},
]

# ── SESSION STATE ────────────────────────────────────────────────────────────
if 'votes' not in st.session_state:
    st.session_state.votes = {t['id']: t['seed'] for t in TRENDS}
if 'user_votes' not in st.session_state:
    st.session_state.user_votes = set()
if 'view' not in st.session_state:
    st.session_state.view = 'grid'
if 'category' not in st.session_state:
    st.session_state.category = 'Tutte'

# ── HELPERS ──────────────────────────────────────────────────────────────────
def toggle_vote(trend_id):
    if trend_id in st.session_state.user_votes:
        st.session_state.user_votes.discard(trend_id)
        st.session_state.votes[trend_id] = max(0, st.session_state.votes[trend_id] - 1)
    else:
        st.session_state.user_votes.add(trend_id)
        st.session_state.votes[trend_id] += 1

def total_votes():
    return sum(st.session_state.votes.values())

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
    <div class="eyebrow">🌾 AgriFood Italia 2030</div>
    <h1>Vota le tendenze che<br><span>plasmeranno il futuro</span></h1>
    <p>Esplora e classifica i trend tecnologici, demografici, sociali, ambientali e normativi<br>
    più rilevanti per il settore agroalimentare italiano.</p>
    <div class="hero-stats">
        <div><div class="stat-val">{total_votes():,}</div><div class="stat-lbl">Voti Totali</div></div>
        <div><div class="stat-val">20</div><div class="stat-lbl">Tendenze</div></div>
        <div><div class="stat-val">5</div><div class="stat-lbl">Categorie</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGAZIONE ──────────────────────────────────────────────────────────────
col_v1, col_v2, col_spacer = st.columns([1, 1, 6])
with col_v1:
    if st.button("📊 Esplora", use_container_width=True,
                 type="primary" if st.session_state.view == 'grid' else "secondary"):
        st.session_state.view = 'grid'
        st.rerun()
with col_v2:
    if st.button("🏆 Classifica", use_container_width=True,
                 type="primary" if st.session_state.view == 'ranking' else "secondary"):
        st.session_state.view = 'ranking'
        st.rerun()

st.markdown("<div style='margin-top:8px'></div>", unsafe_allow_html=True)

# ── VISTA GRIGLIA ─────────────────────────────────────────────────────────────
if st.session_state.view == 'grid':

    # Filtro categoria
    cat_options = ['Tutte'] + [v['label'] for v in CATEGORIES.values()]
    cat_label_to_key = {v['label']: k for k, v in CATEGORIES.items()}

    st.session_state.category = st.segmented_control(
        "Categoria", cat_options,
        default=st.session_state.category,
        label_visibility="collapsed"
    )

    st.markdown("<div style='margin-top:16px'></div>", unsafe_allow_html=True)

    # Filtra tendenze
    active_cat = cat_label_to_key.get(st.session_state.category)
    filtered = [t for t in TRENDS if active_cat is None or t['cat'] == active_cat]

    title = "Tutte le Tendenze" if st.session_state.category == 'Tutte' else st.session_state.category
    n = len(filtered)
    st.markdown(f"""
    <div class="section-head">
        <span class="section-title">{title}</span>
        <span class="section-count">{n} tendenz{"a" if n==1 else "e"}</span>
    </div>""", unsafe_allow_html=True)

    # Griglia 3 colonne
    cols = st.columns(3, gap="medium")
    for i, trend in enumerate(filtered):
        cat = CATEGORIES[trend['cat']]
        voted = trend['id'] in st.session_state.user_votes
        votes = st.session_state.votes[trend['id']]

        with cols[i % 3]:
            st.markdown(f"""
            <div class="trend-card">
                <div class="card-top" style="background:{cat['color']}"></div>
                <div class="card-body">
                    <span class="card-badge" style="background:{cat['bg']};color:{cat['color']}">
                        {cat['icon']} {cat['label']}
                    </span>
                    <div class="card-title">{trend['title']}</div>
                    <div class="card-desc">{trend['desc']}</div>
                </div>
                <div class="card-footer"></div>
            </div>
            """, unsafe_allow_html=True)

            btn_label = f"✓ {votes} voti" if voted else f"▲ {votes} voti"
            if st.button(btn_label, key=f"btn_{trend['id']}",
                         type="primary" if voted else "secondary",
                         use_container_width=True):
                toggle_vote(trend['id'])
                st.rerun()

# ── VISTA CLASSIFICA ──────────────────────────────────────────────────────────
else:
    st.markdown("""
    <div class="section-head">
        <span class="section-title">Classifica per Voti</span>
        <span class="section-count">20 tendenze</span>
    </div>""", unsafe_allow_html=True)

    sorted_trends = sorted(TRENDS, key=lambda t: st.session_state.votes[t['id']], reverse=True)
    max_votes = st.session_state.votes[sorted_trends[0]['id']] if sorted_trends else 1

    for rank, trend in enumerate(sorted_trends, 1):
        cat = CATEGORIES[trend['cat']]
        votes = st.session_state.votes[trend['id']]
        pct = round((votes / max_votes) * 100)
        rank_class = {1: 'rank-gold', 2: 'rank-silver', 3: 'rank-bronze'}.get(rank, '')
        voted = trend['id'] in st.session_state.user_votes

        col_main, col_btn = st.columns([5, 1])
        with col_main:
            st.markdown(f"""
            <div class="rank-row" style="border-left: 4px solid {cat['color']}">
                <div class="rank-num {rank_class}">#{rank}</div>
                <div style="flex:1; min-width:0">
                    <div class="rank-title">{trend['title']}</div>
                    <div style="margin-top:4px">
                        <span class="rank-badge" style="background:{cat['bg']};color:{cat['color']}">
                            {cat['icon']} {cat['label']}
                        </span>
                    </div>
                </div>
                <div style="display:flex;align-items:center;gap:12px;flex-shrink:0">
                    <div style="width:120px">
                        <div class="rank-bar-bg">
                            <div class="rank-bar-fill" style="width:{pct}%;background:{cat['color']}"></div>
                        </div>
                    </div>
                    <div class="rank-votes" style="color:{cat['color']}">{votes}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_btn:
            btn_label = "✓ Votato" if voted else "▲ Vota"
            if st.button(btn_label, key=f"rank_btn_{trend['id']}",
                         type="primary" if voted else "secondary",
                         use_container_width=True):
                toggle_vote(trend['id'])
                st.rerun()

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.markdown(
    "<p style='text-align:center;font-size:0.75rem;color:#9C968F'>"
    "AgriFood Italia 2030 · "
    "<a href='https://github.com/eleonorabarelli/agrifood-trends-italia' style='color:#16A34A'>GitHub</a>"
    "</p>",
    unsafe_allow_html=True
)
