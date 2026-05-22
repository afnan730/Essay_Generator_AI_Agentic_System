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

body {
    font-family: 'Inter', sans-serif;
    background-color: #F8FAFC;
}

.main-title {
    font-family: 'Outfit', sans-serif;
    font-size: 46px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(135deg, #3B82F6, #8B5CF6, #EC4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 40px;
    text-shadow: 0px 4px 20px rgba(139, 92, 246, 0.15);
}

.section-title {
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: #1E293B;
    margin-bottom: 15px;
    padding-bottom: 5px;
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
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(226, 232, 240, 0.8);
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);
    margin-bottom: 30px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.block:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.1);
    border-color: rgba(203, 213, 225, 1);
}

img {
    border-radius: 16px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

img:hover {
    transform: scale(1.03);
}

/* Custom sidebar header styles */
[data-testid="stSidebar"] {
    background-color: #0F172A !important;
}

[data-testid="stSidebar"] * {
    color: #F1F5F9 !important;
}

[data-testid="stSidebar"] h1 {
    font-family: 'Outfit', sans-serif;
    background: linear-gradient(135deg, #38BDF8, #818CF8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>
""", unsafe_allow_html=True)

st.title("AI Essay Generator")


topic = st.text_input(
    "Enter topic",
    "Palestine and Palestinian rights"
)


if st.button("Generate Essay"):

    with st.spinner("Generating essay... (Please wait about 20-30 seconds to run all agents safely)"):
        try:
            final_data = generate_essay(topic)

            st.markdown(f"<div class='main-title'>{final_data['title']}</div>", unsafe_allow_html=True)
            st.sidebar.title("📚 Sections")

            for i, section in enumerate(final_data["sections"]):
                st.sidebar.write(f"{i+1}. {section['heading']}")

            for section in final_data["sections"]:

                with st.container():

                    st.markdown("<div class='block'>", unsafe_allow_html=True)

                    # st.markdown(f"<div class='section-title'>{section['heading']}</div>", unsafe_allow_html=True)

                    col1, col2 = st.columns([1, 2])

                    with col1:
                        if section.get("image_url"):
                            st.image(section["image_url"], width=280)

                    with col2:
                        st.markdown(f"<div class='content'>{section['content']}</div>", unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error("⚠️ An error occurred during essay generation.")
            if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e) or "rate limit" in str(e).lower():
                st.warning("🔄 The API rate limit was temporarily exceeded. Please wait 15-30 seconds and click 'Generate Essay' again.")
            else:
                st.exception(e)


    

    # for section in final_data["sections"]:

    #     st.header(section["heading"])
    #     st.sidebar.title("Sections")

    #     image_url = section.get("image_url")

    #     if image_url:
    #         st.image(
    #             image_url,
    #             width=400
    #         )

    #     st.write(section["content"])

    #     st.divider()