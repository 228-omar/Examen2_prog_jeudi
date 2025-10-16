import pytest
from debogage_mot_long import mot_plus_long, pourcentage_mots_max  # Remplacer par le nom de ton fichier

# ============================
# Tests pour mot_plus_long
# ============================
# TODO: Tests unitaires pour la fonction mot_plus_long (maximum 5 différents)
@pytest.mark.parametrize("n1, n2, n3, n4 ,resultat_attendu",[
    ["chat", "chien","éléphant","oiseau"], "éléphant",
    ["éléphant","oiseau", "souris", "chien"], "éléphant", "éléphant",
    ["chat","chien","éléphant","hippopotame"], "hippopotame",
    ["hippopotame", 42, None, "oiseau"], "hippopotame",
    [42, None, True, 12], TypeError,
])
def test_mot_plus_long(n1, n2, n3 , n4 ,resultat_attendu):
    #arrange

    #act
    resultat = mot_plus_long(n1, n2)

    #assert

    assert resultat == resultat_attendu

# Tests pour pourcentage_mots_max
# ============================
def test_pourcentage_mots_max_normal():
    mots = ["poney", "girafe", "hippopotame", "chaton"]
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat == 75.0

def test_pourcentage_mots_max_tous_superieur():
    """
    Lorsque tous les mots présents dépassent la taille,
    le pourcentage retourné est 100%.
    """
    # TODO: Complèter ce test unitaire.
    assert False

def test_pourcentage_mots_max_elements_invalides():
    mots = ["pamplemousse", 42, "cacahuète", None]
    resultat = pourcentage_mots_max(mots, 8)

    assert resultat == 100.0

def test_pourcentage_mots_max_liste_vide():
    mots = []
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat is None

def test_pourcentage_mots_max_tous_inferieur():
    """
    Lorsque tous les mots présents sont
    plus petits que la taille, le pourcentage
    retourné est 0.0%.
    """
    # TODO: Ajouter le cas de test correspondant à la description
    #       au plan de tests et complèter ce test unitaire.
    assert False

def test_pourcentage_mots_max_tous_inferieur():
    mots = 7
    resultat = pourcentage_mots_max(mots, 3)

    assert resultat == None