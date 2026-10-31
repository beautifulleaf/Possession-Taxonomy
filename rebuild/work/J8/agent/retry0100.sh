cd /home/user/Possession-Taxonomy/rebuild
for i in 1 2 3 4 5 6 7 8; do
  python3 work/J8/agent/wiki0100.py work/J8/agent/t0100.txt 700 > work/J8/agent/w0100.out 2>&1
  if ! grep -q "error': 429" work/J8/agent/w0100.out; then echo done; exit 0; fi
  sleep 45
done
echo failed
