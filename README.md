# h2c-indexer-service

Service indexer for [helmfile2compose](https://github.com/helmfile2compose/helmfile2compose) — indexes K8s Service manifests and builds alias/port maps for hostname resolution and port remapping.

**The Weaver** — one of the Eight Monks, the founding extensions of the helmfile2compose distribution.

> Heresy level: 2/10 — reads the maps others consult, names the names others invoke.

## Type

`IndexerConverter` (priority 50)

## Kinds

- `Service`

## Install

Via [h2c-manager](https://github.com/helmfile2compose/h2c-manager):

```sh
python3 h2c-manager.py service-indexer
```

Or listed in `distribution.json` — installed automatically when building a distribution.
