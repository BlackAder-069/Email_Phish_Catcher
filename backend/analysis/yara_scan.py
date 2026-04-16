import yara

YARA_RULES_PATH = "../yara_rules/rules.yar"

def yara_match(text):
    rules = yara.compile(YARA_RULES_PATH)
    matches = rules.match(data=text)
    return [match.rule for match in matches]