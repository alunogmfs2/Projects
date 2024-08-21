novo = 0
        y_novo = 0.16 * y
    elif r < 0.86:
        # 2
        x_novo = 0.85 * x + 0.04 * y
        y_novo = -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        # 3
        x_novo = 0.2 * x + -0.26 * y
        y_novo = 0.23 * x + 0.22 * y + 1.6
    else:
        # 4
        x_novo = -0.15 * x + 0.28 * y
        y_novo = 0.26 * x + 0.24 * y + 0.44
