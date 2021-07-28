class NerModelTestDouble:
    """
    Test double for spaCy NLP model
    """

    def __init__(self, model):
        self.model = model

    def returns_doc_entities(self, entities):
        self.entities = entities

    def __call__(self, sentence):
        return DocTestDouble(sentence, self.entities)


class DocTestDouble:
    """
    Test double for spaCy Doc
    """

    def __init__(self, sentence, entities):
        self.entities = [SpanTestDouble(entity['text'], entity['label_'])
                         for entity in entities]

    def patch_method(self, attr, return_value):
        def patched(): return return_value
        setattr(self, attr, patched)
        return self


class SpanTestDouble:
    """
    Test double for spaCy Span
    """

    def __init__(self, text, label):
        self.text = text
        self.label_ = label
