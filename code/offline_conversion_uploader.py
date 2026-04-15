"""
offline_conversion_uploader.py — v0.1.0 stub for offline conversion upload.

This file is a thin convenience wrapper around
google_ads_client.upload_offline_conversions(). The marketing plugin
documentation references this file by name; v0.1.0 ships the stub so the
skill's references resolve.

For elocal_clone specifically, this is the bridge between the Twilio
routing engine's call-billed event and Google Ads:
  routing-engine → call-billed event → this script → Google Ads
                                                       conversion API

The contract is documented in marketing-plugin/docs/design.md
"Google Ads API wiring" section.
"""

import sys

from google_ads_client import upload_offline_conversions, STUB_ERROR


def upload_call_billed(
    gclid: str,
    conversion_time_iso: str,
    conversion_value_cad: float,
    customer_id: str,
    conversion_action_id: str,
) -> dict:
    """Upload a single call-billed event from the elocal_clone routing
    engine to Google Ads. The gclid (Google Click ID) is captured by the
    routing engine when the consumer first clicks the ad and stored in the
    call_logs table; conversion_time_iso is the timestamp the call crossed
    the 90-second billing threshold; conversion_value_cad is the dollar
    amount billed to the contractor.

    v0.1.0 stub.
    """
    payload = [
        {
            "gclid": gclid,
            "conversion_action": (
                f"customers/{customer_id}/conversionActions/"
                f"{conversion_action_id}"
            ),
            "conversion_date_time": conversion_time_iso,
            "conversion_value": conversion_value_cad,
            "currency_code": "CAD",
        }
    ]
    return upload_offline_conversions(
        conversions=payload,
        customer_id=customer_id,
        conversion_action_id=conversion_action_id,
    )


if __name__ == "__main__":
    print(STUB_ERROR, file=sys.stderr)
    sys.exit(1)
