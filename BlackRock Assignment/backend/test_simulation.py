import unittest
from simulation import simulate

class TestSimulation(unittest.TestCase):

    def test_zero_iterations(self):
        """Test with zero iterations should return empty results."""
        results = simulate(x0=0, y0=0, z0=0, sigma=10.0, rho=28.0, beta=8/3, delta_t=0.01, n=0)
        self.assertEqual(len(results), 0)

    def test_one_iteration(self):
        """Test with one iteration should return initial state."""
        results = simulate(x0=0, y0=0, z0=0, sigma=10.0, rho=28.0, beta=8/3, delta_t=0.01, n=1)
        self.assertEqual(len(results), 1)
        self.assertAlmostEqual(results[0]['x'], 0)
        self.assertAlmostEqual(results[0]['y'], 0)
        self.assertAlmostEqual(results[0]['z'], 0)

    def test_negative_parameters(self):
        """Test with negative parameters should not raise errors and produce results."""
        results = simulate(x0=-1.0, y0=-1.0, z0=-1.0, sigma=-10.0, rho=-28.0, beta=-8/3, delta_t=0.01, n=10)
        self.assertEqual(len(results), 10)

    def test_large_number_of_iterations(self):
        """Test with a large number of iterations to check for performance or overflow issues."""
        results = simulate(x0=0.1, y0=0.1, z0=0.1, sigma=10.0, rho=28.0, beta=8/3, delta_t=0.01, n=10000)
        self.assertEqual(len(results), 10000)

    def test_small_delta_t(self):
        """Test with a very small delta_t to check for underflow or precision issues."""
        results = simulate(x0=1.0, y0=1.0, z0=1.0, sigma=10.0, rho=28.0, beta=8/3, delta_t=1e-6, n=10)
        self.assertEqual(len(results), 10)

    def test_large_delta_t(self):
        """Test with a large delta_t to check for stability issues."""
        results = simulate(x0=1.0, y0=1.0, z0=1.0, sigma=10.0, rho=28.0, beta=8/3, delta_t=1.0, n=10)
        self.assertEqual(len(results), 10)

    def test_edge_case_parameters(self):
        """Test with edge case parameters that are known to lead to chaotic behavior."""
        results = simulate(x0=19, y0=20, z0=50, sigma=10.0, rho=28.0, beta=8/3, delta_t=0.01, n=10)
        self.assertEqual(len(results), 10)

    def test_with_all_zero_parameters(self):
        """Test with all zero parameters should return all zeros in results."""
        results = simulate(x0=0, y0=0, z0=0, sigma=0, rho=0, beta=0, delta_t=0.01, n=10)
        for r in results:
            self.assertEqual(r['x'], 0)
            self.assertEqual(r['y'], 0)
            self.assertEqual(r['z'], 0)

    def test_with_large_parameters(self):
        """Test with very large parameters to check for overflow issues."""
        results = simulate(x0=1e6, y0=1e6, z0=1e6, sigma=1e6, rho=1e6, beta=1e6, delta_t=0.01, n=10)
        self.assertEqual(len(results), 10)

    def test_random_parameters(self):
        """Test with random parameters should not raise errors."""
        import random
        results = simulate(x0=random.random(), y0=random.random(), z0=random.random(), 
                           sigma=random.random(), rho=random.random(), beta=random.random(), 
                           delta_t=random.random(), n=10)
        self.assertEqual(len(results), 10)

if __name__ == '__main__':
    unittest.main()
