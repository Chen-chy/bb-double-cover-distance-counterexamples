# Publishing this snapshot

The ZIP contains one repository root, `bb-double-cover-research/`. Extract its
contents and retain the supplied directory structure. There are no required
symlinks, linked cloud files, large-file pointer stubs, or hidden remote inputs.
The binary certificate files are real data and must remain in the repository.

Before publishing, review the rights/attribution note and decide the author and
license metadata. No remote has been created or modified by the export task.

A local Git initialization can use:

```sh
git init
git add .
git commit -m "Archive BB double-cover amplification research state"
```

Connect the resulting repository to the intended remote using that service's
normal workflow. No owner, repository URL, access token, or remote name is baked
into the files.

The `.gitattributes` file preserves archival source bytes rather than allowing
line-ending conversion to invalidate their hashes. `.gitignore` excludes writable
materializations, caches, and executables, but does not ignore binary proof
certificates. The `tools/check_repository.py` command can be used before making
a release. New research should be committed as a new round or an explicitly
versioned correction, not silently substituted into historical proof reports.

Keep original logs under their round; put new verification runs under a separate
versioned `checks/` directory only when deliberately releasing them. Ordinary
local runs belong under `.work/`, which is ignored. If a later audit finds a
mathematical error, record the correction and dependent claims explicitly.
