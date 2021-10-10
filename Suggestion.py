import unittest

def generateSubstrings(str1:str,k:int):
    if k == 0 or len(str1)<1:
        return [] # choix de design, au lieu de retourner une liste de n strings vides, je prefere retourner une liste vide

    res = [str1[i:i+k] for i in range(len(str1)-k+1)] # si une chaine est plus long que la chaine que l'on cherche alors on va générer toutes ses sous chaines de meme longueurs que la chaine cherchée
    return res

def hammingDistance(str1:str,str2:str): # la hamming distance est le nombre de remplacements de lettre à effectuer pour transformer le mot m1 de longueur n en le mot m2 de longueur n
    dist = 0
    if len(str1) != len(str2):
        raise ValueError("2 strings must be of the same length")
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            dist +=1
    return dist

def getSuggestions(str1:str ,suggestions : list ,number: int):
    if number> len(suggestions):
        raise ValueError("can't print more elements than the number of suggestions")
    if len(suggestions) < 1 or len(str1) < 1 or number <=0:
        return []
    res = []
    for suggestion in suggestions:
        if len(suggestion)>len(str1):
            subStrings = generateSubstrings(suggestion,len(str1)) # on va générer toutes les sous chaines de meme longueur que le mot cherché
            dists = [hammingDistance(str1,substr) for substr in subStrings] # on calcule la distance de chacune des sous chaines
            # on a désormais une liste des sous chaines et une liste des distances, on pourrait faire un dictionnaire pour optimiser la recherche mais comme on est intéréssés que par la sous chaine avec la distance minimale
            # on va se contenter de prendre l'index de la plus petite
            # nous allons utiliser des paires pour stocker le resultat avec (chaine,distance)
            distMin = min(dists)
            idxMin = dists.index(distMin) 
            res.append((suggestion,distMin))
        elif len(suggestion)<len(str1):
            continue # suggestion plus courte que le mot cherché, on passe
        else:
            dist = hammingDistance(suggestion,str1)
            res.append((suggestion,dist))
    res = sorted(res, key=lambda x: (x[1],x[0])) # on trie notre liste en se basant sur la distance puis sur le mot (donc alphabétique)
    print(res)
    return [x[0] for x in res][:number] # On recupere le nombre de mots désirés


class testGenerateSubstrings(unittest.TestCase):
    def test_generateSubstringsSuccess(self):
        actual = generateSubstrings("aggressif",3)
        expected = ["agg","ggr","gre","res","ess","ssi","sif"]
        self.assertEqual(actual,expected)
    def test_generateSubstringsLength0(self):
        actual = generateSubstrings("aggressif",0)
        expected = []
        self.assertEqual(actual,expected)
    def test_generateSubstringsNoWord(self):
        actual = generateSubstrings("",3)
        expected = []
        self.assertEqual(actual,expected)
class testHammingDistance(unittest.TestCase):
    def test_hammingDistanceSuccess(self):
        actual = hammingDistance("gros","gras")
        expected = 1
        self.assertEqual(actual,expected)
    def test_hammingDistanceLengthMismatch(self):
        with self.assertRaises(ValueError):
            actual = hammingDistance("gros","aggressif")
class test_getSuggestions(unittest.TestCase):
    def test_getSuggestionsSuccess(self):
        actual = getSuggestions("gros",["gros","gras","graisse","aggressif","go","aaaaaros","ros","gro"],2)
        expected = ["gros","aaaaaros"]
        self.assertEqual(actual,expected)
    def test_getSuggestionsParamError(self):
        actual = getSuggestions("",[],0)
        expected = []
        self.assertEqual(actual,expected)
    def test_getSuggestionsExceptionNumber(self):
        with self.assertRaises(ValueError):
            actual = getSuggestions("gros",["gras","gros"],5)
        
if __name__ == '__main__':
    unittest.main()      

# print(getSuggestions("gros",["gros","gras","graisse","aggressif","go","aaaaaros","ros","gro"],2))
# print(getSuggestions("",["gros","gras","123456"],1))
# print(getSuggestions("",[],10))
# print(getSuggestions("gros",["grosgrosgros","grasgrasgras","1235"],2))
# print(getSuggestions("gros",["12345","1235"],2))




            


            
