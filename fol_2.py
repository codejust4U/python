import copy
from pygraphviz import AGraph


class Term:
    def __init__(self):
        self.name = 'void'


class Const(Term):
    '''
    Const represents logical constants.
    '''

    def __init__(self, name):
        self.name = name

    def __repr__(self, level=0):
        # ret = "\t"*level+repr(self.name)+"\n"
        ret = self.name
        return ret

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if type(other) == Const:
            return self.name == other.name
        else:
            return False

    def __hash__(self):
        return self.name

    def head(self):
        return self

    def subs(self, target_var, const):
        return self

    def to_list(self):
        return [self]

    def get_ith_term(self, i):
        assert i == 0, 'Invalid ith term for constant ' + str(self)
        return self

    def all_vars(self):
        return []


class Var(Term):
    '''
    Var represents variables in first-oder logic.
    '''

    def __init__(self, name):
        self.name = name

    def __repr__(self, level=0):
        # ret = "\t"*level+repr(self.name)+"\n"
        ret = self.name
        return ret

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if type(other) == Var and self.name == other.name:
            return True
        else:
            return False

    def __hash__(self):
        return self.name

    def head(self):
        return self

    def subs(self, target_var, const):
        if self.name == target_var.name:
            return const
        else:
            return self

    def to_list(self):
        return [self]

    def get_ith_term(self, i):
        assert i == 0, 'Invalid ith term for variable ' + str(self)
        return self

    def all_vars(self):
        return [self]


class FuncSymbol():
    '''
    FuncSymbol represents function symbols in first-oder logic.
    '''

    def __init__(self, name, arity):
        self.name = name
        self.arity = arity

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.arity == other.arity


class FuncTerm(Term):
    '''
    FuncTerm represents logical terms f(t_1, ..., t_n)
    '''

    def __init__(self, func_symbol, args):
        assert func_symbol.arity == len(
            args), 'Invalid arguments for function symbol ' + func_symbol.name
        self.func_symbol = func_symbol
        self.args = args

    def __str__(self):
        s = self.func_symbol.name + '('
        for arg in self.args:
            s += arg.__str__() + ','
        s = s[0:-1]
        s += ')'
        return s

    def __repr__(self, level=0):
        return self.__str__()

    def __eq__(self, other):
        if type(other) == FuncTerm:
            for i in range(len(self.args)):
                if not self.args[i] == other.args[i]:
                    return False
            return True
        else:
            return False

    def head(self):
        return self.func_symbol

    def pre_order(self, i):
        if i == 0:
            return self.func_symbol
        else:
            return self.pre_order(i-1)

    def get_ith_symbol(self, i):
        return self.to_list()[i]

    def get_ith_term(self, i):
        index = [0]
        result = [Term()]

        def _loop(x, i):
            nonlocal index, result
            if i == index[0]:
                result[0] = x
            else:
                if type(x) == FuncTerm:
                    for term in x.args:
                        index[0] += 1
                        _loop(term, i)
        _loop(self, i)
        return result[0]

    def to_list(self):
        ls = []

        def _to_list(x):
            nonlocal ls
            if type(x) == FuncTerm:
                ls.append(x.func_symbol)
                for term in x.args:
                    _to_list(term)
            else:
                # const or var
                ls.append(x)
        _to_list(self)
        return ls

    def subs(self, target_var, const):
        self.args = [arg.subs(target_var, const) for arg in self.args]
        return self

    def all_vars(self):
        var_list = []
        for arg in self.args:
            # var_list.append(arg.all_vars())
            var_list += arg.all_vars()
        return var_list


class Predicate():
    def __init__(self, name, arity):
        self.name = name
        self.arity = arity

    def __eq__(self, other):
        if type(other) == Predicate:
            return self.name == other.name
        else:
            return False


class Atom():
    def __init__(self, pred, terms):
        assert pred.arity == len(
            terms), 'Invalid arguments for predicate symbol ' + pred.name
        self.pred = pred
        self.terms = terms
        self.neg_state = False

    def __eq__(self, other):
        if self.pred == self.pred:
            for i in range(len(self.terms)):
                if not self.terms[i] == other.terms[i]:
                    return False
            return True
        else:
            return False

    def __str__(self):
        s = self.pred.name + '('
        for arg in self.terms:
            s += arg.__str__() + ','
        s = s[0:-1]
        s += ')'
        return s

    def __repr__(self):
        return self.__str__()

    def subs(self, target_var, const):
        self.terms = [term.subs(target_var, const) for term in self.terms]

    def neg(self):
        self.neg_state = not self.neg_state

    def all_vars(self):
        var_list = []
        for term in self.terms:
            # var_list.append(term.all_vars())
            var_list += term.all_vars()
        return var_list


class EmptyAtom(Atom):
    def __init__(self):
        self.neg_state = False

    def __eq__(self, other):
        if type(other) == EmptyAtom:
            return True
        else:
            return False

    def __str__(self):
        return ''

    def __repr__(self):
        return self.__str__()

    def subs(self, target_var, const):
        return self

    def neg(self):
        return self

    def all_vars(self):
        return []


class Clause():
    '''
    Clause represents the definite clauses A <- B_1, ..., B_n.
    '''

    def __init__(self, head, body):
        self.head = head
        self.body = body

    def __str__(self):
        head_str = self.head.__str__()
        body_str = ""
        for bi in self.body:
            body_str += bi.__str__()
            body_str += ','
        body_str = body_str[0:-1]
        body_str += '.'
        return head_str + ' :- ' + body_str

    def __repr__(self):
        return self.__str__()

    def resolution(self, other):
        '''
        A resolution function between two definite clauses.
        '''
        # remove if p(x) and neg p(x)
        pos_atoms = [self.head, other.head]
        neg_atoms = self.body + other.body
        atoms_to_remove = []
        for pos_atom in pos_atoms:
            if pos_atom in neg_atoms:
                atoms_to_remove.append(pos_atom)
        resulted_clause = Clause()
        # compress same literals
        return resulted_clause

    def subs(self, target_var, const):
        if type(self.head) == Atom:
            self.head.subs(target_var, const)
        for bi in self.body:
            bi.subs(target_var, const)

    def all_vars(self):
        var_list = []
        # var_list.append(self.head.all_vars())
        var_list += self.head.all_vars()
        for bi in self.body:
            # var_list.append(bi.all_vars())
            var_list += bi.all_vars()

        def flatten(x): return [z for y in x for z in (
            flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]
        var_list = flatten(var_list)
        # remove duplication
        result = []
        for v in var_list:
            if not v in result:
                result.append(v)
        return result


class EmptyClause(Clause):
    '''
    EmptyClause represents the empty clause □.
    '''

    def __init__(self):
        self.head = []
        self.body = []

    def __str__(self):
        return '□'

    def __repr__(self):
        return '□'


class Subst():
    def __init__(self, tuples):
        self.tuples = tuples


class Refinement():
    def __init__(self, constants, func_symbols, preds):
        self.constants = constants
        self.func_symbols = func_symbols
        self.preds = preds


class Node():
    def __init__(self, label):
        """
        Create a node with the given label.
        """
        self.label = label.replace('\n', '')
        self.children = list()
        self.edge_labels = {}

    def addkid(self, node):
        """
        Add a child node to a given node.
        """
        self.children.append(node)
        # uniof of edge labels
        # self.edge_labels = {**self.edge_labels, **node.edge_labels}
        return self

    def add_edge_label(self, child, label):
        '''
        Save the edge labels.
        '''
        self.edge_labels[child] = label

    def size(self):
        """
        Return the size of tree.
        """
        if len(self.children) == 0:
            return 1
        else:
            return 1 + sum([x.size() for x in self.children])

    def to_list(self):
        """
        Encode the tree representation into a list representation.
        """
        root = self.label
        if len(self.children) > 0:
            children = [c.to_list() for c in self.children]
        else:
            children = []
        return [root, [children]]

    def max_depth(self):
        """
        Return the maximum depth of the tree.
        """
        if len(self.children) == 0:
            return 1
        else:
            child_depths = [c.max_depth() for c in self.children]
            return 1 + max(child_depths)

    def labels_set(self):
        """
        Return the set of labels in the tree.
        """
        if len(self.children) == 0:
            return {self.label}
        else:
            children_labels = set()
            for c in self.children:
                children_labels = children_labels | c.labels_set()
            return set([self.label]) | children_labels

    def edge_list(self):
        edge_list = []

        def _loop_(node, count=0):
            nonlocal edge_list
            if len(node.children) > 0:
                for c in node.children:
                    edge_list.append(
                        (str(id(node)), node.label, str(id(c)), c.label, node.edge_labels[c]))
                    _loop_(c, count+1)
        _loop_(self)
        return edge_list

    def __edge_list(self, ls=[]):
        if len(self.children) == 0:
            return ls
        else:
            # new_edges = [(self.label, c.label, self.edge_labels[c])
            #             for c in self.children]
            # return [c.edge_list(ls+new_edges) for c in self.children]
            for c in self.children:
                ls.append((self.label, c.label, self.edge_labels[c]))
                return c.edge_list(ls)
            # return flatten([c.edge_list(ls+new_edges) for c in self.children])
            # return ls + new_edges

    def visualize(self, name='lp'):
        ls = self.edge_list()

        G = AGraph(directed=True)
        for (_id, label,  next_id, next_label, edge_label) in ls:
            G.add_node(_id, label=label)
            G.add_node(next_id, label=next_label)
            G.add_edge(_id, next_id, label=edge_label)

        G.layout(prog='dot')
        G.draw(name + '.png')


class LogicProgram():
    def __init__(self, clauses, name='lp'):
        self.clauses = clauses
        self.weights = []
        self.ops = LogicOps()
        self.dummy_count = 0
        self.max_n = 10
        self.name = name

    def gen_dummy_clause(self, _clause):
        '''
        Replace all variables into dummy variables.
        '''
        clause = copy.deepcopy(_clause)
        all_vars = clause.all_vars()
        if len(all_vars) == 1 and all_vars[0] == None:
            return clause
        dummy_vars = [Var('_' + v.name + str(self.dummy_count) + '_')
                      for v in all_vars]
        theta_list = [(all_vars[i], dummy_vars[i])
                      for i in range(len(all_vars))]
        for theta in theta_list:
            clause.subs(theta[0], theta[1])

        self.dummy_count += 1
        return clause

    def build_sld_tree(self, query):
        def _loop(query_, n=0):
            if n > self.max_n:
                return Node('FAILED')

            # 現時点のサブゴールのノード
            result_node = Node(str(query_))

            # 空節の場合そのまま返す
            if type(query_) == EmptyClause:
                return result_node
            else:
                for _clause in self.clauses:
                    query = copy.deepcopy(query_)
                    clause = self.gen_dummy_clause(_clause)
                    used_clause_label = str(clause)
                    unify_flag, unifiers = self.ops.unify(
                        [clause.head, query.body[0]])
                    if not unify_flag:
                        continue
                    else:
                        # goal bodyと_clauseのヘッドと単一化可能のとき
                        for unifier in unifiers:
                            clause.subs(unifier[0], unifier[1])
                            query.subs(unifier[0], unifier[1])
                        next_goal = self.ops.resolution(query, clause)
                    # 各ルールの適用ごとにaddkid
                    next_node = _loop(next_goal, n+1)
                    result_node.addkid(next_node)
                    result_node.add_edge_label(next_node, used_clause_label)
                # 全ての枝を貼ったあとreturn
                return result_node
        return _loop(query)

    def visualize_sld_tree(self, query):
        sldtree = self.build_sld_tree(query)
        sldtree.visualize(self.name)


class LogicOps:
    def resolution(self, goal, clause):
        '''
        Resolution function for Horn clauses.
        Just remove an atom in the goal clause body from another clause body.
        '''
        # next_goal_body = [b for b in clause.body if b not in goal.body]
        # 残りのゴールと
        goal_remain_body = [b for b in goal.body if b != clause.head]
        # if len(clause.body) == 0 and len(goal_remain_body) == 0:
        #    return EmptyClause()
        if clause.body == goal_remain_body:
            return EmptyClause()
        return Clause(EmptyAtom(), goal_remain_body + clause.body)

    def get_disagree_index(self, terms):
        symbols_list = [term.to_list() for term in terms]
        n = min([len(symbols) for symbols in symbols_list])
        for i in range(n):
            ith_symbols = [symbols[i] for symbols in symbols_list]
            for j in range(len(ith_symbols)-1):
                if ith_symbols[j] != ith_symbols[j+1]:
                    return (True, i)
        # all the same terms
        return (False, 0)

    def get_disagreements(self, terms):
        disagree_flag, disagree_index = self.get_disagree_index(terms)
        if disagree_flag:
            disagree_terms = [term.get_ith_term(
                disagree_index) for term in terms]
            return disagree_flag, disagree_terms
        else:
            return disagree_flag, []

    def occur_check(self, variable, term):
        if type(term) == Const:
            return False
        elif type(term) == Var:
            return variable.name == term.name
        else:
            # func term case
            for arg in term.args:
                if self.occur_check(variable, arg):
                    return True
            return False

    def find_subs_term(self, subs_var, disagree_set):
        # find term where the var does not occur
        for term in disagree_set:
            if not self.occur_check(subs_var, term):
                return True, term
        return False, Term()

    def is_singleton(self, atoms):
        result = True
        for i in range(len(atoms)-1):
            result = result and (atoms[i] == atoms[i+1])
        return result

    def unify(self, _atoms):
        atoms = copy.deepcopy(_atoms)
        # empty set
        if len(atoms) == 0:
            return (1, [])
        # check predicates
        for i in range(len(atoms)-1):
            if atoms[i].pred != atoms[i+1].pred:
                return (0, [])

        # check all the same
        all_same_flag = True
        for i in range(len(atoms)-1):
            all_same_flag = all_same_flag and (atoms[i] == atoms[i+1])
        if all_same_flag:
            return (1, [])

        k = 0
        theta_list = []

        while(True):
            # check terms from left
            for i in range(atoms[0].pred.arity):
                # atom_1(term_1, ..., term_i, ...), ..., atom_j(term_1, ..., term_i, ...), ...
                terms_i = [atoms[j].terms[i] for j in range(len(atoms))]
                disagree_flag, disagree_set = self.get_disagreements(terms_i)
                if not disagree_flag:
                    continue
                var_list = [x for x in disagree_set if type(x) == Var]
                if len(var_list) == 0:
                    return (0, [])
                else:
                    # substitute
                    subs_var = var_list[0]
                    # find term where the var does not occur
                    subs_flag, subs_term = self.find_subs_term(
                        subs_var, disagree_set)
                    if subs_flag:
                        k += 1
                        theta_list.append((subs_var, subs_term))
                        subs_flag = True
                        for atom in atoms:
                            # UNIFICATION SUCCESS
                            atom.subs(subs_var, subs_term)
                        if self.is_singleton(atoms):
                            return (1, theta_list)
                    else:
                        # UNIFICATION FAILED
                        return (0, [])

    def find_target_clauses(self, fact, clauses):
        result = []
        for clause in clauses:
            unify_flag, unifier = self.unify([fact, clause.head])
            if unify_flag:
                result.append(clause)
        return result

    def inference(self, fact, clauses):
        target_clauses = self.find_target_clauses(fact, clauses)
        return target_clauses


class VariableGenerator():
    def __init__(self, base_name='x'):
        self.counter = 0
        self.base_name = base_name

    def generate(self):
        generated_var = Var(self.base_name + str(self.counter))
        self.counter += 1
        return generated_var


class Language():
    def __init__(self, preds, funcs, consts, max_n=3):
        self.preds = preds
        self.funcs = funcs
        self.consts = consts
        self.var_gen = VariableGenerator()
        self.max_n = max_n

    def refinement(self, clause):
        '''
        Define the ideal refinement operators by following operations:
        1. z/f(x_1, ..., x_n) for every variable in C and every n-ary function symbol f in the language
        2. z/a for every variable z in C and every constant a in the language
        3. z/x for every distinct variables x and z in C
        4. C \cup P(x_1, ..., x_n) for every predicate P
        '''
        refined_clauses = []
        if len(clause.head.all_vars()) == 0:
            return []

        for z in clause.all_vars():
            for f in self.funcs:
                clause1 = copy.deepcopy(clause)
                new_vars = [self.var_gen.generate() for v in range(f.arity)]
                func_term = FuncTerm(f, new_vars)
                clause1.subs(z, func_term)
                refined_clauses.append(clause1)

        for z in clause.all_vars():
            for a in self.consts:
                clause1 = copy.deepcopy(clause)
                clause1.subs(z, a)
                refined_clauses.append(clause1)

        for p in self.preds:
            clause1 = copy.deepcopy(clause)
            new_vars = [self.var_gen.generate() for v in range(p.arity)]
            new_atom = Atom(p, new_vars)
            clause1.body.append(new_atom)
            refined_clauses.append(clause1)

        return refined_clauses

    def linear_refinement(self, clause):
        # TODO: linear refinement
        return clause

    def build_refinement_graph(self, clause):
        def _loop(clause, n=0):
            print(clause)
            if n > self.max_n:
                return Node(str(clause))
            result_node = Node(str(clause))
            refined_clauses = self.refinement(clause)
            for rc in refined_clauses:
                next_node = _loop(rc, n+1)
                result_node.addkid(next_node)
                result_node.add_edge_label(next_node, "")
            return result_node
        return _loop(clause)