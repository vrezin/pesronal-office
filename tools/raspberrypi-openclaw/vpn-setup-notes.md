# Raspberry Pi VPN Setup Notes

- Created: 2026-06-25
- Purpose: network prerequisite before exposing or remotely operating OpenClaw on the Raspberry Pi.

## Current Pi State

- Host: `raspberrypi-codex`
- LAN interface: `wlan0`
- LAN address at first check: `192.168.1.44/24`
- Installed VPN tools: `wireguard-tools` installed on 2026-06-25.
- `wg` and `wg-quick` are available.
- WireGuard kernel module loads successfully.
- `/etc/wireguard/` exists and is root-only.
- `tailscale`, `tailscaled`, and `openvpn` were not installed during the first VPN check.
- `tailscaled` service: not found.
- `wg-quick@personal-office` service: enabled and active after setup.
- WireGuard config installed as `/etc/wireguard/personal-office.conf`.
- VPN interface: `personal-office`.
- VPN address observed after setup: `10.200.173.81/32`.
- External IPv4 observed through the tunnel: `195.181.173.207`.

## Available From Raspbian Apt

The Raspbian/Debian package repository offers:

- `wireguard-tools`
- `wireguard`
- `openvpn`
- `network-manager-openvpn`

No Amnezia package was found through `apt-cache search amnezia`.

## Decision Point

The setup path depends on the VPN config type.

### Ordinary WireGuard

Use if the provided config is a standard `.conf` with sections like:

```ini
[Interface]
PrivateKey =
Address =
DNS =

[Peer]
PublicKey =
AllowedIPs =
Endpoint =
PersistentKeepalive =
```

Pi setup path:

- install `wireguard-tools` (done);
- place config as `/etc/wireguard/<name>.conf`;
- start with `sudo wg-quick up <name>`;
- optionally enable with `sudo systemctl enable wg-quick@<name>`.

Recommended first tunnel name:

```text
personal-office.conf
```

Recommended install commands after receiving the config:

```bash
sudo install -m 600 -o root -g root /tmp/personal-office.conf /etc/wireguard/personal-office.conf
sudo wg-quick up personal-office
sudo wg show
ip -br addr
```

Enable on boot only after the manual `wg-quick up` test succeeds:

```bash
sudo systemctl enable wg-quick@personal-office
```

Setup completed:

```bash
sudo install -m 600 -o root -g root /tmp/personal-office.conf /etc/wireguard/personal-office.conf
sudo wg-quick up personal-office
sudo systemctl enable wg-quick@personal-office
sudo wg-quick down personal-office
sudo systemctl start wg-quick@personal-office
```

Verification completed:

```bash
systemctl is-enabled wg-quick@personal-office
systemctl is-active wg-quick@personal-office
ip -br addr show personal-office
curl -4 --max-time 15 -sS https://ifconfig.me
sudo wg show personal-office latest-handshakes
```

### AmneziaWG

Use if the config includes AmneziaWG-specific fields such as:

```ini
Jc =
Jmin =
Jmax =
S1 =
S2 =
H1 =
H2 =
H3 =
H4 =
```

Ordinary `wg-quick` is not enough for this config. The Pi needs AmneziaWG CLI/tools compatible with Raspbian 13 and 32-bit `armhf` userland.

### OpenVPN

Use if the provided config is `.ovpn`.

Pi setup path:

- install `openvpn`;
- place config under `/etc/openvpn/client/<name>.conf`;
- start with `sudo systemctl start openvpn-client@<name>`;
- optionally enable with `sudo systemctl enable openvpn-client@<name>`.

### VLESS

Use if the provided config is a VLESS URL or JSON.

Pi setup path likely needs a VLESS-capable client such as `xray` or `sing-box`. This is not available from the basic VPN package list and should be handled as a separate tool install decision.

## OpenClaw Boundary

Do not expose OpenClaw Gateway through VPN until:

- the VPN client is installed and verified;
- the Pi has a stable VPN address;
- SSH over VPN is verified;
- OpenClaw remains `bind=loopback` or is explicitly bound only after a security decision;
- the broad accidental repository copy is removed or quarantined.

## Next Required Input

Completed using local config path:

```text
<external-downloads>/Netherlands.conf
```

Do not commit or copy the config into the repository; it contains private keys.
