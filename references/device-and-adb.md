# Device and ADB reference

Use this reference for discovery, capture, controller input, UI automation, and cleanup on any Android handheld.

## ADB discovery

Prefer `ADB_BIN` when supplied, then `command -v adb`. The generic probe intentionally has no host-specific SDK fallback.

```sh
scripts/probe-device.sh [serial]
```

The probe fails when zero or multiple authorized devices exist and no serial was passed. Always use `adb -s SERIAL` after selection.

## Displays

Physical capture IDs and Android logical display IDs are different namespaces.

```sh
adb -s SERIAL shell dumpsys SurfaceFlinger --display-id
adb -s SERIAL shell dumpsys display
adb -s SERIAL exec-out screencap -d PHYSICAL_ID -p > PANEL.png
```

On a single-screen device, still verify rotation, native resolution, refresh rate, and the focused activity. On a multi-screen device, capture every panel after navigation because apps can swap content between them.

## Controller discovery

```sh
adb -s SERIAL shell getevent -il
adb -s SERIAL shell dumpsys input
```

Match a controller by its reported name and capabilities, not an old `/dev/input/eventN` path. A complete `sendevent` press needs key down, sync, a short pause, key up, and sync. Recheck event codes on each model.

Prefer the physical controller for frontend navigation. Use touch only after confirming the intended logical display and fresh coordinates.

## UI automation

- Capture before and after coordinate-based actions.
- Take one action at a time near storage grants, destructive dialogs, and secret fields.
- Verify the focused package and activity with `dumpsys window` or `dumpsys activity` after launches.
- Do not infer success from a process alone. Inspect the rendered UI and, for games, reach interactive gameplay.
- Do not inject keyboard text blindly. An incorrect focus can corrupt a credential or settings field.

## Scoped storage

Android may let an app access its private external directory while the ADB shell cannot enumerate or replace nested files. Treat permission errors as unknown state, not an empty directory. Verify through the app and use its import/export flow when available. Do not change permissions or reinstall solely to bypass scoped storage.

## Cleanup

Before deletion, enumerate exact targets, validate their paths and count in the same shell, exclude links and directories outside the setup scope, then remove only those targets. Verify absence afterward. Keep host-side backups until the user confirms the migration is satisfactory.
