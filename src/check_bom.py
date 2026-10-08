"""Check the course BOM mass balance; this does not calculate an LCA."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


EXPECTED_G = {
    "Kettle": Decimal("723.00"),
    "Packaging": Decimal("137.80"),
}


def read_bom(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    required = {"material", "finished_mass_g", "scope"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError(f"BOM must contain columns: {', '.join(sorted(required))}")
    return rows


def summarize(rows: list[dict[str, str]]) -> dict:
    scope_totals: dict[str, Decimal] = defaultdict(Decimal)
    materials = []
    for line_number, row in enumerate(rows, start=2):
        try:
            grams = Decimal(row["finished_mass_g"])
        except Exception as exc:
            raise ValueError(f"Invalid finished_mass_g on CSV line {line_number}") from exc
        if grams < 0:
            raise ValueError(f"Negative mass on CSV line {line_number}")
        scope = row["scope"].strip()
        scope_totals[scope] += grams
        materials.append(
            {
                "material": row["material"],
                "finished_mass_g": str(grams),
                "finished_mass_kg": str(grams / Decimal("1000")),
                "scope": scope,
            }
        )

    checks = {
        scope: {
            "observed_g": str(scope_totals[scope]),
            "expected_g": str(expected),
            "passed": scope_totals[scope] == expected,
        }
        for scope, expected in EXPECTED_G.items()
    }
    total_g = sum(scope_totals.values(), Decimal("0"))
    checks["total"] = {
        "observed_g": str(total_g),
        "expected_g": str(sum(EXPECTED_G.values(), Decimal("0"))),
        "passed": total_g == sum(EXPECTED_G.values(), Decimal("0")),
    }
    return {
        "calculation_type": "BOM mass-balance check only; no life-cycle impact calculated",
        "material_count": len(materials),
        "scope_totals_g": {scope: str(value) for scope, value in sorted(scope_totals.items())},
        "scope_totals_kg": {
            scope: str(value / Decimal("1000")) for scope, value in sorted(scope_totals.items())
        },
        "total_finished_mass_g": str(total_g),
        "total_finished_mass_kg": str(total_g / Decimal("1000")),
        "checks": checks,
        "all_mass_checks_passed": all(item["passed"] for item in checks.values()),
        "materials": materials,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bom", type=Path, default=Path("kettle-bom.csv"))
    parser.add_argument(
        "--output", type=Path, default=Path("results/independent/bom-check.json")
    )
    args = parser.parse_args()
    report = summarize(read_bom(args.bom))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["all_mass_checks_passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
