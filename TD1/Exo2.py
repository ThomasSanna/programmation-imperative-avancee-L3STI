from unidecode import unidecode

def palindrome(chaine: str) -> bool:
  if " " in chaine:
    chaine = chaine.replace(" ", "").replace("'", "").replace("-", "")
  chaine = unidecode(chaine).lower()
  return chaine == chaine[::-1]

print(palindrome("élu par cette crapule"))