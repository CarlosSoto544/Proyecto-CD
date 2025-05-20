import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import sumar

def test_suma_correcta():
    assert sumar(2, 3) == 5
