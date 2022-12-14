def validate_locale(locale: str) -> bool:
    valid = {
        "el-GR",
        "it-IT",
        "ko-KR",
        "es-ES",
        "ja-JP",
        "zh-CN",
        "tr-TR",
        "ar-SA",
        "hu-HU",
        "pt-PT",
        "no-NO",
        "sv-SE",
        "ro-RO",
        "sk-SK",
        "uk-UA",
        "fr-CA",
        "pl-PL",
        "da-DK",
        "pt-BR",
        "de-DE",
        "ca-ES",
        "sr-SP",
        "cs-CZ",
        "fr-FR",
        "zh-TW",
        "af-ZA",
        "ru-RU",
        "he-IL",
        "nl-NL",
        "en-US",
        "en-GB",
        "fi-FI",
        "vi-VN",
    }

    return locale in valid
