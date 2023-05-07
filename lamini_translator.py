from llama import LLM, Type, Context
import random


class TranslatedText(Type):
    source_language: str = Context("a word representing the language type of the source text, this word also needs to be in the target language")
    translation: str = Context("translated text")


class TextToBeTranslated(Type):
    text: str = Context("a line of text in any language")
    target_language: str = Context("target language type for the translated text; if this field is empty, pick a random target language")


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


class LlaminiTranslator(LLM):
    def __init__(self):
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


def main():
    translator = LlaminiTranslator()
    # rand_text = translator.random_text()
    # rand_lang = translator.random_language()
    text = "Emmmm, test, test, hello, anybody home?"
    translation = translator.translate(text, "日本語")


if __name__ == '__main__':
    main()
