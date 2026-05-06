#!/usr/bin/env python3
"""Sync canonical design-system files into consumer projects.

Why this exists
---------------
The design system has two consumers:

  * offshores-pipeline  — TRUE consumer. Mirrors every file under tokens/,
                          components/, and js/ into public/design-system/
                          and reads them via <link>/<script> tags.
  * offshore-revamp     — FORK. The storefront's j2 templates inline their
                          own copies of the tokens with storefront-specific
                          additions (footer/cause-callout/admin overrides
                          in theme.js, viewport-fit / SW shell, etc).

Sync rule
---------
* Pipeline gets a wholesale copy of every file. Run this script after every
  meaningful canonical change to keep the pipeline at parity.
* Storefront is a fork. Sync DOES NOT touch storefront files. When you change
  a token (color, type, spacing) in canonical, manually mirror it into the
  matching :root block in offshore-revamp/_template/*.j2. Storefront's
  theme.js is its own evolved fork that should be hand-merged when canonical
  ships a meaningful theme.js change.

Usage
-----
  python sync.py              dry-run, lists what would change
  python sync.py --apply      actually copy

Run from anywhere; paths are anchored to this script's location and the
sibling layout C:/Users/dnolt/projects/{offshore-design-system, offshores-
pipeline} that the user maintains.
"""
import argparse
import shutil
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
PIPELINE_ROOT = HERE.parent / "offshores-pipeline"


# Map of source dir (relative to canonical) -> destination dir (relative to
# pipeline root). Most of the design system mirrors into public/design-system/
# so it can be linked via <link>/<Script>; icons mirror to /public/icons/
# so the manifest + apple-touch-icon paths in app/layout.tsx resolve.
SYNCED_DIRS = {
    "tokens": Path("public/design-system/tokens"),
    "components": Path("public/design-system/components"),
    "js": Path("public/design-system/js"),
    "icons": Path("public/icons"),
}


def diff_files() -> list[tuple[Path, Path, str]]:
    """Return (src, dest, status) tuples. Status is 'new' | 'changed' | 'same'.

    `generate.py` inside icons/ stays in canonical only — it's the build
    script for the rasters, not part of the runtime asset set."""
    out: list[tuple[Path, Path, str]] = []
    for src_sub, dest_sub in SYNCED_DIRS.items():
        src_root = HERE / src_sub
        if not src_root.is_dir():
            continue
        for src in sorted(src_root.rglob("*")):
            if not src.is_file():
                continue
            if src.name == "generate.py":
                continue
            rel = src.relative_to(src_root)
            dest = PIPELINE_ROOT / dest_sub / rel
            if not dest.exists():
                out.append((src, dest, "new"))
            elif src.read_bytes() != dest.read_bytes():
                out.append((src, dest, "changed"))
            else:
                out.append((src, dest, "same"))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually copy files. Without this flag, prints a diff plan.",
    )
    args = parser.parse_args()

    if not PIPELINE_ROOT.exists():
        print(f"!! Pipeline root missing: {PIPELINE_ROOT}", file=sys.stderr)
        print("   Expected sibling layout: ~/projects/{offshore-design-system,offshores-pipeline}", file=sys.stderr)
        return 2

    plan = diff_files()
    new = [p for p in plan if p[2] == "new"]
    changed = [p for p in plan if p[2] == "changed"]
    same = [p for p in plan if p[2] == "same"]

    print(f"Canonical:  {HERE}")
    print(f"Pipeline:   {PIPELINE_ROOT}")
    print()
    print(f"  {len(new):3d} new   files would be copied")
    print(f"  {len(changed):3d} changed files would be overwritten")
    print(f"  {len(same):3d} same  files (no-op)")

    for src, dest, status in plan:
        if status == "same":
            continue
        rel = src.relative_to(HERE)
        marker = "+ " if status == "new" else "M "
        print(f"    {marker}{rel}")

    if not (new or changed):
        print("\nUp-to-date.")
        return 0

    if not args.apply:
        print("\nDry run. Re-run with --apply to copy.")
        return 0

    for src, dest, status in plan:
        if status == "same":
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    print(f"\nApplied {len(new) + len(changed)} change(s).")
    print("Note: storefront (offshore-revamp) is a fork and is intentionally")
    print("not synced. Mirror token changes into the j2 :root blocks by hand.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
