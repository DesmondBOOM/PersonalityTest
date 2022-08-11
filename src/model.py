from dataclasses import dataclass, field

import streamlit as st

tag_to_index = {'Strongly Disagree': 1, 'Disagree': 2, 'Neutral': 3, 'Agree': 4, 'Strongly Agree': 5}


@dataclass
class Question:
    question: str
    key: str = ""

    def generate(self, question_index: int):
        st.radio(
            label=f"{question_index + 1}. {self.question}",
            index=2,
            options=['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'],
            key=self.key,
        )


@dataclass
class Section:
    title: str
    questions: list[Question]
    keywords: list[str] = field(default_factory=list)

    def __post_init__(self):
        for question_index, section_question in enumerate(self.questions):
            key = f"{self.title} {question_index}"
            self.keywords.append(key)
            section_question.key = key

    def generate(self):
        st.write(f"### {self.title}")
        for question_index, section_question in enumerate(self.questions):
            section_question.generate(question_index=question_index)

    def calculate(self):
        score = 0
        for key in self.keywords:
            score += tag_to_index[st.session_state[key]]
        return score
