# Cocoon reference

Use this reference to install and configure Cocoon, map players, organize Android apps, and verify scraping.

## Installation and storage

- Get the current release from `https://cocoon-shell.com/` or its official release channel.
- Verify version, package ID, checksum, and signer before an in-place sideload.
- Open Cocoon once before configuring storage permissions.
- Use the storage root requested by the user. Do not copy a removable-storage layout to an internal-storage setup or vice versa.

## Library setup

1. Add one folder per requested platform.
2. Map each platform to an installed player whose launch intent has been tested.
3. Refresh Cocoon's platform definitions after installing a new emulator or RetroArch core.
4. Rescan and read the result dialog. Confirm added and removed counts.
5. Reject duplicate playlist or disc entries before scraping.

Adding a platform is separate from rescanning existing platforms:

1. Open `Settings > Library & data`.
2. Dismiss the search keyboard if it is visible. A controller shortcut can type into the search field while that keyboard owns focus.
3. Press `Y` to open `Add Platforms`.
4. Select the platform, confirm it, verify the detected ROM folder and default player, then run `Rescan Games`.

Use this flow when a folder existed during onboarding but contained no directly discoverable games at the time. `Rescan Games` can omit an unregistered platform even after valid files arrive. Register the platform instead of flattening or renaming a working library.

Cocoon 3 observed behavior:

- Settings > Library & data contains `Rescan Games` and `Scrape`.
- App Drawer `Y -> Add to Home` creates an Android app tile.
- In Edit Grid, A picks up and drops a tile; Y changes tile size.
- Dropping an app onto a folder removes it from the home grid and adds it to that folder.
- A picker opened from inside a folder may launch an app instead of adding it. Moving a home tile into the folder is a reliable fallback.

Treat navigation details as version-specific and verify them on the live UI.

## Scraping

Configure ScreenScraper, SteamGridDB, Steam, or other requested services through Cocoon's intended UI. Use an approved secret manager and keep secrets out of logs and screenshots.

Completed scrape reports have been observed under:

```text
/storage/emulated/0/Android/data/rip.moth.cocoonshell/files/scrape_reports/
```

Parse the newest completed JSONL report. Useful fields include `changed`, `skippedReason`, `metadataWinners`, `mediaWinners`, `sources`, and `platform`. Provider matches and downloaded media files are stronger evidence than an enabled toggle.

## Disc-based systems

Do not rename `.cue`, `.bin`, `.chd`, `.iso`, or playlist files casually. Generic filenames can scrape poorly, but a working disc structure is better than a renamed one with broken internal references. Test one playlist before creating many; confirm Cocoon hides or excludes its source discs without producing duplicates.

For nested multi-disc libraries, a top-level `.m3u` may point to CHDs or cue sheets through relative subpaths. Validate every referenced path, add the platform explicitly, and rescan. A zero-game rescan is not proof that M3U or CHD is unsupported; first check whether the platform is present in the rescan platform list and has a default player.

## Final checks

- Launch a representative game for every player from Cocoon.
- Confirm Cocoon regains focus when the game exits.
- Check that native apps appear in the requested folder or dock.
- Run the final scrape only after the final rescan and cleanup.
- Leave Cocoon on a useful home page.
