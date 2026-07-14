from pathlib import Path
import json
import re

import yaml
import networkx as nx
from networkx.readwrite import json_graph

BASE_DIR = Path(__file__).resolve().parent
TAXONOMY_DIR = BASE_DIR / "taxonomy"
OUTPUT_FILE = BASE_DIR / "graph.json"

EXCLUDED_KEYS = {"items", "knowledge", "metadata", "relations"}
RELATION_KEYS = {
    "related",
    "uses",
    "implemented_in",
    "written_in",
    "powered_by",
    "built_with",
    "stored_in",
    "deployed_on",
    "connected_to",
    "belongs_to",
    "part_of",
    "requires",
    "supports",
}

def slugify(text: str) -> str:
    text = str(text).strip().lower()
    replacements = {
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "à": "a", "â": "a", "ä": "a",
        "ù": "u", "û": "u", "ü": "u",
        "î": "i", "ï": "i",
        "ô": "o", "ö": "o",
        "ç": "c",
        "'": "",
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def normalize_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [v for v in value if v is not None and str(v).strip()]
    return [value]

def ensure_node(G, name, category=None, **attrs):
    node_id = slugify(name)
    if G.has_node(node_id):
        current = G.nodes[node_id]
        if category and not current.get("category"):
            current["category"] = category
        for k, v in attrs.items():
            if v is not None and k not in current:
                current[k] = v
        aliases = set(current.get("aliases", []))
        aliases.update(normalize_list(attrs.get("aliases")))
        current["aliases"] = sorted(aliases)
    else:
        clean_attrs = {}
        for k, v in attrs.items():
            if v is None:
                continue
            if k == "aliases":
                clean_attrs[k] = sorted(set(normalize_list(v)))
            else:
                clean_attrs[k] = v
        clean_attrs["id"] = node_id
        clean_attrs["label"] = name
        clean_attrs["category"] = category
        G.add_node(node_id, **clean_attrs)
    return node_id

def add_relation(G, source, target, relation):
    if not source or not target:
        return
    if not G.has_node(source):
        G.add_node(source, id=source, label=source, category="unclassified")
    if not G.has_node(target):
        G.add_node(target, id=target, label=target, category="unclassified")
    if G.has_edge(source, target):
        rels = set(normalize_list(G.edges[source, target].get("relations")))
        rels.add(relation)
        G.edges[source, target]["relations"] = sorted(rels)
    else:
        G.add_edge(source, target, relations=[relation])

def main():
    G = nx.DiGraph()
    stats = {}

    for path in sorted(TAXONOMY_DIR.glob("*.yaml")):
        data = load_yaml(path)
        category = path.stem

        if category == "relations":
            continue

        items = data.get("items", {})
        if not isinstance(items, dict):
            continue

        stats[category] = {"nodes": 0, "edges": 0}

        for name, attrs in items.items():
            if attrs is None:
                attrs = {}
            if not isinstance(attrs, dict):
                attrs = {"value": attrs}

            aliases = normalize_list(attrs.get("aliases"))
            node_attrs = {k: v for k, v in attrs.items() if k not in RELATION_KEYS}
            node_attrs["aliases"] = aliases

            node_id = ensure_node(G, name, category=category, **node_attrs)
            stats[category]["nodes"] += 1

            for key, value in attrs.items():
                if key in RELATION_KEYS:
                    for target in normalize_list(value):
                        target_id = ensure_node(G, target)
                        add_relation(G, node_id, target_id, key)
                        stats[category]["edges"] += 1

    G.graph["stats"] = stats
    G.graph["taxonomy_files"] = sorted([p.name for p in TAXONOMY_DIR.glob("*.yaml")])

    payload = json_graph.node_link_data(G)
    OUTPUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
