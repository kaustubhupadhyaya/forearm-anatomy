# References and provenance

The three unreconciled volume totals (486.9, 438.7, 447.8 cm3) and the missing volume/PCSA citations are documented in `DATA-NOTES.md`.

## What the source cites

The current `forearm_mass_anatomy.html` has no formal citations. The long-form scientific section in `scripts/generate_segment.py` contains two in-text citations for forearm architectural data:

- Holzbaur et al., 2005
- Lieber et al., 1992

That section targets an older HTML revision and is not present in the current trimmed artifact. The source tree does not contain the full bibliographic records: no journal, volume, page numbers or DOI. They are reproduced here only as they appear in the source file. Verify the exact papers before citing them.

## Image provenance

The working tree that produced this repo contained `Gray414.png`, `Gray415.png`, `Gray417.png` and `Gray418.png`. The four `images/plate_*.jpg` files are the derived plates used by the HTML. The filenames point to Gray's Anatomy figures. The exact edition and scan source are not recorded. Verify the public-domain or license status before redistributing the plates. If provenance cannot be established, replace them.

No other sources, tables or datasets are recorded in this repo. The volume and PCSA values are not tied to a specific page or table.

## Gaps to close

- Replace the provisional volumes and PCSA values with cited values from a standard anatomy source.
- Record the full reference for each value, including the page or table used.
- Reconcile the three totals: 486.9 cm3 from the 20-row table, 438.7 cm3 from the header and video cards, and 447.8 cm3 from the 12 grouped records. The grouped percentages sum to 102.2%.
- Record the edition and scan source for the four plates, or replace them with images whose provenance is documented.
