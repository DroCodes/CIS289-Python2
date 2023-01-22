import re

search_string = "“I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.” – Frank Herbert, Dune"

contains_f = re.findall(r"\b\w*[f]\w*\b", search_string, flags=re.IGNORECASE)
starts_with_f = re.findall(r"\b[f]\w+", search_string, flags=re.IGNORECASE)
find_not = re.findall(r"\bnot\b", search_string, flags=re.IGNORECASE)
substitute_i = re.sub(r"\bi\b", "You", search_string, flags=re.IGNORECASE)
substitute_me = re.sub(r"\bmy\b", "your", substitute_i, flags=re.IGNORECASE)
updated_search_string = re.sub(r"\bme\b", "you", substitute_me, flags=re.IGNORECASE)

print(contains_f)
print(starts_with_f)
print(find_not)
print(updated_search_string)