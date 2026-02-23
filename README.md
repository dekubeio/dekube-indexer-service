# h2c-indexer-simple-service

Service indexer for [helmfile2compose](https://github.com/helmfile2compose/helmfile2compose) — indexes K8s Service manifests and builds alias/port maps for hostname resolution and port remapping.

**The Weaver** — one of the Seven Bishops, the founding extensions of the helmfile2compose distribution.

## Type

`IndexerConverter` (priority 50)

## Kinds

- `Service`

## Note

This is a **build-time only** extension, designed to be concatenated by `build-distribution.py` into a single-file distribution. It uses internal core imports that are resolved at build time. It is **not** designed for runtime loading via `--extensions-dir`.

## Install

Listed in `distribution.json` — installed automatically when building a distribution via `h2c-manager`.
