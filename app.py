import streamlit as st
from generate_essay import generate_essay


st.set_page_config(
    page_title="AI Essay Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;800&display=swap');

body { font-family: 'Inter', sans-serif; background-color: #F8FAFC; }

.main-title {
    font-family: 'Outfit', sans-serif;
    font-size: 46px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(135deg, #3B82F6, #8B5CF6, #EC4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 40px;
}

.section-title {
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: #1E293B;
    margin-bottom: 15px;
}

.content {
    font-family: 'Inter', sans-serif;
    font-size: 17px;
    line-height: 1.85;
    color: #334155;
}

.block {
    padding: 30px;
    border-radius: 20px;
    background: rgba(255,255,255,0.9);
    border: 1px solid rgba(226,232,240,0.8);
    box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05);
    margin-bottom: 30px;
    transition: all 0.3s ease;
}

.block:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 40px -15px rgba(0,0,0,0.1);
}

/* ─── IMAGE GRID ─────────────────────────────────────────────── */
/*
   We bypass st.image() entirely and render raw HTML <img> tags.
   This gives us full CSS control over height and object-fit.
*/

.img-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;   /* always 2 equal columns   */
    gap: 16px;
    margin: 24px 0 32px;
}

.img-grid-item {
    width: 100%;
    height: 300px;                     /* ← fixed, equal height     */
    border-radius: 16px;
    overflow: hidden;                  /* clip anything outside box */
    box-shadow: 0 10px 25px -5px rgba(0,0,0,0.15);
    transition: transform 0.3s ease;
}

.img-grid-item:hover { transform: scale(1.02); }

.img-grid-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;                 /* fill box, crop symmetrically */
    object-position: center;
    display: block;
}

/* single image (odd count last row) → centre it, half width */
.img-grid-single {
    display: flex;
    justify-content: center;
    margin: 24px 0 32px;
}

.img-grid-single .img-grid-item {
    width: 50%;
}

/* Sidebar */
[data-testid="stSidebar"] { background-color: #0F172A !important; }
[data-testid="stSidebar"] * { color: #F1F5F9 !important; }
[data-testid="stSidebar"] h1 {
    font-family: 'Outfit', sans-serif;
    background: linear-gradient(135deg, #38BDF8, #818CF8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>
""", unsafe_allow_html=True)


# ── helpers ──────────────────────────────────────────────────────────────────

def image_grid_html(urls: list[str]) -> str:
    """
    Build a pure-HTML image grid from a list of URLs.
    Uses object-fit: cover so every image is exactly 300px tall
    regardless of its original aspect ratio. No st.image() involved.
    """
    if not urls:
        return ""

    # Split into pairs
    rows = [urls[i:i+2] for i in range(0, len(urls), 2)]
    html_parts = []

    for pair in rows:
        if len(pair) == 2:
            # Two equal columns
            html_parts.append('<div class="img-grid">')
            for url in pair:
                html_parts.append(
                    f'<div class="img-grid-item">'
                    f'<img src="{url}" loading="lazy" alt="essay image">'
                    f'</div>'
                )
            html_parts.append('</div>')
        else:
            # Single image — centre at half width
            html_parts.append('<div class="img-grid-single">')
            html_parts.append(
                f'<div class="img-grid-item">'
                f'<img src="{url}" loading="lazy" alt="essay image">'    # noqa
                f'</div>'
            )
            html_parts.append('</div>')

    return "\n".join(html_parts)


# ── app ───────────────────────────────────────────────────────────────────────

st.title("AI Essay Generator")

topic = st.text_input("Enter topic", "Palestine and Palestinian rights")

if st.button("Generate Essay"):

    with st.spinner("Generating essay... (Please wait about 20–30 seconds)"):
        try:
            final_data = generate_essay(topic)

            # Title
            st.markdown(
                f"<div class='main-title'>{final_data['title']}</div>",
                unsafe_allow_html=True
            )

            # ── Collect images ────────────────────────────────────────────
            all_images = []
            for section in final_data["sections"]:
                if section.get("image_urls"):
                    all_images.extend(section["image_urls"])
                elif section.get("image_url"):
                    all_images.append(section["image_url"])

            # ── Render image grid (pure HTML — no st.image()) ─────────────
            if all_images:
                st.markdown(image_grid_html(all_images), unsafe_allow_html=True)

            # ── Sidebar ───────────────────────────────────────────────────
            st.sidebar.title("📚 Sections")
            for i, section in enumerate(final_data["sections"]):
                st.sidebar.write(f"{i+1}. {section['heading']}")

            # ── Essay sections ────────────────────────────────────────────
            for section in final_data["sections"]:
                st.markdown(
                    f"""
                    <div class='block'>
                        <div class='section-title'>{section['heading']}</div>
                        <div class='content'>{section['content']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.error("⚠️ An error occurred during essay generation.")
            if any(k in str(e) for k in ("RESOURCE_EXHAUSTED", "429", "rate limit")):
                st.warning("🔄 Rate limit hit. Wait 15–30 s and try again.")
            else:
                st.exception(e)