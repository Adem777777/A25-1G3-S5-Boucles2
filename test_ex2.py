from SolutionDebug2 import retrait

def test_retrait():
    #Arrange
    solde = 1000
    montant = 500
    resultat_attendu = 500

# Act
    resultat_obtenu = retrait(solde, montant)

#Assert
    assert resultat_attendu == resultat_obtenu

def test_retrait_2():
    #Arrange
    solde = 1000
    montant = -100
    resultat_attendu = 1000

# Act
    resultat_obtenu = retrait(solde, montant)

#Assert
    assert resultat_attendu == resultat_obtenu

def test_retrait_3():
    #Arrange
    solde = 1000
    montant = 900
    resultat_attendu = 100

# Act
    resultat_obtenu = retrait(solde, montant)

#Assert
    assert resultat_attendu == resultat_obtenu

def test_retrait_4():
    #Arrange
    solde = 1000
    montant = 200
    resultat_attendu = 800

# Act
    resultat_obtenu = retrait(solde, montant)

#Assert
    assert resultat_attendu == resultat_obtenu