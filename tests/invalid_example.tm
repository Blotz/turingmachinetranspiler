// example program "hello world"
INIT          _ = 104, print, print_hello1;
print_hello1  _ = 101, print, print_hello2;
print_hello2  _ = 108, print, print_hello3;
print_hello3  _ = 108, print, print_hello4;
print_hello4  _ = 111, print, print_hello5;
print_hello5  _ = 32,  print, print_hello6
print_hello6  _ = 119, print, print_hello7;
print_hello7  _ = 111, print, print_hello8;
print_hello8  _ = 114, print, print_hello9;
print_hello9  _ = 108, print, print_hello10;
print_hello10 _ = 100, print, HALT;