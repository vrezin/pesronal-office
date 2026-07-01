# Raspberry Pi 64-bit Reimage Runbook

- Created: 2026-06-25
- Purpose: replace the current 32-bit `armhf` Raspberry Pi OS image with a 64-bit userland so OpenClaw can run the native Codex app-server runtime.

## Current Finding

The Raspberry Pi hardware/kernel is 64-bit capable:

```text
uname -m -> aarch64
```

But the installed OS userland is 32-bit:

```text
dpkg --print-architecture -> armhf
node -p 'process.platform + " " + process.arch' -> linux arm
```

The OpenClaw Codex plugin reaches `@openai/codex`, but the bundled Codex executable rejects the current platform:

```text
Unsupported platform: linux (arm)
```

## Correct Image

Use Raspberry Pi OS Lite 64-bit.

Official source:

```text
https://www.raspberrypi.com/software/operating-systems/
```

Download endpoint checked on 2026-06-25:

```text
https://downloads.raspberrypi.com/raspios_lite_arm64_latest
```

Redirect observed:

```text
https://downloads.raspberrypi.com/raspios_lite_arm64/images/raspios_lite_arm64-2026-06-19/2026-06-18-raspios-trixie-arm64-lite.img.xz
```

Official metadata:

- Release date: 2026-06-18
- System: 64-bit
- Debian: 13 `trixie`
- Kernel: 6.18
- Download size: 501 MB
- Storage required: 2,840 MB
- SHA256: `acff736ca7945e3b305f07cda4abdb870910e12634991da69783611756e381b3`

Downloaded and verified locally:

```text
/tmp/2026-06-18-raspios-trixie-arm64-lite.img.xz
```

Persistent workstation copy:

```text
<external-downloads>/2026-06-18-raspios-trixie-arm64-lite.img.xz
```

Verified hash:

```text
acff736ca7945e3b305f07cda4abdb870910e12634991da69783611756e381b3
```

## Reimage Constraint

The live Pi currently boots from the SD card:

```text
/dev/mmcblk0p1 -> /boot/firmware
/dev/mmcblk0p2 -> /
```

Do not attempt to rewrite `/dev/mmcblk0` from the running Pi. Use one of:

- remove the microSD and flash it from the workstation;
- flash a second microSD/USB and swap boot media;
- use Raspberry Pi Imager on Windows/macOS/Linux with an SD reader.

## Recommended Path

Use Raspberry Pi Imager on the workstation.

Image:

```text
Raspberry Pi OS Lite (64-bit)
```

Use Imager OS Customisation before writing the card. This is required for a headless Wi-Fi-only setup.

Recommended customisation settings:

- hostname: `raspberrypi`
- username: `pi`
- enable SSH
- use public-key SSH if convenient; otherwise set a temporary password and rotate later
- configure Wi-Fi SSID/password if the Pi will boot headless on Wi-Fi
- locale/timezone as needed

Important: for Raspberry Pi OS Bookworm/Trixie, do not rely on the old `wpa_supplicant.conf` boot-partition method. Official docs say that method is no longer available from Bookworm onward. Configure Wi-Fi in Raspberry Pi Imager before first boot, or use wired Ethernet/USB Ethernet for first access.

After first boot, verify:

```bash
ssh raspberrypi-codex 'uname -m; dpkg --print-architecture; node -p "process.platform + \" \" + process.arch" || true'
```

Expected:

```text
aarch64
arm64
linux arm64
```

## Post-Reimage Bootstrap Checklist

1. Confirm SSH profile `raspberrypi-codex` works.
2. Confirm `dpkg --print-architecture` is `arm64`.
3. Keep `pi` as the administrative SSH/bootstrap user.
4. Create a dedicated `openclaw` user without sudo privileges for OpenClaw runtime state.
5. Enable linger for `openclaw` if using user systemd services.
6. Install VPN client and restore `/etc/wireguard/personal-office.conf` from the private source config, not from the repository. VPN remains a root/system service.
7. Enable and start `wg-quick@personal-office`.
8. Install Node.js 22.19+ or 24 arm64 under `/home/openclaw/.local/`.
9. Install OpenClaw under the `openclaw` user.
10. Install and enable `@openclaw/codex` under the `openclaw` user.
11. Recreate `po-router` under `/home/openclaw/personal-office-agent/`.
12. Create or configure a separate `default` agent for dashboard/bare CLI traffic if the UI does not explicitly select `po-router`.
13. Keep `default` and `po-router` on separate `agentDir` paths; OpenClaw rejects shared agent directories because they collide on auth/session state.
14. Point `default` at the same cookbook workspace as `po-router` if the dashboard should exercise the Personal Office cookbook route.
15. Sync cookbook-only bundle, not raw Personal Office data.
16. Run OpenAI/Codex device-code auth again for every agent that can receive traffic (`po-router` and `default` in the current test contour).
17. Run agent smoke tests for both an explicit `po-router` route and the bare/default route.
18. Remove/quarantine any old broad Personal Office copy if it reappears.

## Runtime User Model

Use two users:

- `pi`: administrator for SSH, package installs, VPN service setup, and emergency recovery.
- `openclaw`: non-sudo runtime owner for Node.js, OpenClaw, agent workspaces, OAuth/session state, cookbooks, and Gateway service.

Do not put `openclaw` in `sudo`, `adm`, or other broad host-control groups unless there is a specific reviewed reason.

## Safety Notes

- Reimaging destroys the current SD card contents.
- The current Pi contains a working WireGuard config and OpenClaw OAuth state, but these should be treated as runtime state, not as source of truth.
- Do not copy raw Personal Office directories to the Pi during bootstrap.
