
class IpaSym:

    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    @staticmethod
    def VC_checker(word):
        for i in word:
            if isinstance(i, Consonant):
                print("'{}' is a consonant".format(i.symbol))
            else:
                print("'{}' is a vowel".format(i.symbol))

    @staticmethod
    def mop_syllabification(word):
        all_syllables = []
        syllable = ""
        for el in word:
            if isinstance(el, Consonant):
                syllable += el.symbol
            else:
                syllable += el.symbol
                all_syllables.append(syllable)
                syllable = ""
        last_syll = all_syllables[-1]
        num = -1
        cons_to_add = ""
        while num >= -5:
            if not isinstance(word[num], Consonant):
                cons_to_add = cons_to_add[::-1]
                last_syll += cons_to_add
                all_syllables[-1] = last_syll
                break
            else:
                cons_to_add += word[num].symbol
            num -= 1
        return all_syllables

    @staticmethod
    def word_initial_check(syllables):

        three_c_clusters = ["spl", "spr", "str", "skr", "skw"]
        two_c_clusters = ["sm", "sn", "st", "sw", "sk", "sl", "sp", "sf", "θw",
                          "dw", "tw", "θr", "dr", "tr", "kw", "kr", "kl", "pr",
                          "fr", "br", "gr", "pl", "fl", "bl", "gl", "ʃr"]

        vowels = "iɪeæəʌɚuɔʊɑ"
        syl_num = len(syllables)
        for j in range(1, syl_num):
            sound_num = len(syllables[j])
            syllable = syllables[j]
            cluster = ""
            for k in range(sound_num):
                if syllable[k] in vowels:
                    break
                else:
                    cluster += syllable[k]
            if cluster not in three_c_clusters and cluster != "":
                syllables[j-1] += cluster[0]
                syllables[j] = syllable[1:sound_num]
        print(syllables)


class Consonant(IpaSym):

    def __init__(self, symbol, value):
        super().__init__(symbol, value)

    @staticmethod
    def sonority_checker(ch1, ch2):
        return ch1.value > ch2.value


# ___Vowels___
ch_001 = IpaSym("i", 8)
ch_002 = IpaSym("ɪ", 8)
ch_003 = IpaSym("e", 8)
ch_004 = IpaSym("æ", 8)
ch_005 = IpaSym("ə", 0)
ch_006 = IpaSym("ʌ", 8)
ch_007 = IpaSym("ɚ", 8)
ch_008 = IpaSym("u", 8)
ch_009 = IpaSym("ɔ", 8)
ch_010 = IpaSym("ʊ", 8)
ch_011 = IpaSym("ɑ", 8)
# ___Consonants___
ch_01 = Consonant("p", 1)
ch_02 = Consonant("b", 1)
ch_03 = Consonant("t", 1)
ch_04 = Consonant("d", 1)
ch_05 = Consonant("k", 1)
ch_06 = Consonant("g", 1)
ch_07 = Consonant("ʔ", 1)
ch_08 = Consonant("ʧ", 2)
ch_09 = Consonant("ʤ", 2)
ch_10 = Consonant("f", 3)
ch_11 = Consonant("v", 3)
ch_12 = Consonant("θ", 3)
ch_13 = Consonant("ð", 3)
ch_14 = Consonant("s", 3)
ch_15 = Consonant("z", 3)
ch_16 = Consonant("ʃ", 3)
ch_17 = Consonant("ʒ", 3)
ch_18 = Consonant("m", 4)
ch_19 = Consonant("n", 4)
ch_20 = Consonant("ŋ", 4)
ch_21 = Consonant("r", 5)
ch_22 = Consonant("l", 5)
ch_23 = Consonant("ɾ", 6)
ch_24 = Consonant("w", 7)
ch_25 = Consonant("j", 7)


# example -> word: impartial
w_list_1 = [ch_002, ch_18, ch_01, ch_011, ch_21, ch_16, ch_005, ch_22]
# example -> word: install
w_list_2 = [ch_002, ch_19, ch_14, ch_03, ch_011, ch_22, ch_22]
# example -> word: destruction
w_list_3 = [ch_04, ch_002, ch_14, ch_03, ch_21, ch_006, ch_05, ch_16, ch_005, ch_19]
# example -> word: pastry
w_list_4 = [ch_01, ch_003, ch_001, ch_14, ch_03, ch_21, ch_001]



list_of_words = [w_list_1, w_list_2, w_list_3, w_list_4]

for word in list_of_words:
    syll_list = IpaSym.mop_syllabification(word)
    print(syll_list)
    IpaSym.word_initial_check(syll_list)


"""

vowel > glide > flap > liquid > nasal > fricative > affricate > plosive

plosive = "pbtdkgʔ"
nasal = "mnŋ"
tap_flap = "ɾ"
fricative = "fvθðszʃʒ"
liquid = "ɹl"
glide = "wj"
affricate = "ʧʤ"

"""