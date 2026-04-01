import sympy as sp


def get_equations():
    z1, z2, z3, t1, t2, t3 = sp.symbols("z1 z2 z3 t1 t2 t3")
    # équation de g avec la méthode de la chute libre
    g_fall = (2 / (1000 * (t3 - t2))) * (
        ((z1 - z3) / (t1 - t3)) - ((z1 - z2) / (t1 - t2))
    )

    # Define symbols
    lcp, lm, ti, tf = sp.symbols("lcp lm ti tf")
    pi = sp.pi
    # équation de g avec la méthode du pendule
    g_pendulum = 4 * (pi**2) * (lcp + lm / 2) / (1000 * ((tf - ti) ** 2))
    return (g_fall, g_pendulum)


def get_sensitivity(expression):
    """
    Calcule automatiquement les facteurs de pondération (theta_i) pour une expression donnée
    """
    # Identifier toutes les variables libres (z1, t1, L, etc.)
    variables = expression.free_symbols

    # Calculer la dérivée partielle pour chaque variable trouvée
    thetas = {var: sp.diff(expression, var) for var in variables}

    return thetas
