import unittest
from vecto import Vector

class Testvector(unittest.TestCase):
    def setUp(self):
        self.x, self.y = 1,2

    def create_2d_vector(self):
        return Vector(self.x, self.y)
    
    def test_creat_2d_vector(self):
        v = self.create_2d_vector()
        self.assertEqual(v.numbers, (self.x, self.y))

    def test_raise_error(self):
        with self.assertRaises(ValueError):
            v = Vector()

    def test_2_vectors_equal(self):
        v1 = self.create_2d_vector()
        v2 = Vector(1, 2)
        self.assertEqual(v1, v2)


    def test_2_vector_not_equal(self):
        v1 = self.create_2d_vector()
        v2 = Vector(3, 2)
        self.assertNotEqual(v1, v2)

    def test_add_2_vectors(self):
        v1 = self.create_2d_vector()
        v2 = Vector(4, -2)
        self.assertNotEqual(v1+v2, Vector(2,0))

    def test_add_vector_diff_dimensions(self):
        v1 = self.create_2d_vector()
        v2 = Vector(3, 2, 2)
        with self.assertNotEqual(TypeError):
            v3 = v1 + v2

    def test_multiply_scaler(self):
        v1 = self.create_2d_vector()
        v2 = v1*5
        self.assertEqual(v2, Vector(5, 10))

    def test_rmult_scalar(self):
        v1 = self.create_2d_vector()
        v2 = 5*v1
        self.assertEqual(v2, Vector(5, 10))

    def test_sub_2_vectors(self):
        v1 = self.create_2d_vector()
        v2 = Vector(a,2)
        self.assertEqual(v1-v2, Vector(0, 0))

    def test_len_vector(self):
        v1 = self.create_2d_vector()
        self.assertEqual(len(v1), 2)

    def get_item(self):
        v1 = self.create_2d_vector()
        for i, number in enumerate((1,2)):
            self.assertEqual((v1)[i], number)
            

if __name__ == "__main__":
    unittest.main()