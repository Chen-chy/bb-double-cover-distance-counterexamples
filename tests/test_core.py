import unittest
from bbcover import BBCode, cubic_interval, get_example, names, validate_double_cover
from bbcover.gf2 import bits, from_support, rank, solve


class GF2Tests(unittest.TestCase):
    def test_rank_and_solve(self):
        self.assertEqual(rank([0b11, 0b110, 0b101]), 2)
        self.assertEqual(solve([0b11, 0b110], 0b101), 0b11)
        self.assertIsNone(solve([0b11, 0b110], 0b1))
        self.assertEqual(solve([], 0), 0)
        self.assertEqual(list(bits(0b1010)), [1, 3])
        self.assertEqual(from_support([1, 1, 3]), 8)

    def test_invalid_vectors(self):
        for fun in (lambda: list(bits(-1)), lambda: rank([-2]), lambda: solve([1], -1)):
            with self.assertRaises(ValueError): fun()


class ExampleTests(unittest.TestCase):
    def test_parameters_witnesses_and_commutation(self):
        for name in names():
            with self.subTest(name=name):
                c, w, d = get_example(name)
                self.assertEqual([c.n, c.k, w.bit_count()], d["parameters"])
                self.assertTrue(c.is_logical(w))
                self.assertTrue(c.is_connected())
                for b in c.boundary_columns:
                    self.assertEqual(c.syndrome(b), 0)
                self.assertEqual(rank(c.hx_rows), c.order - c.k//2)
                self.assertEqual(rank(c.hz_rows), c.order - c.k//2)
                self.assertTrue(all(v.bit_count() == 3 for v in c.syndrome_columns))
                self.assertTrue(all(v.bit_count() == 6 for v in c.hx_rows + c.hz_rows))

    def test_inversion_swap(self):
        for name in names():
            c, w, _ = get_example(name)
            j = c.inversion_swap(w)
            self.assertEqual(c.inversion_swap(j), w)
            self.assertEqual(j.bit_count(), w.bit_count())
            self.assertTrue(all((row & j).bit_count() % 2 == 0 for row in c.hz_rows))
            self.assertIsNone(solve(c.hx_rows, j))

    def test_cover_neighborhoods(self):
        c0, _, _ = get_example("q39")
        c1, _, _ = get_example("q78")
        c2, _, _ = get_example("q78x2")
        self.assertEqual(validate_double_cover(c0, c1)["vertices_checked"], 312)
        self.assertEqual(validate_double_cover(c1, c2)["vertices_checked"], 624)
        with self.assertRaises(ValueError): validate_double_cover(c0, c2)

    def test_transfer_kills_weight_six_logical(self):
        c0, w0, _ = get_example("q39")
        c1, _, _ = get_example("q78")
        left = w0 & ((1 << c0.order) - 1)
        right = w0 >> c0.order
        transferred = (left ^ (left << 39)) | ((right ^ (right << 39)) << 78)
        self.assertEqual(transferred.bit_count(), 12)
        h = c1.boundary_preimage(transferred)
        self.assertIsNotNone(h)
        self.assertEqual(c1.boundary(h), transferred)

    def test_new_kernel_sector_projects_to_boundary(self):
        base, _, _ = get_example("q78")
        cover, w, _ = get_example("q78x2")
        projected = 0
        for q in bits(w):
            block, pos = divmod(q, cover.order)
            i, j = divmod(pos, cover.m)
            projected ^= 1 << (block * base.order + base.index((i, j)))
        self.assertEqual(projected.bit_count(), 12)
        self.assertIsNotNone(base.boundary_preimage(projected))
        self.assertTrue(cover.is_logical(w))

    def test_collapsed_checks_are_rejected(self):
        with self.assertRaises(ValueError):
            BBCode(2, 1, ((0, 0), (1, 0), (2, 0)), ((0, 0), (1, 0), (0, 1)))
        with self.assertRaises(ValueError): get_example("unknown")


class BoundTests(unittest.TestCase):
    def test_examples(self):
        b = cubic_interval(6, 78, k=4, k2=4)
        self.assertEqual((b.lower, b.upper), (2, 78))
        b = cubic_interval(14, 156, k=4, k2=8)
        self.assertEqual((b.lower, b.upper), (2, 28))
        self.assertTrue(b.full_dimension_transfer_used)

    def test_integer_rounding(self):
        for d in list(range(2, 10000, 2)) + [10**30, 10**100]:
            b = cubic_interval(d)
            self.assertEqual(b.lower % 2, 0)
            self.assertGreaterEqual(4*b.lower**3, d)
            self.assertTrue(b.lower == 2 or 4*(b.lower-2)**3 < d)
            self.assertEqual(b.upper, 8*d**3)

    def test_invalid_bounds(self):
        for kw in ({"d": 3}, {"d": 0}, {"d": 6, "n": 10},
                   {"d": 6, "k": 4}, {"d": 6, "k": 4, "k2": 10}):
            with self.assertRaises(ValueError): cubic_interval(**kw)


if __name__ == "__main__":
    unittest.main()
