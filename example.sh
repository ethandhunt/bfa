clear
set +x
printf './main.py'
read
./main.py
printf './main.py flags'
read
./main.py flags
printf './main.py compile prog.bf prog -xr --verbose'
read
./main.py compile prog.bf prog -xr --verbose
