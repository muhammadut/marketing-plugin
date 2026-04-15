"""
google_ads_client.py — v0.1.0 stub wrapper for Google Ads API push.

This file is the contract surface the marketing-ship-campaign skill calls.
v0.1.0 is INTENTIONALLY a stub — it documents the function signatures the
skill expects and exits with a clear error if invoked.

Why a stub: the marketing plugin's brief-and-judge architecture explicitly
keeps the plugin out of the loop for visual generation. Google Ads API push
is the ONE place the plugin is allowed to call an external API, but the
production wrapper requires the user's own google-ads-python SDK
installation, OAuth consent, developer token approval, and account IDs.
None of those can be hardcoded into a redistributable plugin, so v0.1.0
ships the contract as a stub and the user wires up the live wrapper as a
v0.1.1 step (or in a private fork of the plugin repo).

To make this real:
  1. pip install google-ads (currently 28.x as of April 2026)
  2. Place your google-ads.yaml at the path declared in
     .marketing/context.md (default: ~/.google-ads.yaml)
  3. Replace the stub functions below with calls to the SDK
  4. Test against a developer-token-approved account in TEST mode FIRST
  5. Set the v0.1.1 flag in .claude-plugin/plugin.json once verified

The marketing-ship-campaign skill ALWAYS pushes campaigns in PAUSED state,
NEVER auto-enables, requires explicit per-campaign --go-live confirmation,
and refuses to push if .marketing/context.md cost ceilings would be
exceeded. This contract is enforced regardless of which wrapper
implementation is wired in. See marketing-plugin/docs/design.md
"Google Ads API wiring" section for the full safety model.
"""

import sys
from typing import Any


STUB_ERROR = (
    "google_ads_client.py is a v0.1.0 STUB. The production wrapper has not "
    "been wired in. Either install google-ads-python and replace the stub "
    "functions in this file with SDK calls, or run /marketing:ship-campaign "
    "with --dry-run to print the campaign payload without pushing. See "
    "marketing-plugin/code/google_ads_client.py docstring and "
    "marketing-plugin/docs/known-gaps.md for migration notes."
)


def push_campaign(payload: dict, paused: bool = True) -> dict:
    """Push a campaign payload to Google Ads in PAUSED state.

    The contract:
      - Always creates the campaign with status=PAUSED. Live activation is
        a separate call (enable_campaign).
      - Returns a dict with {'campaign_id': ..., 'status': 'PAUSED', 'url': ...}
        on success.
      - Raises on any error (auth, quota, validation, account suspended).
      - Refuses to run if paused=False (the skill never asks for this; if a
        future caller does, fail loudly).

    v0.1.0 stub: prints the payload and exits with a clear error.
    """
    if not paused:
        print(
            "REFUSED: google_ads_client.push_campaign cannot be called with "
            "paused=False. Live activation goes through enable_campaign() "
            "after explicit user confirmation. This is a hard safety rule.",
            file=sys.stderr,
        )
        sys.exit(2)

    print("=== STUB push_campaign payload ===", file=sys.stderr)
    print(repr(payload), file=sys.stderr)
    print(STUB_ERROR, file=sys.stderr)
    sys.exit(1)


def enable_campaign(campaign_id: str, account_id: str) -> dict:
    """Enable a previously-paused campaign. Requires explicit user confirmation
    upstream — the marketing-ship-campaign skill prompts for confirmation
    before invoking this.

    v0.1.0 stub.
    """
    print(
        f"=== STUB enable_campaign(campaign_id={campaign_id!r}, "
        f"account_id={account_id!r}) ===",
        file=sys.stderr,
    )
    print(STUB_ERROR, file=sys.stderr)
    sys.exit(1)


def upload_offline_conversions(
    conversions: list[dict],
    customer_id: str,
    conversion_action_id: str,
) -> dict:
    """Upload offline conversion events (e.g., call-billed events from the
    elocal_clone routing engine) to Google Ads via Enhanced Conversions for
    Leads or the Offline Conversion Upload API.

    v0.1.0 stub.
    """
    print(
        f"=== STUB upload_offline_conversions count={len(conversions)} "
        f"customer={customer_id} action={conversion_action_id} ===",
        file=sys.stderr,
    )
    print(STUB_ERROR, file=sys.stderr)
    sys.exit(1)


def dry_run_print_payload(payload: dict) -> None:
    """Print a campaign payload to stdout for inspection without pushing.
    This is what marketing-ship-campaign --dry-run calls instead of
    push_campaign(). It always works, even in stub mode.
    """
    import json
    print(json.dumps(payload, indent=2, default=str))


if __name__ == "__main__":
    print(STUB_ERROR, file=sys.stderr)
    sys.exit(1)
