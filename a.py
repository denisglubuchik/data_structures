def gcdOfStrings(str1: str, str2: str) -> str:
    small = min(str1, str2)
    for i in range(len(small)):
        pref = small[:len(small)-i]
        if len(str1) % len(pref) == 0 and len(str2) % len(pref) == 0:
            n1 = len(str1) // len(pref)
            n2 = len(str2) // len(pref)
            if str1 == pref * n1 and str2 == pref * n2:
                return pref
    return ""

print(gcdOfStrings('ABCABC', 'ABC'))