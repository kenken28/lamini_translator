from llama import LLM, Type, Context


class TranslatedText(Type):
    source_language: str = Context("a word representing the language type of the source text, this word also needs to be in the target language")
    translated_text: str = Context("translated text")


class TextToBeTranslated(Type):
    source_text: str = Context("a line of text in any language")
    target_language: str = Context("target language type for the translated text")


def main():
    translator_llm = LLM(name="translator")

    input_text = TextToBeTranslated(
        source_text="Emmmm, test, test, hello, anybody home?",
        target_language="日本語",
    )
    translated_text = translator_llm(input=input_text, output_type=TranslatedText)

    if '\n' in translated_text.source_language:
        idx = translated_text.source_language.find('\n')
        translated_text.source_language = translated_text.source_language[:idx]
    print(translated_text)


if __name__ == '__main__':
    main()
