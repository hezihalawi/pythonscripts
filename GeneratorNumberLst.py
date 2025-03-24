class GeneratorNumberLsrt:
    @staticmethod
    def non_forbidden_lst(min_bound,max_bound,forbidden_elements):
        all_num=set(list(range(min_bound,max_bound)))
        all_num.difference_update(forbidden_elements)
        return all_num

    @staticmethod
    def random_element_from_lst(lst):
        n= len(lst)
        index=randint(0,n-1)
        return lst[index]
    @staticmethod
    def randomPoly(P,deg,bounded_coef_lst,has_free=True):
        deg_coef=[GeneratorNumberLsrt.random_element_from_lst(bounded_coef_lst) for i in list(range(deg))]
        deg_coef.insert(0,GeneratorNumberLsrt.random_element_from_lst(bounded_coef_lst))
        deg_coef[deg]=randint(1, max(bounded_coef_lst))
        return P(deg_coef)

