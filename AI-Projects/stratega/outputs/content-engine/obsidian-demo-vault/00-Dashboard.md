# Dashboard

## Quick Links
- [[ICP]] - Ideal Customer Profile
- [[Sales Playbook MOC]] - Full playbook
- [[Competitor Intel]] - Market research
- [[Content Calendar]] - Publishing schedule

## Active Clients
```dataview
TABLE status, revenue, next-action
FROM "02-Clients"
WHERE status = "active"
SORT revenue DESC
```

## This Week
- [ ] Follow up [[Client - Acme Corp]]
- [ ] Update [[Pricing Strategy]] with Q4 data
- [ ] Review [[Competitor Intel]] for new entrants
- [ ] Publish [[Tool Friday Ideas|Tool Friday]]

## Recent Notes
```dataview
LIST
FROM ""
SORT file.mtime DESC
LIMIT 5
```
