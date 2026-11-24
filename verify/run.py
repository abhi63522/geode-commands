import glob, json, os, re, subprocess, sys, tempfile

NAME = sys.argv[1]
BASE = dict(os.environ, TERM="xterm", LC_ALL="C")


def sh(cmd, cwd, env=BASE, limit=2000):
    try:
        p = subprocess.run(["bash", "-c", cmd], cwd=cwd, env=env, text=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30)
        return p.stdout.strip()[:limit], p.returncode
    except Exception as ex:
        return "ERROR %s" % ex, 1


def flags(text):
    return set(re.findall(r"(?<![\w-])(--?[A-Za-z][\w-]*)", text))


def bind_tmux(b):
    d = tempfile.mkdtemp()
    env = dict(BASE, HOME=d, TMUX_TMPDIR=d)
    out, _ = sh("tmux new-session -d -s k && tmux list-keys; tmux kill-server", d, env)
    pat = r"-T\s+prefix\s+" + re.escape(b["key"]) + r"\s+" + re.escape(b["action"])
    return "ok" if re.search(pat, out) else "missing"


_ks = []


def kitty_sources():
    if not _ks:
        for root in ("/usr/lib", "/usr/lib64", "/usr/share", "/opt"):
            for dp, _, fs in os.walk(root):
                if "kitty" in dp:
                    _ks.extend(os.path.join(dp, f) for f in fs
                               if f in ("definition.py", "config_data.py", "config.py"))
    return _ks


def bind_kitty(b):
    files = kitty_sources()
    if not files:
        return "no-source"
    act = re.compile(r"\b" + re.escape(b["action"]) + r"\b")
    keys = [re.compile(r"(?<![\w+])" + re.escape(k) + r"(?!\w)") for k in b["keys"]]
    for f in files:
        for line in open(f, errors="ignore"):
            l = line.lower()
            if act.search(l) and any(k.search(l) for k in keys):
                return "ok"
    return "missing"


result = {"distro": NAME, "versions": {}, "entries": {}, "flags": {}}
for f in sorted(glob.glob("entries/*.json")):
    t = json.load(open(f))
    tool = t["tool"]
    v = sh(t["version_cmd"], ".")[0]
    result["versions"][tool] = v.splitlines()[0] if v else ""
    if t.get("flag_help"):
        real = flags(sh(t["flag_help"], ".", BASE, 10**6)[0])
        doc = set()
        for e in t["entries"]:
            for a in e.get("args", []):
                doc |= flags(a["flag"])
        result["flags"][tool] = {"bad": sorted(doc - real), "uncovered": sorted(real - doc)}
    for e in t["entries"]:
        r = {}
        if e.get("run"):
            d = tempfile.mkdtemp()
            env = dict(BASE, HOME=d, TMUX_TMPDIR=d)
            out, rc = sh(e.get("setup", "") + "\n" + e["run"], d, env)
            sh("tmux kill-server", d, env)
            r["out"], r["rc"] = out, rc
            r["status"] = ("pass" if out == e["expect"] else "FAIL") if "expect" in e else "recorded"
        b = e.get("bind")
        if b:
            r["bind"] = bind_tmux(b) if b["app"] == "tmux" else bind_kitty(b)
        result["entries"][e["id"]] = r

os.makedirs("out", exist_ok=True)
json.dump(result, open("out/%s.json" % NAME, "w"), indent=1)
print("done", NAME)
