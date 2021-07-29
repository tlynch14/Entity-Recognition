
class NamedEntityClient:

    # NEC Abstracted - see app.py
    def __init__(self, model):
        self.model = model

    def get_entities(self, sentence):
        doc = self.model(sentence)
        entities = [{'entity': entity.text, 'label': self.map_label(entity.label_)}
                    for entity in doc.entities]
        return {'entities': entities, 'html': ''}
        # doc = self.model(sentence)

    @staticmethod
    def map_label(label):
        label_map = {
            'PERSON': 'Person',
            'NORP': 'Group',
            'LOC': 'Location',
            'GPE': 'Location',
            'LANGUAGE': 'Language'
        }

        return label_map.get(label)
