import srsly
import typer
import streamlit as st
from typing import List, Sequence, Optional, Dict, Union
import spacy
import pandas as pd

from spacy import displacy

import base64


@st.cache_resource()
def load_model(name: str) -> spacy.language.Language:
    """Load a spaCy model."""
    return spacy.load(name)


@st.cache_resource()
def process_text(model_name: str, text: str) -> spacy.tokens.Doc:
    """Process a text and create a Doc object."""
    nlp = load_model(model_name)
    return nlp(text)


def get_svg(svg: str, style: str = "", wrap: bool = True):
    """Convert an SVG to a base64-encoded image."""
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" style="{style}"/>'
    return get_html(html) if wrap else html


def get_html(html: str):
    """Convert HTML so it can be rendered."""
    WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""
    # Newlines seem to mess with the rendering
    html = html.replace("\n", " ")
    return WRAPPER.format(html)

def get_json(sample_loc: str):
    """Get sample of records"""
    examples = srsly.read_jsonl(sample_loc)
    texts = (eg["text"] for eg in examples)
    return list(texts)


def visualize_nerparser(
    doc: spacy.tokens.Doc,
) -> None:
        
        # Double newlines seem to mess with the rendering
        #displacy_options["ents"] = label_select
    html = displacy.render(
        doc,
        style="ent",
        #options=displacy_options,
        #manual=manual,
    )
    style = "<style>mark.entity { display: inline-block }</style>"
    st.write(f"{style}{get_html(html)}", unsafe_allow_html=True)


def main():
    st.title("Address extraction NER model")
    models = ["training/model-best","training/model-last"]
    default_text = "Steve lives at 124 Main Street in Phoenix, Arizona."
    
    input_model = st.sidebar.selectbox(label="Choose model", options=models)
    input_text = st.text_area(label="Input", value=default_text, height = 100)  
    doc = process_text(input_model, input_text)
    visualize_nerparser(doc)
    st.json(input_model + ".json")


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass