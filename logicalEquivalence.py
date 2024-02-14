""" logic equivalent class
    input a string and number of logical inputs of type a, b, c, d, ...

    use the == or != comparison between two Logic classes to test if two
    logical strings are equivalent

    at the moment only works for AND and OR strings without (). ideally for k_maps
    AND: Nothing between inputs Ex. abc, bc, de
    OR: +
    NOT: ! or ~ (before input) !a, ~a, a!b, a~b

    isSame = Logic(2, 'a!b + !ab') == Logic(2, 'b!a + !ba')

    or use Logic.equivalence(logic_str_a, logic_str_b) -> bool
"""

class Logic():

    key = ['a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm']

    @staticmethod
    def bool_gen(inputs) -> list:
        bools = []
        for i in range(2 ** inputs):
            set = [(i >> j) & 0x1 for j in range(inputs)]
            bools.append(set)
        for i in range(0, 2 ** inputs, 4):
            bools[i + 2], bools[i + 3] = bools[i + 3], bools[i + 2]
        return bools


    @staticmethod
    def logicSize(logic) -> int:
        return max(i + 1 for i, alp in enumerate(Logic.key) if alp in logic)


    @staticmethod
    def equivalence(logic_a, logic_b) -> bool:
        size = max(Logic.logicSize(logic_a),
                   Logic.logicSize(logic_b))
        return Logic(size, logic_a) == Logic(size, logic_b)


    def __init__(self, inputs, logic=None):

        self._bools = self.bool_gen(inputs)
        self._output = [int(0) for _ in range(2 ** inputs)]

        self._input_size = inputs
        self._logic = ''
        if logic is not None:
            self.logic = logic


    @property
    def logic(self):
        return self._logic


    @logic.setter
    def logic(self, logic):
        if logic == '':
            raise ValueError("logic equation cannot be empty")
        self._logic = logic
        self._logic.replace(" ", "")
        self.evaluate()


    @property
    def inputs(self):
        return len(self._bools)


    @inputs.setter
    def inputs(self, inputs):
        self._input_size = inputs
        self._bools = self.bool_gen(inputs)
        self._output = [int(0) for _ in range(2 ** inputs)]


    @property
    def outputs(self):
        return self._output


    def __eq__(self, other) -> bool:
        if isinstance(other, (list, tuple)):
            if not len(other) == len(self.outputs):
                raise ValueError(f"List size needs to match Logic output size: {len(self.outputs)}")
            return self.outputs == other
        elif not hasattr(other, 'outputs'):
            raise TypeError("Cannot compare Non-Logic objects")
        elif other.inputs != self.inputs:
            raise ValueError("Logic classes do not match in size")

        return self.outputs == other.outputs


    def __ne__(self, other) -> bool:
        return not (self == other)


    def __str__(self) -> str:
        return self._logic


    def evaluate(self):
        if self.logic == '':
            return

        def replace_at_index(input_str, index, new_substring):
            return input_str[:index] + new_substring + input_str[index + len(new_substring):]

        for out_index, bl in enumerate(self._bools):
            new_logic = self.logic

            for index, alp in enumerate(self.key[:self._input_size]):
                new_logic = new_logic.replace(alp, str(bl[index]))

            for i in range(len(new_logic) - 1):
                if new_logic[i] == '~' or new_logic[i] == '!':
                    rpl = str(int(not bool(int(new_logic[i + 1]))))
                    new_logic = replace_at_index(new_logic, i + 1, rpl)

            new_logic = new_logic.replace("~", "").replace("!", "")
            self._output[out_index] = any((not '0' in part) for part in new_logic.split("+"))


    def table(self):
        apls = self.key[:self._input_size]
        apls.reverse()
        print(" ".join(apl for apl in apls), "| out",)
        print("_"*(self._input_size*2 - 1 + 6), "\n")
        for bools, output in zip(self._bools, self.outputs):
            bools.reverse()
            print(" ".join(str(bool) for bool in bools), "|", int(output))


def test():

  logic_a = 'ab!cd+abc+!ad'
  logic_b = 'abc+bd+d!a'
  print(f"Test case: {logic_a=} {logic_b=}")
  a = Logic(4, 'ab!cd+abc+!ad')
  b = Logic(4, 'abc+bd+d!a')
  print(f"logic a & b equivalent? {a==b}")

  print("\nlogic_a truth table:\n")
  a.table()

  print("\n\nlogic_b truth table:\n")


  
  b.table()
