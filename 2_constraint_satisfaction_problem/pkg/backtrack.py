from pkg.eightqueens import EightQueens


def backtrack(csp, state, domains):
    
    csp = EightQueens()
    state_copy = state    
    
    if csp.heuristic == 0:
        return 1
    
    for row in state:
        if row == -1:
            for col in domains[row]:
                if csp.is_consistent(row, col):
                    state[row] = col
                    if inferences(row, col, domains, csp.size):
                        backtrack()


def inferences(row, col, domains, size):
    
    backup_domains = domains
    
    for r in range(row + 1, size):
        to_remove = []
        for c in domains[r]:
            if c == col or abs(row - r) == abs(col - c):
                to_remove.append(c)
        for c in to_remove:
            domains[r].remove(c)
        if not domains[r]:
            domain = backup_domains
            return False
    return True