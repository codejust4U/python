class AlphaBeta:
    def __init__(self, game_tree):
        self.game_tree = game_tree
        self.root = game_tree.root

    def alpha_beta_search(self, node):
        best_val = self.max_value(node, float('-inf'), float('inf'))
        best_state = None
        for state in self.getSuccessors(node):
            if self.min_value(state, float('-inf'), float('inf')) == best_val:
                best_state = state
                break
        print("AlphaBeta: Utility Value of Root Node: = " + str(best_val))
        print("AlphaBeta: Best State is: " + best_state.Name)
        return best_state

    def max_value(self, node, alpha, beta):
        if self.isTerminal(node):
            return self.getUtility(node)
        value = float('-inf')
        for state in self.getSuccessors(node):
            value = max(value, self.min_value(state, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    def min_value(self, node, alpha, beta):
        if self.isTerminal(node):
            return self.getUtility(node)
        value = float('inf')
        for state in self.getSuccessors(node):
            value = min(value, self.max_value(state, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

    def getSuccessors(self, node):
        assert node is not None
        return node.children

    def isTerminal(self, node):
        assert node is not None
        return len(node.children) == 0

    def getUtility(self, node):
        assert node is not None
        return node.value
