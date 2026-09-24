"""Service indexer — populates ctx.services_by_selector, ctx.alias_map, ctx.service_port_map."""

from dekube import ConverterResult, IndexerConverter, build_alias_map, build_service_port_map  # pylint: disable=import-error  # h2c resolves at runtime


class ServiceIndexer(IndexerConverter):  # pylint: disable=too-few-public-methods  # contract: one class, one method
    """Index Service manifests and build alias/port maps."""
    name = "service"
    kinds = ["Service"]

    def convert(self, _kind, manifests, ctx):
        """Index Service manifests and build alias/port maps."""
        for svc_manifest in manifests:
            svc_meta = svc_manifest.get("metadata") or {}
            svc_spec = svc_manifest.get("spec") or {}
            svc_name = svc_meta.get("name", "")
            ctx.services_by_selector[svc_name] = {
                "name": svc_name,
                "namespace": svc_meta.get("namespace") or "",
                "selector": svc_spec.get("selector") or {},
                "type": svc_spec.get("type") or "ClusterIP",
                "ports": svc_spec.get("ports") or [],
            }
        ctx.alias_map.update(build_alias_map(ctx.manifests, ctx.services_by_selector))
        ctx.service_port_map.update(
            build_service_port_map(ctx.manifests, ctx.services_by_selector))
        return ConverterResult()
