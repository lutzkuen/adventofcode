
import code

class ISolve:
    def __init__(self, filename):
        self.meals = []
        self.allgs = []
        self.ings = []
        with open(filename, "r") as f:
            for line in f.readlines():
                self.meals.append({
                    "ings": [l.replace(',', '').replace(' ', '') for l in line.split("(contains")[0].split(" ") if l != ""],
                    "allgs": [l.replace(',', '').replace(' ', '') for l in line.replace("\n", "").split("(contains")[1].replace(")", "").split(" ") if l != ""],
                })
                for allg in self.meals[-1]["allgs"]:
                    if allg not in self.allgs:
                        self.allgs.append(allg)
                for ing in self.meals[-1]["ings"]:
                    if ing not in self.ings:
                        self.ings.append(ing)
            print(self.meals)
            print(self.allgs)

    def find_none_allgs(self):
        self.solve_allgs()
        good_ings = []
        for ing in self.ings:
            potential_allg = False
            for aso in self.allg_solve:
                if ing in aso["ings"]:
                    potential_allg = True
            # candidates = []
            # is_first = True
            # for meal in self.meals:
            #     if ing not in meal["ings"]:
            #         continue
            #     if is_first:
            #         candidates = meal["allgs"]
            #         is_first = False
            #     else:
            #         candidates = [c for c in candidates if c in meal["allgs"]]
            if not potential_allg:
                good_ings.append(ing)
        print(good_ings)
        c = 0
        for meal in self.meals:
            c += len([_ for _ in meal["ings"] if _ in good_ings])
        return c

    def sort_by_allg(self):
        self.solve_allgs()
        sorted_allgs = sorted(self.allg_solve, key = lambda x: x["allg"])
        print(','.join([c["ings"][0] for c in sorted_allgs]))
    
    def solve_allgs(self):
        self.allg_solve = []
        for allg in self.allgs:
            is_first = True
            candidates = []
            for meal in self.meals:
                if allg in meal["allgs"]:
                    if is_first:
                        for ing in meal["ings"]:
                            candidates.append(ing)
                        is_first = False
                    else:
                        candidates = [c for c in candidates if c in meal["ings"]]
                        # to_remove = []
                        # for ing in candidates:
                        #     if ing not in meal["ings"]:
                        #         to_remove.append(ing)
                        # for rem in to_remove:
                        #     candidates.remove(rem)
            # for occu in self.allg_solve:
            #     if occu in candidates:
            #         candidates.remove(occu)
            # if len(candidates) != 1:
            #     code.interact(banner='', local=locals())
            self.allg_solve.append({"allg": allg, "ings": candidates})
        is_done = False
        while not is_done:
            is_done = True
            new_allg_solve = []
            for aso in self.allg_solve:
                if len(aso["ings"]) > 1:
                    for asi in self.allg_solve:
                        if len(aso["ings"]) == 1:
                            break
                        if len(asi["ings"]) == 1:
                            # print(aso)
                            aso["ings"] = [c for c in aso["ings"] if c not in asi["ings"]]
                            # print(aso)
                            # code.interact(banner='', local=locals())
                            is_done = False
                new_allg_solve.append(aso)
            self.allg_solve = new_allg_solve
        print(self.allg_solve)
                                

iso = ISolve("test_input.txt")
iso.sort_by_allg()
# assert iso.find_none_allgs() == 5

# iso = ISolve("input.txt")
# print(iso.find_none_allgs())
iso = ISolve("input.txt")
iso.sort_by_allg()
