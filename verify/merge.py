import datetime, glob, json

D = {}
for f in sorted(glob.glob("out/*.json")):
    d = json.load(open(f))
    D[d["distro"]] = d
names = list(D)
tools, meta = [], {}
for f in sorted(glob.glob("entries/*.json")):
    t = json.load(open(f))
    tools.append(t)
    for e in t["entries"]:
        meta[e["id"]] = (t["tool"], e)

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
res = {"generated": now, "distros": names,
       "versions": {n: D[n]["versions"] for n in names},
       "flags": {n: D[n]["flags"] for n in names},
       "entries": {i: {n: D[n]["entries"].get(i) for n in names} for i in meta}}
json.dump(res, open("verify/results.json", "w"), indent=1)

L = ["# Verify report", "", "generated " + now, "", "## Versions", "",
     "| tool | " + " | ".join(names) + " |", "|---|" + "---|" * len(names)]
for t in tools:
    L.append("| %s | %s |" % (t["tool"], " | ".join(D[n]["versions"].get(t["tool"], "-") or "MISSING" for n in names)))
L += ["", "## Flag check", ""]
for t in tools:
    tl = t["tool"]
    have = [n for n in names if tl in D[n]["flags"]]
    if not have:
        continue
    bad = {n: D[n]["flags"][tl]["bad"] for n in have if D[n]["flags"][tl]["bad"]}
    unc = set.intersection(*[set(D[n]["flags"][tl]["uncovered"]) for n in have])
    L.append("- %s documented but not in --help: %s" % (tl, bad or "none"))
    L.append("- %s real flags not covered yet: %s" % (tl, " ".join(sorted(unc)) or "none"))
L += ["", "## Entries"]
for i, (tool, e) in meta.items():
    rs = {n: D[n]["entries"].get(i, {}) for n in names}
    ok = all(r.get("status") != "FAIL" and r.get("bind", "ok") == "ok" for r in rs.values())
    L += ["", "### %s %s `%s` (%s)" % ("OK" if ok else "CHECK", e["cmd"], i, e["level"])]
    if e.get("bind"):
        L.append("- binding: " + ", ".join("%s=%s" % (n, rs[n].get("bind", "?")) for n in names))
        if any(rs[n].get("bind") != "ok" for n in names):
            for n in names:
                if rs[n].get("bind_seen"):
                    L.append("  - %s saw: %s" % (n, " / ".join(rs[n]["bind_seen"])))
    if e.get("run"):
        g = {}
        for n in names:
            g.setdefault(rs[n].get("out"), []).append(n)
        L.append("- output same on all %d distros" % len(names) if len(g) == 1 else "- OUTPUT DIFFERS")
        for o, ns in g.items():
            L += ["", "on " + ", ".join(ns) + ":", "```", str(o), "```"]
open("verify/REPORT.md", "w").write("\n".join(L) + "\n")
print("report written")
