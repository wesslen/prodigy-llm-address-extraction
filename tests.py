import spacy
import pytest

@pytest.fixture(scope='module')
def nlp():
    path_to_package = 'packages/en_address_extraction-0.2.0/en_address_extraction/en_address_extraction-0.2.0'

    # Load the spaCy model from the local package
    nlp = spacy.load(path_to_package)
    return nlp

def test_ner_1(nlp):
    # Define the test text
    text = "Ryan lives at 234 Nuthatch Ct in Charlotte."

    # Process the text with the NER component
    doc = nlp(text)

    # Check the named entities
    assert any(entity.label_ == 'STREET_NUM' and entity.text == '234' for entity in doc.ents)
    assert any(entity.label_ == 'STREET' and entity.text == 'Nuthatch Ct' for entity in doc.ents)
    assert any(entity.label_ == 'CITY' and entity.text == 'Charlotte' for entity in doc.ents)


def test_ner_article_1(nlp):
    # Define the test text
    text = "Authorities are investigating a fire that broke out on 3874 Cedar Road in \
    Townsville, Ohio. The incident, which occurred in the zip code 45678, has raised \
    concerns about fire safety in the area. Fortunately, no injuries were reported \
    during the incident."

    # Process the text with the NER component
    doc = nlp(text)

    # Check the named entities
    assert any(entity.label_ == 'STREET_NUM' and entity.text == '3874' for entity in doc.ents)
    assert any(entity.label_ == 'STREET' and entity.text == 'Cedar Road' for entity in doc.ents)
    assert any(entity.label_ == 'CITY' and entity.text == 'Townsville' for entity in doc.ents)
    assert any(entity.label_ == 'STATE' and entity.text == 'Ohio' for entity in doc.ents)
    #assert any(entity.label_ == 'ZIP' and entity.text == '45678' for entity in doc.ents)


def test_ner_marketing_1(nlp):
    # Define the test text
    text = "Discover luxury living at its finest! Our exquisite condominium is situated at 2468 \
    Oak Lane, #957 in Villageville, Florida. Don't miss out on the upscale amenities and breathtaking \
    views offered by this address."

    # Process the text with the NER component
    doc = nlp(text)

    # Check the named entities
    assert any(entity.label_ == 'STREET_NUM' and entity.text == '2468' for entity in doc.ents)
    assert any(entity.label_ == 'STREET' and entity.text == 'Oak Lane' for entity in doc.ents)
    assert any(entity.label_ == 'CITY' and entity.text == 'Villageville' for entity in doc.ents)
    assert any(entity.label_ == 'STATE' and entity.text == 'Florida' for entity in doc.ents)
    #assert any(entity.label_ == 'STREET_EXT' and entity.text == '#957' for entity in doc.ents)


def test_ner_legal_2(nlp):
    # Define the test text
    text = "By the power vested in me as an attorney, I hereby certify that the document executed \
    at 9876 Willow Lane, Office 7A, Riverside, IL (78901) is a true and accurate representation of \
    the parties' agreement."

    # Process the text with the NER component
    doc = nlp(text)

    # Check the named entities
    assert any(entity.label_ == 'STREET_NUM' and entity.text == '9876' for entity in doc.ents)
    assert any(entity.label_ == 'STREET' and entity.text == 'Willow Lane' for entity in doc.ents)
    assert any(entity.label_ == 'CITY' and entity.text == 'Riverside' for entity in doc.ents)
    assert any(entity.label_ == 'STATE' and entity.text == 'IL' for entity in doc.ents)
    #assert any(entity.label_ == 'STREET_EXT' and entity.text == 'Office 7A' for entity in doc.ents)
    #assert any(entity.label_ == 'ZIP' and entity.text == '78901' for entity in doc.ents)
