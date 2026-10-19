def build_report(records):
    """Build a simple score summary report."""
    total = sum(r["score"] for r in records)
    top = max(records, key=lambda r: r["score"])
    return {
        "total": total,
        "average": total / len(records),
        "top_student": top["name"],
    }
