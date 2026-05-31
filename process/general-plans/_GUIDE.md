# General Plans Folder

This directory holds cross-cutting plans, reports, and references that are not specific to a single large feature cluster.

## Folder Structure

```
process/general-plans/
  active/       -- in-progress plans (e.g. general architecture updates, migrations)
  completed/    -- archived completed plans
  backlog/      -- deferred/future plans
  reports/      -- general operational reports, audits, and checklists
  references/   -- research, reference docs, and shared design guidelines
```

## Lifecycle

1. Store new, cross-cutting, or single-phase plans in `active/`
2. Once implemented and verified, move the plans to `completed/`
3. If a plan is deferred or planned for the future, move it to `backlog/`
4. If a plan grows to spawn multiple files or sub-phases exceeding 5+ artifacts, promote it to a dedicated feature folder under `process/features/{feature-name}/`
