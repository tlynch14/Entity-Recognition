import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble


class TestNerClient(unittest.TestCase):

    def test_get_entities_returns_dictionary_given_empty_string_causes_empty_spacy_doc_entities(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_entities([])
        ner = NamedEntityClient(model)
        entities = ner.get_entities("")
        self.assertIsInstance(entities, dict)

    def test_get_entities_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_entities(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_entities([])
        ner = NamedEntityClient(model)
        entities = ner.get_entities("Madison is a city in Wisconsin")
        self.assertIsInstance(entities, dict)

    def test_get_entities_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble('eng')
        doc_entities = [{'text': 'Laurent Fressinet', 'label_': 'PERSON'}]
        model.returns_doc_entities(doc_entities)
        ner = NamedEntityClient(model)
        result = ner.get_entities('...')
        expected_result = {
            'entities': [{'entity': 'Laurent Fressinet', 'label': 'Person'}], 'html': ""}
        self.assertListEqual(result['entities'], expected_result['entities'])
