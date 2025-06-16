
# CYB333 Mid-Term

## Part 1 – Socket connection
```powershell
# window 1 (server)
python server.py                       # shows "Server listening …"

# window 2 (client)
python client.py "hello world"         # sent/recv demo
python client.py "should fail"         # when server is off
```

## Part 2 – Port scanner
```powershell
python scanner.py --host 127.0.0.1 --start 20 --end 25
python scanner.py --host 127.0.0.1 --start 80 --end 85
python scanner.py --host scanme.nmap.org --start 22 --end 80
```

Screenshots are stored in **tests/part1** and **tests/part2**.
