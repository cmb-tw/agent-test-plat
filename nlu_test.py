import streamlit as st
from tabs.nlu_test_cases import nlu_test_cases_tab
from tabs.add_nlu_case import add_nlu_case_tab


def nlu_test_page():
    tabs = st.tabs(["运行NLU测试", "编辑NLU测试用例"])

    with tabs[0]:
        nlu_test_cases_tab()

    with tabs[1]:
        add_nlu_case_tab()