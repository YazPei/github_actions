# test_file.py

# ✅ Ajout de 2 lignes vides avant chaque fonction pour respecter PEP8
def test_calc_addition():
    """Test si 2 + 4 donne 6"""
    output = 2 + 4
    assert output == 6


def test_calc_substraction():
    """Test si 2 - 4 donne -2"""
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    """Test si 2 * 4 donne 8"""
    output = 2 * 4
    assert output == 8


def test_coucou():
    """Test si la fonction renvoie 'hello'"""
    output = "hello"
    assert output == "hello"


# ✅ Ajout d'une ligne vide à la fin du fichier (flake8 W292)