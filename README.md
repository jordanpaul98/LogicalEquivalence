# LogicalEquivalence
Logical Equivalence class comparator. See if two string representation of logic equation equally match truth tables

<pre>
  logic equivalent class
    input a string and number of logical inputs of type a, b, c, d, ...

    use the == or != comparison between two Logic classes to test if two
    logical strings are equivalent

    at the moment only works for AND and OR strings without (). ideally for k_maps
    AND: Nothing between inputs Ex. abc, bc, de
    OR: +
    NOT: ! or ~ (before input) !a, ~a, a!b, a~b

    isSame = Logic(2, 'a!b + !ab') == Logic(2, 'b!a + !ba')

    or use Logic.equivalence(logic_str_a, logic_str_b) -> bool
</pre>


<pre>
  OUTPUT of test()


  Test case: logic_a='ab!cd+abc+!ad' logic_b='abc+bd+d!a'
  logic a & b equivalent? True
  
  logic_a truth table:
  
  d c b a | out
  _____________ 
  
  0 0 0 0 | 0
  0 0 0 1 | 0
  0 0 1 1 | 0
  0 0 1 0 | 0
  0 1 0 0 | 0
  0 1 0 1 | 0
  0 1 1 1 | 1
  0 1 1 0 | 0
  1 0 0 0 | 1
  1 0 0 1 | 0
  1 0 1 1 | 1
  1 0 1 0 | 1
  1 1 0 0 | 1
  1 1 0 1 | 0
  1 1 1 1 | 1
  1 1 1 0 | 1
  
  
  logic_b truth table:
  
  d c b a | out
  _____________ 
  
  0 0 0 0 | 0
  0 0 0 1 | 0
  0 0 1 1 | 0
  0 0 1 0 | 0
  0 1 0 0 | 0
  0 1 0 1 | 0
  0 1 1 1 | 1
  0 1 1 0 | 0
  1 0 0 0 | 1
  1 0 0 1 | 0
  1 0 1 1 | 1
  1 0 1 0 | 1
  1 1 0 0 | 1
  1 1 0 1 | 0
  1 1 1 1 | 1
  1 1 1 0 | 1

</pre>
