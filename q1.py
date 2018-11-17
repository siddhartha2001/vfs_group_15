class Valid:
    def __init__(self, string):
        self.str = string
    def validity(self):
        for i in self.str:
            for j in self.str:
                if i == "(":
                    if j>i and j== ")":
                        print "valid"
                else:
                    print "invalid"


if __name__ == "__main__":
    v1 = Valid("({)")
    v2 = Valid(")(")
    print v2.validity()
