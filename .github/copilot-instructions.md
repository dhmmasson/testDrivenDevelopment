# Copilot Instructions

## Project Overview

This is the **Advanced Programming course wiki** for ESTIA (2A students). It is a teaching website covering the **Pandora** Java project, Git/GitHub workflows, and software engineering practices (TDD, Conventional Commits, Semantic Versioning, CI/CD).

The site is a **Quarto website** built from Markdown source files. It also doubles as an **Obsidian vault**.

## Build & Preview

```bash
# Render the full site to _site/
quarto render

# Live-reload preview in browser
quarto preview
```

> The `_site/` directory is generated output — never edit HTML files there directly.

## Repository Structure

```
_quarto.yml             # Quarto project config (theme, navbar)
_Sidebar.md             # Sidebar navigation (Obsidian wiki / GitHub wiki format)
index.qmd               # Landing page (Quarto front matter required)
about.qmd               # About page
CHANGELOG.md            # Course-level changelog (reverse-chronological by year)
styles.css              # Custom CSS overrides (cosmo + brand theme)

Pandora/                # Pandora project specification docs
ProjectManagement/      # Dev process guides (commits, versioning, TDD, releases…)
  TestDrivenDevelopment/
git-101/                # Git tutorial exercises
Resources/              # CLI reference
tools/                  # IDE & tooling guides (Eclipse, VS Code, Maven, Git clients)
grade/                  # Grading rubrics per year
images/                 # Static assets referenced in markdown

_site/                  # ← Generated output (do not edit)
.obsidian/              # Obsidian vault configuration (plugins: Linter, QuickAdd)
```

## Content Conventions

- **Source format**: plain Markdown (`.md`) for all pages; `.qmd` only for pages needing Quarto features (YAML front matter, callouts, code execution).
- **Internal links**: use wiki-style relative links without extension — e.g., `[Pandora](Pandora)`, `[Conventional Commits](Conventional%20Commits)`. Quarto resolves them at build time.
- **Navigation**: update `_Sidebar.md` when adding pages (Obsidian/GitHub wiki sidebar) and `_quarto.yml` navbar for top-level entries.
- **New sections**: add a new subdirectory and update `_Sidebar.md`.
- **CHANGELOG**: entries go under the relevant year heading, newest first within each section. Format: `YYYY-MM-DD - description with [links](Page)`.
- **Code blocks**: use fenced code blocks with language identifiers (` ```java `, ` ```bash `).
- **Heading levels**: `# H1` for page title, `## H2` for major sections — never skip levels.

## Project Domain Context

The course centres on **Pandora**, a Java CLI tool that parses flight data recorder (`.dfr` / `.frd`) files and outputs computed statistics. Students implement features incrementally, releasing via GitHub with:
- Semantic Versioning tags (`vX.Y.Z`)
- Conventional Commits (`feat:`, `fix:`, `chore(release):` …)
- `manifest.json` listing implemented features
- Automated CI grading triggered by tags on the `release` branch

When editing docs in `Pandora/`, be precise about CLI flags, output format, and constant values — students' grades depend on exact string matching against the reference implementation.

## Key Files to Understand Patterns

- [Pandora/Pandora.md](../Pandora/Pandora.md) — canonical CLI man-page style doc
- [ProjectManagement/Conventional Commits.md](../ProjectManagement/Conventional%20Commits.md) — commit convention reference
- [ProjectManagement/Release.md](../ProjectManagement/Release.md) — release process
- [ProjectManagement/Test-Driven-Development.md](../ProjectManagement/TestDrivenDevelopment/Test-Driven-Development.md) — TDD guide
