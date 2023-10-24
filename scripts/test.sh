gcc -shared -o build/structs.so src/c/structs.c

python3 -m pytest
