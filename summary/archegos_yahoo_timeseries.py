from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import pandas as pd
import yfinance as yf


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
START_DATE = "2020-01-01"
END_DATE = "2021-04-30"


@dataclass(frozen=True)
class StockRequest:
    name: str
    output_stem: str
    candidates: tuple[str, ...]
    note: str = ""


STOCKS: tuple[StockRequest, ...] = (
    StockRequest(
        name="ViacomCBS",
        output_stem="viacomcbs",
        candidates=("VIAC", "PARA", "PSKY"),
        note="Yahoo no longer serves the historical ViacomCBS ticker consistently; the script falls back to the first symbol that still returns the requested history.",
    ),
    StockRequest(name="Tencent Music", output_stem="tencent_music", candidates=("TME",)),
    StockRequest(name="Vipshop", output_stem="vipshop", candidates=("VIPS",)),
    StockRequest(
        name="Farfetch",
        output_stem="farfetch",
        candidates=("FTCH", "FTCHQ"),
        note="Yahoo currently exposes Farfetch history under a post-delisting symbol in some environments.",
    ),
    StockRequest(name="Texas Capital Bancshares", output_stem="texas_capital_bancshares", candidates=("TCBI",)),
    StockRequest(name="iQIYI", output_stem="iqiyi", candidates=("IQ",)),
    StockRequest(
        name="Discovery",
        output_stem="discovery",
        candidates=("DISCA", "DISCK", "WBD"),
        note="Discovery class symbols may no longer resolve directly on Yahoo; the script tries legacy tickers first, then the successor symbol that still returns backfilled history.",
    ),
    StockRequest(
        name="GSX / Gaotu",
        output_stem="gsx_gaotu",
        candidates=("GSX", "GOTU"),
        note="GSX changed its trading symbol to GOTU.",
    ),
    StockRequest(name="Baidu", output_stem="baidu", candidates=("BIDU",)),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download Archegos-related stock histories from Yahoo Finance into CSV files."
    )
    parser.add_argument("--start", default=START_DATE, help=f"Start date in YYYY-MM-DD format. Default: {START_DATE}")
    parser.add_argument("--end", default=END_DATE, help=f"End date in YYYY-MM-DD format. Default: {END_DATE}")
    parser.add_argument("--interval", default="1d", help="Yahoo Finance interval. Default: 1d")
    parser.add_argument(
        "--output-dir",
        default=str(DATA_DIR),
        help=f"Directory where CSVs and metadata are written. Default: {DATA_DIR}",
    )
    return parser.parse_args()


def normalize_history(df: pd.DataFrame, ticker_used: str, request: StockRequest) -> pd.DataFrame:
    if df.empty:
        return df

    if isinstance(df.columns, pd.MultiIndex):
        if ticker_used in df.columns.get_level_values(-1):
            df = df.xs(ticker_used, axis=1, level=-1)
        else:
            df.columns = ["_".join(str(part) for part in column if part) for column in df.columns.to_flat_index()]

    df = df.reset_index()
    df.columns = [str(column).replace(" ", "_") for column in df.columns]
    df.insert(0, "company_name", request.name)
    df.insert(1, "ticker_used", ticker_used)
    return df


def fetch_history(request: StockRequest, start: str, end: str, interval: str) -> tuple[str | None, pd.DataFrame]:
    for candidate in request.candidates:
        df = yf.download(
            candidate,
            start=start,
            end=end,
            interval=interval,
            auto_adjust=False,
            progress=False,
            threads=False,
        )
        normalized = normalize_history(df, candidate, request)
        if not normalized.empty:
            return candidate, normalized

    return None, pd.DataFrame()


def download_all(start: str = START_DATE, end: str = END_DATE, interval: str = "1d", output_dir: Path | None = None) -> list[dict]:
    target_dir = Path(output_dir) if output_dir is not None else DATA_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []

    for request in STOCKS:
        ticker_used, history = fetch_history(request, start=start, end=end, interval=interval)
        csv_path = target_dir / f"{request.output_stem}.csv"

        result = {
            "name": request.name,
            "output_stem": request.output_stem,
            "requested_candidates": list(request.candidates),
            "ticker_used": ticker_used,
            "rows": int(len(history)),
            "csv_path": str(csv_path),
            "status": "downloaded" if ticker_used else "unavailable",
            "note": request.note,
            "start": start,
            "end": end,
            "interval": interval,
        }

        if ticker_used:
            history.to_csv(csv_path, index=False)
        results.append(result)

    manifest = {
        "start": start,
        "end": end,
        "interval": interval,
        "output_dir": str(target_dir),
        "stocks": results,
    }

    (target_dir / "download_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    pd.DataFrame(results).to_csv(target_dir / "download_manifest.csv", index=False)
    return results


def main() -> None:
    args = parse_args()
    results = download_all(
        start=args.start,
        end=args.end,
        interval=args.interval,
        output_dir=Path(args.output_dir),
    )

    for result in results:
        ticker_label = result["ticker_used"] or "none"
        print(f"{result['name']}: {result['status']} ({ticker_label}, rows={result['rows']})")


if __name__ == "__main__":
    main()
