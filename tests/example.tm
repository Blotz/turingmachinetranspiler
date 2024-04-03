// example program "hello world"
INIT          _ = 104, print, print_hello1;
print_hello1  _ = 101, print, print_hello2;
print_hello2  _ = 108, print, print_hello3;
print_hello3  _ = 108, print, print_hello4;
print_hello4  _ = 111, print, print_hello5;
print_hello5  _ = 32,  print, print_hello6;
print_hello6  _ = 119, print, print_hello7;
print_hello7  _ = 111, print, print_hello8;
print_hello8  _ = 114, print, print_hello9;
print_hello9  _ = 108, print, print_hello10;
print_hello10 _ = 100, print, HALT;

// example program adder
INIT _ = _, none, setup_adder1;

// write the input values to tape
setup_adder1 _ = 0, right, setup_adder1;
setup_adder2 _ = 1, left, lhs_adder;

// start adder 
lhs_adder 0 = 0, right, rhs_adder_0;
lhs_adder 1 = 1, right, lhs_adder_1;
rhs_adder_0 0 = 0, print, HALT;
rhs_adder_0 1 = 1, print, HALT;
rhs_adder_1 0 = 1, print, HALT;
rhs_adder_1 1 = 2, print, HALT;

// for loop
INIT _ = _, none, loop_marker;

loop_marker _ = 255, right, loop_setup;
loop_setup  _  = 10, none, loop_inner_start;

// pointer is pointing at loop mem
is_zero 0  = 0, none, HALT;
is_zero _  = _, none, decrement_1;

// Ideally this would go from 255-0
// pointer is pointing at loop mem
decrement 10 = 9, none, loop_inner_start;
decrement 9  = 8, none, loop_inner_start;
decrement 8  = 7, none, loop_inner_start;
decrement 7  = 6, none, loop_inner_start;
decrement 6  = 5, none, loop_inner_start;
decrement 5  = 4, none, loop_inner_start;
decrement 4  = 3, none, loop_inner_start;
decrement 3  = 2, none, loop_inner_start;
decrement 2  = 1, none, loop_inner_start;
decrement 1  = 0, none, loop_inner_start;

// pointer is pointing at loop memory. 
// to avoid issues, we move right
loop_inner_start    _ = _, right, print_hello;

// inner loop code memory from here -> right free
// 255 is reserved for loop marker
print_hello   _ = 104, print, print_hello1;
print_hello1  _ = 101, print, print_hello2;
print_hello2  _ = 108, print, print_hello3;
print_hello3  _ = 108, print, print_hello4;
print_hello4  _ = 111, print, print_hello5;
print_hello5  _ = 32,  print, print_hello6;
print_hello6  _ = 119, print, print_hello7;
print_hello7  _ = 111, print, print_hello8;
print_hello8  _ = 114, print, print_hello9;
print_hello9  _ = 108, print, print_hello10;
print_hello10 _ = 100, print, loop_inner_end;

// clean up inner
loop_inner_end _ = _, none, go_to_loop_mem;

// go to memory where we store the number of loops
go_to_loop_mem 255 = 255, right, is_zero;
go_to_loop_mem _   = _, left, go_to_loop_mem;
