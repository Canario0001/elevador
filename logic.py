# m → massa 
# a → aceleração
# p → peso
# n → normal
# g → gravidade

err = 'Não foi possível encontrar'

def s1(m, a, p, n, g):
    a = 0

    if not p:
        try:
            p = float(n)
        except (ValueError, TypeError):
            try:
                p = m * g
            except (ValueError, TypeError):
                p = err

    if not n:
        try:
            n = float(p)
        except (ValueError, TypeError):
            try:
                n = m * g
            except (ValueError, TypeError):
                n = err
    
    if not m:
        try:
            m = p / g
        except (ValueError, TypeError):
            try:
                m = n / g
            except (ValueError, TypeError):
                m = err
    if not g:
        try:
            g = p / m
        except (ValueError, TypeError):
            try:
                g = n / m
            except (ValueError, TypeError):
                g = err

    result = {
        'm': m,
        'a': a,
        'p': p,
        'n': n,
        'g': g
    }

    return result

def s2(m, a, p, n, g):
    if not m:
        try: 
            m = (n - p) / a
        except (ValueError, TypeError):
            try:
                m = p / g
            except (ValueError, TypeError):
                m = err

    if not n:
        try:
            n = p + m * a
        except (ValueError, TypeError):
            try:
                n = m * g + m * a
            except (ValueError, TypeError):
                n = err

    if not p:
        try:
            p = m * g
        except (ValueError, TypeError):
            try:
                p = n - m * a
            except (ValueError, TypeError):
                p = err
    
    if not g:
        try:
            g = p / m
        except (ValueError, TypeError):
            g = err

    if not a:
        try:
            a = (n - p) / m
        except (ValueError, TypeError):
            a = err

    result = {
        'm': m,
        'a': a,
        'p': p,
        'n': n,
        'g': g
    }

    return result

def s3(m, a, p, n, g):
    if not m:
        try:
            m = - ((n - p) / a)
        except (ValueError, TypeError):
            m = p / g

    if not n:
        try:
            n = p - m * a
        except (ValueError, TypeError):
            try:
                n = m * g - m * a
            except (ValueError, TypeError):
                n = err

    if not p: 
        try:
            p = n + m * a
        except (ValueError, TypeError):
            try:
                p = m * g
            except (ValueError, TypeError):
                p = err

    if not g: 
        try:
            g = p / m 
        except (ValueError, TypeError):
            g = err

    if not a:
        try:
            a = - ((n - p) / m)
        except (ValueError, TypeError):
            a = err
    
    result = {
        'm': m,
        'a': a,
        'p': p,
        'n': n,
        'g': g
    }

    return result

def s4(m, a, p, n, g):
    result = s2(m, a, p, n, g)

    return result

def s5(m, a, p, n, g):
    n = 0

    if not g:
        try:
            g = float(a)
        except (ValueError, TypeError):
            try:
                g = p / m
            except (ValueError, TypeError):
                g = err
    
    if not a:
        try:
            a = float(g)
        except (ValueError, TypeError):
            a = err

    if not p:
        try:
            p = m * g
        except (ValueError, TypeError):
            p = err

    if not m:
        try:
            m = p / g
        except (ValueError, TypeError):
            m = err

    result = {
        'm': m,
        'a': a,
        'p': p,
        'n': n,
        'g': g
    }

    return result
