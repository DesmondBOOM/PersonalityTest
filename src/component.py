from questions import sections, question_list
import streamlit as st


def display_in_section():
    for section in sections:
        section.generate()
        st.write(f"{section.calculate()}")


def display_in_random():
    for index, question in enumerate(question_list):
        question.generate(index)


def button_to_display():
    clicked = st.button("Submitted")
    if clicked:
        sections.sort(key=lambda section: section.calculate(), reverse=True)
        for section in sections[:3]:
            st.write(f"{section.title} Score: {section.calculate()}")
