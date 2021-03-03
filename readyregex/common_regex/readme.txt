Hey Morgan -

    1. Some notes on the design:
        - The complex patterns (like PhoneNumber) should err on the side of being permissive by default 
        - This will encourage the perception that the patterns "just work"
        - Complex patterns should accept just an Options parameter
        - Options should:
            * indicate that the pattern will only match an uncommon or unusual variation (like Options.NoAreaCode)
            * indicate some global behavior of the pattern (like Options.IgnoreExtraWhitespace)
            * require that the pattern follow some specific behavior (like Options.MandatoryAreaCodeParentheses)


Based on the statistics collected here in Dec 2019, we should aim for backwards compatibility with Python 3.5 and up: https://dev.to/hugovk/python-version-share-over-time-6-1jb8

Our dependency, typeguard, requires 3.5.3+, I consider that close-enough to the 3.5+ backwards compatibility goal
Type hints were introduced in Python 3.5, and we will have to confirm that we are not using any backwards-compatibility-breaking aspects of type hints.