---
name: handholder
description: Set up, migrate, repair, or audit Android gaming handhelds over ADB, including Cocoon, emulators, lawful ROM and save migration, artwork, controls, displays, and launch testing. Includes profiles for AYN Thor and Retroid Pocket Nova; use the generic workflow for other Android handhelds.
---

# Handholder

Build a verified, console-like Android handheld without assuming a model, host path, storage volume, package version, or controller mapping.

## Route the task

1. Run `scripts/probe-device.sh [serial]` before changing the device.
2. Identify the device from live properties. Read only the matching profile:
   - AYN Thor: [references/devices/ayn-thor.md](references/devices/ayn-thor.md)
   - Retroid Pocket Nova: [references/devices/retroid-pocket-nova.md](references/devices/retroid-pocket-nova.md)
   - Other model: use the generic workflow and create a dated profile only after live verification.
3. Read [references/device-and-adb.md](references/device-and-adb.md) before screen, touch, or controller automation.
4. Read [references/cocoon.md](references/cocoon.md) when Cocoon is in scope.
5. Read [references/emulators.md](references/emulators.md) before selecting apps, cores, BIOS paths, or platform mappings.
6. Read [references/saves-and-native-ports.md](references/saves-and-native-ports.md) for save migration, native ports, or dual-screen mods.

## Required workflow

### 1. Define scope and preserve state

- Confirm the exact ADB serial and authorization. If more than one device is online, require an explicit serial.
- Treat display IDs, input paths, storage roots, UI coordinates, package names, signing certificates, and versions as live state.
- Resolve source and destination storage explicitly. Honor the user's requested internal or removable storage even when a guide prefers another layout.
- Inventory packages, frontend data, emulator data, ROM folders, BIOS folders, saves, free space, displays, and controllers before mutation.
- Back up relevant app and shared-storage data before replacing, uninstalling, clearing, or importing.
- Use only game data, BIOS files, disc images, keys, patches, and decompilation inputs supplied by the user as lawful backups. Never search for copyrighted game data.

### 2. Research current software

- Verify releases against the project's official site, repository, store listing, or signed update channel immediately before installation.
- Prefer official builds. Use a community fork only when it supplies a required capability and its provenance, package ID, signer, and update path are understood.
- Record the source URL, version, package ID, checksum, and signer for sideloaded APKs.
- Never assume a version or package ID from a dated device profile is still current.

### 3. Transfer the library

- Measure source file count, byte count, and free destination capacity first.
- Apply exclusions before transfer. Preserve the remaining system folders, disc subdirectories, filenames, cue sheets, and playlists.
- Validate every cue sheet against the files beside it. Repair only a staging copy when a referenced track name is wrong; never rewrite the user's source image.
- When a lossless, emulator-supported container is needed to fit the requested storage, convert a copy, verify the result, and retain the original source. Typical examples are PSP ISO to CSO and optical-disc cue/bin to CHD.
- Use an observable, resumable method for large libraries. Poll file and byte counts until stable.
- Compare source and destination relative paths and sizes. Hash small or disputed files; do not hash a large library without a reason.
- Keep BIOS files separate from ROMs when the chosen emulator expects that layout. Never download missing BIOS data.

### 4. Configure emulators

- Install the smallest maintained set that covers the requested systems.
- Open each app once, grant only needed storage access, set the ROM and BIOS roots, map the built-in controller, and choose a renderer appropriate to the device.
- Preserve native 4:3 output on 4:3 displays unless the game itself supports widescreen. Use per-game overrides for compatibility or performance exceptions.
- For RetroArch, install only the selected cores, update core information and shaders when requested, configure hotkeys deliberately, and save overrides at the correct scope.
- Do not call an emulator configured until a representative game reaches interactive gameplay with working controls and audio.

### 5. Configure Cocoon

- Install the current official release, open it once, and set the user-requested storage root.
- Add only requested platforms. Map every platform to a verified installed player, then rescan.
- Add native ports or Android games to clearly named folders when requested.
- Retrieve integration credentials only through an approved secret manager. Never print, log, persist, or photograph them.
- Scrape only after the final rescan. Monitor the UI and parse the newest completed JSONL report before claiming success.
- Launch one representative title per emulator family from Cocoon, not only from the emulator UI.

### 6. Reconcile saves

- Build a candidate manifest from the supplied roots and the device. Match game identity, region, title ID, emulator/core, extension, size, and modification time; filename alone is insufficient.
- Back up the destination before replacement. Prefer native in-game saves over save states for cross-emulator migration.
- Import one game family at a time, launch it, and prove the expected progress appears in-game.
- Preserve ambiguous and incompatible saves in the backup. Never discard them or force-convert them without a documented compatible path.

### 7. Finish and prove

- Verify controller input, audio, aspect ratio, suspend/resume, relaunch, frontend return behavior, and one representative title for every configured system.
- Capture and inspect every physical panel on multi-display devices. A running process does not prove correct screen ownership.
- Remove only exact, enumerated setup artifacts after the installed apps, copied data, and artwork are proven.
- Run `scripts/validate-public.sh` before publishing changes to this skill.
- Leave the handheld on Cocoon or the user's chosen frontend and report versions, tested systems, save coverage, scrape coverage, exclusions, and unresolved limitations.

## Safety invariants

- Never uninstall or clear a frontend or emulator before salvaging its saves and configuration.
- Never send blind keyboard input. Capture the current UI and confirm focus before entering text; avoid text injection around credentials.
- Never reuse a controller event path or display ID after reconnect or reboot without probing it again.
- Never weaken Android permissions, root a device, or replace a signing key merely to bypass scoped storage.
- Stop before a destructive or signer-changing action whose exact data impact is not proven and authorized.
