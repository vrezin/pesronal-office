#!/usr/bin/env bash
set -euo pipefail

TABLE="${HH_DIRECT_ROUTE_TABLE:-51820}"
HOSTS="${HH_DIRECT_ROUTE_HOSTS:-hh.ru www.hh.ru auth.hh.ru api.hh.ru}"

if [[ "${EUID}" -ne 0 ]]; then
  echo "Run as root; route updates require CAP_NET_ADMIN." >&2
  exit 1
fi

main_default="$(ip -4 route show table main default | head -n 1)"
if [[ -z "$main_default" ]]; then
  echo "No IPv4 default route in table main." >&2
  exit 1
fi

gateway="$(awk '{for (i=1; i<=NF; i++) if ($i == "via") print $(i+1)}' <<<"$main_default")"
dev="$(awk '{for (i=1; i<=NF; i++) if ($i == "dev") print $(i+1)}' <<<"$main_default")"
src="$(ip -4 addr show dev "$dev" scope global | awk '/inet / {sub(/\/.*/, "", $2); print $2; exit}')"

if [[ -z "$gateway" || -z "$dev" || -z "$src" ]]; then
  echo "Could not resolve gateway/dev/src from main default route: $main_default" >&2
  exit 1
fi

resolved_ips="$(
  for host in $HOSTS; do
    getent ahostsv4 "$host" | awk '{print $1}'
  done | sort -u
)"

if [[ -z "$resolved_ips" ]]; then
  echo "No HH IPv4 addresses resolved for: $HOSTS" >&2
  exit 1
fi

while IFS= read -r ip; do
  [[ -n "$ip" ]] || continue
  ip route replace "$ip/32" via "$gateway" dev "$dev" src "$src" table "$TABLE"
  echo "$ip/32 via $gateway dev $dev src $src table $TABLE"
done <<<"$resolved_ips"
