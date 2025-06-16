import argparse, socket, concurrent.futures, time
def scan(h,p,t=1):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.settimeout(t)
        return p if s.connect_ex((h,p))==0 else None
def main():
    a=argparse.ArgumentParser();a.add_argument("--host",required=True)
    a.add_argument("--start",type=int,required=True)
    a.add_argument("--end",type=int,required=True);x=a.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as e:
        futs={e.submit(scan,x.host,p):p for p in range(x.start,x.end+1)}
        for f in concurrent.futures.as_completed(futs):
            r=f.result();time.sleep(0.05)
            if r: print(f"{x.host}:{r} OPEN")
if __name__=="__main__":
    try: main()
    except Exception as e: print("error:",e)
