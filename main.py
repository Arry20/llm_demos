from utils import generate_script
import streamlit as st

st.title("视频脚本生成器")
with st.sidebar:
    openai_api_key=st.text_input("请输入openai API密钥:",type="password")
    st.markdown("[获取OpenAI密钥](https://api.aigc369.com/v1)")
subject=st.text_input("请输入视频主题")
length=st.number_input("请输入视频的大致市场(单位:分钟)",max_value=150.0,min_value=1.0,step=0.1)
creativity=st.slider("请输入视频的创造力",min_value=0.0,max_value=1.2,value=0.2,step=0.1)
submit=st.button("提交")
if submit and not openai_api_key:
    st.info("请输入你的OPENAI API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit and not length>=0.2:
    st.info("视频长度需大于或等于0.1")
    st.stop()
if submit:
    with st.spinner("AI正在思考中,请稍等..."):
        search_result,title,script=generate_script(subject,length,creativity,openai_api_key)
    st.success("视频脚本已经生成!")
    st.subheader("标题:")
    st.write(title)
    st.subheader("视频脚本:")
    st.write(script)
    with st.expander("维基百科搜索结果:"):
        st.info(search_result)
