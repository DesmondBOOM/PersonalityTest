import streamlit as st

from questions import sections, question_list


def display_in_section():
    for section in sections:
        section.generate()
        st.write(f"{section.calculate()}")


def display_in_random():
    for index, question in enumerate(question_list):
        question.generate(index)
    st.write("## 结果")
    sections.sort(key=lambda section: section.calculate(), reverse=True)
    for section in sections[:3]:
        st.write(f"{section.title} Score: {section.calculate()}")


st.title('荣格的十二人格原型测验')

# display_in_section()
display_in_random()
