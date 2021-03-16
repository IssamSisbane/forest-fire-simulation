import unittest
import ForetBrule as fbt



class TestVoisinsFonction(unittest.TestCase):

    def test_voisins_bord_haut_gauche(self):
        self.assertEqual(fbt.recup_voisins(0,0), [(1,0),(0,1)])

    def test_voisins_bord_bas_gauche(self):
        self.assertEqual(fbt.recup_voisins(9,0), [(8,0),(9,1)])

    def test_voisins_bord_bas_droit(self):
        self.assertEqual(fbt.recup_voisins(9,8), [(8, 8), (9, 9), (9, 7)])

    def test_voisins_bord_haut_droit(self):
        self.assertEqual(fbt.recup_voisins(0,9), [(1,9),(0,8)])

    def test_voisin_milieu(self):
        self.assertEqual(fbt.recup_voisins(5,5), [(4, 5), (6, 5), (5, 6), (5, 4)])

    def test_voisin_milieu_haut(self):
        self.assertEqual(fbt.recup_voisins(0,5), [(1, 5), (0, 6), (0, 4)])

    def test_voisin_milieu_droit(self):
        self.assertEqual(fbt.recup_voisins(5,9), [(4, 9), (5, 8), (6, 9)])

    def test_voisin_milieu_gauche(self):
        self.assertEqual(fbt.recup_voisins(5,0), [(4, 0), (6, 0), (5, 1)])

    def test_voisin_milieu_bas(self):
        self.assertEqual(fbt.recup_voisins(9,5), [(8, 5), (9, 6), (9, 4)])

    def test_valeur_impossible(self):
        self.assertRaises(ValueError, fbt.recup_voisins, -1,-1)
        self.assertRaises(ValueError, fbt.recup_voisins, 10,10)

    def test_types_impossibles(self):
        self.assertRaises(TypeError, fbt.recup_voisins, True, True)
        self.assertRaises(TypeError, fbt.recup_voisins, "oui", "non")
    

if __name__ == '__main__':
    unittest.main()