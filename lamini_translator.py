from llama import LLM, Type, Context
import yaml
import collections
import random


def flatten_dict(d, parent_key='', sep='.'):
    """
    Flatten a nested dictionary
    :param d: original dictionary
    :param parent_key: key of the parent dictionary
    :param sep: delimiter
    :return: a flattened dictionary
    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def load_yaml(yaml_path):
    """
    Load a yaml config file into a flattened dictionary
    :param yaml_path: path to yaml file
    :return: a flattened dictionary
    """
    with open(yaml_path, 'r') as f:
        d = yaml.safe_load(f)
        return flatten_dict(d)


class TranslatedText(Type):
    source_language: str = Context("language type of the source text")
    translation: str = Context("translated text")


class TextToBeTranslated(Type):
    text: str = Context("a line of text in any language")
    target_language: str = Context("target language type for the translated text")


# class RandomText(Type):
#     text: str = Context("a line of text generated from the provided seed")
#
#
# class RandomLanguage(Type):
#     language: str = Context("a random language")
#
#
# class RandomSeed(Type):
#     seed: str = Context("a random seed string")


class LaminiTranslator(LLM):
    def __init__(self, config_path=None):
        if config_path is not None:
            config = load_yaml(config_path)
            super().__init__(name="translator", config=config)
        else:
            super().__init__(name="translator")

    def translate(self, text, language) -> tuple:
        """
        Translate a text using Lamini
        :param text: A line of text to be translated
        :param language: target language
        :return: A tuple of source language and translated text
        """
        input_text = TextToBeTranslated(text=text, target_language=language)
        result = self(input=input_text, output_type=TranslatedText)
        src_lang = self.remove_unexpected_str(result.source_language)
        return src_lang, result.translation

    @staticmethod
    def remove_unexpected_str(text):
        """
        Remove unexpected text from source_language string
        """
        return text[:text.find('\n')] if '\n' in text else text

    # def random_text(self) -> str:
    #     """
    #     Get a random text using Lamini
    #     :return: a random text in a random language
    #     """
    #     rand_seed = RandomSeed(seed=str(random.randrange(9999999)))
    #     return self(input=rand_seed, output_type=RandomText).text
    #
    # def random_language(self) -> str:
    #     """
    #     Get a random language using Lamini
    #     :return: a random language
    #     """
    #     rand_seed = RandomSeed(seed=str(random.randrange(9999999)))
    #     return self(input=rand_seed, output_type=RandomLanguage).language


def test_translator():
    translator = LaminiTranslator(config_path='./configure_llama.yaml')
    # rand_text = translator.random_text()
    # rand_lang = translator.random_language()
    text = 'Emmmm, test, test, hello, anybody home?'
    print(translator.translate(text, "日本語"))
