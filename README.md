# Entity-Recognition

# E-E

This project uses Spacy for Entity Recoginition and has been developed using TDD. 

`setup.py - Bundled as package`

# Tooling

# Testing 

## NamedEntityClient 

Created a NamedEntityClient callable via get_entities. Upon which we have asserted a return type of entity in a dictionary format. 

Our testing will account for a variety of use cases: 
- test_get_entities_returns_dictionary_given_empty_string_causes_empty_spacy_doc_entities
- test_get_entities_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_entities
- test_get_entities_given_spacy_PERSON_is_returned_serializes_to_Person 

All use cases rely on a test double NerModelTestDouble and a double mocked structure using DocTestDouble and intern SpanTestDouble. 

In order to break our problem down we require Doc and Span objects, both of which are mocked via DocTestDouble and SpanTestDouble respectively.