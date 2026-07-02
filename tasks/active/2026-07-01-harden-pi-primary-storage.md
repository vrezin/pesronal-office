# Harden Pi Primary Storage

- Created: 2026-07-01
- Status: Active
- Area: tools / automation / infrastructure
- Related plan: `tools/raspberrypi-openclaw/pi-storage-hardening-plan-2026-07-01.md`
- Related storage decision: `tools/raspberrypi-openclaw/personal-office-shared-storage-decision-2026-07-01.md`
- Related runtime task: `tasks/active/2026-06-28-finish-pi-job-search-contour-runtime.md`

## Goal

Move the Pi-primary Personal Office runtime away from fragile microSD-only
storage and onto a more durable filesystem layout before relying on it as the
always-on home automation host.

## Current State

- Current root filesystem is `/dev/mmcblk0p2` ext4 on microSD.
- Root has about 29G total, 11G used, 17G free.
- `/tmp` is already tmpfs.
- zram swap is present.
- 2026-07-01 `lsblk` snapshot had no USB SSD or external data disk.
- 2026-07-02 snapshot after attaching the available USB flash drive:
  - `/dev/sda` SanDisk Ultra USB 3.0, 114.6G;
  - `/dev/sda1` `vfat`, label `LINUX MINT`, mounted at
    `/media/pi/LINUX MINT`.
- 2026-07-02 contents check from `pi@raspberrypi-codex`:
  - 7.8G used, 107G available;
  - top-level contents are Linux Mint boot/live image directories and files:
    `.disk`, `[boot]`, `boot`, `casper`, `EFI`, `dists`, `isolinux`, `pool`,
    `md5sum.txt`, `efi.img`, `syslinux.cfg`, `autorun.*`;
  - one user-visible data directory: `МедРеки`, 4.9G, 719 files;
  - no other top-level data directory was observed.
- The flash has enough capacity for the current runtime, but `vfat` is not
  acceptable for OpenClaw/browser/SQLite runtime state. It must be reformatted
  to `ext4` before use, which will erase existing contents.
- High-write runtime paths currently remain on microSD:
  - `/home/openclaw/personal-office-agent`;
  - `/home/openclaw/.openclaw`;
  - `/home/openclaw/.config/personal-office`.

## Migration Evidence

2026-07-02:

- User confirmed that `/dev/sda1` may be erased.
- `/dev/sda1` was reformatted from `vfat` to `ext4`.
- New filesystem:
  - label: `personal-office-`;
  - UUID: `9b8095ed-2272-41b4-a03d-437b669922a3`;
  - mounted at `/srv/personal-office`.
- `/etc/fstab` now mounts `/srv/personal-office` by UUID with `noatime`.
- Bind mounts are active:
  - `/srv/personal-office/home-openclaw/personal-office-agent` ->
    `/home/openclaw/personal-office-agent`;
  - `/srv/personal-office/home-openclaw/.openclaw` ->
    `/home/openclaw/.openclaw`;
  - `/srv/personal-office/home-openclaw/.config-personal-office` ->
    `/home/openclaw/.config/personal-office`.
- `df -hT` shows all three runtime paths on `/dev/sda1` ext4, 113G total,
  3.0G used, 104G available.
- Rollback copies retained on microSD:
  - `/home/openclaw/personal-office-agent.sdcard-backup-20260702`;
  - `/home/openclaw/.openclaw.sdcard-backup-20260702`;
  - `/home/openclaw/.config/personal-office.sdcard-backup-20260702`.
- OpenClaw gateway restarted and reported reachable.
- `linkedin-mcp.service` restarted and is active/running.
- `personal-office-pi-job-search-gmail-monitor.timer` restarted and is
  active/waiting.
- `personal-office-pi-job-search-sync.timer` restarted and is active/waiting.
- OpenClaw Telegram channel `job-search-telegram` is installed, configured, and
  enabled with tokenFile auth.
- First post-migration scheduled Gmail monitor passed on the USB-backed runtime:
  `automation/runs/2026-07-02-1623-pi-job-search-gmail-monitor.md` and
  `automation/runs/2026-07-02-1627-pi-job-search-gmail-monitor.md`.
- First post-migration Pi sync pushed completed monitor artifacts/state to the
  private Git remote. Verified Pi commit:
  `cc3ba09 job-search: sync pi runtime artifacts`.
- First post-migration Telegram outbound smoke passed through
  `job-search-telegram`; OpenClaw reported Telegram message id `357`.
- Sync race mitigation was installed after the first post-migration monitor:
  `run-pi-job-search-sync.sh` now skips while Gmail/Telegram runtime locks are
  active. Verified Pi commit:
  `adb86e1 job-search: skip sync while runtime locks are active`.

## Target Direction

Use a USB SSD or NVMe HAT as the durable data layer, mounted at:

```text
/srv/personal-office
```

Move or bind-mount the Pi-primary Personal Office working tree, OpenClaw state,
local secrets/config, browser profiles, and SQLite runtime stores onto that
disk.

## Storage Attachment Decision

Preferred: attach SSD/NVMe directly to the Raspberry Pi and use it as a local
Linux filesystem for runtime data.

Interim accepted path: use the currently attached direct USB flash drive as a
short-term runtime data disk to reduce microSD writes, while treating it as
less durable than the final SSD/NVMe target.

Router-mounted SSD is useful as backup/archive storage, but should not be the
primary runtime filesystem for SQLite, browser profiles, OpenClaw state, or the
Git working tree because network filesystem locking, latency, and router USB
storage behavior are weaker failure modes for unattended automation.

If direct attachment is not physically possible, use the router share only as a
nightly encrypted backup target and keep hot runtime state local until a direct
SSD/NVMe path is available.

## Next Actions

1. Let one Telegram inbound intake run on the USB-backed runtime.
2. Verify LinkedIn/HH auth state after the migration.
3. Observe the next scheduled Gmail monitor with the sync-lock mitigation in
   place.
4. If the acceptance window passes, remove the `.sdcard-backup-20260702`
   rollback copies from microSD to reclaim space.
5. Add backup/archive job for non-Git state.

## Done When

- Durable writable paths are no longer on `/dev/mmcblk0p2`.
- Pi job-search Gmail monitor still runs.
- Telegram inbound job-search intake still runs.
- LinkedIn/HH auth state still works.
- Git sync still works.
- Non-Git runtime state has an off-device backup path.
